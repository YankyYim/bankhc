#coding=utf-8
import html_download
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):

        count = 1
        new_url = root_url
        #self.urls.add_new_url(root_url)
        while new_url >= root_url: #self.urls.has_new_url():
            try:
                #new_url = self.urls.get_new_url()
                if new_url==75158:
                    break


                print( 'craw %d :%d' %(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_data,new_detail = self.parser.parse(new_url,html_cont)

                #self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data,new_url)
                self.outputer.output_html(new_detail)

            except:
                print("craw failed")

            finally:

                count = count+1
                new_url = new_url+1
                #self.outputer.output_html()


if __name__ == "__main__":
    root_url = 59664
    #root_url="http://m.yinhangzhaopin.com/m/74526.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    