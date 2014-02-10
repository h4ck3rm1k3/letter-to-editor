import yaml

def read (filename):
    stream = open(filename, 'r')
    data = yaml.load(stream)
    return data

index = {}
index2 = {}

def index_data(filename, data):

    for i in data.keys():
        d = data[i]

        for k in d.keys() :
            v = d[k]

            if not isinstance(v,str):
                continue

            if not v:
                continue

            if v == "NONE":
                continue

            v = v.strip().rstrip()
            v = v.rstrip("/")
            v = v.replace("http://","")
            v = v.replace("https://","")

            if v not in index:
                index[v]={}

            if k not in index[v]:
                index[v][k]={}

            ref = "|".join((filename,i))

            if ref not in index[v][k] :
                index[v][k][ref]=0
            
            index[v][k][ref]=index[v][k][ref]+1

            index2[ref] = d


for f in ('kansas_simple.yaml',
          'media_in_kansas.yaml',
          'usnpl.yaml'):
    d = read(f)
    index_data(f,d)

o= open('merge.yaml', 'w')
o.write (yaml.dump({"index":index, "data" : index2}, indent=4,default_flow_style=False ))
