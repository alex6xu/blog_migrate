import urllib2
# import 
import html2text
from bs4 import BeautifulSoup as BS
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

blog_url = "http://blog.csdn.net/permike/article/details/70157580"


class Blog(object):
    """docstring for Blog"""
    def __init__(self, url):
        super(Blog, self).__init__()
        self.url = url

    def save(self):
        req = urllib2.Request(self.url)
        logging.info('blog url : [%s]' % self.url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0')
        rsp = urllib2.urlopen(req)
        html = rsp.read()
        formt = BS(html, 'lxml')
        title = formt.find('h1').text.strip()
        # import pdb;pdb.set_trace()
        title_n = title.split('/')
        if len(title_n) > 1:
            title = reduce(lambda x, y: x+y, title_n)

        detail = formt.find('div', id="article_details")
        content = formt.find('div', id="article_content")
        
        if content.div:
            content = content.div

        md = html2text.html2text(content.text)
        filename = 'csdn/' + title.encode("utf-8") + '.md'
        mfile = open(filename, 'w')
        mfile.write(md.encode('utf-8'))
        mfile.close()


if __name__ == "__main__":
    url = "http://blog.csdn.net/permike/article/list/"
    for i in range(3,8):
        import pdb; pdb.set_trace()
        list_url = url + str(i)
        req = urllib2.Request(list_url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0')
        logging.info('list url : [%s]' % list_url)
        rsp = urllib2.urlopen(req)
        html = rsp.read()
        fomat = BS(html, 'lxml')
        
        content = fomat.find('div', id="article_list")
        for item in content.find_all('h1'):
            title = item.span.a.text
            atcurl = 'http://blog.csdn.net' + item.span.a['href']

            blog = Blog(atcurl)
            blog.save()
