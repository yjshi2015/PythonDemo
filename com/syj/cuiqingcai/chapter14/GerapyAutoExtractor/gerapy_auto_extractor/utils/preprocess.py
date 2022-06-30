from lxml.html import HtmlElement, etree

from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.element \
    import children, remove_children, remove_element
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.schemas.element import Element

CONTENT_EXTRACTOR_USELESS_TAGS = ['meta', 'style', 'script', 'link', 'video', 'audio', 'iframe', 'source', 'svg',
                                  'path',
                                  'symbol', 'img', 'footer', 'header']
CONTENT_EXTRACTOR_STRIP_TAGS = ['span', 'blockquote']
CONTENT_EXTRACTOR_NOISE_XPATHS = [
    '//div[contains(@class, "comment")]',
    '//div[contains(@class, "advertisement")]',
    '//div[contains(@class, "advert")]',
    '//div[contains(@style, "display: none")]',
]


def preprocess4content_extract(element: HtmlElement):
    # 移除无用标签及其下内容
    etree.strip_elements(element, *CONTENT_EXTRACTOR_USELESS_TAGS)
    # 移除标签，保留其下的内容
    etree.strip_tags(element, *CONTENT_EXTRACTOR_STRIP_TAGS)
    # 移除评论/广告相关的节点，根据xpath移除
    remove_children(element, *CONTENT_EXTRACTOR_NOISE_XPATHS)

    # html的直接子节点，只有2个元素，head/body
    for child in children(element):
        # 合并span、strong标签下的文本到p标签中
        if child.tag.lower() == 'p':
            etree.strip_tags(element, 'span')
            etree.strip_tags(element, 'strong')
        # 移除text为空的节点
        if not (child.text and child.text.strip()):
            remove_element(child)
        # 无子节点的div节点，改为p节点
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'


LIST_EXTRACTOR_USELESS_TAGS = CONTENT_EXTRACTOR_USELESS_TAGS
LIST_EXTRACTOR_STRIP_TAGS = CONTENT_EXTRACTOR_STRIP_TAGS
LIST_EXTRACTOR_NOISE_XPATHS = CONTENT_EXTRACTOR_NOISE_XPATHS


def preprocess4list_extractor(element: Element):
    """
    preprocess element for list extraction
    :param element:
    :return:
    """
    # remove tag and its content
    etree.strip_elements(element, *LIST_EXTRACTOR_USELESS_TAGS)
    # only move tag pair
    etree.strip_tags(element, *LIST_EXTRACTOR_STRIP_TAGS)

    remove_children(element, *LIST_EXTRACTOR_NOISE_XPATHS)

    for child in children(element):

        # merge text in span or strong to parent p  tag
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')

            if not (child.text and child.text.strip()):
                remove_element(child)

        # if a div tag does not contain any sub node, it could be converted to p node.
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'


LIST_CLASSIFIER_USELESS_TAGS = ['style', 'script', 'link', 'video', 'audio', 'iframe', 'source', 'svg', 'path',
                                'symbol', 'footer', 'header']
LIST_CLASSIFIER_STRIP_TAGS = ['span', 'blockquote']
LIST_CLASSIFIER_NOISE_XPATHS = [
    '//div[contains(@class, "comment")]',
    '//div[contains(@class, "advertisement")]',
    '//div[contains(@class, "advert")]',
    '//div[contains(@style, "display: none")]',
]


def preprocess4list_classifier(element: HtmlElement):
    """
    preprocess element for list classifier
    :param element:
    :return:
    """
    # remove tag and its content
    etree.strip_elements(element, *LIST_CLASSIFIER_USELESS_TAGS)
    # only move tag pair
    etree.strip_tags(element, *LIST_CLASSIFIER_STRIP_TAGS)

    remove_children(element, LIST_CLASSIFIER_NOISE_XPATHS)

    for child in children(element):

        # merge text in span or strong to parent p tag
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')

            if not (child.text and child.text.strip()):
                remove_element(child)

        # if a div tag does not contain any sub node, it could be converted to p node.
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'
