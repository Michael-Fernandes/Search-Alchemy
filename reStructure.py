""" ************************************************************************************************ '''
	The following allows an User to select traits and visualize how there google searches changed
    overtime based on those traits

    Note: Place this file in the same folder as searchAlchemy. For the script to run properly the file 
    structure must look as follows:
    	Current Directory> Google Searches/Searches/Searches/Personas
    	   ^
      	   Contains Google Search extraction folder
'''	************************************************************************************************ """

import json
import glob
import numpy as np
import matplotlib.pyplot as plt


def getTrait(data, name):
	### input: An Alchemy insight json obj, name of a personality trait(i.e. "intellect")
	### Returns the data for a given trait
	for personalityType in data:
		for personality in personalityType['children']:
			for personalityTrait in personality['children']:
				
				if(personalityTrait['id'] == name):
					return personalityTrait


def getTraitLst(data):
	"""Gets list of all personality traits """
	possiblePersonas = []

	for personalityType in data:
		for personality in personalityType['children']:
			for personalityTrait in personality['children']:
				
				if(personalityTrait['id'] not in possiblePersonas):
					possiblePersonas.append( str(personalityTrait['id']) )
	return possiblePersonas


global personaArry = []
global selections = []

#Possible traits an user can select from
global possibleTraits = ['Adventurousness', 'Artistic interests', 'Emotionality', 'Imagination', 'Intellect', 'Liberalism', 
					'Achievement striving', 'Cautiousness', 'Dutifulness', 'Orderliness', 'Self-discipline',
					 'Self-efficacy', 'Activity level', 'Assertiveness', 'Cheerfulness', 'Excitement-seeking', 
					 'Friendliness', 'Gregariousness', 'Altruism', 'Cooperation', 'Modesty', 'Morality', 
					 'Sympathy', 'Trust', 'Anger', 'Anxiety', 'Depression', 'Immoderation', 'Self-consciousness', 
					 'Vulnerability']


def process(file):
	### In: ALchemy insights json file name
	### Obtains selected traits from a passed in personality file
	# Opens current file
	persona = json.load( open(file, "r") )
	fSplit = file.split(".")

	data = persona['tree']['children'][0]['children'] # Prunes json tree

	selectedTraits = []
	for trait in selections:
		call =  getTrait(data, trait)
		selectedTraits.append( call )

	fileDate =  file.split(".")[0] # Saves end date for particular file's data collection period
	
	# Stores selected traits
	temp = [{'date': fileDate}]
	for trait in selectedTraits:
		temp.append( {'name':trait['name'], 'percentage':trait['percentage']} )

	personaArry.append(temp)
	

def fileProcess():
	### Processes all insight file for Google Search data set
	files = glob.glob("googleSearch/SearchesSearches/Personas/*.txt")
	print files
	for f in files:
		process(f)


def writeFile():	
	### Stores collected data to file
	string = "var dataAggr = " + str(personaArry)
	fOut = open('test.js', 'w');
	fOut.write(string)
	fOut.close()


def collect():
	### User selects desired traits 
	i = 1
	for trait in possibleTraits:		# Allows User to see types of traits that can be 

		print  str(i) + ".\t " + str(trait)
		i = i + 1

	print "\nEnter 1 - 5 traits by typing the name or number of a trait that you would like to know more about. "
	print "If you wish to enter less then 5 traits type done. \n"

	# User selects desired traits 
	response = ""
	i = 1
	while( i < 6 and "done" not in response.lower()): #User selects trait
		response = raw_input("Trait " + str(i) + ">>>  ").lower().title()
		if( response.isdigit() ):
			selectedTrait = possibleTraits[int(response) - 1]
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
	
	#Add each seleced trait to legend
	num = 0
	for trait in traitArry.keys():
		num = len(traitArry[trait]) 
		plt.plot(traitArry[trait], label=trait)


	plt.axis([0, num - 1, 0, 1])

	# Add the legend with some customizations.
	plt.legend(loc='upper left')
	
	#Add time labels to x axis
	dateLabel = []
	for i in range(len(dates) ):
		date = dates[i].split(" ")
		dateLabel.append(date[len(date) - 2][0:3] + " '" + date[len(date) - 1][2:4])

	plt.xticks(range(len(dates)), dateLabel) # Labels axis
	plt.ylabel("Percentile")

	plt.show() # Plots graph


def reStructure():
	cont = ""
	while(cont != "n"):
		collect()
		fileProcess()
		writeFile()
		graph()
		cont = "n"


if __name__ == "__main__": reStructure()




