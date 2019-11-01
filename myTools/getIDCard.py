from bs4 import BeautifulSoup
import re
import requests

class GetIDCard():
    def __init__(self):
        self.mainpage = r'http://www.smggw.com/sx/NewsClass.asp?Page=1&ClassIDOne=28&ClassIDTwo=38&ClassIDThree=0'
        self.soup = None
        self.linklist = []
        self.wholelink = []
        self.totalpage = None
        self.pagelist = []
        self.idcards = {}

    def gettotalpage(self):         #得到总页数
        pagere = r'(?:第)(\d+)(?:页</option>  </select> </td></tr> </table></div>)'
        pagenumber = re.findall(pattern=pagere, string=self.soup)
        self.totalpage = pagenumber[0]

    def getpagelist(self):          #得到每页目录的list
        for i in range(1, int(self.totalpage)+1):
            self.pagelist.append('http://www.smggw.com/sx/NewsClass.asp?Page=' + str(i) + '&ClassIDOne=28&ClassIDTwo=38&ClassIDThree=0')
            print(self.pagelist[i-1])

    def getsoup(self, url):              #得到目录第一页的soup
        re = requests.get(url).text
        return re

    def getlinklist(self, soup):          #得到当前页面所有连接的list
        linklist=[]
        if soup != None:
            self.linklist = re.findall(pattern=r'show\.asp\?id=\w+&ClassIDOne=28&ClassIDTwo=38&ClassIDThree=0', string=self.soup)
        else:
            print('获取soup失败')

    def spelllink(self):            #将当前页面的所有连接的list拼接完整
        for item in self.linklist:
            self.wholelink.append(r'http://www.smggw.com/sx/' + str(item))
        return self.wholelink

    def getIDcard(self,soup):
        sou = BeautifulSoup(soup, 'html.parser')
        content1 = sou.find(id='ContentBody')
        print(content1)
        name = re.findall(pattern='(?:<div>★)(\D+)(?:\d)', string=str(content1))
        idcard = re.findall(pattern=r'[1-9][0-9]{14}|[1-9][0-9]{16}[0-9xX]', string=str(content1))
        print(name)
        print(idcard)
        """
        content2 = content1.find_all('div')
        #print(content2)
        #ll = []
        for item in content2:
            if item.text != '<div> </div>' and item.text != None:
                #ll.append(item.text)
                idcard = re.findall(pattern=r'([1-9][0-9]{14})|([1-9][0-9]{16}[0-9xX])', string=item.text)
                name = re.findall(pattern=r'(?:★)(\D+)(?:[^身])', string=item.text)

                self.idcards[name] = idcard"""
        return self.idcards


if __name__ == '__main__':
    gc = GetIDCard()
    soup = gc.getsoup('http://www.smggw.com/sx/show.asp?id=369636&ClassIDOne=28&ClassIDTwo=38&ClassIDThree=0')
    result = gc.getIDcard(soup)
    print(result)