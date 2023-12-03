from flask import Flask,redirect,request,url_for,render_template,session
# from cryptography.fernet import Fernet
import datetime as dt
import sqlite3
import re
import json 
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# import pandas as pd
from glob import glob
from os.path import expanduser


app = Flask(__name__)
app.secret_key = "Onyxkillerwolf"
# key_x = b'BCS_ihcYsg3K0brRD2l_cbrDB35G8kw0EO_4wHZuXoQ='
# fernet = Fernet(key_x)

user_namex = ""



@app.route('/')
@app.route('/',methods = ['POST','GET'])
def login():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_auth ")
    data_x = c.fetchall()
    print(data_x)
    if request.method == 'POST':
        user_name = request.form['name']
        user_password = request.form['password']
        
        if user_name == 'admin' and user_password == '3232':
            user_name = user_namex

            session['user_password'] = user_password
            
            return redirect(url_for('index'))
        else:
            error = "Incorrect Paswsword"
            return render_template("login.html",error=error)

    return render_template("login.html")


@app.route('/')
@app.route('/analytic',methods = ['POST','GET'])
def analytic():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    conx = sqlite3.connect('main.db')
    c = conx.cursor() 
    if "user_password" in session:
        if request.method == 'POST':
            
            type_botx = request.form['type_bot']
            remain_botx = request.form['remain_bot']
            type_boxx= request.form['type_box'] 
            # remain_birrx = request.form['remain_birr']

            info = [type_botx,type_boxx,remain_botx,day]
            if not remain_botx == "":
                c.execute("INSERT INTO empty_box VALUES(?,?,?,?)",info)
                conx.commit()
                conx.close()
            else:
                print("wrong")
                warn = "Please insert Again"
                return render_template("analytic.html",warn=warn)


        return render_template("analytic.html")
    else:
        return redirect(url_for('login'))





@app.route('/')
@app.route('/index',methods = ['POST','GET'])
def index():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    conx = sqlite3.connect('main.db')
    c = conx.cursor() 
    if "user_password" in session:
        if request.method == 'POST':
           
            type_botx = request.form['type_bot']
            amount_botx = request.form['amount_bot']
            type_boxx= request.form['type_box'] 
            if not amount_botx == "":
                
                info = [type_botx,type_boxx,amount_botx,day]
                c.execute("INSERT INTO e_income VALUES(?,?,?,?)",info)
                conx.commit()
                conx.close()
            else:
                print("wrong")
                warn = "Please insert Again"
                return render_template("index.html",warn=warn)
                      
        
        return render_template("index.html")
    else:
        return render_template("login.html")




@app.route('/')
@app.route('/home',methods = ['POST','GET'])
def accept():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    if "user_password" in session:

        con = sqlite3.connect('main.db')
        c = con.cursor() 
        c.execute(f"SELECT * FROM e_income WHERE  Date = '" + day +"' ")
        incomerow = c.fetchall()
        print(incomerow)
        
        irowco = 0
        irowab = 0
        irowno = 0
        irowpe = 0
        for irow in incomerow:
            if irow[0] == "Coca":
                irowco = irow[2] * 390
            if irow[0] == "Ambo":
                irowab = irow[2] * 370
            if irow[0] == "Novida":
                irowno = irow[2] * 416
            if irow[0] == "Pet":
                irowpe = irow[2] * 365


        c.execute(f"SELECT * FROM empty_box WHERE Date = '" + day +"' ")
        emcomerow = c.fetchall() 
        erowco = 0
        erowab = 0
        erowno = 0
        erowpe = 0
        

        for irowx in emcomerow:
            if irowx[0] == "Coca":
                erowco = irowx[2] 
            if irowx[0] == "Ambo":
                erowab = irowx[2] 
            if irowx[0] == "Novida":
                erowno = irowx[2] 
            if irowx[0] == "Pet":
                erowpe = irowx[2] 
        cc = int(irowco/390) - erowco
        ca = int(irowab/280) - erowab
        cn = int(irowno/416) - erowno
        cp = int(irowpe/365) - erowpe






        sumx = 0
        for irowx in emcomerow:
            sumx =sumx + irowx[2]
        print("All credit case: ",sumx)

        
        print("coca",erowco,"ambo",erowab,"novida",erowno,"Pet",erowpe)
        
        c_tot = (cc * 390) + (ca * 280) + (cn * 416) + (cp*365)
        tot = irowco + irowab + irowno + irowpe
        print("all credit filter birr: ",c_tot)
        print("total birr: ",tot)
        print("coca c",cc ,"ambo c",ca ,"novida c",cn,"Pet c",cp)
        

        c.execute(f"SELECT * FROM credit_box WHERE Date = '" + day +"' ")
        item = c.fetchall()

        sumy = 0
        for itemx in item:
            sumy = sumy + itemx[1]
        infox=[sumy,c_tot-sumy,c_tot,day]

        
        c.execute("INSERT INTO t_income VALUES(?,?,?,?)",infox)
        con.commit()
        con.close()
       
        




        
        return redirect(url_for('analytic'))
    else:
        return redirect(url_for('index'))




