import sqlite3
import datetime as dt
day = str(dt.datetime.now())[0:11]
con = sqlite3.connect('main.db')
c = con.cursor() 
c.execute(f"SELECT * FROM e_income WHERE  Date = '" + day +"' ")
incomerow = c.fetchall()
print(incomerow)


df = ["one","two","there","Four"]
c.execute(f"ALTER TABLE e_income DROP '" + df[0] +"' ")
for i in range(len(df)):
   c.execute(f"ALTER TABLE e_income ADD '" + df[i] +"' INTEGER")
con.commit()
con.close()
       
