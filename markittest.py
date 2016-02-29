import requests
import time

import xml.etree.ElementTree as ET
import tweet

# ddd MMM d HH:mm:ss UTCzzzzz yyyy
# timestamp=Wed Apr 1 10:30:43 UTC-04:00 2015
def buildURL(Symbol, Timestamp):
	symbol = 'symbol='+Symbol
	timestamp = 'timestamp='+Timestamp
	url = 'http://dev.markitondemand.com/Api/v2/Quote?'
	return url+symbol+'&'+timestamp

	

def markitRequest(symbol, timestamp):
	url = 'http://dev.markitondemand.com/Api/v2/Quote'
	r = requests.post(url, params={'symbol':symbol, 'timestamp':timestamp})
	time.sleep(0.1)
	print r.status_code
	return parseXML(str(r.text))


def parseXML(xml):
	dic = {}
	root = ET.fromstring(xml)
	fields = ['Status','Name','Symbol','LastPrice','Change','ChangePercent','Timestamp' ,'MSDate','MarketCap','Volume','ChangeYTD','ChangePercentYTD','High','Open']
	for filed in fields:
		dic[filed] = root.find(filed).text

	return dic



def main():

	stream = open('processed_tweets.txt')
	for line in stream:
		tweet =  line.split(';')
		print tweet[3]
		xml = markitRequest('AAPL', tweet[3])
		print
		print xml['Name'], xml['LastPrice'], tweet[3]



	# build url 
	
if __name__ == "__main__":
    main()





