print("This is text-editor.py file")

#Import tkinter module for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox


# Main window Code
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

#create text area for writing
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("GUnjan's project", 18)
)

text.pack(expand=True, fill=tk.BOTH)


# Main logic starts from here 

#Function 1- to create a new file


def new_file():
    text.delete(1.0, tk.END)  # Clear the text area

#Function 2- to open the file


def open_file():
    # Open a file dialogue to select a file
    file_path = filedialog.askopenfilename(
        defaulttextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        #Open selected file
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)  # Clear existing content
            text.insert(tk.END, file.read())  # Insert new content
    
#Function 3 - to save the file


def save_file():
    #open save file dialogue 
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        #Save the content to the selected file
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))  # Write content to file

    messagebox.showinfo("Save", "File saved successfully!")

#Menu bar creation

menu = tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)

#New, Open, Save, Exit

#Add file menu to menu bar 
menu.add_cascade(label="file",menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# starts and keeps the window open
root.mainloop()



