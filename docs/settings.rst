.. _settings:

=================
Defining settings
=================

Create a model that inherits from ``BaseSetting``,
and register it using the ``register_setting`` decorator:

.. code:: python

    from wagtailsettings import BaseSetting, register_setting

    @register_setting
    class SocialMediaSettings(BaseSetting):
        facebook = models.URLField(
            help_text='Your Facebook page URL')
        instagram = models.CharField(
            max_length=255, help_text='Your Instagram username, without the @')
        trip_advisor = models.URLField(
            help_text='Your Trip Advisor page URL')
        youtube = models.URLField(
            help_text='Your YouTube channel or user account URL')


A 'Social media settings' link will appear in the Wagtail admin 'Settings' menu.

Edit handlers
-------------

Settings use edit handlers much like the rest of Wagtail.
Add a `panels` setting to your model defining all the edit handlers required:

.. code:: python

    @register_setting
    class ImportantPages(BaseSetting):
        donate_page = models.ForeignKey(
            'wagtailcore.Page', null=True, on_delete=models.SET_NULL)
        sign_up_page = models.ForeignKey(
            'wagtailcore.Page', null=True, on_delete=models.SET_NULL)

        panels = [
            PageChooserPanel('donate_page'),
            PageChooserPanel('sign_up_page'),
        ]

Appearance
----------

You can change the label used in the menu by changing the
`verbose_name <https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name>`_
of your model.

You can add an icon to the menu
by passing an 'icon' argument to the ``register_setting`` decorator:

.. code:: python

    @register_setting(icon='icon-placeholder')
    class SocialMediaSettings(BaseSetting):
        # ...

For a list of all available icons, please see the Wagtail style guide.
