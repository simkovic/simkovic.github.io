import sys,os,datetime

def stripRight(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:len(text)-len(suffix)]

try:
    notebook = sys.argv[1]
except:
    print("usage: python publish.py   /path/to/notebook_file.ipynb")
    sys.exit(-1)
outfn=stripRight(notebook,'.ipynb').replace(' ','-')
remchar=['?','!','\'']
for ch in remchar: outfn=outfn.replace(ch,'')

outpath=stripRight(os.getcwd(),'ipynb')+'posts'+os.path.sep
exists= list(filter(lambda x: x.endswith(outfn+'.html'),os.listdir(outpath)))
print(exists)

if len(exists)==1: # rewrite if the filename exists
    outfn=outpath+stripRight(exists[0],'.html')
elif len(exists)==0:
    print('here')
    outfn=outpath+datetime.date.today().isoformat()+'-'+outfn  
else: raise ValueError('Multiple files with the same name already exist')

# convert notebook
com='jupyter nbconvert --to html --template basic \"%s\" --output %s'%(notebook,outfn)
print( com)
os.system(com)
body=open(outfn+'.html','r').read()
header=open(os.getcwd()+os.path.sep+'header','r').read()
html='''---\nlayout: post\ntitle:  %s\n---\n'''%notebook.rstrip('.ipynb')+ \
    '\n<!DOCTYPE html>\n<html>\n'+ header+body+'\n</html>\n'
open(outfn+'.html','w').write(html)
