#map applies a function to every element of a sequence and returns a list (Python 2) or iterator (Python 3):

simpsons = ['homer', 'marge', 'bart']
map(len, simpsons)
#output: [5, 5, 4]

# equivalent list comprehension
[len(word) for word in simpsons]
#output: [5, 5, 4]

map(lambda word: word[-1], simpsons)
#output['r', 'e', 't']

# equivalent list comprehension
[word[-1] for word in simpsons]
#output['r', 'e', 't']

