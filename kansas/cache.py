import os
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError 
import yaml

def cache(url):
    name = url 
    href=None
    name = name.replace("/","").replace(".","").replace(":","")

    filename = "cache/%s.html" % name
    if not os.path.isdir("cache"):
        os.mkdir("cache")

    if not os.path.isfile(filename):
        p = open (filename,"w")    
        res = None
        while(not res):
            try:
                print ("going to open %s" % url)
                res = urllib.request.urlopen(url)
                href=res.geturl()
                
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
        print (res)
        print (res.info())
        print (dir(res))

        data = res.read()
        #string = data.decode()

        obj = {
            'inurl' :url,
            'outurl' :href,
            'data': data.decode('utf-8'),
            }

        yml= yaml.dump(obj,p)
        p.close()
    p = open (filename,"r")    
    try :
        string = p.read()
    except:
        return "ERROR"

    try :
        return yaml.load(string)
    except Exception as exp:
        print (exp)
        return {
            'inurl': url,
            'outurl': url,
            'data': string
            }            
        
