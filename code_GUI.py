from tkinter import *

def Window2(n):
    window2 = Tk()
    window2.title("Hill Cipher")
    #window2 size is 650x600, top-left conner at 120x120
    window2.geometry("580x460+120+120")
    window2.configure(bg='bisque2')
    window2.resizable(False, True)


    #------------------------------------------------
    #Key Matrix area
    #------------------------------------------------
    #Key Matrix frame
    KeyMatrixFrame = LabelFrame(window2, height=180+4*60, width=170, text="KEY MATRIXS", font=('arial', 12, 'bold'))
    KeyMatrixFrame.place(x = 20, y = 20)

    # empty arrays for your Entrys and StringVars
    text_var1= []
    entries1 = []
    text_var2= []
    entries2 = []

    # callback function to get your StringVars
    def getKeyMatrix():
        Key1Matrix = []
        Key2Matrix = []
        for i in range(rows):
            Key1Matrix.append([])
            Key2Matrix.append([])
            for j in range(cols):
                Key1Matrix[i].append(text_var1[i][j].get())
                Key2Matrix[i].append(text_var2[i][j].get())
        for key in Key1Matrix:
            print(key)



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
            entries1[i].append(Entry(KeyMatrixFrame, textvariable=text_var1[i][j],width=3, bg = '#c0c0c0'))
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
            entries2[i].append(Entry(KeyMatrixFrame, textvariable=text_var2[i][j],width=3, bg = '#c0c0c0'))
            entries2[i][j].place(x=30 + x2, y=50 + y2)
            x2 += 30  

        y2 += 30
        x2 = 0
    #Button submit matrix
    
    button= Button(KeyMatrixFrame,text="Submit Keys", bg='#c0c0c0', width=15, command=lambda: getKeyMatrix())
    button.place(x=48 ,y=350)



    #------------------------------------------------
    #Plaintext
    #------------------------------------------------
    PlaintextFrame = LabelFrame(window2, height=110, width=360, text="PLAINTEXT", font=('arial', 12, 'bold'))
    PlaintextFrame.place(x = 200, y = 20)

    #plaintext Box
    plaintextBox = Text(PlaintextFrame, height=1, width=47, font=('arial', 10))
    plaintextBox.place(x = 10, y = 20)

    #submit plaintext button function
    def getPlaintextLink():
        print("Link: " +plaintextBox.get("1.0", "end-1c"))

    #submit plaintext button
    getPlaintextButton = Button(PlaintextFrame, text = "Get Plaintext",bg='#c0c0c0', width=15, command=lambda: getPlaintextLink())
    getPlaintextButton.place(x = 230, y = 50)


    #------------------------------------------------
    #Decryption area
    #------------------------------------------------
    resultFrame = LabelFrame(window2, height=300, width=360, text = "DECRYPTION & COMPARE", font=('arial', 12, 'bold')) 
    resultFrame.place(x = 200, y = 140)

    Label(resultFrame, text = "RESULT HERE").place(x = 50, y = 50)

    #------------------------------------------------
    #Window2 loops
    #------------------------------------------------
    window2.mainloop()

def Window1():
    window1 = Tk()
    window1.title("Hill Cipher")
    #window2 size is 650x600, top-left conner at 120x120
    window1.geometry("270x250+360+120")
    window1.configure(bg='bisque2')
    window1.resizable(False, False)

    Label(window1, text = "This application was created \nto implement  The improved Hill Cipher", width=32).place(x = 20, y = 20)

    KeySizeFrame = LabelFrame(window1, height=160, width=230)
    KeySizeFrame.place(x = 20, y = 70)

    Label(KeySizeFrame, text = "Chose your key's size").place(x = 10, y = 10)
    check1 = StringVar()
    check2 = StringVar()
    check3 = StringVar()

    option1 = Checkbutton(KeySizeFrame, text = "2x2", variable=check1, onvalue="On", offvalue="Off")
    option1.deselect()
    option1.place(x = 20, y = 40)
    option2 = Checkbutton(KeySizeFrame, text = "3x3", variable=check2, onvalue="On", offvalue="Off")
    option2.deselect()
    option2.place(x = 20, y = 60)
    option3 = Checkbutton(KeySizeFrame, text = "4x4", variable=check3, onvalue="On", offvalue="Off")
    option3.deselect()
    option3.place(x = 20, y = 80)

    def GoToWindow2():    
        if  check1.get() == "On":
            Window2(2)
        elif check2.get() == "On":
            Window2(3)
        else:
            Window2(4)

    Button(KeySizeFrame, text= "Next", width= 10, bg = "grey", command= lambda: GoToWindow2()).place(x = 10, y = 110)

    window1.mainloop()

Window1()
