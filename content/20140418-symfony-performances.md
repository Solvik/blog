Title: Symfony performances
Date: 2014-04-18 15:34
Category: System
Tags: symfony2, performances, fabric
Slug: symfony2-performances
Author: Solvik

Since a few weeks, we've stumble upon a few performances problem on our Symfony2 backend.
For the record, it's a 50k line codes, lots of feature and custom bundles.


autoloader
----

On the first request, Symfony PHP's code must discover all the classes of your code.
It does a lot of stat/open/read/close on each file of your project.
We've observe a 100% CPU usage for a few seconds, the time required for the code to discover everything.

By default, this feature is called without the **--optimize** flag.

So we had to custom our fabric script by adding

   	  $ php composer.phar dump-autoload --optimize

For example, our autoloader filer was created with **300** lines before.
After the **--optimize** flag, it now has more than **5 000** lines.


To be continued with APC support and OpCode Cache of PHP 5.5