import tkinter as tk
from tkinter import messagebox
#--------------------------------
# Helen Truong & Alex Ancelovici
# 11/21/2022
#Pizza Project 
#--------------------------------
class MyGUI:

        def __init__(self):
        # this is the function for your submit button
                def click():
                        self.output.delete(0.0, tk.END)
                        #creating variables to help with final output
                        crust, sizeP, self.message  = "", "", ""
                        toppings = "Cheese "
                        price = 0.0
                #checking to make sure the user picks only one size & crust type
                        if (self.small.get()+self.medium.get()+self.large.get()) != 1:
                                self.message = "Please only pick one size!"
                        elif (self.thin_c.get()+self.deep_c.get()+self.hand_c.get()) != 1:
                                        self.message = "Please pick one crust type!"
                        else:
                #after checking we are going to for the users options and print out the reciept 
                                if self.small.get() == 1 :
                                        sizeP = "small"
                                        price += 10.99
                                elif self.medium.get() == 1:
                                        sizeP = "medium"
                                        price += 12.99
                                elif self.large.get() == 1:
                                        sizeP = "large"
                                        price += 14.99

                                if self.thin_c.get() == 1:
                                        crust = "thin-crust"
                                elif self.deep_c.get() == 1:
                                        crust = "deep-dish"
                                elif self.hand_c.get() == 1:
                                        crust = "hand-tossed"

                                if self.mush_T.get()== 1:
                                        toppings += "mushroom "
                                        price += 1.25
                                if self.sausage_T.get()== 1:
                                        toppings += "sausages "
                                        price += 1.25
                                if self.pep_T.get() ==1:
                                        toppings += "pepperoni "
                                        price += 1.25
                                if self.onion_T.get() == 1:
                                        toppings += "onion "
                                        price += 1.25
                                tax = price * 0.0875
                                price += tax 
                                self.message = "Your order is: \n" + sizeP + " pizza \n" + crust + "\nToppings are: \n"+ toppings + "\nTax is: $"+ f"{tax:.2f}"+ "\nYour final cost is: $" + f"{price:.2f}"
                        self.output.insert(tk.END, self.message)
                        #end of the function ^^
        
        #creating window -> setting title -> setting geometry
                self.window = tk.Tk()
                self.window.title("Pizza Project by Helen & Alex")
                self.window.configure(background="black")
                self.window.geometry("1050x800")
        #just a variable to initalize so we dont have to repeat again
                font_text = ('Courier New', 18, 'normal')
                large_font = ('Courier New', 19, 'bold')
        # creating a label 
                self.label = tk.Label(self.window, text="Welcome to PizzAH!",bg= "black", fg= "white", font=('Courier New', 30, "bold"))
                self.label.pack(pady=1)

        #adding a photo
                self.photo1 = tk.PhotoImage(file="pizzah.png")
                self.smallerImage = self.photo1.subsample(2 , 2)
                tk.Label(self.window, image=self.smallerImage, background="black").pack(side="top", anchor="center")

        #create a frame for pizza size, crust, toppings
                size_frame = tk.LabelFrame(self.window, background="black")
                size_frame.pack(pady = 3,side="top", anchor="nw" )
                crust_frame = tk.LabelFrame(self.window,background="black")
                crust_frame.pack(pady = 3,side="top" , anchor="nw")
                toppings_frame = tk.LabelFrame(self.window,background="black")
                toppings_frame.pack(pady = 3,side="top" , anchor="nw")

        #add a text asking for the pizza size
                self.ask_size = tk.Label(size_frame, text="Pick a size (one only): ",bg="black",fg="white", font=large_font)
                self.ask_size.pack(side="top",anchor="nw", pady=2)
        #creating text entry box for pizza size
                self.small = tk.IntVar()
                self.medium = tk.IntVar()
                self.large = tk.IntVar()
        #creating 3 buttons for size
                self.small_c = tk.Checkbutton(size_frame, text="Small",bg="black",fg="white", font=font_text, variable=self.small)
                self.medium_c = tk.Checkbutton(size_frame, text="Medium",bg="black",fg="white", font=font_text, variable=self.medium)
                self.large_c = tk.Checkbutton(size_frame, text="Large",bg="black",fg="white", font=font_text, variable=self.large)
        #placing the button for size 
                self.small_c.pack(side="left", anchor="nw")
                self.medium_c.pack(side="left" )
                self.large_c.pack(side="left")

        #ask user to pick crust type
                self.ask_crust = tk.Label(crust_frame, text="What type of crust would you like? ",bg="black",fg="white", font=large_font)
                self.ask_crust.pack(anchor="w", pady=2)
                self.thin_c = tk.IntVar()
                self.deep_c = tk.IntVar()
                self.hand_c = tk.IntVar()
        #adding a button for the pizza crust add frames for this 
                self.thin = tk.Checkbutton(crust_frame, text="Thin-crust",bg="black",fg="white", font=font_text, variable=self.thin_c)
                self.deep = tk.Checkbutton(crust_frame, text="Deep-Dish",bg="black", fg="white",font=font_text, variable=self.deep_c)
                self.hand = tk.Checkbutton(crust_frame, text="Hand-tossed",bg="black",fg="white", font=font_text, variable=self.hand_c)
        #placement of button crust
                self.thin.pack(side="left")
                self.deep.pack(side="left")
                self.hand.pack(side="left")

        #creating a variable to let the computer know what the user is picking for toppings
                self.mush_T = tk.IntVar()
                self.pep_T = tk.IntVar()
                self.sausage_T = tk.IntVar()
                self.onion_T = tk.IntVar()
        #add check boxes for pizza toppings add frames for this 
                self.ask_top = tk.Label(toppings_frame, text="What toppings would you like? ",bg="black",fg="white", font=large_font)
                self.ask_top.pack(side="top", anchor="nw", pady=2)
                self.mush = tk.Checkbutton(toppings_frame, text="mushrooms",bg="black",fg="white", font=font_text, variable=self.mush_T)
                self.pep = tk.Checkbutton(toppings_frame, text="pepperoni",bg="black", fg="white",font=font_text, variable=self.pep_T)
                self.sausage = tk.Checkbutton(toppings_frame, text="sausage",bg="black",fg="white", font=font_text, variable=self.sausage_T)
                self.onion = tk.Checkbutton(toppings_frame, text="onion",bg="black",fg="white", font=font_text, variable=self.onion_T)
        # placement of buttons for toppings
                self.mush.pack(side="left", anchor="nw")
                self.pep.pack(side="left")
                self.sausage.pack(side="left")
                self.onion.pack(side="left")

        #output text box for ordering the pizza
                self.output = tk.Text(self.window,bg="black", fg="white", height=10,width=43,font=large_font)
                self.output.place(x=458, y=455)
        #creating submit button to finalize order
                self.submit = tk.Button(self.window, text="Submit",foreground="red",command=click, font=large_font)
                self.submit.pack(padx=1, pady = 2, anchor="nw")

                self.window.mainloop()

MyGUI()
