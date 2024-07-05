import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from posts.markdown_extensions import SlugFieldExtension

register = template.Library()


@register.filter(name="markdown")
@stringfilter
def render_markdown(value):
    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite", SlugFieldExtension()]
    )
    return mark_safe(md.convert(value))
