import logging
import re
import numpy as np
from os.path import exists
from types import ModuleType
from collections import defaultdict
from loguru import logger
from lxml.html import fromstring, HtmlElement
from ..schemas.element import Element
from ..utils.similarity import similarity

PUNCTUATION = set('''！，。？、；：“”‘’《》%（）<>{}「」【】*～`,.?:;'"!%()''')


def remove_element(element: Element):
    if element is None:
        return
    p = element.getparent()
    if p is not None:
        p.remove(element)


def remove_children(element: Element, xpaths):
    if element is None:
        return
    if not xpaths:
        return
    for xpath in xpaths:
        nodes = element.xpath(xpath)
        for node in nodes:
            remove_element(node)
    return element


def html2element(html: str):
    if not html:
        return
    element = fromstring(html)
    element.__class__ = Element
    return element


def file2element(file_path):
    if not exists(file_path):
        return
    with open(file_path, encoding='utf-8') as f:
        return html2element(f.read())


def selector(element: Element):
    if element is None:
        return ''
    p = parent(element)
    if p is not None:
        return selector(p) + '>' + alias(element)
    return element.alias


def parent(element: Element):
    if element is None:
        return None
    parent = element.getparent()
    if isinstance(parent, ModuleType):
        parent.__class__ = Element
    return parent


def path_raw(element: Element):
    """
    get tag path using recursive function, only contains raw tag
    for example result: html/body/div/div/ul/li
    :param element:
    :return:
    """
    if element is None:
        return ''
    p = parent(element)
    if p is not None:
        return path_raw(p) + '/' + element.tag
    return element.tag


def path(element: Element):
    if element is None:
        return ''
    result = path_raw(element)
    nth = len(list(element.itersiblings(preceding=True))) + 1
    result += f':nth-child({nth})'
    return result


def a_descendants(element: Element):
    if element is None:
        return []
    descendants = []
    for descendant in element.xpath('.//a'):
        descendant.__class__ = Element
        descendants.append(descendant)
    return descendants


def a_descendants_group(element: Element):
    result = defaultdict(list)
    # todo syj 啥意思
    for linked_descendant in element.a_descendants:
        p = linked_descendant.path_raw
        result[p].append(linked_descendant)
    return result


def children(element: Element, including=False):
    if element is None:
        return []
    if including:
        yield element
    for child in element.iterchildren():
        if isinstance(child, HtmlElement):
            child.__class__ = Element
            yield child


def siblings(element: Element, including=False):
    if element is None:
        return []
    if including:
        yield element
    for sibling in element.itersiblings(preceding=True):
        if isinstance(sibling, HtmlElement):
            sibling.__class__ = Element
            yield sibling
    for sibling in element.itersiblings(preceding=False):
        if isinstance(sibling, HtmlElement):
            sibling.__class__ = Element
            yield sibling


def descendants(element: Element, including=False):
    if element is None:
        return []
    if including:
        yield element
    for descendant in element.iterdescendants():
        if isinstance(descendant, HtmlElement):
            descendant.__class__ = Element
            yield descendant


def children_of_head(element: Element):
    if element is None:
        return []
    body_xpath = '//head'
    body_element = element.xpath(body_xpath)
    if body_element:
        body_element.__class__ = Element
        return descendants(body_element, True)
    return []


def descendants_of_body(element: Element):
    if element is None:
        return []
    body_xpath = '//body'
    elements = element.xpath(body_xpath)
    if elements:
        elements[0].__class__ = Element
        return list(descendants(elements[0], True))
    return []


def text(element: Element):
    if element is None:
        return 0
    text = ''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, re.S)
    return text


def number_of_char(element: Element):
    """
    get number of char, for example, result of `<a href="#">hello</a>world` = 10
    :param element:
    :return: length
    """
    if element is None:
        return 0
    return len(text(element))


def number_of_a_char(element: Element):
    """
    get number of linked char, for example, result of `<a href="#">hello</a>world` = 5
    :param element:
    :return: length
    """
    if element is None:
        return 0
    text = ''.join(element.xpath('.//a//text()'))
    text = re.sub(r'\s*', '', text, re.S)
    return len(text)


