def getWords(text):
	"""Returns the total number count of words in the book"""
	words = text.split()
	count = 0

	for _ in words:
		count+= 1
	print(f"Total number of words in this book: {count}.")

	return count



def sort_on(dict):
	"""Used to sort the dictionary by count ASC order"""
	return dict["count"]


def getReport(text): 
	"""Return an aggregated report of characters
	input: dictionary of characters """

	print("\n--- Begin report of books/frankenstein.txt ---")
	print(f"{ sum(text.values()) } words found in the document")
	
	charList = [] #initialize empty list to store dictionaries 
	
	for k,v in text.items():
		if k == ' ' or k == '.' or k == '#':
			continue
		else: 
			newDict = dict([("char", k), ("count", v)])
			charList.append(newDict)

	charList.sort(reverse=True, key=sort_on)

	for x in charList:
		if x["char"].isalpha():
			print(f"The '{x["char"]}' character was found {x["count"]} times")





def getCharApperances(text):
	"""Gets text from string and shows qty that some character appeared"""
	wordDict = {}
	
	# loop through text and add 1 if any character matches 
	for _ in text.lower():
		if _ not in [' ','#','.']:
			if _ in wordDict:
				wordDict[_] += 1
			else: 
				wordDict[_] = 1
		else:
			continue

	return wordDict

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		print(file_contents)
		print('\n')
		total_words = getWords(file_contents)
		print(total_words)

		print(getCharApperances(file_contents))

		print('\n')
		getReport(getCharApperances(file_contents))

main()
