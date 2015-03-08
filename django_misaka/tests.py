from django.template import Context, Template
from django.template.loader import render_to_string
from django.test import TestCase


def render_template(template_string, **kwargs):
    template = Template(template_string)
    return template.render(Context(kwargs)).strip()


class DjangoMisakaTestCase(TestCase):
    def test_filter(self):
        md = "{% load markdown %}\n{{ var|markdown|safe}}"
        self.assertEqual(render_template(md, var='**double asterisks**'),
                         '<p><strong>double asterisks</strong></p>')

    def test_tag(self):
        md = render_to_string('tests/test_tag.html')
        rendered_result = render_to_string('tests/rendered_result/tag.html')
        self.assertHTMLEqual(md, rendered_result)

    def test_syntax_highlighting(self):
        md = render_to_string('tests/test_syntax_highlighting.html')
        rendered_result = render_to_string(
            'tests/rendered_result/syntax_highlighting.html')
        self.assertHTMLEqual(md, rendered_result)
