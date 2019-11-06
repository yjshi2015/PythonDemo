# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyimusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    music_id = scrapy.Field()

    # 音乐名称
    music_name = scrapy.Field()

    # 歌手
    singer = scrapy.Field()

    # 评论数
    comment_num = scrapy.Field()


class CommentItem(scrapy.Item):

    music_id = scrapy.Field()

    comment_id = scrapy.Field()

    comment_content = scrapy.Field()

    # 点赞数
    zan_num = scrapy.Field()