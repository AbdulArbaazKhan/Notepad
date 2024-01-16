from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os


def New():
    root.title("Untitle - iNote")
    text_area.delete(1.0, END)


def Open():
    global file
    file = filedialog.askopenfilename(defaultextension="*.txt", filetypes=[("All Files", "*.*"),
                                                                           ("Text Documents", "*.txt"),
                                                                           ("Python Files", "*.py")])
    if file == "":
        file = None
    else:
        with open(file, "r") as open_file:
            root.title(os.path.basename(file) + " - iNotes")
            text_area.delete(1.0, END)
            text_area.insert(1.0, open_file.read())
            open_file.close()


def Save():
    global file
    if file is None:
        file = filedialog.asksaveasfilename(initialfile="Untittled.txt", defaultextension="*.txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt"),
                                                       ("Python Files", "*.py")])
        if file == "":
            file = None
        else:
            # save a new file
            with open(file, "w") as save_file:
                save_file.write(text_area.get(1.0, END))
                save_file.close()
            root.title(os.path.basename(file) + " - iNote")
    else:
        with open(file, "w") as save_file:
            save_file.write(text_area.get(1.0, END))
            save_file.close()


def Save_as():
    global file
    if file is None:
        Save()
    else:
        file = filedialog.asksaveasfilename(initialfile=f"{os.path.basename(file)}", defaultextension="*.txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt"),
                                                       ("Python Files", "*.py")])
        if file == "":
            file = None
        else:
            with open(file, "w") as save_as_file:
                save_as_file.write(text_area.get(1.0, END))
                save_as_file.close()


def Wrap():
    if wrap_choose.get() == 1:
        text_area.config(wrap="none")
        xscroll.pack(side=BOTTOM, fill=X)
    elif wrap_choose.get() == 0:
        text_area.config(wrap=WORD)
        xscroll.pack_forget()


def Font():
    rootf = Tk()
    rootf.geometry("534x444")
    rootf.title("Font Customization")
    font_frame = ttk.LabelFrame(rootf, text="Font Customization")
    font_list_var = StringVar()
    font_style_list_var = StringVar()
    font_size_list_var = StringVar()

    ttk.Label(font_frame, text="Choose Font:", anchor=CENTER).grid(row=0,column=1)
    fonts_list = Listbox(font_frame, listvariable=font_list_var)
    fonts_list.grid(row=1,column=1,padx=20)

    ttk.Label(font_frame, text="Choose Font Style:").grid(row=0,column=2)
    fonts_style_list = Listbox(font_frame, listvariable=font_size_list_var)
    fonts_style_list.grid(row=1,column=2, padx=20)

    ttk.Label(font_frame, text="Choose Font Size:").grid(row=0, column=3)
    fonts_style_list = Listbox(font_frame, listvariable=font_style_list_var)
    fonts_style_list.grid(row=1, column=3, padx=20)
    font_frame.pack(fill=X)
    rootf.mainloop()


root = Tk()
root.geometry("760x740")
root.title("iNotes")

# Creating Text Area
file = None
text_area = Text(root, undo=TRUE, maxundo=10, font="timesnewroman 14")
text_area.pack(expand=1, fill=BOTH)
main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0, title="File", )
file_menu.add_command(label="New", command=New)
file_menu.add_command(label="Open", command=Open)
file_menu.add_command(label="Save", command=Save)
file_menu.add_command(label="Save As", command=Save_as)
main_menu.add_cascade(menu=file_menu, label="File")

edit_menu = Menu(main_menu, tearoff=0, title="File", )
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=lambda: text_area.event_generate("<<Undo>>"))
edit_menu.add_command(label="Redo", command=lambda: text_area.event_generate("<<Redo>>"))
wrap_choose = IntVar()
edit_menu.add_checkbutton(label="Wrap", command=Wrap, variable=wrap_choose)
edit_menu.add_command(label="Font", command=Font)
main_menu.add_cascade(menu=edit_menu, label="Edit")

help_menu = Menu(main_menu, tearoff=0, title="File", )
help_menu.add_command(label="About",
                      command=lambda: messagebox.showinfo("iNotes - Notes Taking Easy", "iNotes by Arbaz Khan"))
help_menu.add_command(label="Exit", command=root.destroy)
help_menu.add_command(label="Count", command=lambda: print(text_area.count(1.0, END)))
main_menu.add_cascade(menu=help_menu, label="Help")

root.config(menu=main_menu)

# Adding x and y scroll bar
scroll = Scrollbar(text_area)
xscroll = Scrollbar(text_area, orient=HORIZONTAL)
scroll.pack(side=RIGHT, fill=Y)
# Pack for xscroll is on wrap func
scroll.config(command=text_area.yview)
xscroll.config(command=text_area.xview)
text_area.config(yscrollcommand=scroll.set)
text_area.config(xscrollcommand=xscroll.set)

root.mainloop()
