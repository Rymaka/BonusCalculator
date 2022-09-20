from turtle import color
from tkinter import *
from tkinter.scrolledtext import *
import re


root = Tk()
root.wm_title("Anus for Bonus")
# Open window having dimension 300x220
root.geometry('300x220')
root.minsize(300,220)
root.maxsize(300,220)
root.configure(bg='black')
root.iconbitmap("fox_creative_craft_paper_origami_icon_226504.ico")
lines = []
#make an entry box
Text_Entry = Entry(root, width=100, font=('Helvetica', '14', 'bold'))
Text_Entry.pack(side = 'top')
#clear log.txt before any action
def clearTxt():
    f = open('log.txt', 'w')
    f.close

#input your data to a txt file. It will put /n between inputs
def inputTextToAFile():
    clearTxt()
    file = open('log.txt','a+')
    file.write(Text_Entry.get() + '\n')
    file.close()
    Text_Entry.delete(0, 'end')
    changeTxtToAnormal()
    main()

#change text in a file from a garbage dispisal to a shiny numbers
def changeTxtToAnormal():
    with open('log.txt','r') as p:
        global ok
        numbersreaded = open('log.txt').read()
        ok = re.findall("(?<=[AZaz])?(?!\d*=)[0-9]+", numbersreaded)
        p.close
 


#main script for summint entered numbers in text
def main():
    global ListOfNumbers
    global rawinput
    global f
    global p
    global numbersWithSpace
    global ok
    global lbl
    gg = list(map(int,ok))
    eBall = (sum(gg))
    ball = eBall/10
    stringOfBall= str(ball)
    lbl.config(text='Earned eBalls = ' + stringOfBall)

#bind commands in russian to normal 
    
def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
        event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

#create a button to make calculations
Action = Button(root, text = 'Start Calculation', height = 3, width = 100, fg='#993af0', bg='#262626', font=('Helvetica',14,'bold'), command = inputTextToAFile)
Action.pack(side='top')
lbl = Label(root, text="", height = 3, width = 100, bg = 'black', fg= '#993af0', font=('Helvetica',14,'bold') )
lbl.pack(side = 'bottom')


#stay on top of all programms
root.attributes('-topmost',True)

#dont forget to focus
Text_Entry.focus_set()
#to make russian commands run in a window
root.bind('<Return>', lambda event: inputTextToAFile())

root.bind_all("<Key>", _onKeyRelease, "+")
#the end of the root script
root.mainloop()