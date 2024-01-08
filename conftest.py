import pytest


@pytest.fixture()
def misaka_settings(settings):
    settings.MISAKA = {
        "default": {
            "flags": (),
            "extensions": (
                "fenced-code",
                "no-intra-emphasis",
            ),
        },
        "test": {
            "flags": (),
            "extensions": (
                "fenced-code",
                "no-intra-emphasis",
                "tables",
                "autolink",
            ),
        },
    }
