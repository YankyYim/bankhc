#coding=utf-8
from bs4 import BeautifulSoup

class HtmlParser(object):


    def _get_new_url(self, page_url, soup):
        new_urls = set()
        new_urls.add(page_url+1)
        return new_urls


    def _get_new_detail(self, page_url, soup):

        #
        new_detail= soup.find("aside")

        return new_detail

    def _get_new_data(self, page_url, soup):
        res_data ={}
        title_node = soup.find("h1")
        res_data['tittle'] = title_node.get_text()

       # < div style = "text-align:center; margin-bottom:10px; color:#ccc" > 发布时间：2018 - 07 - 20:09:41 < / div >


        time_node = soup.find("div",style="text-align:center; margin-bottom:10px; color:#ccc")
        res_data['time'] = time_node.get_text()

        # h3 a标签 <h3><span></span>最新招聘 > <a href=" /wzcb/ "> 温州银行招聘 </a></h3>
        bank_node = soup.find("h3").find("a")
        res_data["bank"] = bank_node.get_text()

        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup  = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb2312')
        new_urls = self._get_new_url(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        new_detail = self._get_new_detail(page_url,soup)

        # print(new_data)

        return new_data, new_detail


