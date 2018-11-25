#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
from datetime import datetime

AUTHOR = u'Solvik Blum'
SITEURL = 'http://127.0.0.1:8000/'
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
    ('Linkedin', 'fr.linkedin.com/in/solvikblum'),
    ('Twitter', 'https://twitter.com/solvik'),
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'pelican-themes')
THEME_CHOICE = 'Flex'
THEME = os.path.join(THEME_PATH, THEME_CHOICE)
