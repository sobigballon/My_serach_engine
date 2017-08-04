import crawler
def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None
'''def test():
    seed="http://www.sobigballon.com/bigballon/index.html"
    index=crawler.crawl_web(seed)
    print lookup(index,'is')

test()'''
