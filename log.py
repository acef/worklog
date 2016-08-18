from datetime import datetime, date, time


"""
Costume logger for time keeping purposes.
should be lightweight.
will keep time, will serve for notes, will 
make alerts
will be brutally simple
will only have one text pattern reserved, any string 
which startd with #, so #*, excluding spaces of course.
will use simple hashtags for tagging and parsing purposes.

will also allow for data colection.
will store log in specific file and will always append 
to such file

must be backwards compatible

"""

#will get entry from user, will break it up 
#for further use. Get entry will show a prompt 
#showing the time.

def getEntry():
	prompt = str(datetime.now())[:-7] + ' ' + '------>' + ' '
	entry = raw_input(prompt)
	#refresh date and time
	f = open('worklog.txt', 'a')
	prompt = str(datetime.now())[:-7] + ' ' + '------>' + ' '
	f.write(prompt + entry + '\n')
	f.close()
	return [datetime.now()] + entry.split()



#will parse text entry and count hashtags
#will store it in a diccionary
def parse():
	return 


while 1:
	getEntry()