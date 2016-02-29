
from os import listdir, walk 
from os.path import isfile, join


folders = next(walk('sheets'))[1]

filepaths = []
for folder in folders:
	path = "sheets/"+folder
	filepaths += [ (folder, path+'/'+f) for f in listdir(path) if isfile(join(path,f)) ]

for path in filepaths:
	print path