import xlrd, tweet


def get_workbook(workbook_name):
	return xlrd.open_workbook(workbook_name)

def get_sheet(workbook,sheet_name):
	return workbook.sheet_by_name(sheet_name)

# column: the column you want to read.
# ws: <Worksheet object>
# return a list where each element is the content of a cell in thr given column
def read_cells(category, ws):

	# get tweet IDs
	tweets = []

	current_row = 0
	num_rows = ws.nrows-1
	while current_row < num_rows:
		current_row += 1
		tweet_id = ws.cell(current_row, 0).value
		tweet_date = ws.cell(current_row, 1).value
		tweet_time = ws.cell(current_row, 2).value
		tweet_user = ws.cell(current_row, 3).value
		tweet_content = ws.cell(current_row, 5).value
		tweet1 = tweet.Tweet(tweet_id, category, tweet_user, tweet_content, tweet_date, tweet_time)
		tweets.append(tweet1)


	return tweets





		
