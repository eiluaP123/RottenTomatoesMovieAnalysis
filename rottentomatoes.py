import urllib
import re
import json
import time

file = open("movie_ID_name.txt", "w")
filesim = open("movie_ID_sim_movie_ID.txt", "w")
list = []
namelist = []
for idx in range(1,7):
	htmltext = urllib.urlopen("http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=tsfmk85u6p6bvgu38ub75bem&q=life&page_limit=50&page=" +str(idx))
	data = json.load(htmltext)
#print data
	for i in data['movies']:
		#print i['title']
		id = i['id']
		file.write(i['id']),
		file.write(", ")
		file.write(i['title'])
		file.write("\n")
	
		time.sleep(.5)
		simhtml = urllib.urlopen("http://api.rottentomatoes.com/api/public/v1.0/movies/" + str(id) + "/similar.json?apikey=tsfmk85u6p6bvgu38ub75bem&limit=5")
		simdata = json.load(simhtml)
		for j in simdata['movies']:
			#filesim.write(id),
			#filesim.write(", "),
			#filesim.write(j['id'])
			#filesim.write("\n")
			list.append((id,j['id']))
			namelist.append((i['title'],j['title']))
upd_list = set(list)
upd_namelist = set(namelist)	
#print upd_list
for item in upd_list:
	#print item[0] + "," + item[1]
	filesim.write(item[0]),
	filesim.write(","),
	filesim.write(item[1])
	filesim.write("\n")
			
#for d in upd_namelist:
	#print d[0] + "," + d[1]
	
filesim.close()
file.close()