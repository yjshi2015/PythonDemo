import numpy as np
from lxml import etree
from loguru import logger
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.schemas.element import Element
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.preprocess import \
    preprocess4content_extract
from base import BaseExtractor
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.element import descendants_of_body


class ContentExtractor(BaseExtractor):

    def process(self, element: Element):
        # 1.预处理
        preprocess4content_extract(element)

        element_infos = []
        '''
        -----------注意-----------
        descendants不仅包含了最底层的
        不可展开的子节点，还包含了父、
        祖父、祖祖父……之类的节点
        -----------注意-----------
        '''
        descendants = descendants_of_body(element)
        # 所有子节点的文本密度
        density_of_text = [descendant.density_of_text for descendant in descendants]
        # 方差？
        density_of_text_std = np.std(density_of_text, ddof=1)

        # 计算密度得分
        for descendant in descendants:
            score = np.log(density_of_text_std) * \
                    descendant.density_of_text * \
                    np.log10(descendant.number_of_p_descendants + 2) * \
                    np.log(descendant.density_of_punctuation)
            descendant.density_score = score

        # 排序
        descendants = sorted(descendants, key=lambda x: x.density_score, reverse=True)
        '''
        -----------注意-----------
        得分最高的不一定是最底层的不可展
        开的子节点，有可能是某个父/祖父/祖祖父节点
        -----------注意-----------
        '''
        descendant_first = descendants[0] if descendants else None
        if descendant_first is None:
            return None

        # html_str = etree.tostring(element).decode('utf-8')
        # logger.info('--------' + html_str)

        selected_node = etree.tostring(descendant_first).decode('utf-8')
        logger.info('--------' + selected_node)

        for i in range(0, 10):
            top10 = etree.tostring(descendants[i])
            class_attr = descendants[i].xpath('./@class')
            score = descendants[i].density_score
            logger.info('class = ' + ''.join(class_attr)
                        + '，score:' + str(score)
                        + ', 文本密度:' + str(descendants[i].density_of_text)
                        + ', 符号密度:' + str(descendants[i].density_of_punctuation))

        # 获取新闻内容
        paragraphs = descendant_first.xpath('.//p//text()')
        paragraphs = [paragraph if paragraph.strip() else '' for paragraph in paragraphs]
        paragraphs = list(filter(lambda x: x, paragraphs))
        text = '\n'.join(paragraphs)
        text = text.strip()
        return text


content_extract = ContentExtractor()


def extract_content(html):
    return content_extract.extract(html)


if __name__ == '__main__':
    with open('../detail.html', encoding='utf-8') as f:
        content = extract_content(f.read())
    print(content)