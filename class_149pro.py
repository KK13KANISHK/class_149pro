
"""
Created on Thu May 18 17:26:15 2023

@author: kanis
"""

from tkinter import *
import random

root = Tk()
root.title("Random word generator generator")
root.geometry("500x500")

label1 = Label(root)
list1 = ["K", "k", "B", "Z", "@", "&", "a", "S", "*", "idk"]
print(list1)

def random_number():
    random_no = random.randint(0,4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("Your word is: " + random_lucky_friend)
    label1["text"] = random_lucky_friend
    
btn = Button(root)
btn1 = Button(root, text="Random word is:  ", command = random_number)
btn1.place(relx=0.5,rely=0.5,anchor= CENTER)
label1.place(relx=0.5,rely=0.6,anchor=CENTER)



root.mainloop()