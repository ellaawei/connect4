from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Connect 4")
root.geometry("853x720")
clicked = True
count = 0

def checkifwon():
    pass

def b_click(b):
    global clicked, count
    if(b["text"]==" " and clicked == True):
        b["text"] = "red"
        clicked = False
        count += 1
        #checkifwon()
    elif(b["text"]==" " and clicked == False):
        b["text"] = "yellow"
        clicked = True
        count += 1
        #checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey, that box has already been selected\nPick Another Box.")

def reset():
    global buttons
    buttons = []
    for i in range (6):
        row = []
        for j in range(7):
            b = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 7, bg="White")
            row.append(b)
            b = None
        buttons.append(row)
        
    for r in range(6):
        for c in range(7):
            (buttons[r][c]).grid(row=r, column=c)
            (buttons[r][c]).configure(root, text=" ", command=lambda x1 = r, y1 = c: b_click(buttons[x1][y1]))
    
        
reset()
root.mainloop()
