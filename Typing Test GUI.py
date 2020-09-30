# Typing Test GUI
# Version 2.0
# Created by Han
# Finished on 6/5/2020


#import modules
import tkinter as tk
from time import time
from tkinter import messagebox


# Function to configure the easy level 
def easygen():
    global sptext
    global counter

    # Enable the start and finish button
    startbutton['state'] = tk.NORMAL
    finishbutton['state'] = tk.NORMAL
    # set the counter into the configured time
    counter = 60
    m, s = divmod(counter, 60)
    timelabel.config(text="Time remaining:" + str(m).zfill(1) + ':' + str(s).zfill(2) )

    text = 'To believe or not to believe.'
    actext = 'To believe or not to believe.'

    gen = True
    if gen == True:
        wordlabel['text'] = text
    
    # splits the paragraph into a list
    sptext = actext.split()


# Function to configure the moderate level 
def moderategen():
    global sptext
    global counter

    startbutton['state'] = tk.NORMAL
    finishbutton['state'] = tk.NORMAL
    counter = 120
    m, s = divmod(counter, 60)
    timelabel.config(text="Time remaining:" + str(m).zfill(1) + ':' + str(s).zfill(2) )

    text = 'It didn’t take long to make me realise I had fucked up my\nlife, physically and mentally. Over the past three years living\nthe wrong life decision, I have managed to fail my health\ncheck-up, my quality of life,and even throwing everything\naway that made me human.'
    actext = 'It didn’t take long to make me realise I had fucked up my life, physically and mentally. Over the past three years living the wrong life decision, I have managed to fail my health check-up, my quality of life, and even throwing everything away that made me human.'

    gen = True
    if gen == True:
        wordlabel['text'] = text
    
    sptext = actext.split()


# Function to configure the hard level 
def hardgen():
    global sptext
    global counter
    startbutton['state'] = tk.NORMAL
    finishbutton['state'] = tk.NORMAL
    counter = 180
    m, s = divmod(counter, 60)
    timelabel.config(text="Time remaining:" + str(m).zfill(1) + ':' + str(s).zfill(2) )
    text = 'A freelancer or freelance worker, is a term commonly used\nfor a person who is self-employed and is not necessarily\ncommitted to a particular employer long-term. Freelance\nworkers are sometimes represented by a company or a\ntemporary agency that resells freelance labor to clients;\nothers work independently or use professional associations\nor websites to get work.'
    actext = 'A freelancer or freelance worker, is a term commonly usedfor a person who is self-employed and is not necessarily committed to a particular employer long-term. Freelance workers are sometimes represented by a company or a temporary agency that resells freelance labor to clients; others work independently or use professional associations or websites to get work.'
    gen = True
    if gen == True:
        wordlabel['text'] = text

    sptext = actext.split()


# Function when the start button is clicked 
def start():
    global begin

    # Enable the typebox for input
    typingbox.configure(state="normal")

    def count():
        global counter
        m, s = divmod(counter, 60)
        if counter >0:
            counter -= 1
            timelabel.config(text="Time remaining:" + str(m).zfill(1) + ':' + str(s).zfill(2) )
            timelabel.after(1000, count)
        elif finish():
            timelabel.config(text="")
        elif counter <=0:
            timelabel.config(text="Time remaining:0:00")
            end = time()
            answer_verification()
            typingbox.delete('1.0', end)
            typingbox.configure(state="disabled")
            startbutton['state'] = tk.DISABLED
            finishbutton['state'] = tk.DISABLED
    
    count()
    begin = time()


# Function when the finish button is clicked
def finish():
    global counter
    global end 

    counter = 0
    end = time()


# Function to check the typed words 
def answer_verification():
    # To get the content from the typebox
    result=typingbox.get("1.0","end")
    resultbreak = result.split()

    errorcount = 0
    correct = 0

    for i in range(len(resultbreak)):
        if resultbreak[i] != sptext[i]:
            errorcount +=1
        else:
            correct += 1
            
    final = (end - begin) /60
    wpm = float(len(resultbreak)) // final 
    accu = correct/len(sptext) * 100 
    messagebox.showinfo("Results", "Your typed " + str(correct) + " out of " + str(len(sptext)) + " words correctly.\n" + "Your WPM is: " + str(wpm) + "\nYour overall accuracy is " + str(accu))
    

