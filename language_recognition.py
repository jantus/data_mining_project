#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

try: 
	from nltk import wordpunct_tokenize
	from nltk.corpus import stopwords
except ImportError:
	print "[!] You need to install nltk"


def _calculate_languages_ratios(text):
	languages_ratios = {}

	tokens = wordpunct_tokenize(text)
	words = [word.lower() for word in tokens]

	for language in stopwords.fileids():
		stopwords_set = set(stopwords.words(language))
		words_set = set(words)
		common_elements = words_set.intersection(stopwords_set)

		languages_ratios[language] = len(common_elements)

	return languages_ratios


def detect_language(text):

	ratios = _calculate_languages_ratios(text)

	most_rated_language = max(ratios, key=ratios.get)
	return most_rated_language

def is_ascii(s): 
	return all(ord(c) < 128 for c in s)

if __name__=="__main__":
	text = "RT Hyperkin: Check out device that turns your iPhone into a Gameboy: Reddit is going crazy for a n... http://t.co/kEENEUPjnE #Follow #Me"

	language = detect_language(text)

	print language