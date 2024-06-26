from textwrap import wrap
import customtkinter as ctk 



class RSL(ctk.CTkFrame):
    def __init__(self, master, indexes, xl_read, rsl_num=None,  *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.rsl_num = rsl_num
        self.indexes = indexes
        self.xl_read = xl_read.read_into_dataframe()
        self.curr_idx = 0
        self.idx = indexes[self.curr_idx]
        self.row = self.xl_read.loc[self.idx]

        self.info = ctk.CTkFrame(self)
        self.info.grid(row=0, column=0, columnspan=6, rowspan=2, sticky='nsew', padx=10, pady=10)

        self.rsl_prc_frame = ctk.CTkFrame(self)
        self.rsl_prc_frame.grid(row=2, column=0, columnspan=6, rowspan=2, sticky='nsew', padx=10, pady=10)

        self.rsl_prc_frame.columnconfigure(0, weight=1)

        num = len(xl_read.get_row_indexes_needing_printing(self.rsl_num))
        self.data = {}

        self.start(num + 1)

    def clear_display(self):
        for widget in self.info.winfo_children():
            widget.grid_forget()
        self.info.grid(row=0, column=0, columnspan=6, rowspan=2, sticky='nsew', padx=10, pady=10)

    def curr_info(self):
        self.row = self.xl_read.loc[self.idx]    
        self.artist = self.row['Artist']
        self.data['Artist'] = self.artist
        self.title = self.row['Title']
        self.data['Title'] = self.title
        self.loc = self.row['Loc'] 
        self.data['Loc'] = self.loc
        self.conf = self.row['Conf.']
        self.data['Conf.'] = self.conf
        self.label = self.row['Label']
        self.data['Label'] = self.label
        self.label_num = self.row['Label #']
        self.data['Label #'] = self.label_num
        self.year = self.row['Notes']
        self.data['Notes'] = self.year
        self.condition = self.row['Con']
        self.data['Notes'] = self.condition
        self.display_info()

    
    def display_info(self):

        self.clear_display()
        artist_label = ctk.CTkLabel(self.info, text="Artist: " +  self.artist, font=("Courier New Greek", 22), anchor="center")
        artist_label.grid(row=0, column=0, pady=15, padx=30, sticky='nsew')

        title_label = ctk.CTkLabel(self.info, text="Ttile: " + self.title, font=("Courier New Greek", 22),anchor="center")
        title_label.grid(row=1, column=0, pady=15, padx=30, sticky='nsew')

        loc_label = ctk.CTkLabel(self.info, text="Genre: " + self.loc, font=("Courier New Greek", 22), anchor="center")
        loc_label.grid(row=0, column=1, pady=15, padx=30, sticky='nsew')

        conf_label = ctk.CTkLabel(self.info, text="Type: " + self.conf, font=("Courier New Greek", 22), anchor="center")
        conf_label.grid(row=1, column=1, pady=15, padx=30, sticky='nsew')

        label_label = ctk.CTkLabel(self.info, text="Label: " + self.label, font=("Courier New Greek", 22), anchor="center")
        label_label.grid(row=0, column=2, pady=15, padx=30, sticky='nsew')

        label_num_label = ctk.CTkLabel(self.info, text="Label #: " + self.label_num, font=("Courier New Greek", 22), anchor="center")
        label_num_label.grid(row=1, column=2, pady=15, padx=30, sticky='nsew')

        condition_label = ctk.CTkLabel(self.info, text="Condition: " + self.condition, font=("Courier New Greek", 22), anchor="center", wraplength=750)
        condition_label.grid(row=2, column=1, pady=15, padx=30, sticky='nsew')

        year_label = ctk.CTkLabel(self.info, text=self.year, font=("Courier New Greek", 22), anchor="center", wraplength=750)
        year_label.grid(row=0, column=3, columnspan=2, rowspan=3, pady=15, padx=30, sticky='nsew')

        edit = ctk.CTkButton(self.info, text="Edit", font=("Courier New Greek", 18), command=lambda: self.edit())
        edit.grid(row=4, column=2, pady=15, padx=30, sticky='nsew')
    
    def edit(self):
        self.clear_display()
        self.artist_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.artist_entry.insert(0, self.artist)
        self.artist_entry.grid(row=0, column=0, pady=7, padx=25)
        
        self.title_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.title_entry.insert(0, self.title)
        self.title_entry.grid(row=1, column=0, pady=7, padx=25)
        
        loc_list = ["PRL", "RBL", "MTL", "FKL", "API",   "SGCL", "SNTL", "JZL", "VNL", "BLL", "CLL", "CML", "CSL", "CWL", "DDL", "HOL", "HHL", "HSL", "HWL", "INL", "MTL", "NAL", "RGL", "RPL", "SPL", "SLA", "STCL", "STL", "SYL", "SWL", "WOL", "ZZL"]
        self._loc = ctk.StringVar(value=self.loc)
        self.loc_option = ctk.CTkComboBox(self.info, variable=self._loc, font=("Courier New Greek", 22), state="readonly", values=loc_list, hover=True, dropdown_font=("Courier New Greek", 15))
        self.loc_option.grid(row=0, column=1, pady=7, padx=25)

        self.conf_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 18), width=200)
        self.conf_entry.insert(0, self.conf)
        self.conf_entry.grid(row=1, column=1, pady=20, padx=25)
        
        self.label_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.label_entry.insert(0, self.label)
        self.label_entry.grid(row=0, column=2, pady=7, padx=25)
        
        self.label_num_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.label_num_entry.insert(0, self.label_num)
        self.label_num_entry.grid(row=1, column=2, pady=7, padx=25)
        
        conditions_list = [
            "New", "Very Good", "Good", "Fairly Good", "Fair"
        ]
        self.condition_selection = ctk.StringVar()
        self.condition_option = ctk.CTkComboBox(self.info, variable=self.condition_selection, font=("Courier New Greek", 22), state="readonly", values=conditions_list, hover=True, dropdown_font=("Courier New Greek", 15))
        self. condition_option.set(self.condition)
        self.condition_option.grid(row=2, column=1, pady=7, padx=25, sticky="ew")

        self.descritption_entry = ctk.CTkTextbox(self.info, font=("Courier New Greek", 20), width=450, wrap="word")
        self.descritption_entry.grid(row=0, column=3, columnspan=2, rowspan=3, pady=15, padx=30)
        self.descritption_entry.insert("0.0", self.year)
        
        save_btn = ctk.CTkButton(self.info, text="Save", command=self.save_edited_info, font=("Courier New Greek", 22))
        save_btn.grid(row=4, column=2, pady=7, padx=25)

    def save_edited_info(self):
        self.artist = self.artist_entry.get()
        self.title = self.title_entry.get()
        self.loc = self._loc.get()
        self.conf = self.conf_entry.get()
        self.label = self.label_entry.get()
        self.label_num = self.label_num_entry.get()
        self.year = self.descritption_entry.get("1.0", ctk.END)
        self.condition = self.condition_option.get()
        self.new_info = {"Artist": self.artist, "Title": self.title, "Loc": self.loc, "Conf.": self.conf, "Label": self.label, "Label #": self.label_num, "Notes": self.year, "Con": self.condition}
        self.master.update_row(self.idx + 2, self.new_info)
        self.data.update(self.new_info)
        self.row = self.xl_read.iloc[self.idx]
        self.display_info()

    def clear_display(self):
        for widget in self.info.winfo_children():
            widget.grid_forget()
        self.info.grid(row=0, column=0, columnspan=8, rowspan=2, sticky='nsew', padx=10, pady=7)

    def start(self, start_num = 1):
        self.start_num = start_num
        self.curr_info()
        self.rsl_price = {"Assignment": self.rsl_num + "{:03d}".format(self.start_num), "Retail": None}
        self.idx = self.indexes[self.curr_idx]

        rsl_label = ctk.CTkLabel(self.rsl_prc_frame, text=self.rsl_price["Assignment"], font=("Courier New Greek", 22), anchor="center")
        rsl_label.grid(row=0, column=0, columnspan=2, pady=15, padx=30, sticky='nsew')

        price_label = ctk.CTkLabel(self.rsl_prc_frame, text="Price: ", font=("Courier New Greek", 22))
        price_label.grid(row=0, column=2, pady=5, padx=30, sticky='e')
        self.price_entry = ctk.CTkEntry(self.rsl_prc_frame, font=("Courier New Greek", 22))
        self.price_entry.grid(row=0, column=3, pady=15, padx=30, sticky='nsew')
        self.price_entry.focus_set()

        save_btn = ctk.CTkButton(self.rsl_prc_frame, text="Save", command=self.save, font=("Courier New Greek", 22))
        save_btn.grid(row=0, column=4, pady=15, padx=(30,10),  sticky='nsew')
        self.master.bind('<Return>', lambda event: self.save())

    def save(self):
        price = float(self.price_entry.get())
        price_str = "{:.2f}".format(price)
        self.rsl_price["Retail"] = price_str

        self.master.update_row(self.idx, self.rsl_price)
        self.clear_fields()
        self.curr_idx += 1

        if self.curr_idx < len(self.indexes):
            self.idx = self.indexes[self.curr_idx]
            self.row = self.xl_read.iloc[self.idx]
            self.start(self.start_num + 1)
        else:
            self.master.current_crate_num = self.rsl_num
            self.master.section6_start(self.rsl_num)

    def clear_fields(self):
        for widget in self.rsl_prc_frame.winfo_children():
            widget.grid_forget()





