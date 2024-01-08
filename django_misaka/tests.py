from django import template
from django.template import Context, Template
from django.template.loader import render_to_string

import pytest
from pytest_django.asserts import assertHTMLEqual

from django_misaka.conf import Settings


def render_template(template_string, **kwargs):
    template = Template(template_string)
    return template.render(Context(kwargs)).strip()


def test_filter():
    md = "{% load markdown %}\n{{ var|markdown }}"

    assert (
        render_template(md, var="**double asterisks**")
        == "<p><strong>double asterisks</strong></p>"
    )


def test_filter_with_setting(misaka_settings):
    md = "{% load markdown %}\n{{ var|markdown:'test' }}"

    assert (
        render_template(md, var="https://www.google.com")
        == '<p><a href="https://www.google.com">https://www.google.com</a></p>'
    )


@pytest.mark.parametrize(
    "markdown,expected",
    [
        (
            "tests/test_tag.html",
            "tests/rendered_result/tag.html",
        ),
        (
            "tests/test_syntax_highlighting.html",
            "tests/rendered_result/syntax_highlighting.html",
        ),
    ],
)
def test_tag(
    markdown,
    expected,
):
    assertHTMLEqual(
        render_to_string(markdown),
        render_to_string(expected),
    )


def test_tag_with_setting(misaka_settings):
    assertHTMLEqual(
        render_to_string("tests/test_tag_with_argument.html"),
        render_to_string("tests/rendered_result/tag_with_argument.html"),
    )


def test_tag_with_multiple_settings(misaka_settings):
    md = "{% load markdown %}\n{% markdown 'first' 'second' %}\n{% endmarkdown %}"

    with pytest.raises(template.TemplateSyntaxError):
        render_template(md)


def test_setting_name(misaka_settings):
    md = "{% load markdown %}\n{{ var|markdown:'foo' }}"

    with pytest.raises(KeyError):
        render_template(md, var="https://www.google.com")


def test_setting_attribute():
    setting = Settings()

    with pytest.raises(AttributeError):
        setting.bar  # noqa: B018
