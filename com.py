import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS e_cost(
        Reason TEXT,
        Birr INTEGE,
        Comment TEXT,
        User TEXT,
        Date TEXT
       
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS empty_box(
        
        Type TEXT,
        Box TEXT,
        Amount INTEGER,
        Date TEXT
       
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS credit_box(
        
        Name TEXT,
        Amount INTEGER,
        Date TEXT
       
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS t_cost(

        Birr INTEGE,
        Date TEXT
               
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS e_income(
        
        Type TEXT,
        Box TEXT,
        
       
        Amount INTEGER,
        Date TEXT
       
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS t_income(
    
        Credit TEXT,
        Total_c INTEGER,
        Total INTEGER,
        Date TEXT
        
       
        )""")



c.execute("""CREATE TABLE IF NOT EXISTS user_auth(
        Auth_Type TEXT,
        Username TEXT,
        Password TEXT
        
       
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS Item_conf(
     
        Name TEXT,
        Price INTEGER
        
       
        )""")



c.execute("""CREATE TABLE IF NOT EXISTS stock(
     
        Name TEXT
     
        
       
        )""")
conn.commit()
conn.close()
    
             
