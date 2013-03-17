Favorites for Django
====================

django-favorites is a LGPL Licensed app for Django.

| Requires: Django +1.4.3
| Tested on: Python 2.7, Django 1.5

Config
------

Add ``favorites`` to ``INSTALLED APPS``.

    | #settings.py
    | INSTALLED_APPS = (
    | ...
    | 'favorites',
    | ...
    | )
    | # Add every model (app_label.model) you are going to add favorites.
    | FAVORITE_MODELS = ['test.article', ]
|
    | #template
    | {% load favorites %}
    | {% render_favorite_form obj user next=request.get_full_path %}

Demo
----

An app is provided, called test, showing the basic usage.

License
-------

Copyright (C) 2013 Esteban Borsani ochdownloader@gmail.com
|
| This program is free software; you can redistribute it and/or modify
| it under the terms of the GNU Lesser General Public License as published by
| the Free Software Foundation; either version 3 of the License, or
| (at your option) any later version.
|
| This program is distributed in the hope that it will be useful,
| but WITHOUT ANY WARRANTY; without even the implied warranty of
| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
| GNU Lesser General Public License for more details.