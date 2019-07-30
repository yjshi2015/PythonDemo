# coding=utf-8

import ahocorasick
from timeit import default_timer

class ACAutoDemo(object):

    def __init__(self, words):
        self.WORDS = words
        self.AC = ahocorasick.Automaton()
        bts = default_timer()
        self.build_trie()
        print('build tire tree use: {0} s'.format(default_timer() - bts))
        self.AC.make_automaton()
        print('build automaton use {0} s'.format(default_timer() - bts))

    def build_trie(self):
        print(type(self.WORDS))
        print(type(self.WORDS).__name__)
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
            print 'value---------------' + value
            print end_inx
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


if __name__ == '__main__':
    words = ['王俊凯', '俊凯', '凯凯', '小凯']

    wordsDict = {}
    wordsDict['小凯'] = '王俊凯'
    wordsDict['凯爷'] = '王俊凯'


    acDemo = ACAutoDemo(wordsDict)
    matchedWords, matchedDict = acDemo.match_all_word('王俊凯好棒哦,加油,王俊凯你最棒')
    print '最终结果--------->'
    print matchedWords
    print matchedDict
    for matched in matchedWords:
        print matched