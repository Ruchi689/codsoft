from tkinter import *
from tkinter import ttk

class todo: 
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry('350x410+300+150')

        self.text_result = Text(self.root, bd=5, height=2, width=46, font='ariel, 10 italic bold')
        self.text_result.place(x=10, y=10)
        self.calculation = ""

        def add_to_calculation(symbol):
            # global calculation
            self.calculation += str(symbol)
            self.text_result.delete(1.0, "end");
            self.text_result.insert(1.0, self.calculation)
        def evaluate_calculation():
            try:
                result = str(eval(self.calculation))
                self.calculation = ""
                self.text_result.delete("1.0", "end")
                self.text_result.insert("1.0", result)
            except Exception as e:
                clear_field()
                self.text_result.insert("1.0", "Error: " + str(e))  

        def clear_field():
            self.calculation = ""     
            self.text_result.delete(1.0,"end");
        

        mul=60
        xdiv=10;
        ydiv=mul;
        ydiv1=mul+70;
        ydiv2=mul+70*2;
        ydiv3=mul+70*3;
        ydiv4=mul+70*4;

        # first row
        self.button = Button(self.root, text="c", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:clear_field())
        self.button.place(x=xdiv, y=ydiv)
        self.button1 = Button(self.root, text="√", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation("√"))
        self.button1.place(x=xdiv+90, y=ydiv)
        self.button2 = Button(self.root, text="/", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation("/"))
        self.button2.place(x=xdiv+180, y=ydiv)
        self.button3 = Button(self.root, text="<-", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:clear_field())
        self.button3.place(x=xdiv+270, y=ydiv)

        # second row
        self.button12 = Button(self.root, text="7", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(7))
        self.button12.place(x=xdiv, y=ydiv1)
        self.button13 = Button(self.root, text="8", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(8))
        self.button13.place(x=xdiv+90, y=ydiv1)
        self.button14 = Button(self.root, text="9", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(9))
        self.button14.place(x=xdiv+180, y=ydiv1)
        self.button15 = Button(self.root, text="*", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation("*"))
        self.button15.place(x=xdiv+270, y=ydiv1)

        # third row
        self.button8 = Button(self.root, text="4", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(4))
        self.button8.place(x=xdiv, y=ydiv2)
        self.button9 = Button(self.root, text="5", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(5))
        self.button9.place(x=xdiv+90, y=ydiv2)
        self.button10 = Button(self.root, text="6", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(6))
        self.button10.place(x=xdiv+180, y=ydiv2)
        self.button11 = Button(self.root, text="-", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation("-"))
        self.button11.place(x=xdiv+270, y=ydiv2)


        # fourth row
        self.button = Button(self.root, text="1", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(1))
        self.button.place(x=xdiv, y=ydiv3)
        self.button = Button(self.root, text="2", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(2))
        self.button.place(x=xdiv+90, y=ydiv3)
        self.button = Button(self.root, text="3", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(3))
        self.button.place(x=xdiv+180, y=ydiv3)
        self.button = Button(self.root, text="+", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation("+"))
        self.button.place(x=xdiv+270, y=ydiv3)


        # fifth row
        self.button = Button(self.root, text="!", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation("!"))
        self.button.place(x=xdiv, y=ydiv4)
        self.button = Button(self.root, text="0", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation(0))
        self.button.place(x=xdiv+90, y=ydiv4)
        self.button = Button(self.root, text=".", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:add_to_calculation("."))
        self.button.place(x=xdiv+180, y=ydiv4)
        self.button = Button(self.root, text="=", font='serif, 20 bold italic', width=3, bg='purple', fg='white', command=lambda:evaluate_calculation())
        self.button.place(x=xdiv+270, y=ydiv4)



def main():
    root = Tk()
    u1 = todo(root)
    root.mainloop()


if __name__ =="__main__":
    main()