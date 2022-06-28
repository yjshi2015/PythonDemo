from difflib import SequenceMatcher

'''
    字符串匹配函数，http://www.manongjc.com/detail/30-lfmfwwdgxwmspug.html
'''

def lcs_of_2(a, b):
    """
    get longest common string
    :param a:
    :param b:
    :return:
    """
    match = SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))
    return a[match[0]: match[0] + match[2]]


def lcs_of_list(*args):
    if len(args) == 2:
        return lcs_of_2(args[0], args[1])
    first = args[0]
    remains = args[1:]
    return lcs_of_2(first, lcs_of_list(*remains))