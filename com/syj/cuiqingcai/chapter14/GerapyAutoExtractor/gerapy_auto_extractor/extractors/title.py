from .base import BaseExtractor
from lxml.html import HtmlElement
from ..patterns.title import METAS
from ..utils.lcs import lcs_of_2
from ..utils.similarity import similarity2


class TitleExtractor(BaseExtractor):

    def extract_by_meta(self, element: HtmlElement) -> str:
        for xpath in METAS:
            title = element.xpath(xpath)
            if title:
                return ''.join(title)


    def extract_by_title(self, element: HtmlElement) -> str:
        return ''.join(element.xpath('//title//text()')).strip()


    def extract_by_h2(self, element: HtmlElement) -> str:
        hs = element.xpath('.//h1//text()|//h2//text()|//h3//text()')
        return hs or []


    def extract_by_h(self, element: HtmlElement) -> str:
