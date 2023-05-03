import sqlite3
from sqlite3 import Error
import os
from datetime import datetime


# def sql_connection():

#     try:

#         con = sqlite3.connect(':memory:')

#         print("Connection is established: Database is created in memory")

#     except Error:

#         print(Error)

#     finally:

#         con.close()

# sql_connection()

def init():
	con = sqlite3.connect('diarys.db')
	cursorObj = con.cursor()
	cursorObj.execute("""CREATE TABLE diarys(id integer PRIMARY KEY, name text, created integer, modified integer, content text, encrypted integer)""")
	cursorObj.execute("""CREATE TABLE tags(id integer PRIMARY KEY, name text)""")
	cursorObj.execute("""CREATE TABLE diary_tag(diary_id integer, tag_id integer, FOREIGN KEY("tag_id") REFERENCES "tags"("id"), FOREIGN KEY("diary_id") REFERENCES "diarys"("id"))""")


	con.commit()


def add_all_dairys():
	con = sqlite3.connect('diarys.db')
	cursorObj = con.cursor()
	entries = os.listdir('diarys/')
	# print(entries)
	diarys = []
	for entry in entries:
		if "encrypt" not in entry and "asset" not in entry and "save" not in entry:
			diarys.append(entry)
	# try:
	for diary in diarys:
		date = diary
		with open("diarys/"+diary+".encrypt") as file:
			content = file.read()
		# print("INSERT INTO diarys VALUES({}, {}, {}, {}, {}, 1)".format(date, '"'+date+'"', date+"000000", datetime.now().strftime("%Y%m%d%H%M%S"), "'"+content+"'"))
		sql = "INSERT INTO diarys VALUES({}, {}, {}, {}, {}, 1);".format(date, '"'+date+'"', date+"000000", datetime.now().strftime("%Y%m%d%H%M%S"), "'"+content+"'")
		try:
			cursorObj.execute(sql)
		# break
			con.commit()
		except:
			pass
	# except Error:
	# 	print(str(Error))



if __name__ == "__main__":
	# init()
	add_all_dairys()