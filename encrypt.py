import os
import hashlib
import csv
#from user_dashboard import access


def CheckFileExist():
    try:
        os.path.isfile("passlist.csv")
        GenPassword()
    except:
        print("generating new file")
        foo = open("passlist.txt" , 'w')
        foo.write('')
        foo.close()
        GenPassword()

def SHA512Enc():
    userInfo = input("Enter username: \n")
    hashString = input("Enter a password: \n")

    sha_sig = hashlib.sha512(hashString.encode()).hexdigest()
#    with open("passlist.txt" , 'a') as foo:
    with open('passlist.csv','a',newline='') as foo:
            a = csv.writer(foo)
            data = [userInfo,sha_sig]
            a.writerows([data])
    #    foo.write(sha_sig)
    #    foo.close()




def GenPassword():
    function = input("Register for full access, do you accept? y|n\n")
    if function == "y":
        SHA512Enc()
    else:
        pass

def SignIn():
    get_user = input("Enter your username \n")
    get_pass = input("enter your password \n")
    sha_sig = hashlib.sha512(get_pass.encode()).hexdigest()
    print(sha_sig)

    with open('passlist.csv','r') as foo:
        usr = csv.reader(foo)
        for row in usr:
            if row[0] == get_user and row[1] == sha_sig:
                print("yay!")
            else:
                pass
