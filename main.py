import os, time
from getPath import getpath as gp
from selection import select_option as se
from backInPath import back_in_p as bip
from encrypt import CheckFileExist as cfe
from encrypt import SignIn as si




def main():
    selec = se()
    if selec == "1":
        gp()
        main()
    elif selec == "2":
        bip()
        gp()
        main()
    elif selec == "3":
        cfe()
    elif selec == "4":
        si()


main()
