from tkinter import *
from tkinter.font import BOLD
from HillCipher import *
from tkinter import ttk
import numpy as np

# INPUT: KEY1, KEY2, PLAINTEXT
#OUTPUT: TABLE CIPHERTEXT (CLASSICAL, IMPROVED), TIME (CLASSICAL, IMPROVED)
# main Window which get input, process and show result
# in this we'll get 2 Key matrix and Plaintext Path
def Window1(n):
    
    Key1Matrix = []
    Key2Matrix = []

    classical_ciphertext = ""
    improve_ciphertext = ""

    window1 = Tk()
    window1.title("Hill Cipher")
    #window2 size is 650x600, top-left conner at 120x120
    window1.geometry("580x480+120+120")
    window1.configure(bg='bisque2')
    window1.resizable(False, False)

    #------------------------------------------------
    #Key Matrix area
    #------------------------------------------------
    #Key Matrix frame
    KeyMatrixFrame = LabelFrame(window1, height=440, width=170, text="KEY MATRIXS", font=('arial', 12, 'bold'))
    KeyMatrixFrame.place(x = 20, y = 20)
    
    # empty arrays for your Entrys and StringVars
    text_var1= []
    entries1 = []
    text_var2= []
    entries2 = []

    def Encrypt_result(size):

        for i in range(rows):
            Key1Matrix.append([])
            Key2Matrix.append([])
            for j in range(cols):
                Key1Matrix[i].append(int(text_var1[i][j].get()))
                Key2Matrix[i].append(int(text_var2[i][j].get()))
        
        Key1 = np.array(Key1Matrix)
        Key2 = np.array(Key2Matrix)

        planitextPath = StringVar()
        planitextPath =  plaintextBox.get("1.0", "end-1c")
        
        classical_ciphertext = ""
        improve_ciphertext = ""

        encrypt_classical = Classical(Key1,size,planitextPath,classical_ciphertext)
        encrypt_improved = Improve(Key1,Key2,size,planitextPath,improve_ciphertext)

        time_encrypt_classical = encrypt_classical.encrypt()
        time_encrypt_improve = encrypt_improved.encrypt()

        classical_ciphertext = encrypt_classical.ciphertext
        improve_ciphertext = encrypt_improved.ciphertext

        resultTable.insert(parent='', index='end', iid = 0, text = "Ciphertext", values = (classical_ciphertext, improve_ciphertext))
        resultTable.insert(parent='', index='end', iid = 1, text = "Excuted\nTime", values = (time_encrypt_classical, time_encrypt_improve))

    # callback function to get your StringVars
    '''def getKeyMatrix():
        for i in range(rows):
            Key1Matrix.append([])
            Key2Matrix.append([])
            for j in range(cols):
                Key1Matrix[i].append(int(text_var1[i][j].get()))
                Key2Matrix[i].append(int(text_var2[i][j].get()))
        
        Key1 = np.array(Key1Matrix)
        Key2 = np.array(Key2Matrix)'''


    rows = n
    cols = n
    #Display Key 1
    x1 = 0
    y1 = 10 
    Label(KeyMatrixFrame, text="Key1 ", font=('arial', 10, 'bold'), bg="#c0c0c0").place(x=x1+10, y=y1+10)
    for i in range(rows):
        # append an empty list to your two arrays
        # so you can append to those later
        text_var1.append([])
        entries1.append([])
        for j in range(cols):
            # append your StringVar and Entry
            text_var1[i].append(StringVar())
            key = Entry(KeyMatrixFrame, textvariable=text_var1[i][j],width=3, bg = '#c0c0c0')
            key.insert(0, "k"+str(n*i+j+1))
            entries1[i].append(key)
            entries1[i][j].place(x=30 + x1, y=50 + y1)
            x1 += 30  

        y1 += 30
        x1 = 0

    #Display Key 2
    x2 = 0
    y2 = 180
   
    Label(KeyMatrixFrame, text="Key2 (improved cipher)", font=('arial', 10, 'bold'), bg="#c0c0c0").place(x=x2+10, y=y2+10)
    for i in range(rows):
        text_var2.append([])
        entries2.append([])
        for j in range(cols):
            text_var2[i].append(StringVar())
            key = Entry(KeyMatrixFrame, textvariable=text_var2[i][j],width=3, bg = '#c0c0c0')
            key.insert(0, "k"+str(n*i+j+1))
            entries2[i].append(key)
            entries2[i][j].place(x=30 + x2, y=50 + y2)
            x2 += 30  

        y2 += 30
        x2 = 0
    
    # WE GET KEY MATRIXS HERE, BY THIS BUTTON
    #Button submit matrix
    '''Button(KeyMatrixFrame,text="Submit Keys", bg='#c0c0c0', width=15, command=lambda: getKeyMatrix()).place(x=48 ,y=350)'''

    #Button change Key size
    Button(KeyMatrixFrame, text = "Change Key size",  bg='#c0c0c0', width=15, command=lambda: Window2(window1)). place(x = 48, y = 380)


    #------------------------------------------------
    #Plaintext
    #------------------------------------------------
    PlaintextFrame = LabelFrame(window1, height=110, width=360, text="PLAINTEXT", font=('arial', 12, 'bold'))
    PlaintextFrame.place(x = 200, y = 20)

    #plaintext Box
    plaintextBox = Text(PlaintextFrame, height=1, width=47, font=('arial', 10))
    plaintextBox.place(x = 10, y = 20)

    #submit plaintext button function
    '''def getPlaintextLink():
        planitextPath = StringVar()
        planitextPath =  plaintextBox.get("1.0", "end-1c")'''

    # WE GET KEY MATRIXS HERE, BY THIS BUTTON
    #submit plaintext button
    '''getPlaintextButton = Button(PlaintextFrame, text = "Get Plaintext",bg='#c0c0c0', width=15, command=lambda: getPlaintextLink())
    getPlaintextButton.place(x = 230, y = 50)'''


    #------------------------------------------------
    #Decryption area
    #------------------------------------------------
    resultFrame = LabelFrame(window1, height=320, width=360, text = "DECRYPTION & COMPARE", font=('arial', 12, 'bold')) 
    resultFrame.place(x = 200, y = 140)

    resultTable = ttk.Treeview(resultFrame, height=3)
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview.Heading", 
        font = (None, 10, 'bold'),
        background = "silver",
        foreground = "black",
        rowheight = 60)
    style.configure("Treeview", 
        background = "white",
        foreground = "black",
        rowheight = 60,
        fieldbackground = "silver")
    style.map("Treeview", background = [('selected', 'green')])
    


    #Define Column
    resultTable['columns'] = ( "Classical", "Improved")

    resultTable.column("#0",  anchor = "center", width = 80, minwidth = 25)
    resultTable.column("Classical", anchor = "center",  width = 125)
    resultTable.column("Improved", anchor = "center",  width = 125)
    
   
    resultTable.heading("#0", text = "Hill Cipher", anchor = "center")
    resultTable.heading("Classical", text = "Classical", anchor = "center")
    resultTable.heading("Improved", text = "Improved", anchor = "center")
   
    #TODO: ADD RESULT IN VALUES LIST
    '''resultTable.insert(parent='', index='end', iid = 0, text = "Ciphertext", values = ("Classical Ciphertext", "Improved Ciphertext"))
    resultTable.insert(parent='', index='end', iid = 1, text = "Excuted\nTime", values = ("Classical\nExcuted Time", "Improved\nExcuted Time"))'''

    resultTable.place(x=10, y=10)
    #------------------------------------------------
    #Window1 loops
    #------------------------------------------------

    Button(window1,text="Result", bg='#c0c0c0', width=15, command=lambda: Encrypt_result(n)).place(x=300 ,y=400)

    window1.mainloop()
    return(window1)
    

