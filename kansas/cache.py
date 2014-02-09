import os
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError 
def cache(url):
    name = url 
    name = name.replace("/","").replace(".","").replace(":","")

    filename = "cache/%s.html" % name

    if not os.path.isfile(filename):
        p = open (filename,"wb")    
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
                print("URL timeout %s" % url)
                print("URL exp %s" % exp)
                res = None


        print("URL loaded: %s" % url)
        data = res.read()
        #string = data.decode()
        p.write(data)
        p.close()
    p = open (filename,"r")    
    string = p.read()
    return string
