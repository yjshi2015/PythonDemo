#!usr/bin/python3
# -*- coding:utf-8 -*-
import re
import datetime
import os
import sys
import zipfile
import ahocorasick
from timeit import default_timer
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import HiveContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
#ss = SparkSession.builder.appName("ip_pw_extract").enableHiveSupport().getOrCreate()
#sc = ss.sparkContext
conf = SparkConf().setAppName("ip_extract").setMaster("yarn-cluster")
sc = SparkContext.getOrCreate(conf)
sqlContext = HiveContext(sc)
today = datetime.date.today() 
oneday = datetime.timedelta(days=1) 
yesterday = today - oneday
last_date = yesterday.strftime('%Y-%m-%d')
class ACAutomaton():
    def __init__(self, words):
        self.WORDS = words
        self.AC = ahocorasick.Automaton()
        bts = default_timer()
        self.build_trie()
        print('build tire tree use: {0} s'.format(default_timer() - bts))
        self.AC.make_automaton()
        print('build automaton use {0} s'.format(default_timer() - bts))

    def build_trie(self):
        if type(self.WORDS).__name__ == 'list':
            for word in self.WORDS:
                self.AC.add_word(word, word)
        if type(self.WORDS).__name__ == 'dict':
            for word, v in self.WORDS.items():
                self.AC.add_word(word, (word, v))

    def match_all_word(self, intext):
        """
        匹配词库中所有的词
        :param intext: 输入字符串
        :return: 输入为list时返回匹配到词的list，输入为dict时返回匹配到词的list和对应的dict
        """
        words = []
        word_dict = {}
        for item in self.AC.iter(intext):
            end_inx, value = item
            if type(self.WORDS).__name__ == 'list':
                word = value
                words.append(word)
            if type(self.WORDS).__name__ == 'dict':
                word, v = value
                words.append(word)
                word_dict[word] = v
        if type(self.WORDS).__name__ == 'list':
            return words
        if type(self.WORDS).__name__ == 'dict':
            return words, word_dict

    def match_word_deduplication(self, intext):
        """
        匹配词库中所有的词，然后去除包含和重合的情况
        :param intext: 输入字符串
        :return: 输入为list时返回匹配到并过滤后词的list，输入为dict时返回匹配到并过滤后词的list和对应的dict
        """
        words = []
        word_dict = {}
        for item in self.AC.iter(intext):
            end_inx, value = item
            if type(self.WORDS).__name__ == 'list':
                word = value
                words.append(word)
            if type(self.WORDS).__name__ == 'dict':
                word, v = value
                words.append(word)
                word_dict[word] = v
        # 去除包含和重合的情况，但是会存在一个问题，就是一个标题中同一个词出现多次无法统计频率
        i = 0
        flag = False
        while i < len(words):
            for j in range(len(words)):
                if j == i:
                    continue
                if words[i] in words[j]:
                    del words[i]
                    flag = True
                    break
            if flag:
                flag = False
                continue
            else:
                i += 1
                flag = False
        if type(self.WORDS).__name__ == 'list':
            return words
        if type(self.WORDS).__name__ == 'dict':
            result_dict = {}
            for word in words:
                result_dict[word] = word_dict[word]
            return words, result_dict

    def maximum_match_word(self, intext):
        """
        匹配词库中所有的词，然后根据每个词的位置，去除在原字符串中同位置被其他词包含的词，其余地方出现的这个词依旧保留
        :param intext: 输入字符串
        :return: 输入为list时返回匹配到并过滤后词的list，输入为dict时返回匹配到并过滤后词的list,对应起止位置list和对应的dict
        """
        words = []
        word_inx_list = []
        word_dict = {}
        for item in self.AC.iter(intext):
            end_inx, value = item
            if type(self.WORDS).__name__ == 'list':
                word = value
                words.append(word)
                word_inx_list.append([end_inx-len(word) + 1, end_inx + 1])
            if type(self.WORDS).__name__ == 'dict':
                word, v = value
                words.append(word)
                word_inx_list.append([end_inx - len(word) + 1, end_inx + 1])
                word_dict[word] = v

        i = 0
        flag = False
        while i < len(words):
            for j in range(len(words)):
                if j == i:
                    continue
                # if word_inx_list[i][0] >= word_inx_list[j][0] and word_inx_list[i][1] <= word_inx_list[j][1]:
                #     del words[i]
                #     del word_inx_list[i]
                #     flag = True
                #     break
                if word_inx_list[j][0] <= word_inx_list[i][0] < word_inx_list[j][1] or word_inx_list[j][0] < word_inx_list[i][1] <= word_inx_list[j][1]:
                    if len(words[i]) < len(words[j]):
                        del words[i]
                        del word_inx_list[i]
                        flag = True
                        break
                    if len(words[i]) == len(words[j]):
                        if i > j:
                            del words[i]
                            del word_inx_list[i]
                            flag = True
                            break
            if flag:
                flag = False
                continue
            else:
                i += 1
                flag = False
        if type(self.WORDS).__name__ == 'list':
            return words, word_inx_list
        if type(self.WORDS).__name__ == 'dict':
            result_dict = {}
            for word in words:
                result_dict[word] = word_dict[word]
            return words, word_inx_list, result_dict

    def replace_to_space(self, matched):
        """
        将匹配到的字符串替换
        :return:
        """
        matched_str = matched.group('en_num')
        if 'polo' in matched_str or 'POLO' in matched_str:
            return matched_str
        else:
            matched_len = len(matched_str)
            return ' ' * matched_len

    def maximum_match_word_without_ennum(self, intext):
        """
        首先在输入中将超过两个字符的连续英文或者数字或单个特殊符号替换为空格，部分保护词，如 polo 等不替换
        匹配词库中所有的词，然后根据每个词的位置，去除在原字符串中同位置被其他词包含的词，其余地方出现的这个词依旧保留
        :param intext: 输入字符串
        :return: 输入为list时返回匹配到并过滤后词的list，输入为dict时返回匹配到并过滤后词的list,对应起止位置list和对应的dict
        """
        intext = re.sub('(?P<en_num>[a-zA-Z0-9]{2,}|[^a-zA-Z0-9\s\u4e00-\u9fa5])', self.replace_to_space, intext)
        words = []
        word_inx_list = []
        word_dict = {}
        for item in self.AC.iter(intext):
            end_inx, value = item
            if type(self.WORDS).__name__ == 'list':
                word = value
                words.append(word)
                word_inx_list.append([end_inx-len(word) + 1, end_inx + 1])
            if type(self.WORDS).__name__ == 'dict':
                word, v = value
                words.append(word)
                word_inx_list.append([end_inx - len(word) + 1, end_inx + 1])
                word_dict[word] = v

        i = 0
        flag = False
        while i < len(words):
            for j in range(len(words)):
                if j == i:
                    continue
                if word_inx_list[i][0] >= word_inx_list[j][0] and word_inx_list[i][1] <= word_inx_list[j][1]:
                    del words[i]
                    del word_inx_list[i]
                    flag = True
                    break
            if flag:
                flag = False
                continue
            else:
                i += 1
                flag = False
        if type(self.WORDS).__name__ == 'list':
            return words
        if type(self.WORDS).__name__ == 'dict':
            result_dict = {}
            for word in words:
                result_dict[word] = word_dict[word]
            return words, word_inx_list, result_dict

    def max_match_cut(self, intext):
        """
        正向最大匹配词库中的词进行分词
        :param intext:
        :return:
        """
        words = ['']
        for i in intext:
            if self.AC.match(words[-1] + i):
                words[-1] += i
            else:
                words.append(i)
        return words

    def max_match_word(self, intext):
        """
        正向最大匹配词库中的词
        :param intext:
        :return:
        """
        result = []
        words = ['']
        flag = False # 判断前一步是否匹配
        for i in intext:
            if self.AC.match(words[-1] + i):
                words[-1] += i
                flag = True
            else:
                if flag:
                    if self.AC.exists(words[-1]):
                        result.append(words[-1])
                words.append(i)
                flag = False
        if self.AC.exists(words[-1]):
            result.append(words[-1])
        return result

