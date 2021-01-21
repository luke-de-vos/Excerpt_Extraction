#Luke De Vos
#EVL Labs
#Excerpt Extractor: Creates directory splitDoc.py and populates with excerpts of specified word count range from passed file
#Excerpts begin and end with the beginning and ends of sentences respectively.
#If a sentence begins before the minLength and persists through the maxLength, the excerpt is deleted.\
#To use:
#	python3 splitDoc.py [filePath] [minLength] [maxLength] 

import sys
import os
import queue

#Checks for end of sentence + queue's size being over minLength. Empties queue into excerpt file if so.
def check():
	global fileNo, overMax
	if lastChar in PUNCT_LIST and len(word) > 2 and word not in TITLE_LIST:
		if q.qsize()>=minLength:
			with open(outputDir+"/"+fileName+str(fileNo)+".txt", 'a') as out:	#file to be written to
				while q.empty()==False:								
					out.write(q.get() + " ")
			if overMax==False:					
				fileNo+=1
		overMax=False
	return




#command-line args
filePath=sys.argv[1]
minLength=int(sys.argv[2])
maxLength=int(sys.argv[3])

#other vars
fileNo=1
overMax=False
q = queue.Queue(maxsize=maxLength)					#to store words until conditions for writing excerpt are met
PUNCT_LIST=['.','?','!',';']
TITLE_LIST=["Mr.","Mrs.","Ms."]
snippet=filePath[0:len(filePath)-4]				#full path without trailing .txt	
fileName=os.path.basename(os.path.normpath(snippet))	#just file name, no path
outputDir="splitDoc_Output/"+fileName+"_Excerpts"


#execution
os.makedirs(outputDir, exist_ok=True)		#create folder to hold excerpts
with open(filePath) as f:
	for line in f:
		for word in line.split():
			if q.qsize() >= maxLength:
				overMax=True			#overMax is changed to False in check() when the end of a sentence is found.
									#once that happens, normal queue filling resumes
				print(fileName+str(fileNo)+" draft deleted due to length.")			
				q.queue.clear()
			else:
				if not overMax:		
					q.put(word)		
				lastChar=word[len(word)-1]
				check()
				if lastChar in ["\"","\'"]:		#account for sentences ending within quotes
					lastChar=word[len(word)-2]		
					check()
					
print("-"+fileName+".txt Processed-")



