import yaml

def read (filename):
    stream = open(filename, 'r')
    data = yaml.load(stream)
    return data

index = {}


def index_data(filename, data):

    for i in data.keys():
        d = data[i]

        for k in d.keys() :
            v = d[k]

            if not isinstance(v,str):
                continue

            v = v.strip().rstrip()
            v = v.rstrip("/")
            v = v.replace("http://","")
            v = v.replace("https://","")

            if v not in index:
                index[v]={}

            if k not in index[v]:
                index[v][k]={}

            if filename not in index[v][k] :
                index[v][k][filename]={}

            if i not in index[v][k][filename] :
                index[v][k][filename][i]=1

for f in ('kansas_simple.yaml',
          'media_in_kansas.yaml',
          'usnpl.yaml'):
    d = read(f)
    index_data(f,d)

o= open('merge.yaml', 'w')
o.write (yaml.dump(index, indent=4,default_flow_style=False ))
