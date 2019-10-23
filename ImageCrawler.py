from icrawler.builtin import BauduImageCrawler

baidu_storage = {'root_dir': 'your root'}
baidu_crawler = BaiduImageCrawler(parser_threads = 2, downloader_threads =2,
                                  storage = baidu_storage
                        )
baidu_crawler.crawl(keyword = '杰尼龟',
                    max_num = 100)

###这个包是一个MIT大佬写的，附上大佬包的链接https://github.com/hellock/icrawler
