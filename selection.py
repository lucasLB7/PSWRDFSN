import time
def select_option():
    print("Please select the opertion you would want to do: \n")
    time.sleep(2)
    print("1: View current directory \n")
    print("2: Go back in directory \n")
    print("3: Register account \n")
    print("4: Sign In \n")


    selection = (input())
    return(selection)
