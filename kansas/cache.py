import os
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError 

bad = (
    'http://www.youtube.com/user/cjonline11',
    'http://www.twitter.com/udk_news',
    'https://www.facebook.com/ElDoradoTimes',
    'http://www.kstatecollegian.com/',
    'http://www.holtonrecorder.com/'
)
#http://www.sterling.edu/stir-newspaper

def fetch (url):    
    if url == " " :
        return None 

    print("to fetch URL: '%s'" % url)
    res = None
    while(not res):
        try:
            res = urllib.request.urlopen(url)                
        except HTTPError as exp:
            print("URL http Failed %s" % url)
            print("URL http exp %s" % exp)
            if exp.code == 403:
                return None
            if exp.code == 404 :
                return None
            return None

        except URLError  as exp:
            print("URL error %s" % url)
            estr = str(exp)
            print("URL exp %s" % estr)
            if exp.reason.errno == 110 : # timeout
                return None
            elif exp.reason.errno == -2 : # 
                return None
            res = None
    data = res.read()
    return data
    

def cache(url):
    url = url.strip().rstrip()

    if not url :
        return None
    if url == "":
        return None
    if url[0:3]=="www":
        url = "http://" + url
    elif url[0]=="?":
        return None
    elif url.startswith('http://'):
        pass
    elif url.startswith('https://'):
        pass
    else :
        url = "http://" + url

    name = url 
    name = name.replace("/","").replace(".","").replace(":","")
    filename = "cache/%s.html" % name
    if not os.path.isfile(filename):
        data = None
        if url in bad:
            print("URL skipped %s" % url)        
            data = "SKIPPED"
        else:
            data = fetch(url)
        if (data):
            print("URL loaded: %s with data len:%s" % (url, len(data)))
        else:
            print("URL loaded: %s with no data" % (url))
            data = None

        #string = data.decode()
        p = open (filename,"wb")    
        if (data):
            p.write(data)
        p.close()
    else:
        print("URL cached: %s in file:%s" % (url, filename))

    p = open (filename,"r")    
    string = p.read()
    return string
