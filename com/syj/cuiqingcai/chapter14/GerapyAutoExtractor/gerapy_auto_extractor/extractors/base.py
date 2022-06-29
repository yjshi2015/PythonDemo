from lxml.html import fromstring
from loguru import logger
from lxml.html import etree
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.schemas.element import Element


class BaseExtractor(object):
    kwargs = None

    def to_string(self, element: Element, limit: int = None):
        result = etree.tostring(element, pretty_print=True, encoding='utf-8', method='html').decode('utf-8')
        if limit:
            return result[: limit]
        return result

    def process(self, element: Element):
        logger.error('you must implement process method in your extractor')
        raise NotImplementedError

    def extract(self, html, **kwargs):
        """
        base extract method, firstly, it will convert html to WebElement, then it call
        process method that child class implements
        :param html:
        :return:
        """
        self.kwargs = kwargs
        element = fromstring(html=html)
        element.__class__ = Element
        return self.process(element)
