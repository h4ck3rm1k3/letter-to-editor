
import urllib.request
from html.parser  import HTMLParser
import os
import yaml

# create a subclass and override the handler methods
names= {}

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.state = []
        self.href= ""
        self.field = []
        self.obj = {}
        self.objs = []
        self.done = False

    def handle_starttag(self, tag, attrs):
        if self.done:
            return
        if attrs:
            if self.state[0:8] == ['html', 'head', 'meta', 'body', 'div', 'div', 'div', 'div']:
#                print ("Encountered a start tag:", tag)
                #print ("D:  %s:" % (self.state))
                href = attrs[0][1]
                if href == 'clearfloat':
                    self.done = True
                    return
                    
                if href[0] == "h" :
                    self.href = href
                else:
                    url = "http://www.usnpl.com/%s" % href
                    self.href = url

            if self.href == 'http://www.usnpl.com/address/npmail.php' :
                self.href = ""

        self.state.append(tag)
            
    def handle_endtag(self, tag):
        if self.done:
            return

        #print ("Encountered an end tag :", tag)
        self.state.pop()
        #self.field = []

    def handle_data(self, data):

        if self.field:
            if self.field[0] == "clearfloat":
                #raise Exception()
                self.done = True
                return

        if self.done:
            return

        if self.state[0:8] == ['html', 'head', 'meta', 'body', 'div', 'div', 'div', 'div']:
            data= data.replace("\n","")
            data = data.strip().rstrip()
            if (data) :
                if data ==  "(":
                    pass
                elif data == ')(' : 
                    pass
                else:

                    #print ("D2: %s" % (data))
                    if data == "for address downloads." :
                        self.field=[]

                    if data in (
                            '&',
                            '(A) for Address, phone, fax, editor, translate',
                            '(C) for County Results',
                            '(C) for County Results',
                            '(F) for Facebook',
                            '(F) for Facebook:',
                            '(T) for Twitter',
                            '(T) for Twitter:',
                            '(V) for Video',
                            '(V) for Video:',
                            '(W) for Local Weather',
                            '(W) for Local Weather:',
                            'Click',
                            'Forecast',
                            'Newspapers',
                            'Untitled Document',
                            'here',
                            'for address downloads.'
                    ):
                        return

                    elif data ==  ")":
                        #print ("Field:" + str(self.field))
                        #self.obj[data] = str(self.href)
                        self.href = ""
                        self.objs.append(self.obj)
                        self.obj = {}
                    else:
                        #print ("'%s'" % data)
                        self.obj[data] = str(self.href)
                        self.href = ""
                    


def cache(url):
    name = url 
    name = name.replace("/","").replace(".","").replace(":","")

    filename = "cache/%s.html" % name

    if not os.path.isfile(filename):
        p = open (filename,"w")    
        res = urllib.request.urlopen(url)
        data = res.read()
        string = data.decode()
        p.write(string)
        p.close()
    p = open (filename,"r")    
    string = p.read()
    return string


string = cache("http://www.usnpl.com/ksnews.php")
parser = MyHTMLParser()
parser.feed(string)

o= open('usnpl.yaml', 'w')
o.write (yaml.dump(parser.objs, indent=4,default_flow_style=False ))

