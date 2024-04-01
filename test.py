import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("List Manager")
        self.geometry("500x500")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menuBar = tk.Menu(self)
        #File
        file_menu = tk.Menu(menuBar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menuBar.add_cascade(label="File", menu=file_menu)

        #Edit
        edit_menu = tk.Menu(menuBar, tearoff=0)
        edit_menu.add_command(label="Add", command=self.add_item)
        edit_menu.add_command(label="Delete", command=self.delete_item)
        edit_menu.add_command(label="Edit", command=self.edit_item)
        menuBar.add_cascade(label="Edit", menu=edit_menu)

        #Help
        Help_menu = tk.Menu(menuBar, tearoff=0)
        Help_menu.add_command(label="About", command=self.show_about)
        menuBar.add_cascade(label="Help", menu=Help_menu)

        #Show Menu in Window
        self.config(menu=menuBar)

    #File Menu
    def create_widgets(self):
        #Frame
        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill="both", expand=True)

    def open_file(self):
        #Open File in File Manager
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        #Get File Content to ListBox
        if file_path:
            with open(file_path, "r") as file:
                self.listbox.delete(0, tk.END)
                for line in file:
                    self.listbox.insert(tk.END, line.strip())
    
    def save_file(self):
        #Save File Settings to File Manager
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        #Save File
        if file_path:
            with open(file_path, "w") as file:
                for i in range(self.listbox.size()):
                    file.write(self.listbox.get(i) + "\n")

    #Edit Menu
    def add_item(self):
        #DialogBox for Input
        item = simpledialog.askstring("Add Item", "Enter Item:")

        #Add Item to the ListBox
        if item:
            self.listbox.insert(tk.END, item)
    
    def delete_item(self):
        #Get the Selected Item
        selected_item = self.listbox.curselection()

        #Delete Selected Item
        if selected_item:
            for index in selected_item[::-1]:
                self.listbox.delete(index)

    def edit_item(self):
        #Get the Selected Item
        selected_item = self.listbox.curselection()

        #Edit the Selected Item
        if selected_item:
            item = self.listbox.get(selected_item)
            new_item = simpledialog.askstring("Edit Item", "Enter New Value:", initialvalue=item)

            #Edit the Selected Item with New Value
            if new_item:
                self.listbox.delete(selected_item)
                self.listbox.insert(selected_item, new_item)

    #Help Menu
    def show_about(self):
        messagebox.showinfo("About", "List Manager\nVersion 1.0\nAuthor: Villaber, Christian Jude")




app = Application()
app.mainloop()