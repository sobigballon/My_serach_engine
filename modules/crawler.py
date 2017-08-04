def get_page(url): #becasuse do not have some seed page
    try:
        if url == "http://www.sobigballon.com/bigballon/index.html":
            return '''<html> <body> This is a test page for learning to crawl!
<p> It is a good idea to
<a href="http://www.sobigballon.com/bigballon/crawling.html">
learn to crawl</a> before you try to
<a href="http://www.sobigballon.com/bigballon/walking.html">walk</a> or
<a href="http://www.sobigballon.com/bigballon/flying.html">fly</a>.</p></body></html>'''

        elif url == "http://www.sobigballon.com/bigballon/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http://www.sobigballon.com/bigballon/kicking.html">kicking</a>.
</body> </html>'''

        elif url == "http://www.sobigballon.com/bigballon/walking.html":
            return '''<html> <body> I cant get enough
<a href="http://www.sobigballon.com/bigballon/index.html">crawling</a>!</body></html>'''

        elif url == "http://www.sobigballon.com/bigballon/flying.html":
            return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""

def crawl_web(seed):  #crawl_function
    tocrawl = [seed]  #use list as a queue
    crawled = []      
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def union(a, b): #prevent the 'page' repeat,maybe use the set() more convenient
    for e in b:
        if e not in a:
            a.append(e)
            


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:  #if keyword already exists
            for entry_u in  entry[1]:
                if entry_u[0]==url: #if the url already exists
                    return
            entry[1].append([url]) 
            return
    # not found, add new keyword to index
    index.append([keyword, [url]]) 

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

'''def test():
    seed="http://www.sobigballon.com/bigballon/index.html"
    return crawl_web(seed)

print test()'''
