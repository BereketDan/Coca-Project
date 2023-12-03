# import sqlite3
# import datetime as dt
# day = str(dt.datetime.now())[0:11]


# mad = []
# # ------------------ for daily income --------------------
# con = sqlite3.connect('main.db')

# c = con.cursor() 
# c.execute(f"SELECT * FROM e_income WHERE  Date = '" + day +"' ")
# uno = c.fetchall()

# print(">>> income per day list ")
# print()
# for _ in uno:
#     print(_[0],_[2])
#     mad.append(_)
# # ------------------ for daily income --------------------


# print()
# print()
# print() #############################################################
# print()




# # ------------------ for unsold   --------------------
# k = con.cursor() 
# k.execute(f"SELECT * FROM empty_box WHERE  Date = '" + day +"' ")


# unoox = k.fetchall()


# print(">>> credit birr list per day")
# print()
# for i in unoox:
#     print(i[0],i[2])

#     mad.append(i)

# # ------------------ for unsold  --------------------




# print()
# print()
# print() #############################################################
# print(mad)
# print()



# # ------------------ for defalt price  --------------------
# d = con.cursor() 
# d.execute(f"SELECT * FROM Item_conf ")


# unoo = d.fetchall()

# print(">>> price fixed")
# print()
# for i in unoo:
#     print(i[0],i[1])

# # ------------------ for defalt price  --------------------




# print()
# print()
# print() #############################################################
# print()





# # ------------------ for credit   --------------------
# b = con.cursor() 
# b.execute(f"SELECT * FROM credit_box WHERE  Date = '" + day +"' ")


# unox = b.fetchall()


# print(">>> credit birr list per day")
# print()
# for i in unox:
#     print(i[0],i[1])

# # ------------------ for credit   --------------------




# print()
# print()
# print() #############################################################
# print()




from cryptography.fernet import Fernet

# we will be encrypting the below string.
message = "hello geeks"

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = b'BCS_ihcYsg3K0brRD2l_cbrDB35G8kw0EO_4wHZuXoQ='

# Instance the Fernet class with the key

fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
