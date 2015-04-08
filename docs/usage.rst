.. _usage:

==================
Using the settings
==================

Settings are designed to be used both in Python code, and in templates.

Using in Python
---------------

If access to a setting is required in the code,
the ``BaseSetting.for_site`` method will retrieve the setting for the supplied site:

.. code:: python

    def view(request):
        social_media_settings = SocialMediaSettings.for_site(request.site)
        ...

Using in templates
------------------

Add the ``request`` and ``wagtailsettings`` context processors to your settings:

.. code:: python

    from django.conf import global_settings
    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'wagtailsettings.context_processors.settings',
    )

Then access the settings through ``settings``:

.. code:: html+django

    {{ settings.app_label.SocialMediaSettings.instagram }}

If you are not in a RequestContext, then context processors will not have run,
and the ``settings`` variable will not be availble. To get the ``settings``,
use the provided template tags:

.. code:: html+django

    {% load wagtailsettings_tags %}
    {% get_settings %}
    {{ settings.app_label.SocialMediaSettings.instagram }}

.. note:: You can not reliably get the correct settings instance for the
    current site from this template tag, as the request object is not
    available. This is only relevant for multisite instances of Wagtail though,
    so most developers will not have to worry.
