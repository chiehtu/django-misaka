from django import template
import misaka as m
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()


class MisakaRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                m.escape_html(text.strip())

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)


@register.filter(name='markdown')
def markdown_filter(value):
    renderer = MisakaRenderer(flags=m.HTML_ESCAPE)
    md = m.Markdown(renderer,
                    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS)
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
        renderer = MisakaRenderer(flags=m.HTML_ESCAPE)
        md = m.Markdown(renderer,
                        extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS)
        return md(value)
