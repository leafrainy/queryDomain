#coding:utf8
# 域名批量查询
# 注意：因API局限性，仅支持部分域名
# 2017-03-21
# leafrainy (leafrainy.cc)  

import requests
import time  
import json
import sys
reload(sys)  
sys.setdefaultencoding('utf8')


#查询域名是否可用
def queryDomainStatus(domainLastName):

    s = requests.Session()
    queryUrl = "http://www.yumingco.com/api"
    allWord = "abcdefghijklmnopqrstuvwxyz"
    allTuple = tuple(allWord)

    #2-3字母
    for firstWord in allTuple:
        for twoWord in allTuple:
            allData2 = s.get(queryUrl,params={'domain':firstWord+twoWord,'suffix':domainLastName})
            getDomainStatus(allData2,firstWord+twoWord,domainLastName)
            for threeWord in allTuple:
                allData3 = s.get(queryUrl,params={'domain':firstWord+twoWord+threeWord,'suffix':domainLastName})
                getDomainStatus(allData3,firstWord+twoWord+threeWord,domainLastName)
                goSleep()
            goSleep()
        goSleep()

#查询域名状态
def getDomainStatus(allData,domainHead,domainLastName):
    domain = domainHead+"."+domainLastName
    if json.loads(allData.text)['status']:
        print domain+"--->查询正常"
        if json.loads(allData.text)['available']:
            print domain+"--->可以注册"
            writeToFile(domain+"\n")

#写文件
def writeToFile(domainName):
	f = open('domain.txt','a')
	f.write(domainName)
	f.close()

#休息时间
def goSleep():
    time.sleep(0.3)

if __name__ == "__main__":
    domainLastName = "run"
    queryDomainStatus(domainLastName)