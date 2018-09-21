import sys

print ('The command line arguments are:')
for i in sys.argv:
	print (i)
for p in sys.path :

	print('there are:=' + str(len(sys.path)) + ' pythonpath entries')
	print (p)

	print('\n')












