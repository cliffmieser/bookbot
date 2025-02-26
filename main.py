import sys
import os
from stats import get_num_words

def sort_on(dict):
	"""Used to sort the dictionary by count ASC order"""
	return dict["count"]


def getReport(text): 
	"""Return an aggregated report of characters
	input: dictionary of characters """

	# get the name of file 
	title = sys.argv[1]

	print(f"\n--- Begin report of {title} ---")
	print(f"{ sum(text.values()) } words found in the document")
	
	charList = [] #initialize empty list to store dictionaries 
	
	for k,v in text.items():
		# if k == ' ' or k == '.' or k == '#':
		if k.isalpha() != True:
			continue
		else: 
			newDict = dict([("char", k), ("count", v)])
			charList.append(newDict)

	charList.sort(reverse=True, key=sort_on)

	for x in charList:
		if x["char"].isalpha():
			print(f"{x["char"]}: {x["count"]}")





def getCharApperances(text):
	"""Gets text from string and shows qty that some character appeared"""
	wordDict = {}

	# loop through text and add 1 if any character matches 
	for char in text.lower():
		if char.isalpha():
			if char in wordDict:
				wordDict[char] += 1
			else: 
				wordDict[char] = 1
		else:
			continue

	return wordDict

def displayHelp(): 
	"""Prints to command line how to use the program"""
	print("Usages: python3 main.py <path_to_book>")
	sys.exit(1)

def getPath(): 
	"""returns path to book (relative)"""
	book = sys.argv[1]
	return os.getcwd() + f"/{book}" # gets books/input.txt 


def main():
	if not len(sys.argv) == 2:
		displayHelp()
	else:
		# print(f"argument list: {sys.argv}")
		path = getPath()
		with open(path) as f:
			file_contents = f.read().strip()
			# print(file_contents)
			
			total_words = get_num_words(file_contents)
			print(total_words)

			# print(getCharApperances(file_contents))

			# print('\n')
			getReport(getCharApperances(file_contents))

main()
