from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib as plt
import tkinter as tk


class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Viewer")
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand="true")
        self.geometry("900x800")

def open_file_dialog():
    """
    Opens the file dialog
    For now it does not return anything
    """
    root.filename = filedialog.askopenfilename(initialdir="/home/adrikos/Desktop/My_projects/Simple_Data_Visualizer/csv_files", 
                                           title="Select A File", 
                                           filetypes=(("csv files", "*.csv"),
                                           ("all files", "*.*")))




if __name__ == "__main__":
    root = Aplication()
    tk.Button(root,text='Open File',command=open_file_dialog).pack()
    root.mainloop()