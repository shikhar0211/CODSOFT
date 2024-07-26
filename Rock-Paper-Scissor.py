import tkinter
from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Rock-Paper-Scissor")
window.configure(background="black")


#computer side
image_default1 = ImageTk.PhotoImage(Image.open("Default-1.png"))
image_rock1 = ImageTk.PhotoImage(Image.open("Rock-L.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("Paper-L.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("Scissor-L.png"))

#user side
image_default2 = ImageTk.PhotoImage(Image.open("Default-2.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("Rock-R.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("Paper-R.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("Scissor-R.png"))

label_user = Label(window, image=image_default1)
label_computer = Label(window, image=image_default2)
label_computer.grid(row=1, column=0)
label_user.grid(row=1, column=4)

computer_score = Label(window, text=0, font=("arial", 60, "bold"), fg="red")
user_score = Label(window, text=0, font=("arial", 60, "bold"), fg="red")
computer_score.grid(row=1, column=1)
user_score.grid(row=1, column=3)

user_indicator = Label(window, font=("arial", 40, "bold"), text="USER", bg="orange", fg="blue")
computer_indicator = Label(window, font=("arial", 40, "bold"), text="COMPUTER", bg="orange", fg="blue")
computer_indicator.grid(row=0, column=1)
user_indicator.grid(row=0, column=3)

def msg_updation(a):
    final_msg['text'] = a
    
def comp_update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)

def user_update():
    final = int(user_score['text'])
    final += 1
    user_score["text"] = str(final)

def winner_check(u, c):
    if u==c:
        msg_updation("It's a Tie")
    elif u=="rock":
        if c=="paper":
            msg_updation("Computer Wins !!")
            comp_update()
        else:
            msg_updation("User Wins !!")
            user_update()
    elif u=="paper":
        if c=="scissor":
            msg_updation("Computer Wins !!")
            comp_update()
        else:
            msg_updation("User Wins !!")
            user_update()
    elif u=="scissor":
        if c=="rock":
            msg_updation("Computer Wins !!")
            comp_update()
        else:
            msg_updation("User Wins !!")
            user_update()
    else:
        pass

to_select = ["rock", "paper", "scissor"]

def choice_update(a):

    choice_comp = to_select[randint(0, 2)]
    if choice_comp == "rock":
        label_computer.configure(image=image_rock1)
    elif choice_comp == "paper":
        label_computer.configure(image=image_paper1)
    else:
        label_computer.configure(image=image_scissor1)

    if a == "rock":
        label_user.configure(image=image_rock2)
    elif a == "paper":
        label_user.configure(image=image_paper2)
    else:
        label_user.configure(image=image_scissor2)

    winner_check(a, choice_comp)



final_msg = Label(window, font=("arial", 40, "bold"), bg="red", fg="white")
final_msg.grid(row=3, column=2)

button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update("rock")).grid(row=2, column=1)
button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update("paper")).grid(row=2, column=2)
button_scissor = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update("scissor")).grid(row=2, column=3)


window.mainloop()
