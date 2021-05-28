from tkinter import *
from tkinter import filedialog

def plaintextDialog():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    filepath_label = Label(root,text=filepath,font=("bold",10))
    filepath_label.place(x=202,y=450)

root = Tk()
root.geometry('700x700')
root.title("Btl Ly thuyet mat ma")

label = Label(root, text="Encrypt",width=20,font=("bold", 20))
label.place(x=180,y=53)

#enter key1
k1_label = Label(root, text="K1:",width=20,font=("bold", 10))
k1_label.place(x=80,y=130)

k1_feild = Text(root, height=5, width=35,
            padx=8, pady=8)
k1_feild.place(x=200,y=130)

#enter key2
k2_label = Label(root, text="K2:",width=20,font=("bold", 10))
k2_label.place(x=80,y=270)

k2_feild = Text(root, height=5, width=35,
            padx=8, pady=8)
k2_feild.place(x=200,y=270)

#enter plaintext
plaintext_label = Label(root, text="Plaintext:",width=20,font=("bold", 10))
plaintext_label.place(x=70,y=410)
Button(root, text="Open", width=20, command=plaintextDialog).place(x=200,y=410)

#enter type
type_label = Label(root, text="Type:",width=20,font=("bold", 10))
type_label.place(x=80,y=490)

type_list = ['Classical','Improve'];
c=StringVar()
droplist=OptionMenu(root,c, *type_list)
droplist.config(width=40)
c.set('select cipher') 
droplist.place(x=200,y=490)

Button(root, text='Submit', width=20,bg='brown',fg='white').place(x=300,y=550)

root.mainloop()