def product_ip_pyspark(dt):
    rdd = sqlContext.sql("select a.* from (select item_id,item_name from gdm.gdm_m03_item_sku_da where dt = '"+dt+"' and sku_valid_flag = '1' group by item_id,item_name)a where a.item_name is not NULL").rdd
    sql = "select \
				first_prefer_name,\
				second_prefer_name,\
				third_prefer_name \
			from \
				tmp.tmp_dwm_interest_tag_hierarchy_det_da"
    ip_words = sqlContext.sql(sql).rdd.collect()
    ip_words_set = {}
    for ip_word in ip_words:
        ip_words_set[ip_word['second_prefer_name']] = ip_word['second_prefer_name']
        if ip_word['third_prefer_name'] is None:
            pass
        else:
            word_split = ip_word['third_prefer_name'].split('|')
            for word in word_split:
                ip_words_set[word] = ip_word['second_prefer_name']
    IP_SET = sc.broadcast(ip_words_set)
   # sc.broadcast(IP_SET)
    IP_EXTRACT = ACAutomaton(IP_SET.value)
    def extract_ip_pw(title):
        title = title.strip()
        # 替换特殊空格
        pattern = re.compile(
            '[\u0000-\u001f\u0080-\u00a0\u0378-\u0379\u061c\u180b-\u180e\u2000-\u200f\u202a-\u202f\u205f-\u206f\u3000\ufeff]')
        title = re.sub(pattern, ' ', title)
        # 删除特殊符号
        pattern = re.compile(
            '[\u003f\u007f-\u00af\u00b1-\u00b6\u00b8-\u00d6\u00d8-\u00ff\u0378-\u0379\u0384\u0391-\u0392\u0395-\u0397\u0399-\u039a\u039c-\u039d\u039F\u03a1\u03a4-\u03a5\u03a7\u03dc\u03f3\u03fa\u03ff\u061c\u180b-\u180e\u2000-\u200f\u202a-\u202f\u203b\u2039\u203a\u203c\u203f\u205f-\u206f\u2100-\u2102\u2104-\u215f\u216a-\u222c\u22b0\u22da\u2460-\u26ff\u2700-\u27bf\u3000\u3004\u3020\u3036\u30fb\u3105-\u312d\u3200-\u3370\u337b-\u337f\u33c2\u33c7\u33d8\u33e0-\u33ff\ufe00-\ufe0f\ufeff\uff20-\uff3a\uff41-\uff5a\uff61-\uffdc\uffe1-\uffee]')
        title = re.sub(pattern, '', title)
        # 先将多个空格合并成一个，如果空格前后为汉字，则删除
        title = re.sub(' +', ' ', title)
        title = list(title)
        i = 0
        while i < len(title):
            if title[i] == ' ':
                if 0 < i < len(title)-1:
                    if '\u4e00' <= title[i-1] <= '\u9fff' and '\u4e00' <= title[i+1] <= '\u9fff':
                        del title[i]
                        continue
            i += 1
        title = ''.join(title)
        #IP_EXTRACT = ACAutomation(IP_SET)
        extracted_words, word_inx,words_dict = IP_EXTRACT.maximum_match_word(title)
        # 连续的英文字母或者数字不拆分
        extracted_label = []
        for words,label in words_dict.items():
            extracted_label.append(label)
        return extracted_label

    def map_func(x):
        """
        对于每一条数据 x 的处理方法
        :param x:
        :return: 处理完的返回值
        """
       # IP_EXTRACT = ACAutomaton(IP_SET)
        item_id, item_name = x['item_id'], x['item_name']
        labels = extract_ip_pw(item_name)
        if not labels:
            return
       # result = []
       # for label in set(labels):
       #     result.append(item_id +'\t'+ item_name + '\t'+ label)
       # return '\n'.join(result)
        return item_id, item_name, labels
    result_rdd = rdd.repartition(400).map(lambda x: map_func(x))
    result_rdd = result_rdd.filter(lambda x: x is not None)
    #result_rdd = sqlContext.parallelize(result_rdd)
    schema = StructType([StructField("item_id", StringType(), True),
                        StructField("item_name", StringType(), True),
                        StructField("label", StringType(), True)
                        ])
    data_to_frame = sqlContext.createDataFrame(result_rdd,schema)
    test_data_name = 'data_temp'
    data_to_frame.createOrReplaceTempView(test_data_name)
    final_data_test = "insert overwrite table app.app_spu_label_prefer_dim partition(dt = '" + last_date + "') select * from " + test_data_name
    print("test_data_name done")
    sqlContext.sql("use app")
    sqlContext.sql(final_data_test)
   # sqlContext.stop()
    #os.system("hdfs dfs -rm -r hdfs://ns1007/user/mart_sch/app.db/app_spu_label_prefer_dim/dt={0}".format(dt))
    #sqlContext.sql("ALTER TABLE app.app_spu_label_prefer_dim DROP IF EXISTS PARTITION (dt='{0}')".format(dt))
    #result_rdd.repartition(100).saveAsTextFile("hdfs://ns1007/user/mart_sch/app.db/app_spu_label_prefer_dim/dt=" + dt)
    #sqlContext.sql("alter table app.app_spu_label_prefer_dim add partition(dt='{0}')".format(dt))


if __name__ == '__main__':
    dt = sys.argv[1]
    start_time = datetime.datetime.now()
    product_ip_pyspark(dt)
    end_time = datetime.datetime.now()
    print('time:', str(end_time - start_time))
