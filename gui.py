import tkinter
from tkinter import filedialog
import customtkinter
from PIL import ImageTk,Image
import webbrowser
import datetime
import time
import os
import index

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")  

#app
app = customtkinter.CTk()  
app.geometry("620x520")
app.title("musicRR")
app.resizable(False, False)

def getDate():
    print("Up")

def generateButton():
    time = str(entryTime.get())
    time = time.split(":")
    date = str(entryDate.get())
    date = date.split("/")
    d = datetime.datetime(int(date[2]),int(date[1]),int(date[0]),int(time[0]),int(time[1]), tzinfo=datetime.timezone.utc)
    start_date = d.timestamp()
    if checkbox.get() == "on":
        print(int(entry2.get()))
        index.main(float(entry1.get()),int(entry2.get()),int(entry3.get()),int(entry4.get()),filename,start_date)
    if checkbox.get() == "off":
        index.main(float(entry1.get()),0,int(entry3.get()),int(entry4.get()),filename,start_date)

def openURL():
    webbrowser.open_new("https://github.com/msharr/Visualising-RR-Through-Music#readme")

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

# background
img = Image.open("img/ekg-monitor.png")
img1 = ImageTk.PhotoImage(img)
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

# frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
l2=customtkinter.CTkLabel(master=frame, text="musicRR",font=("Century Gothic",20))
l2.place(x=115, y=35)

# input date
entryTime=customtkinter.CTkEntry(master=frame, width=109, placeholder_text="Time (e.g 17:15)")
entryTime.place(x=50, y=75)
entryDate=customtkinter.CTkEntry(master=frame, width=110, placeholder_text="dd/mm/yyyy")
entryDate.place(x=161, y=75)

# input 1
entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Tuning level")
entry1.place(x=50, y=110)

# input 2
entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Exclusion duration")
entry2.place(x=50, y=145)

checkbox = customtkinter.CTkCheckBox(master=frame,width=0, height =0,  text="", 
                                      onvalue="on", offvalue="off")
checkbox.place(x=15, y=147)

# input 3
entry3=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Min Tempo")
entry3.place(x=50, y=180)

# input 4
entry4=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Max Tempo")
entry4.place(x=50, y=215)

# button main
button1 = customtkinter.CTkButton(master=frame, width=220, text="Generate", command=generateButton, corner_radius=6)
button1.place(x=50, y=255)

# button 1
img2 = customtkinter.CTkImage(Image.open("img/patient.png").resize((20,20), Image.Resampling.LANCZOS))
button2 = customtkinter.CTkButton(master=frame, image=img2, text="Patient", width=100, height=20, compound="left", fg_color="white", text_color="black", hover_color="#AFAFAF", command = browseFiles)
button2.place(x=50, y=295)

# button 2
img3 = customtkinter.CTkImage(Image.open("img/file.jpg").resize((20,20), Image.Resampling.LANCZOS))
button3 = customtkinter.CTkButton(master=frame, image=img3, text="Help", width=100, height=20, compound="left", fg_color="white", text_color="black", hover_color="#AFAFAF", command = openURL)
button3.place(x=170, y=295)

# loop
app.mainloop()
