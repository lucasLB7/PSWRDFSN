# Simple enough, just import everything from tkinter.
from tkinter import *


#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("PASSWORD FUSION")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="sign up", command=self.client_sign_up)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("chat.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def SHA512Enc(self):
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



    def GenPassword(self):
        function = input("Register for full access, do you accept? y|n\n")
        if function == "y":
            SHA512Enc()
        else:
            pass


    def client_exit(self):
        exit()

    def client_sign_up(self):
        CheckFileExist()

    def CheckFileExist(self):
        try:
            os.path.isfile("passlist.csv")
            GenPassword()
        except:
            print("generating new file")
            foo = open("passlist.txt" , 'w')
            foo.write('')
            foo.close()
            GenPassword()










# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)


#mainloop
root.mainloop()
