import json
import glob
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

personaArry = []
selections = []
possibleTraits = ['Adventurousness', 'Artistic interests', 'Emotionality', 'Imagination', 'Intellect', 'Liberalism', 
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
		response =  getTrait(data, trait)
		selectedTraits.append( response )

	#fileDate =  file.split("/")[2].split(".")[0]
	fileDate =  file.split(".")[0]

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
			response = possibleTraits[int(response)]

		if response != "done":
			selections.append(response)
			i = i + 1

def graph():
	### Graphs selected traits
	traitArry = {}
	dates = []
	for trait in personaArry[1:]:

		# Collects dates
		dates.append(trait[0]['date'])

		# Compiles each trait's percentage
		for t in trait[1:]:
			if t['name'] not in traitArry:
				traitArry[t['name']] = []
			traitArry[t['name']].append(t['percentage'])

	# Y axis
	axes = plt.gca()
	axes.set_ylim([0,1])
	plt.ylabel("Percentile")

	for trait in traitArry.keys():
		plt.plot(range(len(personaArry) - 1), traitArry[trait], label=trait)

	# Add the legend with some customizations.
	fig, ax = plt.subplots()
	legend = ax.legend(loc='best', shadow=True)

	# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
	frame = legend.get_frame()
	frame.set_facecolor('0.90')

	labels = [item.get_text() for item in ax.get_xticklabels()]
	labels[0] = ""

	for i in range(1, len(dates)):
		date = dates[i].split(" ")
		labels[i] = date[len(date) - 2][0:3] + " '" + date[len(date) - 1][2:4]	

	ax.set_xticklabels(labels)
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




