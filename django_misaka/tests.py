from django.template import Context, Template
from django.template.loader import render_to_string

import pytest
from pytest_django.asserts import assertHTMLEqual


def render_template(template_string, **kwargs):
    template = Template(template_string)
    return template.render(Context(kwargs)).strip()


def test_filter():
    md = "{% load markdown %}\n{{ var|markdown|safe }}"

    assert (
        render_template(md, var="**double asterisks**")
        == "<p><strong>double asterisks</strong></p>"
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
