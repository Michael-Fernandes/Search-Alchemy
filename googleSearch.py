import json
import glob
import sys
import reStructure
import datetime
reload(sys)
sys.setdefaultencoding("utf8")

import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV2


### ********* Input Username and Password from bluemix here. **************
Username = '28f9b46e-6391-4bf0-a746-bcb93f6ddd0d'
Password = '2DFGd8cgXPiu'

def insights(aggr):
	personality_insights = PersonalityInsightsV2(
	    username=Username,
	    password=Password)

	personality = personality_insights.profile(text=aggr)

	return personality


def writePersonality(personality, f):
	fOut = open("personalities/" + f.split("/")[1] + ".txt", 'w')
	json.dump(personality, fOut)
	fOut.close()


def aggrgateQueries(dic):
	queryUnion = ''
	for i in range(0, len(dic)):
		queryUnion += " " + dic[i]["query"]['query_text']
	return queryUnion


def main():
	print "running \n\n"
	files = glob.glob("Searches/*.json")
	#halfFile = files[0].split()[0].split("/")[1]
	#print halfFile
	files.sort(key=lambda x: datetime.datetime.strptime( x.split()[0].split("/")[1], '%Y-%m-%d'))
	samples = len(files)
	for i in range(0, samples, 2):
		file1 = json.load( open(files[i]) )
		file2 = json.load( open(files[i + 1]) )
		
		queryUnion = aggrgateQueries( file1["event"] ) + aggrgateQueries( file2["event"] )
		personality = insights( queryUnion )
		writePersonality( personality, files[i] )
		#reStructure.reStructure()

	if(samples % 2 == 1):
		file = json.load( open(files[samples - 1]) )
		queryUnion = aggrgateQueries(File["event"])
		queryUnion += queryUnion
		personality = insights( queryUnion )
		writePersonality( personality, file )
		#reStructure.reStructure()
	print "Files are done"


def temp():
	for f in files:
		print "processing " + f
		recent = json.load( open(f) )

		queryUnion = aggrgateQueries( recent["event"] )
		personality = insights( queryUnion )
		writePersonality( personality, file )
	reStructure.reStructure()


##Runs program 
if __name__ == "__main__": main()





