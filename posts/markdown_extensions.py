import markdown
from django.urls import reverse
from markdown.inlinepatterns import LinkInlineProcessor, LINK_RE


class SlugFieldLinkInlineProcessor(LinkInlineProcessor):
    def getLink(self, data: str, index: int) -> tuple[str, str | None, int, bool]:
        href, title, index, handled = super().getLink(data, index)
        if href.startswith("slug"):
            slug = href.split(":")[1]
            relative_url = reverse("detail", args=[slug])
            href = relative_url
        return href, title, index, handled


class SlugFieldExtension(markdown.Extension):
    def extendMarkdown(self, md: markdown.Markdown) -> None:
        md.inlinePatterns.register(
            SlugFieldLinkInlineProcessor(LINK_RE, md), "link", 160
        )
