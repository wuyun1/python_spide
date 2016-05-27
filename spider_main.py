

class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self, arg):
		super(SpiderMain, self).__init__()
		self.arg = arg
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader
	def  craw(self,root_url):
		pass
		


if __name__ == '__main__':
	root_url = "http://baike.baidu.com/view/3974030.htm"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
