import yaml

def read (filename):
    stream = open(filename, 'r')
    data = yaml.load(stream)
    return data

index = {}
index2 = {}

def index_object(filename, data,i):
    d = data[i]
    for k in d.keys() :
        if k not in (
            'A',
            'C',
            'contact_page',
            'F', 
            'facebook', 
            'ksa_site', 
            'named' ,
            'src_url', 
            'T', 
            'twitter', 
            'user_forum', 
            'V', 
            'W', 
            'website', 
            'Website', 
            'wikipedia'):
            continue
        v = d[k]

        if not isinstance(v,str):
            continue

        if not v:
            continue

        if v == '':
            continue

        if v == "NONE":
            continue
        if v.startswith('No Website') :
            continue

        if v[0] == "?":
            continue
        v = v.strip().rstrip()
        v = v.rstrip("/")
        v = v.replace("http://","")
        v = v.replace("https://","")
        if v not in index:
            index[v]={}
        if k not in index[v]:
            index[v][k]=[]
            print ("adding key:'%s' val'%s'" % (k, v))
            index[v][k].append(d)
#            ref = "|".join((filename,i))
#            if ref not in index[v][k] :
#                index[v][k][ref]=0
#            index[v][k][ref]=index[v][k][ref]+1
#            index2[ref] = d

def index_data(filename, data):

    for i in data.keys():
        index_object(filename, data,i)


for f in (
    'kansas_simple.yaml',
    'media_in_kansas.yaml',
    'usnpl.yaml',
    'mondotimes.yaml'
    ):
    d = read(f)
    index_data(f,d)

o= open('merge.yaml', 'w')
o.write (yaml.dump(
        {
            "index":index, 
            #"data" : index2
            }, indent=4,default_flow_style=False ))
