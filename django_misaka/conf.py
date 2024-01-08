from django.conf import settings as django_settings

DEFAULTS = {
    "default": {
        "flags": ("escape",),
        "extensions": (
            "tables",
            "fenced-code",
            "footnotes",
            "strikethrough",
            "underline",
            "highlight",
            "quote",
            "superscript",
            "no-intra-emphasis",
            "space-headers",
        ),
    },
}


class Settings:
    def __init__(self, setting_name="default"):
        self._settings = DEFAULTS
        self._settings.update(getattr(django_settings, "MISAKA", {}))
        if setting_name not in self._settings:
            raise KeyError("'{}' is not a valid setting name".format(setting_name))
        self._setting_name = setting_name

    def __getattr__(self, name):
        if name not in self._settings[self._setting_name]:
            raise AttributeError("'Settings' object has no attribute '{}'".format(name))

        value = self._settings[self._setting_name][name]
        setattr(self, name, value)

        return value
