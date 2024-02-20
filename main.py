import sqlite3

con = sqlite3.connect("mycompany.db")
cur_obj = con.cursor()

cur_obj.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)")
con.commit()

def insert_values(id,name,salary,department,position):
    cur_obj.execute("INSERT INTO employees VALUES(?,?,?,?,?)",(id,name,salary,department,position))
    con.commit()

def update_values(sal,id):
    cur_obj.execute("UPDATE employees SET salary=? WHERE id=?",(sal,id))
    con.commit()

def fetch_all():
    cur_obj.execute("SELECT * FROM employees")
    print(cur_obj.fetchall())

def delete_all():
    cur_obj.execute("DELETE FROM employees")
    con.commit()

fetch_all()
cur_obj.close()
con.close()