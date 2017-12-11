#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

# Server

SITEURL = 'https://SabrinaBernardelli.github.io/'
RELATIVE_URLS = False
AUTHOR = 'Zam Ackerman'
SITENAME = 'Zam Ackerman'
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
TIMEZONE = 'America/Argentina/Buenos_Aires'
PAGE_ORDER_BY = 'order'


# Plugins

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-ert', 'backreftranslate', 'summary']

# ERT

ERT_WPM = 150
ERT_FORMAT = '{time}'

# Localization

DEFAULT_LANG = 'en'

# Directories Layout

USE_FOLDER_AS_CATEGORY = True

# UI

DISPLAY_CATEGORIES_ON_MENU = True

# URL Settings

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
AUTHOR_AVATAR = "https://pbs.twimg.com/profile_images/885213794603028480/mkDFAD6X_400x400.jpg"


# Blogroll 

DISQUS_SITENAME = "zam-ackerman"
GOOGLE_ANALYTICS = "UA-71773079-4"

SOCIAL = (
    ('twitter', 'https://twitter.com/Shiro_hi18'),
    ('facebook', 'https://www.facebook.com/ShiroHi20'),
    ('envelope', 'mailto:sabriibernardelli@gmail.com'),
)

# Pagination

DEFAULT_PAGINATION = 10
