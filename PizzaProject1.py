import tkinter as tk
from tkinter import messagebox

class MyGUI:
        def __init__(self):

        #creating window -> setting title -> setting geometry
                self.window = tk.Tk()
                self.window.title("Pizza Project by Helen & Alex")
                self.window.configure(background="black")
                self.window.geometry("1050x800")
                font_text = ('Courier New', 20, 'normal')
        # creating a label 
                self.label = tk.Label(self.window, text="Welcome to PizzAH!",bg= "black", fg= "white", font=('Courier New', 30, "bold"))
                self.label.grid(row=0, column=0)

        #adding a photo
                self.photo1 = tk.PhotoImage(file="pizzah.png")
                self.smallerImage = self.photo1.subsample(2 , 2)
                tk.Label(self.window, image=self.smallerImage, background="black").grid(row=1, column=0)

        #add a text asking for the size
                self.ask_size = tk.Label(self.window, text="Pick a size (one only): ",bg="black",fg="white", font=font_text)
                self.ask_size.grid(row=2, column=0)

        #creating text entry box for pizza size
                self.small = tk.IntVar()
                self.medium = tk.IntVar()
                self.large = tk.IntVar()

                self.small_c = tk.Checkbutton(self.window, text="Small",bg="black",fg="white", font=font_text, variable=self.small)
                self.medium_c = tk.Checkbutton(self.window, text="Medium",bg="black",fg="white", font=font_text, variable=self.medium)
                self.large_c = tk.Checkbutton(self.window, text="Large",bg="black",fg="white", font=font_text, variable=self.large)
                #placing the button for size 
                self.small_c.grid(row=3, column=0)
                self.medium_c.grid(row=3, column=1)
                self.large_c.grid(row=3, column=2)

                #ask user to pick crust type
                self.ask_crust = tk.Label(self.window, text="What type of crust would you like? ", font=font_text)
                self.ask_crust.grid(row=6, column=20)
                self.thin_c = tk.IntVar()
                self.deep_c = tk.IntVar()
                self.hand_c = tk.IntVar()
                #adding a button for the pizza crust add frames for this 
                self.thin = tk.Checkbutton(self.window, text="Thin-crust",bg="black",fg="white", font=font_text, variable=self.thin_c)
                self.deep = tk.Checkbutton(self.window, text="Deep-Dish",bg="black", fg="white",font=font_text, variable=self.deep_c)
                self.hand = tk.Checkbutton(self.window, text="Hand-tossed",bg="black",fg="white", font=font_text, variable=self.hand_c)
                #placement of button crust
                self.thin.grid(row=6, column=0)
                self.deep.grid(row=7, column=0)
                self.hand.grid(row=8, column=0)

        #creating text box to print order
                self.order = tk.Text(self.window,bg="black", foreground="white", height= 10,width=25,font=font_text)
                self.order.grid(row=9, column=0)
        #adding submit button
                self.submit = tk.Button(self.window, text="Submit",foreground="red", font=font_text)
                self.submit.grid(row=10, column=0)

                #creating a variable to let the computer know what the user is pickingfor toppings
                self.mush_T = tk.IntVar()
                self.pep_T = tk.IntVar()
                self.sausage_T = tk.IntVar()
                self.onion_T = tk.IntVar()
                #add check boxes for pizza toppings add frames for this 
                self.mush = tk.Checkbutton(self.window, text="mushrooms",bg="black",fg="white", font=font_text, variable=self.mush_T)
                self.pep = tk.Checkbutton(self.window, text="pepperoni",bg="black", fg="white",font=font_text, variable=self.pep_T)
                self.sausage = tk.Checkbutton(self.window, text="sausage",bg="black",fg="white", font=font_text, variable=self.sausage_T)
                self.onion = tk.Checkbutton(self.window, text="onion",bg="black",fg="white", font=font_text, variable=self.onion_T)
                # placement of buttons
                self.mush.grid(row=11, column=0)
                self.pep.grid(row=12, column=0)
                self.sausage.grid(row=13, column=0)
                self.onion.grid(row=14, column=0)

                self.window.mainloop()

MyGUI()
