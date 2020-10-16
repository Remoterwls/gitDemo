#!usr/bin/env python
#encoding:utf-8
'''
__Author__:
功能：
'''
# import zmail
#
# mail_content = {'subject': 'successful',
#                 'content_text': 'This Message From Zmail'}
# server = zmail.server('1052042663@qq.com', 'Wls49772')
# server.send_mail('1052042663@qq.com', mail_content)

import zmail

# 你的邮件内容
mail_content = {
    'subject': 'Hello world! Success!',  # 随便填写

    'content_text': 'This message from zmail!',
    'attachments': r'C:\Users\jackw\Desktop\auto.gif'
}

# 使用你的邮件账户名和密码登录服务器

server = zmail.server('1052042663@qq.com', 'elrtsjwetqtrbfhd')
# 发送邮件
server.send_mail('wucc@fusionskye.com', mail_content)
#给多个邮箱发送
#server.send_mail(['555555@qq.com','666666@qq.com'], mail_content)