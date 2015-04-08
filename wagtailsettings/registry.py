from django.core.urlresolvers import reverse
from django.db.models import get_model
from django.utils.functional import cached_property

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.menu import MenuItem


class Registry(object):

    content_type = None

    def __init__(self):
        self.models = []

    def register(self, model, **kwargs):
        if model in self.models:
            return model

        self.models.append(model)

        @hooks.register('register_settings_menu_item')
        def hook():
            return MenuItem(
                model._meta.verbose_name.title(),
                reverse('wagtailsettings_edit', args=[
                    model._meta.app_label, model._meta.model_name]),
                **kwargs)

        return model

    @cached_property
    def content_types(self):
        ContentType = get_model('contenttypes.ContentType')
        content_types = list(map(
            ContentType.objects.get_for_model, self.models))

        return content_types

registry = Registry()


def register_setting(model=None, **kwargs):
    if model is None:
        return lambda model: register_setting(model, **kwargs)
    return registry.register(model, **kwargs)