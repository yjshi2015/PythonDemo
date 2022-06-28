from lxml.html import HtmlElement, etree
from numpy import mean


class Element(HtmlElement):
    _id: int = None
    _selector: str = None
    _parent_selector: str = None
    _alias: str = None
    _tag_name: str = None
    _path: str = None
    _path_raw: str = None
    _children = None
    _parent = None
    _siblings = None
    _descendants = None
    _text = None
    _number_of_char: int = None
    _number_of_a_char: int = None
    _number_of_punctuation: int = None
    _number_of_a_descendants: int = None
    _number_of_p_descendants: int = None
    _number_of_children: int = None
    _number_of_siblings: int = None
    _number_of_descendants: int = None
    _density_of_punctuation: int = None
    _density_of_text: float = None
    _density_score: float = None
    _simimarity_of_siblings: float = None
    _a_descendants: list = None
    _a_descendants_group: dict = None
    _a_descendants_group_text_length: dict = None
    _a_descendants_group_text_min_length: float = None
    _a_descendants_group_text_max_length: float = None

    density_score: float = None

    @property
    def id(self):
        if self._id is not None:
            return self._id
        self._id = hash(self)
        return self._id

    @property
    def nth(self):
        return len(list(self.itersiblings(preceding=True))) + 1

    @property
    def alias(self):
        if self._alias is not None:
            return self._alias
        # self._alias =
