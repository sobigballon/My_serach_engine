import sqlite3

conn = sqlite3.connect('lesson.db')
print "Opened database successfully";

cursor = conn.execute("SELECT name, link, des  from lesson_xx")
conn.commit()
print list(cursor)
'''for row in cursor:
   print "name = ", row[0]
   print "link = ", row[1]
   print "des = ", row[2]
'''
print "Operation done successfully";
conn.close()
