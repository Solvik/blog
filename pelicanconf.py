#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Solvik'
SITENAME = u'/home/solvik/'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (())

# Social widget
SOCIAL = (
    ('Linkedin', 'fr.linkedin.com/in/solvikblum'),
    ('Twitter', 'https://twitter.com/solvik'),
    ('Online', 'http://www.online.net/')
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_PATH = "/home/solvik/blog/pelican-themes/"
THEME_CHOICE = 'tuxlite_zf'
THEME = os.path.join(THEME_PATH, THEME_CHOICE)
