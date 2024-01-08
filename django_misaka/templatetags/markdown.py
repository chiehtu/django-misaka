from django import template
from django.utils.safestring import mark_safe

import misaka
from pygments import highlight
from pygments.formatters import ClassNotFound, HtmlFormatter
from pygments.lexers import get_lexer_by_name

from ..conf import Settings

register = template.Library()


class MisakaRenderer(misaka.HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)

        return "\n<pre><code>{}</code></pre>\n".format(misaka.escape_html(text.strip()))


@register.filter(name="markdown")
def markdown_filter(value, arg="default"):
    return _markdown(value, arg)


@register.tag(name="markdown")
def markdown_tag(parser, token):
    args = token.contents.split()
    if len(args) > 2:
        raise template.TemplateSyntaxError("'markdown' tag requires 1 argument")

    settings_name: str = args[1].strip("'\"") if len(args) > 1 else "default"

    nodelist = parser.parse(("endmarkdown",))
    parser.delete_first_token()

    return MisakaNode(settings_name, nodelist)


class MisakaNode(template.Node):
    def __init__(self, settings_name, nodelist):
        self.settings_name, self.nodelist = settings_name, nodelist

    def render(self, context):
        return _markdown(self.nodelist.render(context), self.settings_name)


def _markdown(value, arg="default"):
    settings = Settings(arg)
    if "escape" not in settings.flags:
        settings.flags = ("escape",) + settings.flags

    renderer = MisakaRenderer(
        flags=settings.flags,
    )
    md = misaka.Markdown(
        renderer,
        extensions=settings.extensions,
    )

    return mark_safe(md(value))
