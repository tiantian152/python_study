#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# 输出：
# (0, 3)
# None