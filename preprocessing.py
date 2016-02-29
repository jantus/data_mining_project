#!/usr/bin/env python
# -*- coding: utf-8 -*- 


from os import listdir, walk 
from os.path import isfile, join
import read_sheet as rs
import language_recognition as lr

# saves tweets to a file.
# each line in the file contains category, id, time, content
# EX
#	sony;123123123123;Wed Apr 1 10:30:43 UTC-04:00 2015;Random tweet content 
processed_tweets = {}




def preprocess_tweets(category, xls_file):
	sheet_name = "Stream"
	output_file = "processed_tweets.txt"
	dirty_words = [" #tits", " #sexy ", " #boobs ", " sex ", " porn ", " pussy ", 
					" blowjob", " cum ", " horny ", " sexual hunger "]
	
	num_dirty_tweets = 0
	copies = 0
	wb = rs.get_workbook(xls_file)
	ws = rs.get_sheet(wb ,sheet_name)

	tweets = rs.read_cells(category, ws)
	english_tweets = []
	output_file = open(output_file, "a")

	for tweet in tweets:
		content = tweet.content
		language = lr.detect_language(content)
		
		if language == "english":
			
			if processed_tweets.has_key(tweet.id):
				continue

			has_dirty_word = 0
			for word in dirty_words: 
				if word in tweet.content:
					num_dirty_tweets += 1
					has_dirty_word += 1
			if not has_dirty_word:
				processed_tweets[tweet.id] = 1
				out_str = tweet.toString()
				output_file.write(out_str.encode('ascii','backslashreplace'))

	output_file.close()

def get_input_files():
	folders = next(walk('sheets'))[1]

	filepaths = []
	for folder in folders:
		path = "sheets/"+folder
		filepaths += [ (folder, path+'/'+f) for f in listdir(path) if isfile(join(path,f)) ]

	for path in filepaths:
		print path

	return filepaths



if __name__=="__main__":
	input_files = get_input_files()

	i = 0
	items = len(input_files)
	for (category, xls_file) in input_files:
		preprocess_tweets(category, xls_file)
		i += 1
		print "done with " + xls_file + ". \t "+str(i)+"/"+str(items)









