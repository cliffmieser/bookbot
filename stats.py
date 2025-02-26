def get_num_words(text):
	"""Returns the total number count of words in the book"""
	words = text.split()
	count = 0

	for _ in words:
		count+= 1
	return f"{count} words found in the document."