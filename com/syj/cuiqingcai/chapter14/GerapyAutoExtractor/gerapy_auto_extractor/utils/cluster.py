from .similarity import similarity
from collections import defaultdict


def cluster(items, threshold=0.9):
    """
    对items(节点的xpath路径)进行聚合，相似度高的路径合为同一组

    clusters是个2维数组，即clusters=[[child1, child3, child5], [child2, child4, child6]]，
    其中1/3/5节点相似度高，2/4/6节点相似度高

    number为聚合后的分组号

    :param items: 不同节点对应的xpath路径，['xpath1', 'xpath2', 'xpath3', 'xpath4',……]
    :param threshold:
    :return: cluster map, 聚合后的分组，如：{[child1, child3, child5]: 0, [child2, child4, child6]: 1}
    """
    number = -1
    clusters_map = {}
    clusters = []
    for name in items:
        # clusters是个2维数组
        for c in clusters:
            if all(similarity(name, w) > threshold for w in c):
                c.append(name)
                # todo syj 如果item是乱序，这种方式number依旧会递增，并不会归入到原始的number下，fix如下
                # group_number = clusters_map[c[0]]
                # clusters_map[name] = group_number
                clusters_map[name] = number

        else:
            number += 1
            clusters.append([name])
            clusters_map[name] = number
    return clusters_map


def cluster_dict(data: dict, threshold=0.8):
    '''
    相似组合并
    :param data: {
        '/html/body/div[@class="main"]/div[1]/ul':[child1, child2, child3]
        '/html/body/div[@class="main"]/div[2]/ul':[child4, child5, child6]
        '/html/body/div[@class="main"]/div[3]/ul':[child7, child8, child9]
        '/html/body/header/div[1]':[child10, child11, child12]
        '/html/body/header/div[2]':[child13, child14, child15]
    }
    :param threshold:
    :return: 最终结果，{
        0:[child1, child2, child3,child4, child5, child6,child7, child8, child9],
        1:[child10, child11, child12]
    }
    '''
    ids = data.keys()
    cluster_map = cluster(ids, threshold)
    result = defaultdict(list)
    for k, v in data.items():
        if isinstance(v, list):
            for c in v:
                result[cluster_map[k]].append(c)
        else:
            result[cluster_map[k]].append(v)
    return dict(result)


if __name__ == '__main__':
    data = {
        '/html/body/div[@class="main"]/div[1]/ul': ['child1', 'child2', 'child3'],
        '/html/body/div[@class="main"]/div[2]/ul': ['child4', 'child5', 'child6'],
        '/html/body/div[@class="main"]/div[3]/ul': ['child7', 'child8', 'child9'],
        '/html/body/header/div[1]': ['child10', 'child11', 'child12'],
        '/html/body/header/div[2]': ['child13', 'child14', 'child15'],
    }
    print(cluster_dict(data, threshold=0.7))