from tkinter import filedialog, ttk,font
from tkinter import messagebox as mb
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
        self.data_tree_view = ttk.Treeview(self.data_frame)

        # Frame for buttons
        self.file_frame = tk.LabelFrame(self, text='Buttons')
        self.load_buttons(self.file_frame)
        self.file_frame.place(height=300, width=900, rely=0.6, relx=0, relwidth=0.53, relheight=0.3)
       
        self.label_file = ttk.Label(self.data_frame,text="No File Selected")
        self.label_file.place(rely=0,relx=0)
        self.geometry("900x800")
        


    def open_file_dialog(self, master):
        """
        Opens the file dialog
        at the test csv files
        """
        file_name = master.filename = filedialog.askopenfile(
            initialdir='/home/adrikos/Desktop/My_projects/Simple_Data_Visualizer/csv_files',
            title='Select a file',
            filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

        self.label_file['text'] = file_name.name
        return None


    def clear_treeview_data(self):
        """
        Clears the treeview data in the first frame
        """
        self.label_file.config(text="")
        self.data_tree_view.delete(*self.data_tree_view.get_children())
        return None


    def tree_view(self):
        """
        Loads a treeview in  the fist frame
        """

        self.clear_treeview_data() 
        
        treescrollx = ttk.Scrollbar(self.data_frame,
                                   orient='horizontal',
                                   command=self.data_tree_view.xview)

        self.data_tree_view.configure(xscrollcommand=treescrollx.set) 

        treescrollx.pack(side="bottom",fill="x",expand=True)

        self.data_tree_view.place(relheight=1,relwidth=1)

        return None

        


    def load_data(self, filename):
        """
        Loads csv data into a pandas dataframe
        and returns the dataframe
        """

        print(self.label_file['text'])

        file_path = self.label_file['text']

        try:
            csv_filename = r"{}".format(file_path)
            if csv_filename[-4:] == ".csv":
                data_frame = pd.read_csv(csv_filename)
            else:
                data_frame = None
        except ValueError:
            mb.showerror("ERROR", "The file you have given is invalid")
            return None
        except FileNotFoundError:
            mb.showerror("ERROR", f"No file found {file_path}")
            return None
        if data_frame is None:
            mb.showerror("ERROR","No file given")

        self.tree_view()

        self.data_tree_view['column'] = list(data_frame)
        self.data_tree_view['show'] = "headings"

        # Adds the columns and rows in the tree view
        for column in self.data_tree_view['columns']:
            self.data_tree_view.heading(column,text=column)
        
        data_frame_rows = data_frame.to_numpy().tolist()
        for rows in data_frame_rows:
            self.data_tree_view.insert("","end",values=rows)


    def load_buttons(self,frame):
        """
        Loads buttons on the File frame of the first window
        """
        file_path = None

        # Open file button to get relative path of file
        open_file_button=tk.Button(frame, text='Open File',
        command=lambda:self.open_file_dialog(self))
        open_file_button.place(height=60,width=60,relx=0,rely=0)

        # Load file button to get access to data
        load_file_button = tk.Button(frame,text='Load File',
        command=lambda:self.load_data(file_path))
        load_file_button.place(height=60,width=60,relx=0.1,rely=0)



def plot_graphs(self, master):
    """
    Plots grpahs in a new window
    """
    pass


"""
TODO:🛠️ MAKE OPEN FILE BUTTON,LOAD CSV BUTTON,SIMPLE BAR PLOT BUTTON ON THE FILE FRAME
TODO:🛠️ GIVE BUTTONS FUNCTIONALITY
TODO:🛠️ MAKE A SEARCH BAR FOR THE DATA FRAME
TODO:🛠️GIVE ABILITY TO CHOOSE X,Y(2 COLUMNS) FOR THE GRPAHS
TODO:🛠️ FIX SCROLLBAR ISSUE WHEN LOADING ANOTHER DATASET
TODO:🛠️ ADD AN EXCEL AND XLSX SUPPORT
"""

if __name__ == "__main__":
    root = Aplication()
    root.mainloop()