root =tk.Tk()
root.title("Typing Test Version 1.0 GUI")

canvas = tk.Canvas(root, height=2736, width=1824)
canvas.pack()

frame = tk.Frame(root, bg="#E8F8F5")
frame.place(relheight=1, relwidth=1)

designlabel = tk.Label(root, height=2736, width=60, bg='#D1F2EB')
designlabel.place(x=0)

title = tk.Label(root, text='Typing\nTest',font='Helvectica 60', relief='flat', bg='#D1F2EB',fg='#45B39D')
title.place(x=75, rely=0.125)

subtitle = tk.Label(root, text='Test your typing skills!', font='Helvectica 15', relief='flat', bg='#D1F2EB', fg='#1ABC9C')
subtitle.place(x=108, y=285)

stripe = tk.Label(root, width=40, bg='#D0D3D4')
stripe.place(x=65, y=360,relheight=0.0001)

context = tk.Label(root, text='Finish typing within the time limit,\nfind out how many words you type\ncorrectly, your WPM, and accuracy.', font='Helvectica 12', bg='#D1F2EB', fg='#1ABC9C', justify='left')
context.place(x=85, y=390)

context2 = tk.Label(root, text='Version 2.0, created by Han, 6/5/2020', font='Helvectica 12', bg='#D1F2EB', fg='#1ABC9C', justify='left')
context2.place(x=75, y=448)

configframe = tk.Frame(root, height=160, width=150, bg='#D1F2EB')
configframe.place(x=125, y=555)

easybutton = tk.Button(configframe, text='Easy',font='Helvectica 20', relief='flat', bg='#8FD0CA',fg='white', command=lambda: easygen())
easybutton.place(relx=0.001, rely=0.002,height=50, width=150)

moderatebutton = tk.Button(configframe, text='Moderate',font='Helvectica 20', relief='flat', bg='#5AC6C6', fg='white', command=lambda: moderategen())
moderatebutton.place(relx=0.001, rely=0.345,height=50, width=150)

hardbutton = tk.Button(configframe, text='Hard',font='Helvectica 20', relief='flat', bg='#40B5BC', fg='white', command=lambda: hardgen())
hardbutton.place(relx=0.001, rely=0.69,height=50, width=150)

upperframe = tk.Frame(root,height=270, width=745, bg='#E8F8F5')
upperframe.place(relx=0.38, rely=0.09)

borderlabel = tk.Label(upperframe, bg='white')
borderlabel.place(relx=0.001, rely=0.002, height=268, width=743)

wordlabel = tk.Label(upperframe, bd=3, bg='#A2D9CE',fg='white', font='Helvectica 20', anchor='nw', justify='left')
wordlabel.place(relx=0.005, rely=0.02, height=260, width=737)

buttonframe = tk.Frame(root, height=50, width=745, bg='#E8F8F5')
buttonframe.place(relx=0.38, rely=0.4715)

timelabel = tk.Label(buttonframe, font='Helvetica 20', relief='flat', bg='#E8F8F5', fg='#148F77', anchor='w')
timelabel.place(relx=0.335, rely=0.002,height=50, width=275)

startbutton = tk.Button(buttonframe, text='Start', font='Helvectica 20', relief='flat', bg='#82E0AA', fg='white',state=tk.DISABLED, command=lambda: start())
startbutton.place(relx=0.001, rely=0.002,height=50, width=150)

finishbutton = tk.Button(buttonframe, text='Finish', font='Helvectica 20', relief='flat', bg='#E74C3C',fg='white', state=tk.DISABLED, command=lambda: finish())
finishbutton.place(relx=0.797, rely=0.002,height=50, width=150)

inputframe = tk.Frame(root,height=270, width=745, bg='#E8F8F5')
inputframe.place(relx=0.38, rely=0.59)

border2label = tk.Label(inputframe, bg='white')
border2label.place(relx=0.001, rely=0.002, height=268, width=743)

typingbox = tk.Text(inputframe, bg='#D5F5E3',fg='#148F77', font='Consolas 15', state='disabled', spacing1=2, spacing2=2, spacing3=3, padx = 10, relief='flat')
typingbox.place(relx=0.005, rely=0.02, height=260, width=737)

root.mainloop()