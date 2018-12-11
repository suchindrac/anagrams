#!/usr/bin/python

import sys
from itertools import *
import copy

dict_file = "words"

def all_chars_in_word(word, chars):
	chars_list = list(chars)
	word_list = list(word)
	word_list_copy = list(word)
	for ch in word_list:
		if ch in chars_list:
 			chars_list.remove(ch)
		word_list_copy.remove(ch)

	if (len(chars_list) == 0) and (len(word_list_copy) == 0):
		return True
	else:
		return False
 
def anagram(input):
	anagrams = []
	dict = ""
	try:
		fd = open(dict_file, 'r')
		dict = fd.read()
		fd.close()
	except:
		print ("E: Unable to open dictionary file, quitting ...")
		sys.exit (1)
	
	dict_list = dict.split()

	len_input = len(input)

	new_dict_list = []

	for key, items in groupby(dict_list, lambda x: x.find("'")):
		if key == -1:
			for word in items:
				new_dict_list.append(word)
	
	dict_list = new_dict_list

	del new_dict_list

	new_dict_list = list(filter(lambda x: len(x) <= len_input, dict_list))

	dict_list = new_dict_list
	del new_dict_list
	
	new_dict_list = []
	for word in dict_list:
		new_dict_list.append(word.lower())
	
	dict_list = new_dict_list
	del new_dict_list

	len_based_dict = {}

	red_words = []
	for key, items in groupby(dict_list, lambda x: len(x)):
		try:
			values = len(len_based_dict[key])
		except:
			len_based_dict[key] = []
		for item in items:
			len_based_dict[key].append(item)
			red_words.append(item)

	red_words2 = copy.deepcopy(red_words)

	for ch in input:
		for i in range(0, len(red_words)):
			index = red_words[i].find(ch)
			if index != -1:
				red_words[i] = red_words[i].replace(ch, "", 1)
	
	red_words3 = []
	for i in range(0, len(red_words)):
		if len(red_words[i]) == 0:
			red_words3.append(red_words2[i])

	for i in range(1, len(red_words3) + 1):
		for combi in combinations(red_words3, i):
			cword = "".join(combi)
			if all_chars_in_word(input, cword):
				if len(cword) == len(input):
					print (combi)

inp = ""
	
try:
	inp = sys.argv[1]
except:
	print ("python anagram.py <some word>")
	print ("Example: python anagram.py suchindra")
	sys.exit(1)

anagram(inp)
