#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import sqlite3 as lite
import sys

#SET A PROPER DATABASE
con = lite.connect('test.db')

### Saving in Database Starts
def saveData(*args):
	try:
		banana = (donnee.get(), )
		#print("you should not see this")
		with con:
		 	cur = con.cursor()

		 	cur.execute("DROP TABLE IF EXISTS Cars")
		 	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT)")
		 	cur.execute("INSERT INTO Cars VALUES(1, ?)", banana)
	except ValueError:
		pass
### Saving in Database Ends

### GUI PART STARTS

root = Tk()		#start tk
root.title("DataBase Test")		#name the window

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

donnee = StringVar()
reponse = StringVar()

donnee_entry = ttk.Entry(mainframe, width=15, textvariable=donnee)
donnee_entry.grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe, width=15, textvariable=reponse).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Show").grid(column=2, row=3, sticky=(W))
ttk.Button(mainframe, text="Save", command=saveData).grid(column=1, row=3, sticky=(W))

ttk.Label(mainframe, text="Write Here").grid(column=1, row=1, sticky=(W))
ttk.Label(mainframe, text="First entry").grid(column=2, row=1, sticky=(W))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
donnee_entry.focus()

##GUI PART ENDS

root.mainloop()