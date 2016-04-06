import json
import glob
import numpy as np
import matplotlib.pyplot as plt

def getTrait(data, name):
	### input: An Alchemy insight json obj, name of a personality trait(i.e. "intellect")
	### Returns the data for a given trait
	for pType in data:
		for personality in pType['children']:
			for pTrait in personality['children']:
				
				if(pTrait['id'] == name):
					return pTrait

def getTraitLst(data):
	possiblePersonas = []
	for pType in data:
		for personality in pType['children']:
			for pTrait in personality['children']:
				
				if(pTrait['id'] not in possiblePersonas):
					possiblePersonas.append( str(pTrait['id']) )

	return possiblePersonas

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2) 

global personaArry = []
global selections = []
global possibleTraits = ['Adventurousness', 'Artistic interests', 'Emotionality', 'Imagination', 'Intellect', 'Liberalism', 
					'Achievement striving', 'Cautiousness', 'Dutifulness', 'Orderliness', 'Self-discipline',
					 'Self-efficacy', 'Activity level', 'Assertiveness', 'Cheerfulness', 'Excitement-seeking', 
					 'Friendliness', 'Gregariousness', 'Altruism', 'Cooperation', 'Modesty', 'Morality', 
					 'Sympathy', 'Trust', 'Anger', 'Anxiety', 'Depression', 'Immoderation', 'Self-consciousness', 
					 'Vulnerability']

def process(file):
	### In: ALchemy insghts json file name
	### Processes files to obtain user inputed traits
	# Opens current file
	persona = json.load( open(file, "r") )
	fSplit = file.split(".")

	# Prunes json tree
	data = persona['tree']['children'][0]['children']

	selectedTraits = []

	for trait in selections:
		call =  getTrait(data, trait)
		selectedTraits.append( call )

	#fileDate =  file.split("/")[2].split(".")[0]
	fileDate =  file.split(".")[0]
	print fileDate
	# Stores selected traits
	temp = [{'date': fileDate}]
	for trait in selectedTraits:
		temp.append( {'name':trait['name'], 'percentage':trait['percentage']} )

	personaArry.append(temp)
	

def fileProcess():
	###Processes all insight file
	files = glob.glob("Searches/Personas/*.txt")
	print files
	for f in files:
		process(f)


def writeFile():	
	### Writes collected data to file
	string = "var dataAggr = " + str(personaArry)
	fOut = open('test.js', 'w');
	fOut.write(string)
	fOut.close()

def collect():
	### Allows user to select desired traits 
	i = 1
	for trait in possibleTraits:		#Allows user to see types of traits that can be 

		print  str(i) + ". " + str(trait)
		i = i + 1

	print "\nEnter 1 - 5 traits by typing the name or number of a trait that you would like to know more about. "
	print "If you wish to enter less then 5 traits type done. \n"

	# User selects desired traits 
	response = ""
	i = 1
	while( i < 6 and "done" not in response.lower()):
		response = raw_input("Trait " + str(i) + ">>>  ").lower().title()
		if( response.isdigit() ):
			selectedTrait = possibleTraits[int(response)]
			response = selectedTrait
			print selectedTrait

		if response.lower() != "done":
			selections.append(response)
			i = i + 1

def graph():
	### Graphs selected traits
	traitArry = {}
	dates = []
	
	for trait in personaArry:
		# Collects dates
		dates.append(trait[0]['date'])

		# Compiles each trait's percentage
		for t in trait[1:]:
			print t
			if t['name'] not in traitArry:
				traitArry[t['name']] = []
			traitArry[t['name']].append(t['percentage'])

	plt.ylabel("Percentile")
	num = 0
	
	for trait in traitArry.keys():
		num = len(traitArry[trait])
		plt.plot(traitArry[trait], label=trait)

	plt.axis([0, num - 1, 0, 1])

	# Add the legend with some customizations.
	plt.legend(loc='upper left')

	#labels = [item.get_text() for item in ax.get_xticklabels()]
	#labels[0] = ""
	
	dateLabel = []
	for i in range(len(dates) ):
		#print labels[i]
		date = dates[i].split(" ")
		dateLabel.append(date[len(date) - 2][0:3] + " '" + date[len(date) - 1][2:4])

	plt.xticks(range(len(dates)), dateLabel)

	#ax.set_xticklabels(labels)
	plt.show()

def reStructure():
	cont = ""
	while(cont != "n"):
		collect()
		fileProcess()
		writeFile()
		graph()
		cont = raw_input("Would you like to create another graph y/n?")

if __name__ == "__main__": reStructure()




