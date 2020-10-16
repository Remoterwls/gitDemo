#!usr/bin/env python
#encoding:utf-8
'''
__Author__:海阔天空
功能：
'''
import random


class DataGenerate(object):
    # 随机生成1个手机号
    def create_phone(self):
        seed = '0123456789'
        phone_list = []
        for i in range(8):
            phone_list.append(random.choice(seed))
        phone_data = '166' + "".join(phone_list)
        return phone_data

phone_list = '   2343   243   '
phone_data = '166' + "".join(phone_list)
phone_list=str.center('12',2)
print(phone_list)
print(phone_data)


# seed = '0123456789'
# s =random.random()
# print('random.random:',s)
# s1 = random.choice(seed)
# print('random.choice:',s1)
# s2 = random.choices(seed, weights=[10, 1, 1, 3, 5, 7, 1, 1, 8, 9], k=3)
# print('random.choices:',s2)
# s3 = random.randint(1,100)
# print('random.randint:',s3)
# s4 = random.uniform(3,9)
# print('random.uniform:',s4)
# s5 = random.sample(seed,2)
# print('random.sample:',s5)
# s6 = random.seed(seed,3)
# s6 =random.random()
# print(s6)
# # s7 = random.randrange(seed,2)
# # print('random.randrange:',s7)
# s8 = random.shuffle(list(seed))
# print('排序：',s8)