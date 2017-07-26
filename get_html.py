import requests, bs4
res = requests.get('http://www.hr-text.hr-online.de/ttxHtmlGenerator/index.jsp?page=193')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
all = []
for i in range (4,20):
	elems = noStarchSoup.select("#ttxRow"+str(i))
	for elem in elems:
		print(str(elem).split())
		for ele in str(elem).split():
			all.append(ele)

filtered = []
for item in all:
	item = str(item).lstrip()
	#print ("item=" + item)
	if item.startswith('<pre'):
		pass
	elif item.startswith('class='):
		pass
	elif item.startswith('id='):
		pass
	elif item.find('</span></pre>') != -1 :
		item = item.replace('</span></pre>','')
		if item != '':
			filtered.append(item)	
	else:
		filtered.append(item) 

print("-------------------------")
print(filtered)

text = ''
words = filtered
merker = False
for word in words:
	if word.endswith('-'):
		text = text + " " + word[0:len(word)-1]
		merker = True
	else: 
		if merker == True:
			merker = False
			text = text + word 
		else:
			text = text + " " + word
print("------------------------")
print("Hessenwetter: ")
print(text)
