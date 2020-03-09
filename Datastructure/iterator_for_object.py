# Basic use of iter() 

languages = ['Python', 'Java', 'C++', 'Objective C'] 


languages_iterator = languages.__iter__() 

try: 
	print(languages_iterator.__next__()) 
	print(languages_iterator.__next__()) 
	print(languages_iterator.__next__()) 
	print(languages_iterator.__next__()) 
	print(languages_iterator.__next__()) #StopIteration error 
except: 
	print(" \nThrowing 'StopIterationError'", 
					"I cannot count more.") 
