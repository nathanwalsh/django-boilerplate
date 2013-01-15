Django Boilerplate for Django 1.4
=================================

A barebones default layout for organised Django development. Inspired from Martin Ogden's Django Boilerplate (link below).


### Usage

This assumes you have pip and django installed (if not, try `$ sudo easy_install pip`)

    $ django-admin.py startproject --template http://github.com/nathanwalsh/django-boilerplate/zipball/master project_name
    $ cd project_name
    $ pip install -r requirements.txt
    $ python manage.py syncdb --migrate
    $ cd config; ln -s environments/settings_production.py settings.py


### Settings

Django settings are configured in `config/common.py` and any settings added in `config/local.py` will be picked up and override any previously defined settings. This is useful for sensitive information such as database credentials or the `SECRET_KEY` etc. By default this file will *NOT* be checked into git.


### Preinstalled Apps

 * [path.py](https://github.com/dottedmag/path.py): A module wrapper for os.path
 * [South](http://south.aeracode.org/): Intelligent database migrations
 * [django-grappelli](https://github.com/sehmaschine/django-grappelli): A jazzy skin for the Django admin interface.
 * [django-extensions](https://github.com/django-extensions): A collection of custom extensions
 * [django-compressor](https://github.com/jezdez/django_compressor): Compresses linked and inline javascript or CSS into a single cached file.
 * [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar): A configurable set of panels that display various debug information about the current request/response.
 * [django-extra-views](https://github.com/AndrewIngram/django-extra-views): The missing class-based generic views for Django


### Credits

Much of the layout is taken from [Martin Ogden's Django Boilerplate](https://github.com/martinogden/django-boilerplate) project which took much of the layout from a great [post](http://blog.zacharyvoase.com/2010/02/03/django-project-conventions/) by Zachary Voase.


