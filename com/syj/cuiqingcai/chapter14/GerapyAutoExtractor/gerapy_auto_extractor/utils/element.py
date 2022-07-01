import logging
import re
import numpy as np
from os.path import exists
from types import ModuleType
from collections import defaultdict
from loguru import logger
from lxml.html import fromstring, HtmlElement, HtmlComment
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.schemas.element import Element
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.similarity import similarity

PUNCTUATION = set('''！，。？、；：“”‘’《》%（）<>{}「」【】*～`,.?:;'"!%()''')


def remove_element(element: Element):
    if element is None:
        return
    p = element.getparent()
    if p is not None:
        p.remove(element)


def remove_children(element: Element, *xpaths):
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
    if element.xpath('./@class') == 'ne_areane_index_area':
        logger.info('逮到了……')
    descendants = []
    # todo syj 这种方式包含了子节点及其本身？
    for descendant in element.xpath('.//a'):
        descendant.__class__ = Element
        descendants.append(descendant)
    return descendants


def a_descendants_group(element: Element):
    ''' 注意：syj
    <html>
        <body>
            <div>
                <ul>
                    <li><a>node1</a></li>
                    <li><a>node2</a></li>
                    <li><a>node3</a></li>
                    <li><a>node4</a></li>
                </ul>
            </div>
        </body>
    </html>
    针对以上html，获取各节点的子孙a节点，及a节点的绝对路径，结果如下：
    节点html子孙a节点 = [a_node1, a_node2, a_node3, a_node4], a_path_raw = html/body/div/ul
    节点body子孙a节点 = [a_node1, a_node2, a_node3, a_node4], a_path_raw = html/body/div/ul
    节点div 子孙a节点 = [a_node1, a_node2, a_node3, a_node4], a_path_raw = html/body/div/ul
    节点ul  子孙a节点 = [a_node1, a_node2, a_node3, a_node4], a_path_raw = html/body/div/ul
    节点li1 子孙a节点 = [], path_raw = a_html/body/div/ul/li
        …………
    节点li4 子孙a节点 = [], path_raw = a_html/body/div/ul/li

    会发现，不管从哪个节点的角度去查看a节点，a节点的绝对路径都是固定的，因此以a节点的路径作为dict的key，就能起到聚合作用
    :param element:
    :return:
    '''
    result = defaultdict(list)
    for linked_descendant in element.a_descendants:
        # 注意
        # ①这里是以a节点的路径作为key，而非当前element的路径做key，因此能起到聚合作用
        # ②这里没有使用alias或者path，就是为了让多个分组（在同一个层级）再聚合
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
        # 移除注释的节点
        if isinstance(descendant, HtmlComment):
            remove_element(descendant)
            continue
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
    text = re.sub(r'\s*', '', text, flags=re.S)
    return text


def text_len(element: Element, xpath):
    result = 0
    if element is None:
        return 0
    texts = element.xpath(xpath)
    word_pattern = re.compile(r'[A-Za-z0-9_-]+\b')
    for text in texts:
        if text is None: continue
        logger.info('**********text:' + text)
        # 1.判断语言类型
        english_words = re.findall(word_pattern, text)
        english_words_len = len(''.join(english_words).strip())
        text_len = len(text)
        words_rate = english_words_len / text_len
        # 2.按语言类型计算长度
        text = re.sub(r'\s*', '', text, flags=re.S)
        if words_rate > 0.5:
            real_text_len = len(text) - english_words_len + len(english_words)
        else:
            real_text_len = len(text)
        # 3.长度累加
        logger.info('**********real_text_len:' + str(real_text_len))
        result += real_text_len
    return result


if __name__ == '__main__':
    # text = '他说 are you ok ic-9?'
    # text = '他说哈哈~'
    text = 'Notice: The content above (including the videos, pictures and audios if any) is uploaded and posted by the user of Dafeng Hao, which is a social media platform and merely provides information storage space services.”'
    # 1.判断语言类型
    pattern = re.compile(r'[A-Za-z0-9_-]+\b')
    english_words = re.findall(pattern, text)
    english_words_len = len(''.join(english_words).strip())
    english_words_times = len(english_words)
    text_len = len(text)
    rate = english_words_len / text_len
    print(text_len)
    print(english_words)
    print(english_words_len)
    print(english_words_times)
    print(rate)

    # 2.按语言类型计算长度
    text = re.sub(r'\s*', '', text, flags=re.S)
    print(text)
    print(len(text))
    if rate > 0.5:
        real_text_len = len(text) - english_words_len + len(english_words)
    else:
        real_text_len = len(text)

    print(real_text_len)


def number_of_char(element: Element):
    """
    get number of char, for example, result of `<a href="#">hello</a>world` = 10
    :param element:
    :return: length
    """
    if element is None:
        return 0
    # return len(text(element))
    return text_len(element, './/text()')


def number_of_a_char(element: Element):
    """
    get number of linked char, for example, result of `<a href="#">hello</a>world` = 5
    :param element:
    :return: length
    """
    if element is None:
        return 0
    text = ''.join(element.xpath('.//a//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    # return len(text)
    return text_len(element, './/a//text()')


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
        k, v = re.sub(r'\s*', '', k, flags=re.S), re.sub(r'\s*', '', v, flags=re.S)
        attribs.append(f'[{k}="{v}"]' if v else f'[{k}]')
    result = ''.join(attribs)
    nth = len(list(element.itersiblings(preceding=True))) + 1
    result += f':nth-child({nth})'
    return result