#SubWindow which change the size of both Keys
def Window2(window1):
    window2 = Tk()
    window2.title("Hill Cipher")
    #window2 size is 650x600, top-left conner at 120x120
    window2.geometry("270x250+360+120")
    window2.configure(bg='bisque2')
    window2.resizable(False, False)

    Label(window2, text = "This application was created \nto implement  The improved Hill Cipher", width=32).place(x = 20, y = 20)

    KeySizeFrame = LabelFrame(window2, height=160, width=230)
    KeySizeFrame.place(x = 20, y = 70)

    Label(KeySizeFrame, text = "Chose your key's size").place(x = 10, y = 10)

    def NewKeySize(i):    
            window1.destroy()
            window2.destroy()
            Window1(i)

    option1 = Button(KeySizeFrame, text="2x2", font=('arial', 10), bg='#c0c0c0', command=lambda: NewKeySize(2), width=15)
    option1.place(x = 20, y = 40)
    option2 = Button(KeySizeFrame, text="3x3", font=('arial', 10), bg='#c0c0c0', command=lambda: NewKeySize(3), width=15)
    option2.place(x = 20, y = 70)
    option3 = Button(KeySizeFrame, text="4x4", font=('arial', 10), bg='#c0c0c0', command=lambda: NewKeySize(4), width=15)
    option3.place(x = 20, y = 100)

    window2.mainloop()

Window1(2)
