#coding=utf-8
import urllib.request


class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None

        full_url = "http://m.yinhangzhaopin.com/m/" + str(url) + ".htm"
        print(full_url)
        response = urllib.request.urlopen(full_url)

        response.encoding = 'gb2312'

        if response.getcode() != 200:
            return None
        return  response.read()