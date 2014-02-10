
from cache import cache
import urllib.request
from html.parser  import HTMLParser
import os
import yaml


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.state = []
        self.href= ""
        self.obj = {}
        self.index = {}
        self.done = False

    def handle_starttag(self, tag, attrs):

        # close unclosed tr
        if self.state == ['html', 'body', 'div', 'div', 'table', 'tr', 'tr',]:
            self.state = ['html', 'body', 'div', 'div', 'table', 'tr',]

        #      print("STATE %s" % self.state)

        if self.done:
            return
        if attrs:

#            print("ATTRS %s" % attrs)
            type_name = attrs[0][0]
            if type_name == "href":
                href = attrs[0][1]                  
                if href[0] == "h" :
                    self.href = href
                else:
                    url = "http://www.mondotimes.com%s" % href
                    self.href = url

        self.href = self.href.strip().rstrip()
        self.href = self.href.replace(" ","%20")
        if self.href.find(" ")> 0:
            print(self.href)
        self.state.append(tag)
            
    def handle_endtag(self, tag):
        if self.done:
            return

        #print ("Encountered an end tag :", tag)
        self.state.pop()
        #self.field = []

    def handle_data(self, data):
        if self.done:
            return

        if self.state == ['html', 'body', 'div', 'div', 'table', 'tr', 'td', 'a', 'a']  :
            if data not in self.index:
                self.index[data]={
                    'name' : data,
                    'info_page' : self.href
                    }
                #print(self.state,data,self.href)
                    


url='http://www.mondotimes.com/newspapers/usa/kansas.html'
string = cache(url)
parser = MyHTMLParser()
parser.feed(string)


for idx in parser.index:
    obj = parser.index[idx]

    # "W", eather, leave that out
    for a in ("city_url","info_page","publisher_page"):
        if a in obj:
            cache(obj[a])

    
o= open('mondotimes.yaml', 'w')
o.write (yaml.dump(parser.index, indent=4,default_flow_style=False ))