def number_of_a_char_log10(element: Element):
    """
    get number of linked char, to log10
    :param element:
    :return: length
    """
    if element is None:
        return 0
    return np.log10(number_of_a_char(element) + 1)


def number_of_p_children(element: Element):
    if element is None:
        return 0
    return len(element.xpath('./p'))


def number_of_p_descendants(element: Element):
    if element is None:
        return 0
    return len(element.xpath('.//p'))


def number_of_p_descendants_log10(element: Element):
    """
    get number of p tags, to log10
    :param element:
    :return:
    """
    if element is None:
        return 0
    return np.log10(number_of_p_descendants(element))


def number_of_a_descendants(element: Element):
    if element is None:
        return 0
    return len(element.xpath('.//a'))


def number_of_punctuation(element: Element):
    if element is None:
        return 0
    text = ''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    punctuations = [c for c in text if c in PUNCTUATION]
    return len(punctuations)


def number_of_descendants(element: Element):
    if element is None:
        return 0
    return len(list(descendants(element, including=False)))


def number_of_siblings(element: Element):
    if element is None:
        return 0
    return len(list(siblings(element, including=False)))


# todo syj 跑个单元测试验证下
def number_of_clusters(element: Element, tags=None):
    from ..extractors.list import LIST_MIN_NUMBER, LIST_MAX_LENGTH, LIST_MIN_LENGTH, \
        SIMILARITY_THRESHOLD
    if element is None:
        return 0
    if tags and not isinstance(tags, (list, tuple)):
        logging.error('you must pass tags args as list or tuple')
    descendants_tree = defaultdict(list)
    descendants = descendants_of_body(element)
    for descendant in descendants:
        if descendant.number_of_siblings + 1 < LIST_MIN_NUMBER:
            continue
        if descendant.a_descendants_group_text_min_length > LIST_MAX_LENGTH:
            continue
        if descendant.a_descentdants_group_text_max_length < LIST_MIN_LENGTH:
            continue
        if descendant.similarity_with_siblings < SIMILARITY_THRESHOLD:
            continue
        if tags and descendant.tag not in tags:
            continue
        descendants_tree[descendant.parsent_selector].append(descendant)
    return len(descendants_tree)


def number_of_children(element: Element):
    if element is None:
        return 0
    return len(list(children(element)))


def density_of_text(element: Element):
    """
    get density of text, using:
               number_of_char - number_of_a_char
    result = ------------------------------------------
               number_of_descendants - number_of_a_descendants
    :return:
    """
    # if denominator is 0, just return 0
    if element.number_of_descendants - element.number_of_a_descendants == 0:
        return 0
    return (element.number_of_char - element.number_of_a_char) / \
           (element.number_of_descendants - element.number_of_a_descendants)


def similarity_with_element(element1: Element, element2: Element):
    """
    get similarity between two elements
    :param element1:
    :param element2:
    :return:
    """
    alias1 = element1.alias
    alias2 = element2.alias
    # TODO: use better metrics to compare the two elements
    return similarity(alias1, alias2)


def similarity_with_siblings(element: Element):
    scores = []
    for sibling in siblings(element):
        scores.append(similarity_with_element(element, sibling))
    if not scores:
        return 0
    return np.mean(scores)


def density_of_punctuation(element: Element):
    """
    get density of punctuation, using
                number_of_char - number_of_linked_char
    result = -----------------------------------------
                 number_of_punctuation + 1
    :param element:
    :return:
    """
    result = (element.number_of_char - element.number_of_a_char) / \
             (element.number_of_punctuation + 1)
    # result should not be zero
    return result or 1


def alias(element: Element):
    """
    get alias of element, concat tag and attribs
    :param element:
    :return:
    """
    if element is None:
        return ''
    tag = element.tag
    if tag in ['html', 'body']:
        return tag
    attribs = [tag]
    for k, v in element.attrib.items():
        k, v = re.sub(r'\s*', '', k), re.sub(r'\s*', '', v)
        attribs.append(f'[{k}="{v}"]' if v else f'[{k}]')
    result = ''.join(attribs)
    nth = len(list(element.itersiblings(proceding=True))) + 1
    result += f':nth-child({nth})'
    return result
