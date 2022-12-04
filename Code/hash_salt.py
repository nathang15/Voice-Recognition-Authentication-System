import bcrypt

#hash and salt the plain password
#return the hashed one

def hash_salt(pwd):
    passwd = pwd.encode() 
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed