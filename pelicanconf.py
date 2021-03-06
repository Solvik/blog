#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
from datetime import datetime

AUTHOR = u'Solvik Blum'
SITELOGO = 'https://en.gravatar.com/userimage/144533955/56e59d953cf9667fa0206fdd677aa7cc.jpg?size=200'
SITEURL = 'https://blog.solvik.fr/'
SITETITLE = '/home/solvik'
SITESUBTITLE = 'my place of sharing'
SUMMARY_MAX_LENGTH = 5000
BROWSER_COLOR = '#3338db'
PYGMENTS_STYLE = 'monokai'

TIMEZONE = 'Europe/Paris'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

ROBOTS = 'index, follow'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 25

USE_LESS = True

# Blogroll
LINKS =  (())

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/solvikblum'),
    ('twitter', 'https://twitter.com/solvik'),
    ('github', 'https://github.com/Solvik'),
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'pelican-themes')
THEME_CHOICE = 'Flex'
THEME = os.path.join(THEME_PATH, THEME_CHOICE)

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