@app.route('/')
@app.route('/total',methods = ['POST','GET'])
def total():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    if "user_password" in session:
        if request.method == 'POST':
             user = request.form['username']
             remain = request.form['remain_birr']
             info = [user,remain,day]
             if user == "" and remain == "" != None:
                print("Nomething going wrong")
             else:
                 c.execute("INSERT INTO credit_box VALUES(?,?,?)",info)
                 conn.commit()
           

        return redirect(url_for('about'))
    else:
        return redirect(url_for('login'))



@app.route('/about')
def about():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    if "user_password" in session:
         c.execute("SELECT * FROM credit_box" )
         item = c.fetchall() 
        

         return render_template("version.html",item=item)
    
    else:
        return render_template("login.html")



@app.route("/delist/<string:id>", methods = ["POST","GET"])
def delist(id):
    if "user_password" in session:
        if request.method == "GET":
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            c.execute("DELETE FROM credit_box WHERE Name = ? ",[id])
            conn.commit()
            return redirect(url_for('about'))
        return render_template("version.html")
    else:
        return render_template("login.html")        
 


@app.route("/Itemdel/<string:id>", methods = ["POST","GET"])
def Itemdel(id):
    if "user_password" in session:
        if request.method == "GET":
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            c.execute("DELETE FROM Item_conf WHERE Name = ? ",[id])
            conn.commit()
            return redirect(url_for('setting'))
        return render_template("setting.html")
    else:
        return render_template("login.html")        
 




