from django import template
import misaka as m
from pygments import highlight
from pygments.formatters import ClassNotFound, HtmlFormatter
from pygments.lexers import get_lexer_by_name

register = template.Library()


class MisakaRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)

        return '\n<pre><code>{}</code></pre>\n'.format(
            m.escape_html(text.strip())
        )


@register.filter(name='markdown')
def markdown_filter(value):
    renderer = MisakaRenderer(
        flags=(
            "escape",
        ),
    )
    md = m.Markdown(
        renderer,
        extensions=(
            "fenced-code",
            "no-intra-emphasis",
        ),
    )

    return md(value)


@register.tag(name='markdown')
def markdown_tag(parser, token):
    nodelist = parser.parse(('endmarkdown',))
    parser.delete_first_token()
    return MisakaNode(nodelist)


class MisakaNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        value = self.nodelist.render(context)
        renderer = MisakaRenderer(
            flags=(
                "escape",
            ),
        )
        md = m.Markdown(
            renderer,
            extensions=(
                "fenced-code",
                "no-intra-emphasis",
            ),
        )

        return md(value)
