from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.extractors.base import BaseExtractor
from lxml.html import HtmlElement
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.patterns.title import METAS
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.lcs import lcs_of_2
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.similarity import similarity2


class TitleExtractor(BaseExtractor):

    def extract_by_meta(self, element: HtmlElement) -> str:
        for xpath in METAS:
            title = element.xpath(xpath)
            if title:
                return ''.join(title)

    def extract_by_title(self, element: HtmlElement) -> str:
        return ''.join(element.xpath('//title//text()')).strip()

    def extract_by_hs(self, element: HtmlElement) -> str:
        hs = element.xpath('.//h1//text()|//h2//text()|//h3//text()')
        return hs or []

    def extract_by_h(self, element: HtmlElement) -> str:
        for xpath in ['//h1', '//h2', '//h3']:
            children = element.xpath(xpath)
            if not children:
                continue
            child = children[0]
            texts = child.xpath('./text()')
            if texts and len(texts):
                return texts[0].strip()

    def process(self, element: HtmlElement):
        title_extracted_by_metas = self.extract_by_meta(element)
        title_extracted_by_h = self.extract_by_h(element)
        title_extracted_by_hs = self.extract_by_hs(element)
        title_extracted_by_title = self.extract_by_title(element)

        if title_extracted_by_metas:
            return title_extracted_by_metas

        # 相似度得分算法，获取跟title最相似的hs
        title_extracted_by_hs = sorted(title_extracted_by_hs,
                                       key=lambda x: similarity2(x, title_extracted_by_title),
                                       reverse=True)

        # 提取相同字符串算法，获取跟title相同的标题内容
        if title_extracted_by_hs:
            return lcs_of_2(title_extracted_by_hs[0], title_extracted_by_title)

        if title_extracted_by_title:
            return title_extracted_by_title

        return title_extracted_by_h


title_extractor = TitleExtractor()


def extract_title(html):
    title = title_extractor.extract(html)
    return title


if __name__ == '__main__':
    with open('../detail.html', encoding='utf-8') as f:
        title = extract_title(f.read())
    print(title)
