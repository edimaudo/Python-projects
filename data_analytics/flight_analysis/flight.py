"""
Goal: Analyse a flight database using flight data stored in a sqlite database
"""

import sys
import sqlite3

try:

	#create connection
	conn = sqlite3.connect("flights.db")
	cur = connection.cursor()

	# test query and output
	#cur.execute("select * from airlines limit 5;")
	#output
	#results = cur.fetchall()
	#print(results)
	# coords = cur.execute("""
	#   select cast(longitude as float), 
	#   cast(latitude as float) 
	#   from airports;"""
	# ).fetchall()
	df = pd.read_sql_query("select * from airlines limit 5;", conn)
	print(df)
	#row insertion
	#values = ('Test Flight', 'Y')
	#cur.execute("insert into airlines values (6049, 19847, ?, '', '', null, null, null, ?)", values)
	#conn.commit()


	#row update
	#values = ('USA', 19847)
	#cur.execute("update airlines set country=? where id=?", values)
	#conn.commit()

	#row delete
	# values = (19847, )
	# cur.execute("delete from airlines where id=?", values)
	# conn.commit()

	#table creation
	#cur.execute("create table daily_flights (id integer, departure date, arrival date, number text, route_id integer)")
	#conn.commit()

	#add data to newly created table
	#cur.execute("insert into daily_flights values (1, '2016-09-28 0:00', '2016-09-28 12:00', 'T1', 1)")
	#conn.commit()

	#close connection and cursor
	cur.close()
	conn.close()
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)



