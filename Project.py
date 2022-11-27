from tkinter import *
from PIL import ImageTk
import os

#Class to create node for circular double linked list
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

#Function to insert the images into the nodes 
def insert(data):
    global head,tail
    temp = head
    while temp.next is not tail:
        temp = temp.next
    newNode = Node(data)
    temp.next = newNode
    tail.prev = newNode
    newNode.next = tail
    newNode.prev = temp

#Assigning the folder's path to "folderPath" variable in the folder in which all our images are present
folderPath = '/Users/sumitkumar/Documents/img_folder'

#Function to change the background image when the user clicks
#next button
def nextImage():
    global root
    bg = ImageTk.PhotoImage(file=next())
    label = Label(root, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    btn = Button(root, text="->", command=nextImage, border=0, height=3, width=1)
    btn.place(x=1330, y=400)
    btn = Button(root, text="<-", command=previousImage, border=0, height=3, width=1)
    btn.place(x=25, y=400)
    root.mainloop()

#Function to change the background image when the user clicks
#previous button
def previousImage():
    global root
    bg = ImageTk.PhotoImage(file=prev())
    label = Label(root, image=bg)
    btn = Button(root, text="->", command=nextImage, border=0, height=3, width=1)
    btn.place(x=1330, y=400)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    btn = Button(root, text="<-", command=previousImage, border=0, height=3, width=1)
    btn.place(x=25, y=400)
    root.mainloop()

#Changing the reference of the variable "counter" to its next node
#when the user clicks next button.It returns the image path of the image which is present in that node 
def next():
    global counter
    counter = counter.next
    return folderPath + '/' + counter.data

#Changing the reference of the variable "counter" to its previous node
#when the user clicks previous button.It returns the image path of the image which is present in that node 
def prev():
    global counter
    counter = counter.prev
    return folderPath + '/' + counter.data

#In os module,'listdir' method returns all the files present in that
#directory as a list
images = os.listdir(folderPath)

#Creating double circular linked list
head = Node(images[0])
tail = Node(images[-1])
counter = head
head.next = tail
tail.prev = head
tail.next = head
head.prev = tail

#Inserting the images into the nodes
for i in range(len(images)):
    if i == 0 or i == len(images) - 1:
        pass
    else:
        insert(images[i])

#Creating a GUI(Graphical User Interface) Window using 'tkinter' module
#in which we are going to display the image
root = Tk()
root.title("I M A G E   V I E W E R")
root.geometry("1400x900")
#Image
bg = ImageTk.PhotoImage(file=folderPath + '/' + images[0])
label = Label(root, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)
#Right button
btn = Button(root, text="->", command=nextImage, border=0, height=3, width=1)
btn.place(x=1330, y=400)
#Left button
btn = Button(root, text="<-", command=previousImage, border=0, height=3, width=1)
btn.place(x=25, y=400)
root.mainloop()
