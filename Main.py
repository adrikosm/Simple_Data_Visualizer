from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib as plt
import tkinter as tk




class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Viewer")

        # Data frame for csv
        self.data_frame = tk.LabelFrame(self,text="Data")
        self.data_frame.place(height=600,width=900,relwidth=0.53,relheight=0.6)
        # Frame for buttons
        self.file_frame = tk.LabelFrame(self,text='Buttons')
        self.file_frame.place(height=300,width=900,rely=0.6,relx=0,relwidth=0.53,relheight=0.4)
        self.geometry("900x800")


    def open_file_dialog(self,master):
        """
        Opens the file dialog
        at the test csv files
        """
        filename = master.filename = filedialog.askopenfile(
                    initialdir='/home/adrikos/Desktop/My_projects/Simple_Data_Visualizer/csv_files',
                    title = 'Select a file',
                    filetypes = (("csv files", "*.csv"),("all files", "*.*")))

        return filename

    
    def load_data(self,master,filename):
        """
        Loads csv data into a pandas dataframe
        and returns the dataframe
        """
        file_path = filename
        try:
            csv_filename = r"{}".format(file_path)
            if csv_filename[-4:] == ".csv":
                data_frame = pd.read_csv(csv_filename)
                return data_frame
            else:
                data_frame = None
        except ValueError:
            master.messagebox.showerror("Information","The file you have given is invalid")
            return None
        except FileNotFoundError:
            master.messagebox.showerror("Information",f"No file found {file_path}")
            return None




if __name__ == "__main__":
    root = Aplication()
    root.mainloop()