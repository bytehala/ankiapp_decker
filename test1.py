import os.path


images = os.scandir(os.getcwd() + "")
#print(images)
sortedimages = sorted(images, key=lambda x: x.stat().st_mtime, reverse=False)
newlist = []

names = ['one.png', 'two.png', 'three.png']
index = 0
for i in sortedimages:
	if(i.name.endswith(".png")):
		#print(i.stat().st_ctime)
		print(i.stat())
		print(i.name)
		print(names[index])
#		os.rename("" + i.name, "" + names[index])
		index = index + 1
