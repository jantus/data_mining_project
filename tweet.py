#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# This is a tweet object

from datetime import datetime, date, time
import re


class Tweet:
	def __init__(self, id, category, user, content, date, time):
		self.id = id
		self.category = category
		self.content = content
		self.user = user
		self.time = self.getDateFromString(date)


	# date: 'YYYY-MM-DD'
	# return: date object
	def getDateFromString(self, date):
		return '/'.join(date.split('-'))

	# time: 'hh:mm'
	# return: time object
	def getTimeFromString(self, Time):
		hh, mm = Time.split(':')
		return time(int(hh), int(mm))



	# TODO: MUST FIND TIMEZONE FORM TWITTER DATA. NOW ASSUME TIME IS UTC
	# date: 'yyyy-mm-dd'
	# time: 'hh:mm'
	# return: 'ddd MMM d HH:mm:ss UTCzzzzz yyyy'
	# EX: Wed Apr 1 10:30:43 UTC-04:00 2015
	def buildTimestamp(self, date, time):
		d = self.getDateFromString(str(date))
		t = self.getTimeFromString(time)		

		weekday = d.strftime("%a")
		month = d.strftime("%b")
		day = d.strftime("%d")
		time = t.strftime("%X")
		zone = "UTC"
		year = d.strftime("%Y")



		return ' '.join((weekday, month, day, time, zone, year))

	def toString(self):
		
		category = str(self.category)
		tweet_id = str(self.id)
		tweet_time = str(self.time)
		content = self.content
		user = self.user

		string = category+';;;;'+tweet_id+';;;;'+ user.replace('\n', ' ')+';;;;'+tweet_time+';;;;'+content.replace('\n', ' ')

		return string+"\n"


