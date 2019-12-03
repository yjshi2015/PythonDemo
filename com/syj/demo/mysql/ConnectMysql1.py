# coding=utf-8

import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='syjmysql2015', db='spider_db',
                      port=3306, charset='utf8')
cur = con.cursor()
'''
create table song_comments(
	id int not null auto_increment primary key comment '主键',
    song_id bigint not null comment '歌曲id',
    song_name varchar(60) not null comment '歌曲名称',
    song_link varchar(240) comment '歌曲链接',
    user_id varchar(120) comment '评论人id',
    nick_name varchar(240) comment '评论人昵称',
    comment_id bigint comment '评论id',
    content varchar(1024) comment '评论内容',
    dian_zan int comment '点赞数',
    comment_time bigint comment '评论时间',
    create_date varchar(60) default null,
    created varchar(60) default null,
    modify_date varchar(60) default null,
    modified varchar(60) default null,
    index (`song_id`, `dian_zan`))
comment '歌曲评论信息表';
'''

cur.executemany('insert into song_comments(song_id, song_name, song_link, user_id, nick_name,'
                'comment_id, content, dian_zan, comment_time, create_date, created) '
                'values(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)',
                [(1, '世界名画与你环环相扣', 'music.163.com', 110, 'nick_name', 10000, '真好听', 999, 20191203,
                  '20191203', 'syj')])
con.commit()
print '--------->数据写入成功ok'

cur.execute('select * from song_comments')
res = cur.fetchall()
for line in res:
    print line