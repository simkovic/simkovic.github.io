import sys,os,datetime

try:
    notebook = sys.argv[1]
except:
    print "usage: python publish.py   /path/to/notebook_file.ipynb"
    sys.exit(-1)
outfn=datetime.date.today().isoformat()+'-'+notebook.rstrip('.ipynb').replace(' ','-')
outfn=os.getcwd().rstrip('.ipynb')+'posts'+os.path.sep+outfn
# convert notebook
os.system('ipython nbconvert --to html \"%s\" --output %s' % (notebook,outfn))
html=open(outfn+'.html','r').read()
html='''---\nlayout: post\ntitle:  %s\n---\n'''%notebook.rstrip('.ipynb') + html
open(outfn+'.html','w').write(html)
