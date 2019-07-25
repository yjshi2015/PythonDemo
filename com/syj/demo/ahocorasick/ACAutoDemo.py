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


if __name__ == '__main__':
    words = ['王俊凯', '俊凯', '凯凯', '小凯']
    acDemo = ACAutoDemo(words)
    matchedWords = acDemo.match_all_word('王俊凯好棒哦,加油,你最棒')
    for matched in matchedWords:
        print matched