# -*- coding: cp936 -*-

import cookielib
import urllib2, urllib
import time
import re
import traceback
import random

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), 
                     ('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'), 
                     ('Connection', 'keep-alive')
                     ]
opener.addheaders.append( ('Accept-encoding', 'identity') )
opener.addheaders.append( ('Referer', '') )


def get_page(url, data=None):
    resp = None
    n = 0
    while n < 5:
        n = n + 1
        try:
            resp = opener.open(url, data, timeout=10)
            page = resp.read()
            return page
        except:
            #traceback.print_exc()
            print "Will try after 2 seconds ..."
            time.sleep(2.0)
            continue
        break
    return "Null"

url = "http://shankungfu.org/account/ajax/register_process/"

success_num = 0
total_num = 0

print "============ 注册精灵 v1.1 =============="


i = input("请输入最小时间间隔(秒):")
j = input("请输入最大时间间隔(秒):")

n = raw_input("请输入最大注册次数(默认为无限循环):")

while True:
    try:
        s = "".join(random.sample('zyxwvutsrqponmlkjihgfedcba',random.randint(4, 12)))
        c = random.choice(["163", "gmail", "qq", "126", "yahoo", "hotmail", "sina"])
        
        email = "%s@%s.com"%(s, c)
        password = "123456"
        user_name = s
        category = str(random.randint(1, 27))
        fit = str(random.randint(1, 5))
        skill = str(random.randint(1, 20))

        print email

        formData = urllib.urlencode({'email' : email,
                                     'password' : password,
                                     'user_name' : user_name,
                                     'category[]' : category,
                                     'fit[]' : fit,
                                     'skill[]' : skill,
                                     'agreement_chk' : "agree",
                                     '_post_type' : "ajax"
                                     })
        p = get_page(url, formData)

        total_num += 1
        if "valid_email" in p:
            success_num += 1
            
        print "%d / %d"%(success_num, total_num)


        if n:
            if success_num >= int(n):
                break

        t = random.randint(i, j)
        time.sleep(t)
    except:
        traceback.print_exc()
        


print "============ 完成！ ================="

raw_input()

    
