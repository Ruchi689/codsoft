from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry('650x410+300+150')

my_password = chr(randint(33,126))

def new_rand():
    # clear entry box
    pw_entry.delete(0,END)
    # Get pw length and convert it to integer
    pw_length = int(my_entry.get())
    # create a variable to hold our pw
    my_password = ''
    # loop through pw length
    for x in range(pw_length):
        my_password += chr(randint(33,126))
    # output password to string
    pw_entry.insert(0, my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

# Create entry box to designate number of characters
my_entry = Entry(lf, font='ariel, 25 bold')
my_entry.pack(pady=20, padx=20)

# create entry box for our returned password
pw_entry = Entry(root, text='', font='ariel, 25 bold', bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# create our buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

my_button2 = Button(my_frame, text="Copy to clipboard", command=clipper)
my_button2.grid(row=0, column=1, padx=10)

root.mainloop()