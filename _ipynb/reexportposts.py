import sys,os,datetime


outfn=datetime.date.today().isoformat()+'-'+notebook.rstrip('.ipynb').replace(' ','-')
outfn=os.getcwd().rstrip('.ipynb')+'posts'+os.path.sep+outfn
remchar=['?','!']
for ch in remchar: outfn=outfn.replace(ch,'')
# convert notebook
print 'ipython nbconvert --to html \"%s\" --output %s' % (notebook,outfn)
os.system('ipython nbconvert --to html \"%s\" --output %s' % (notebook,outfn))
html=open(outfn+'.html','r').read()
html='''---\nlayout: post\ntitle:  %s\n---\n'''%notebook.rstrip('.ipynb') + html
open(outfn+'.html','w').write(html)
