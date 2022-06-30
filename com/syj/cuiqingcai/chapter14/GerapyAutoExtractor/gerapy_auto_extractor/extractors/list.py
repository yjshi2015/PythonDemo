import math
import operator
from loguru import logger
import numpy as np
from collections import defaultdict
from urllib.parse import urljoin
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.cluster import cluster_dict
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.preprocess import \
    preprocess4list_extractor
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.extractors.base import BaseExtractor
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.utils.element import descendants_of_body
from com.syj.cuiqingcai.chapter14.GerapyAutoExtractor.gerapy_auto_extractor.schemas.element import Element

LIST_MIN_NUMBER = 5
LIST_MIN_LENGTH = 8
LIST_MAX_LENGTH = 44
SIMILARITY_THRESHOLD = 0.8


class ListExtractor(BaseExtractor):

    def __init__(self, min_number=LIST_MIN_NUMBER, min_length=LIST_MIN_LENGTH, max_length=LIST_MAX_LENGTH,
                 similarity_threshold=SIMILARITY_THRESHOLD):
        super(ListExtractor, self).__init__()
        self.min_number = min_number
        self.min_length = min_length
        self.max_length = max_length
        self.avg_length = (self.max_length + self.min_length) / 2
        self.similarity_threshold = similarity_threshold

    def _probability_of_title_with_length(self, length):
        """
        get the probability of title according to length
        import matplotlib.pyplot as plt
        x = np.asarray(range(5, 40))
        y = list_extractor.probability_of_title_with_length(x)
        plt.plot(x, y, 'g', label='m=0, sig=2')
        plt.show()
        :param length:
        :return:
        """
        sigma = 6
        return np.exp(-1 * ((length - self.avg_length) ** 2) / (2 * (sigma ** 2))) / (math.sqrt(2 * np.pi) * sigma)

    def _build_clusters(self, element):
        descendants_tree = defaultdict(list)
        descendants = descendants_of_body(element)
        for descendant in descendants:
            # todo syj
            #  此条件保留了子节点（不能再展开的子节点），排除了父/祖父/祖祖父这样的节点
            if descendant.number_of_siblings < self.min_number:
                continue
            # 此条件保留了父/祖父/祖祖父节点，与第一个条件冲突
            if descendant.a_descendants_group_text_min_length > self.max_length:
                continue
            if descendant.a_descendants_group_text_max_length < self.min_length:
                continue
            # 此条件针对子节点，排除了
            if descendant.similarity_with_siblings < self.similarity_threshold:
                continue
            descendants_tree[descendant.parent_selector].append(descendant)
        descendants_tree = dict(descendants_tree)

        # 默认排序，即路径最短最靠前
        selectors = sorted(list(descendants_tree.keys()))
        last_selector = None
        # 倒序，剔除最短的路径元素
        for selector in selectors[::-1]:
            if last_selector and selector and last_selector.startswith(selector):
                # 字典的删除方法
                del descendants_tree[selector]
            last_selector = selector
        # 重要，对字典按相似度分组，key为分组号，value为list结构
        clusters = cluster_dict(descendants_tree)
        return clusters

    def _evaluate_cluster(self, cluster):
        '''
        计算每簇的得分，根据成员节点数量、平均字数分步、文本密度、相似度等，具体可以自行设计
        :param cluster:
        :return:
        '''
        score = dict()
        score['avg_similarity_with_siblings'] = np.mean(
            [element.similarity_with_siblings for element in cluster]
        )
        score['number_of_elements'] = len(cluster)

        score['clusters_score'] = \
            score['avg_similarity_with_siblings'] \
            * np.log10(score['number_of_elements'] + 1) \
            # * clusters_score[cluster_id]['probability_of_title_with_length']
        return score

    def _extend_cluster(self, cluster):
        '''
        寻找遗留的节点
        :param cluster:
        :return:
        '''
        result = [element.selector for element in cluster]
        for element in cluster:
            path_raw = element.path_raw
            siblings = list(element.siblings)
            for sibling in siblings:
                if not isinstance(sibling, element): continue
                sibling_selector = sibling.selector
                sibling_path_raw = sibling.path_raw
                if sibling_path_raw != path_raw: continue

                if sibling_selector not in result:
                    cluster.append(sibling)
                    result.append(sibling_selector)

        cluster = sorted(cluster, key=lambda x: x.nth)
        logger.log('inspect', f'cluster after extend {cluster}')
        return cluster

    def _best_cluster(self, clusters):
        '''
        寻找得分最高的分组
        :param clusters:
        :return:
        '''
        if not clusters:
            logger.error('there is no clusters, just return empty []')
        if len(clusters) == 1:
            logger.info('there is only one cluster, just return first cluster')
            # 按分组号返回
            return clusters[0]
        clusters_score = defaultdict(dict)
        clusters_score_max = -1
        clusters_score_max_group = 0
        for cluster_id, cluster in clusters.item():
            # 计算当前组的得分
            clusters_score[cluster_id] = self._evaluate_cluster(cluster)
            # 获取最大得分
            if clusters_score[cluster_id]['clusters_score'] > clusters_score_max:
                clusters_score_max = clusters_score[cluster_id]['clusters_score']
                clusters_score_max_group = cluster_id
        bset_cluster = clusters[clusters_score_max_group]
        return bset_cluster

    def _extract_cluster(self, cluster):
        if not cluster:
            return None
        probabilities_of_title = defaultdict(list)
        for element in cluster:
            descendants = element.a_descendants
            for descendant in descendants:
                path = descendant.path
                descendant_txt = descendant.text
                probability_of_title_with_lenth = self._probability_of_title_with_length(len(descendant_txt))
                probability_of_title = probability_of_title_with_lenth
                probabilities_of_title[path].append(probability_of_title)

        probabilities_of_title_avg = {k: np.mean(v) for k, v in probabilities_of_title.items()}
        if not probabilities_of_title_avg:
            return None
        # todo syj 啥意思
        best_path = max(probabilities_of_title_avg.items(), key=operator.itemgetter(1))[0]
        logger.log('inspect', f'best tag path {best_path}')

        result = []
        for element in cluster:
            descendants = element.a_descendants
            for descendant in descendants:
                path = descendant.path
                if path != best_path: continue
                title = descendant.text
                url = descendant.attrib.get('href')
                if not url: continue
                if url.startswith('//'):
                    url = 'http:' + url
                base_url = self.kwargs.get('base_url')
                if base_url:
                    url = urljoin(base_url, url)
                result.append({
                    'title': title,
                    'url': url
                })
        return result

    def process(self, element: Element):

        preprocess4list_extractor(element)

        clusters = self._build_clusters(element)
        logger.log('inspect', f'after build clusters {clusters}')

        best_cluster = self._best_cluster(clusters)
        logger.log('inspect', f'best cluster {best_cluster}')

        extended_cluster = self._extend_cluster(best_cluster)
        logger.log('inspect', f'extended cluster {extended_cluster}')

        return self._extract_cluster(best_cluster)


list_extractor = ListExtractor()


def extract_list(html, **kwargs):
    return list_extractor.extract(html, **kwargs)
