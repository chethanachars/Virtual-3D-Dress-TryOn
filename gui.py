#create a python window with two buttons using tkinter module
#one button to choose person image and save it to a folder
#one button to choose cloth image and save it to a folder
#create a button to start the program
#when program starts it will run a couple of shell scripts
#create tkinter window with good size and title and background color with a label

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import subprocess
from PIL import Image, ImageTk

#function to choose person image and save it to a folder
def choose_person():
    global person_image
    person_image = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    print(person_image)
    #save the person image to a folder
    subprocess.call(["cp", person_image, "/home/preethu/Documents/project2/M3D-VTON/mpv3d_example/image"])
    #display the person image in a label in the window
    img = PhotoImage(file=person_image)
    label = Label(window, image=img)
    label.image = img
    label.pack()
    #set position of the label
    label.place(x=300, y=200)


#function to choose cloth image and save it to a folder
def choose_cloth():
    global cloth_image
    cloth_image = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(cloth_image)
    #save the cloth image to a folder
    subprocess.call(["cp", cloth_image, r"./mpv3d_example/cloth"])
    img = ImageTk.PhotoImage(file=cloth_image)
    label2 = Label(window, image=img)
    label2.image = img
    label2.pack()
    #set position of the label
    label2.place(x=1000, y=200)

   




#function to start the program
def start_program():
    #run a shell script to start the program
    subprocess.call(["/home/pi/Desktop/Project/Project.sh"])

#function to close the window
def close_window():
    window.destroy()

#function to create a tkinter window with good size and title and background color with a label
window = tk.Tk()
window.title("Choose Images")
#window.geometry("500x500")
#set window size to fit the screen
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
#set background color
window.configure(background='navy')
label = tk.Label(window, text="Choose Person Image", fg="white", bg="black")
label.pack()
label2 = tk.Label(window, text="Choose Cloth Image", fg="white", bg="black")
label2.pack()
#set position of the label
#label.place(x=100, y=100)
#label.place(x=100, y=200)

#function to create a button to choose person image and save it to a folder
button = tk.Button(window, text="Choose Person Image", command=choose_person)
button.pack()
#set position of the button
button.place(x=100, y=200)

#function to create a button to choose cloth image and save it to a folder
button = tk.Button(window, text="Choose Cloth Image", command=choose_cloth)
button.pack()
#set position of the button
button.place(x=100, y=300)


#function to create a button to start the program
button = tk.Button(window, text="Start Program", command=start_program)
button.pack()
#set position of the button
button.place(x=100, y=400)


#function to create a button to close the window
button = tk.Button(window, text="Close Window", command=close_window)
button.pack()
#set position of the button
button.place(x=100, y=500)


#set position of the image
label.place(x=300, y=200)
label2.place(x=500, y=200)




window.mainloop()


