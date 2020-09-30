import tkinter as tk

#initialize the class root
class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #lable initialization done here
        self.label = tk.Label(self, text="Hello World", padx=5, pady=5)
        
        #this pack() method basically used for packs widgets in rows or columns 
        self.label.pack()

if __name__ == "__main__":
    #call the Root class
    root = Root()
    root.mainloop()
