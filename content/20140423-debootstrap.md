Title: How-To Debootstrap
Date: 2014-04-23 17:00
Category: System
Tags: linux, debootstrap, ubuntu, gpt
Slug: howto-debootstrap
Author: Solvik

For my infrastructure purposes I often need to install as fast as possible.
Most of my servers comes with 4 disks and one or more RAID card.

I usually don't trust the RAID cards, so I always create a raid0 / disk in order to use every logical volume like it was a real disk.

And I always use the above partition schema

| mount | size |
| ----- | ---- |
| /boot | 200M |
| /		| * |

hpacucli
----

    :::shell
	# find your slot
	slot=`hpacucli ctrl all show | grep -i slot | awk '{print $6}'
    hpacucli ctrl slot=$slot ld 1 delete
	# create one raid0 per physical disk
	for phys in `hpacucli ctrl all show config | grep physicaldrive | awk '{print $2}'`;
	do
	  hpacucli controller slot=$slot create type=ld drives=$phys raid=0
	done;


Cleaning
----

If you use an old server, you must do some cleaning

Let's start by zeroing the first 100MB of the partition in order to be sure to erase the partition table, the MBR

    :::shell
	for i in {a..d} ;
	do
	  dd if=/dev/sda of=/dev/zero count=100 bs=1M
	done

Afterwars, let's notify the kernel about devices changes

    :::shell
	partprobe


MSDOS partitions
---

    :::shell
    for i in {a..d} ;
	do
	  parted /dev/sd$i --script -- mklabel msdos
      parted /dev/sd$i -a optimal --script -- unit MB mkpart primary 1 200
      parted /dev/sd$i -a optimal --script -- unit MB mkpart primary 200 -1
	done;


GPT partitions
----

For GPT partitions you need to create [BIOS Boot partition][3] a small partition, at least 1mb.

&nbsp;

    :::shell
    for i in {a..d} ;
	do
		parted /dev/sd$i --script -- mklabel gpt
    	parted /dev/sd$i -a optimal --script -- unit MB mkpart grub fat32 1mb 2mb
    	parted /dev/sd$i -a optimal --script -- unit MB set 1 bios_grub on
    	parted /dev/sd$i -a optimal --script -- unit MB mkpart primary 2mb 200
    	parted /dev/sd$i -a optimal --script -- unit MB mkpart primary 200 -1
	done;



Installation
----

I prefer to use software raid with mdadm.
If you want to boot on a mdadm's volume you need it to use the [0.90 metadatas][1]
For you **/**, use the raid-level you want and don't give any metadata paramaters so it can takes the **1.2** one.

**/!\\** If you use GPT partitions, be aware that **/dev/sdx1** is the BIOS partition, not your future /boot, start at **/dev/sdx2**

    :::shell
	# for msdos partitions
    mdadm --create /dev/md0 --metadata=0.90 --assume-clean --raid-devices=4 --level=1 /dev/sda1 /dev/sdb1 /dev/sdc1 /dev/sdd1
    mdadm --create /dev/md1 --assume-clean --raid-devices=4 --level=6 /dev/sda2 /dev/sdb2 /dev/sdc2 /dev/sdd2

	# for gpt partitions
    mdadm --create /dev/md0 --metadata=0.90 --assume-clean --raid-devices=4 --level=1 /dev/sda2 /dev/sdb2 /dev/sdc2 /dev/sdd2
    mdadm --create /dev/md1 --assume-clean --raid-devices=4 --level=6 /dev/sda3 /dev/sdb3 /dev/sdc3 /dev/sdd3



Let's format the RAID volumes

    :::shell
    mkfs.ext4 /dev/md0
    mkfs.ext4 /dev/md1

Let's start the debootstrap session. I use a basic /etc/apt/sources.list using this [convenient sources.list generator][2]



    :::shell
    mkdir /mnt/root
    mount /dev/md1 /mnt/root
    apt-get update; apt-get install -y debootstrap
    debootstrap trusty /mnt/root
    mount -o bind /dev /mnt/root/dev
    mount -o bind /proc /mnt/root/proc
    mount -o bind /sys /mnt/root/sys

    # basic fstab
    echo "proc            /proc   proc    defaults                0       0
    /dev/md1 /       ext4    errors=remount-ro       0       1
    /dev/md0        /boot   ext4    defaults                0       2
    " > /mnt/root/etc/fstab

    echo "#############################################################
    ################### OFFICIAL UBUNTU REPOS ###################
    #############################################################

    ###### Ubuntu Main Repos
    deb http://fr.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse
    deb-src http://fr.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse

    ###### Ubuntu Update Repos
    deb http://fr.archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse
    deb http://fr.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse
    deb-src http://fr.archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse
    deb-src http://fr.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse
    " > /mnt/root/etc/apt/sources.list

Now we can go the installed volume and prepare the OS


    :::shell
    cd /mnt/root
    chroot .
    # mount /boot for the future kernel installation
    mount /boot
    # generate a few locales
    locale-gen fr_FR.UTF-8
    locale-gen fr_FR
    locale-gen en_US.UTF-8
    locale-gen en_US
    update-locale

    apt-get update
    # don't forget to install mdadm on the system so it can boots correctly
    apt-get install -y mdadm lvm2
    # install the required kernel
    apt-get install -y linux-image-generic
    # install an openssh-server so you can remotely have access to the system
    apt-get install -y openssh-server
    # change your root password!!
    echo "root:changeme"|chpasswd

Stop the few services

    :::shell
    /etc/init.d/ssh stop

Umount everything, sync for the last i/o and reboot

    :::shell
    umount /boot
    exit
	umount /mnt/root/dev
	umount /mnt/root/proc
	umount /mnt/root/sys
    sync
    reboot


LVM
----

Work in progress

Rescue
----

Without LVM
####

If you happen to boot on a rescue live-cd on one of this configuration, it will detect a RAID system but without the correct device names


    :::shell
    mdadm -S /dev/md126
    mdadm -S /dev/md127
	mdadm --examine --scan /dev/sda{1..4} >> /etc/mdadm/mdadm.conf
	mdadm --assemble --scan

Your **/dev/md0** and **/dev/md1** should come online

    :::shell
	mkdir -p /mnt/root
	mount /dev/md1 /mnt/root
    mount -o bind /dev /mnt/root/dev
    mount -o bind /proc /mnt/root/proc
    mount -o bind /sys /mnt/root/sys
	chroot /mnt/root

Here you go!


Credits
----

Thanks to my friends [Pierre Tourbeaux][4] and [Michael Kozma][5] for all the advices and debugging over the year :)

[1]: https://raid.wiki.kernel.org/index.php/RAID_superblock_formats
[2]: http://repogen.simplylinux.ch/
[3]: http://en.wikipedia.org/wiki/BIOS_Boot_partition
[4]: http://www.si7v.fr
[5]: http://www.ipsolution.fr