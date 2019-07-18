# coding=utf-8

import MySQLdb


class DataOutput(object):

    def __init__(self):
        self.con = MySQLdb.connect(host='localhost', user='root', passwd='syjmysql2015', db='spider_db',
                          port=3306, charset='utf8')
        self.cur = self.con.cursor()
        self.datas = []

    def store_data(self, data):
        '''
        数据存储
        :param data:
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_db('movie_info')

    def output_db(self, table_name):
        '''
        数据入库
        :param table_name:
        :return:
        '''
        for data in self.datas:
            print 'data=============>', data
            print 'type data为元组,但是每个元素都为unicode编码=============>', type(data)
            sql = "insert into movie_info (MovieId,MovieTitle,RatingFinal,ROtherFinal,RPictureFinal,RDirectorFinal,RStoryFinal,Usercount,AttitudeCount,TotalBoxOffice,TodayBoxOffice,Rank,ShowDays,isRelease) values %s  " % (data,)
            print 'sql==============>', sql
            print 'sql.decode("unicode_escape")==============>', sql.decode("unicode_escape")
            # 奇淫技巧解决Unicode反编码后汉字还带u的问题
            self.cur.execute(sql.decode("unicode_escape").replace('u\'', '\''))
            self.datas.remove(data)
            self.con.commit()
            print '--------->数据写入成功ok'

    def output_end(self):
        '''
        关闭连接
        :return:
        '''
        if len(self.datas) > 0:
            self.output_db('movie_info')
        self.con.close()