@app.route("/setting", methods = ["POST","GET"])
def setting():
    dat = ""
    if "user_password" in session:
        
        conn = sqlite3.connect('main.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Item_conf ")
        dat = c.fetchall()
        temp_store = []
        for datx in dat:
            print(temp_store.append(datx[0]))

        print(temp_store)




        try:
            for i in range(len(temp_store)):
                c.execute(f"ALTER TABLE stock ADD '" + temp_store[i] +"' INTEGER")
                conn.commit()
        except:  
            pass



            
            
        return render_template("setting.html",dat=dat,user_namex=user_namex)
    else:
        return render_template("login.html")        




@app.route("/item_conf", methods = ["POST","GET"])
def item_conf():
    if "user_password" in session:
        conn = sqlite3.connect('main.db')
        c = conn.cursor()
        if request.method == "POST":
            item_name = request.form['item_name']
            item_price = request.form['item_price']

        print(item_name,item_price)
        info = [item_name,item_price]
        if  item_name == "" and item_price == "":
            print("wrong aaaaaaaaaaaaa")
            return redirect(url_for('setting'))
        else:
            c.execute("INSERT INTO Item_conf VALUES(?,?)",info)
            conn.commit()
            con = sqlite3.connect('main.db')
            cx = con.cursor()


            try:
                cx.execute(f"ALTER TABLE stock ADD '" + info[0] +"' INTEGER")
                con .commit()

            except:  
                pass

            
    
            
            
            
        return redirect(url_for('setting'))
    else:
        return render_template("login.html")        
 






@app.route('/')
@app.route('/auth_app',methods = ['POST','GET'])
def auth_app():
  
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    if "user_password" in session:
        if request.method == 'POST':
             type_userx = request.form['type_user']
            #  encType_user = fernet.encrypt(type_userx.encode())
             new_userx = request.form['new_user']
            #  encNew_user = fernet.encrypt(new_userx.encode())
             new_passx = request.form['new_pass']
            #  encNew_pass = fernet.encrypt(new_passx.encode())
             info = [type_userx,new_userx,new_passx]
            #  info2 = [encType_user,encNew_user,encNew_pass]
            
             print(info)
            #  print(info2)
            #  print(info)
            
             c.execute("INSERT INTO user_auth VALUES(?,?,?)",info)
             conn.commit()

             c.execute("SELECT * FROM user_auth")
           
             fc = c.fetchall()
             prin(fc)
            #  print( " ".join(fc)) 
            # #  print(fc)
            #  for fcx in fc:
                 
            #      print(str(fernet.decrypt(fcx[1].decode())))
            # #  encMessage = fernet.encrypt(fc.encode())
            # #  print(encMessage)
         
            # #  decMessage = fernet.decrypt(encMessage).decode()
            # #  print(decMessage)
           

        return redirect(url_for('setting'))
    else:
        return redirect(url_for('login'))









@app.route('/')
@app.route('/search',methods = ['POST','GET'])
def search():
    
    if "user_password" in session:
    
        
        if request.method == 'POST':
            s_list = request.form['slist']
            s_search = request.form['search']
            print(s_list,s_search)


            con = sqlite3.connect('patientdata.db')
            cx = con.cursor()
            cx.execute(f"SELECT * FROM patient WHERE {s_list} LIKE ? ",('%'+s_search+'%',) )
            item = cx.fetchall()  
        
        return render_template("index.html",item=item)

    else:
         return render_template("login.html")




@app.route('/')

@app.route('/outcome',methods = ['POST','GET'])
def outcome():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    if "user_password" in session:
        conn = sqlite3.connect('outcome.db')
        c = conn.cursor()
        if request.method == 'POST':
            
            do_permision = request.form['opermision']
            do_recivername = request.form['orecivername']
            do_providername = request.form['oprovidername']
            do_amount = request.form['oamount']
            do_reason = request.form['oreason']
            do_sign = request.form['osign']
            info = [do_reason,do_amount,do_providername,do_recivername,do_permision,do_sign,day]
            c.execute("INSERT INTO outcome VALUES(?,?,?,?,?,?,?)",info)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
       
    else:
        return render_template("login.html")  



   




@app.route('/')

@app.route('/income',methods = ['POST','GET'])
def income():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    if "user_password" in session:
        conn = sqlite3.connect('income.db')
        c = conn.cursor()
        if request.method == 'POST':
            
            de_birr = request.form['ebirr']
            info = [de_birr,day]
            c.execute("INSERT INTO income VALUES(?,?)",info)
        conn.commit()
        conn.close()
        
            
        return redirect(url_for('index'))

    else:
        return render_template("login.html")    




@app.route('/tax',methods = ['POST','GET'])
def tax():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    if "user_password" in session:
        conn = sqlite3.connect('tax.db')
        c = conn.cursor()
        if request.method == 'POST':
            
            d_taxbirr = request.form['taxbirr']
            info = [d_taxbirr,day] 
            c.execute("INSERT INTO tax VALUES(?,?)",info)
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    else:
        return render_template("login.html")    




@app.route('/version')
def version():
    
    if "user_password" in session:
        return render_template("versionapp.html")
    else:
        return render_template("login.html")




@app.route('/reserved', methods = ["POST","GET"])
def reserved():
    day = str(dt.datetime.now())[0:11]
    fday = str(dt.datetime.now())[0:7]
    if "user_password" in session:
        if request.method == 'POST':
            cost_reasonx = request.form['cost_reason']
            cost_birrx = request.form['cost_birr']
            cost_commentx= request.form['cost_comment'] 
            olad = [day,cost_reasonx,cost_birrx,cost_commentx]
            print(olad)
        return render_template("manual.html")
    else:
        return render_template("login.html")










@app.route("/delx/<int:id>", methods = ["POST","GET"])
def delx(id):
    if "user_password" in session:
        if request.method == "GET":
            conn = sqlite3.connect('reserve.db')
            c = conn.cursor()
            c.execute("DELETE FROM reserve WHERE Id = ? ",[id])
            conn.commit()
            return redirect(url_for('reserved'))
        return render_template("reserve.html")
    else:
        return render_template("login.html")        
    



@app.route('/manual')
def manual():
    if "user_password" in session:
        return render_template("manual.html")
    
    else:
        return render_template("login.html")



@app.route('/sumpage')
def sumpage():
    if "user_password" in session:
        conn = sqlite3.connect('summary.db')
        c = conn.cursor()
        c.execute("SELECT * FROM summary ")
        countt = c.fetchall()
        res = []
        for num in countt:
            res.append(num)
        return render_template("summary.html",res=res)
    
    else:
        return render_template("login.html")


@app.route('/costpage')
def costpage():
    if "user_password" in session:
        conn = sqlite3.connect('outcome.db')
        c = conn.cursor()
        c.execute("SELECT * FROM outcome ")
        countt = c.fetchall()
        res = []
        for num in countt:
            res.append(num)
       
        return render_template("cost.html",res=res)
    
    else:
        return render_template("login.html")




if __name__ == '__main__':
    app.run(debug = True , port=8080)