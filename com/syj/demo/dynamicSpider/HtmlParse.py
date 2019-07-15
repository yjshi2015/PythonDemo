# coding=utf-8

import json
import re


class HtmlParse(object):

    # 提取网页中的所有电影的链接地址
    def parser_url(self, page_url, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls != None:
            # 将URL去重
            return list(set(urls))
        else:
            return None


    # 根据某部电影的入口链接,解析出动态加载的内容,并提取我们所需要的字段
    '''
    响应体格式如下
    var result_201971492606950 = { "value":{"isRelease":true,"movieRating":{"MovieId":237095,"RatingFinal":7.7,"RDirectorFinal":7.1,"ROtherFinal":8.6,"RPictureFinal":9.1,"RShowFinal":0,"RStoryFinal":7.5,"RTotalFinal":0,"Usercount":543,"AttitudeCount":3382,"UserId":0,"EnterTime":0,"JustTotal":0,"RatingCount":0,"TitleCn":"","TitleEn":"","Year":"","IP":0},"movieTitle":"狮子王","tweetId":0,"userLastComment":"","userLastCommentUrl":"","releaseType":1,"boxOffice":{"Rank":1,"TotalBoxOffice":"2.68","TotalBoxOfficeUnit":"亿","TodayBoxOffice":"3537.4","TodayBoxOfficeUnit":"万","ShowDays":3,"EndDate":"2019-07-14 09:25","FirstDayBoxOffice":"8173.65","FirstDayBoxOfficeUnit":"万"}},"error":null};var movieOverviewRatingResult=result_201971492606950;
    '''
    def parser_json(self, page_url, response):
        # 将"="和";"之间的内容提取出来
        pattern = re.compile(r'=(.*?);')
        # 只取第一个json串
        firstJson = pattern.findall(response)[0]
        if firstJson != None:
            # json模块加载字符串
            value = json.loads(firstJson)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception, e:
                print '解析返回的json串失败', e
                return None
            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url, value)
                else:
                    return self._parser_no_release(page_url, value, isRelease=2)
            else:
                return self._parser_no_release(page_url, value)