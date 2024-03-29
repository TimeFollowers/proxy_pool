import json
from utils import get_page
from pyquery import PyQuery as pq

class ProxyMetaclass(type):
    def __new__(cls, name, bases,attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls,name,bases,attrs)

class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print("获取代理成功",proxy)
            proxies.append(proxy)
        return proxies
    def crawl_daili66(self,page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = "http://www.66ip.cn/{}.html"
        urls = [start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            print("crawling",url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc(".containerbox table tr:gt(0)").items()
                for tr in trs:
                    ip = tr.find("td:nth-child(1)").text()
                    port = tr.find("td:nth-child(2)").text()
                    print("66:",ip,port)
                    yield ip+":"+port

    def crawl_proxy360(self):
        """
        获取proxy360
        :return: 代理
        """
        start_url = "http://www.proxy360.cn/Region/China"
        print("Crawling",start_url)
        html = get_page(start_url)
        if html:
            doc = pq(html)
            print("crawling",start_url)
            lines = doc("div[name='list_proxy_ip']").items()
            for line in lines:
                ip = line.find(".tdBottomLine:nth-child(1)").text()
                port = line.find(".tdBottomLine:nth-child(2)").text()
                print("360:",ip,port)
                yield ip+":"+port

    def crawl_goubanjia(self):
        """
        获取Goubanjia
        :return: 代理
        """
        start_url = "http://www.goubanjia.com/free/gngn/index.html"
        html = get_page(start_url)
        if html:
            doc = pq(html)
            tds = doc('td.ip').items()
            for td in tds:
                td.find("p").remove()
                print("goubanjia",td.text())
                yield td.text().replace(" ","")