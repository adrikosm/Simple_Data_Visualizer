from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib as plt
import tkinter as tk


class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Visualizer")

        # Data frame for csv
        self.data_frame = tk.LabelFrame(self, text="Data")
        self.data_frame.place(height=600, width=900, relwidth=0.53, relheight=0.6)

        # Frame for buttons
        self.file_frame = tk.LabelFrame(self, text='Buttons')
        self.load_buttons(self.file_frame)
        self.file_frame.place(height=300, width=900, rely=0.6, relx=0, relwidth=0.53, relheight=0.4)
        self.geometry("900x800")

        

    def open_file_dialog(self, master):
        """
        Opens the file dialog
        at the test csv files
        """
        filename = master.filename = filedialog.askopenfile(
            initialdir='/home/adrikos/Desktop/My_projects/Simple_Data_Visualizer/csv_files',
            title='Select a file',
            filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

        return filename

    def load_data(self, filename):
        """
        Loads csv data into a pandas dataframe
        and returns the dataframe
        """
        print(filename)
        file_path = filename
        try:
            csv_filename = r"{}".format(file_path)
            if csv_filename[-4:] == ".csv":
                data_frame = pd.read_csv(csv_filename)
                return data_frame
            else:
                data_frame = None
        except ValueError:
            tk.messagebox.showerror("Information", "The file you have given is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No file found {file_path}")
            return None
        if data_frame == None:
            tk.messagebox.showerror("Information","No File Given")

    def load_buttons(self,frame):
        """
        Loads buttons on the File frame of the first window
        """
        # Open file button to get relative path of file
        open_file_button=tk.Button(frame, text='Open File',
        command=lambda:self.open_file_dialog(self))
        open_file_button.place(height=80,width=80,relx=0,rely=0)

        # Load file button to get access to data
        load_file_button = tk.Button(frame,text='Load File',
        command=lambda:self.load_data(open_file_button))
        load_file_button.place(height=80,width=80,relx=0.11,rely=0)


def plot_graphs(self, master):
    """
    Plots grpahs in a new window
    """
    pass


"""
TODO:✅ MAKE OPEN FILE BUTTON,LOAD CSV BUTTON,SIMPLE BAR PLOT BUTTON ON THE FILE FRAME
TODO: GIVE BUTTONS FUNCTIONALITY
TODO: MAKE A SEARCH BAR FOR THE DATA FRAME
TODO: GIVE ABILITY TO CHOOSE X,Y(2 COLUMNS) FOR THE GRPAHS
TODO: MAKE A TREEVIEW ON THE DATA FRAME
"""

if __name__ == "__main__":
    root = Aplication()
    root.mainloop()
