'''
Yuyang Zhang
SoftDev1 pd07
HW09 -- No Treble
2017-10-15
'''



import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="school.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

'''
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);" #put SQL statement in this string
c.execute(command)    #run SQL statement

f= csv.DictReader(open("courses.csv"))

for row in f:
    code = row['code']
    mark = row['mark']
    ident = row['id']
    command = "INSERT INTO courses VALUE(code, mark, indent);"
    c.execute(command)
'''
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER);" #put SQL statement in this string
c.execute(command)    #run SQL statement

f= csv.DictReader(open("peeps.csv"))

for row in f:
    name = row['name']
    age = row['age']
    ident = row['id']
    command = "INSERT INTO peeps VALUE(name, age, indent);" 
    c.execute(command)
    

#==========================================================
db.commit() #save changes
db.close()  #close database


