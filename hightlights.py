import customtkinter as ctk 

class Frame2(ctk.CTkFrame):
    def __init__(self, master, indexes, xl_read, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.indexes = indexes
        self.curr_idx = 0
        self.idx = indexes[self.curr_idx]
        self.addit_info = {}
        self.info = ctk.CTkFrame(self)
        self.xl_read = xl_read.read_into_dataframe()
        self.row = self.xl_read.loc[self.idx]        
        self.hl = ctk.CTkFrame(self)
        self.hl.grid(row=2, column=0, columnspan = 8, sticky='nsew', padx=10, pady=10)
        self.highlight_entry_frame = ctk.CTkFrame(self)
        self.highlight_entry_frame.grid(row=6, column=0, columnspan=8, sticky='nsew', padx=10, pady=10)
        self.highlight_entry_frame.columnconfigure(0, minsize=1, pad=0)
        self.highlight_entry_frame.columnconfigure(4, minsize=1, pad=0)
        self.highlight_entry_frame.columnconfigure(8, minsize=1, pad=0)
        self.highlight_entry_frame.columnconfigure(12, minsize=1, pad=0)
        self.data = {}
        self.start()

    def clear_display(self):
        for widget in self.info.winfo_children():
            widget.grid_forget()
        self.info.grid(row=0, column=0, columnspan=8, rowspan=2, sticky='nsew', padx=10, pady=7)

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
        self.year = self.row['Notes'][:4]
        self.data['Notes'] = self.year
        self.display_info()
    
    def display_info(self):
        self.clear_display()
        artist_label = ctk.CTkLabel(self.info, text="Artist: " +  self.artist, font=("Courier New Greek", 22), anchor="center", width=250)
        artist_label.grid(row=0, column=0, pady=7, padx=25, sticky='nsew')
        title_label = ctk.CTkLabel(self.info, text="Ttile: " + self.title, font=("Courier New Greek", 22),anchor="center", width=250)
        title_label.grid(row=1, column=0, pady=7, padx=25, sticky='nsew')
        loc_label = ctk.CTkLabel(self.info, text="Genre: " + self.loc, font=("Courier New Greek", 22), anchor="center", width=250)
        loc_label.grid(row=0, column=1, pady=7, padx=25, sticky='nsew')
        conf_label = ctk.CTkLabel(self.info, text="Type: " + self.conf, font=("Courier New Greek", 22), anchor="center", width=250)
        conf_label.grid(row=1, column=1, pady=7, padx=25, sticky='nsew')
        label_label = ctk.CTkLabel(self.info, text="Label: " + self.label, font=("Courier New Greek", 22), anchor="center", width=250)
        label_label.grid(row=0, column=2, pady=7, padx=25, sticky='nsew')
        label_num_label = ctk.CTkLabel(self.info, text="Label #: " + self.label_num, font=("Courier New Greek", 22), anchor="center", width=250)
        label_num_label.grid(row=1, column=2, pady=7, padx=25, sticky='nsew')
        year_label = ctk.CTkLabel(self.info, text=self.year, font=("Courier New Greek", 22), width=250, anchor="center")
        year_label.grid(row=2, column=0, columnspan=2, pady=7, padx=25, sticky='nsew')

        edit = ctk.CTkButton(self.info, text="Edit", command=self.edit, font=("Courier New Greek", 22), width=20)
        edit.grid(row=2, column=2, pady=7, padx=25, sticky='nsew')
    
    def edit(self):
        self.clear_display()
        self.artist_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.artist_entry.insert(0, self.artist)
        self.artist_entry.grid(row=0, column=0, pady=7, padx=25, sticky='nsew')
        
        self.title_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.title_entry.insert(0, self.title)
        self.title_entry.grid(row=1, column=0, pady=7, padx=25, sticky='nsew')
        
        loc_list = ["PRL", "RBL", "MTL", "FKL", "API",   "SGCL", "SNTL", "JZL", "VNL", "BLL", "CLL", "CML", "CSL", "CWL", "DDL", "HOL", "HHL", "HSL", "HWL", "INL", "MTL", "NAL", "RGL", "RPL", "SPL", "SLA", "STCL", "STL", "SYL", "SWL", "WOL", "ZZL"]
        self._loc = ctk.StringVar(value=self.loc)
        self.loc_option = ctk.CTkComboBox(self.info, variable=self._loc, font=("Courier New Greek", 22), state="readonly", values=loc_list, hover=True, dropdown_font=("Courier New Greek", 15))
        self.loc_option.grid(row=0, column=1, pady=7, padx=25, sticky='nsew')

        self.conf_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 18), width=200)
        self.conf_entry.insert(0, self.conf)
        self.conf_entry.grid(row=1, column=1, pady=20, padx=25, sticky='nsew')
        
        self.label_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.label_entry.insert(0, self.label)
        self.label_entry.grid(row=0, column=2, pady=7, padx=25, sticky='nsew')
        
        self.label_num_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=250)
        self.label_num_entry.insert(0, self.label_num)
        self.label_num_entry.grid(row=1, column=2, pady=7, padx=25, sticky='nsew')
        
        self.year_entry = ctk.CTkEntry(self.info, font=("Courier New Greek", 22), width=500)
        self.year_entry.insert(0, self.year)
        self.year_entry.grid(row=2, column=0, columnspan=2, pady=7, padx=30, sticky='nsew')
        
        save_btn = ctk.CTkButton(self.info, text="Save", command=self.save_edited_info, font=("Courier New Greek", 22))
        save_btn.grid(row=2, column=2, pady=7, padx=25, sticky='nsew')

    def save_edited_info(self):
        self.artist = self.artist_entry.get()
        self.title = self.title_entry.get()
        self.loc = self._loc.get()
        self.conf = self.conf_entry.get()
        self.label = self.label_entry.get()
        self.label_num = self.label_num_entry.get()
        self.year = self.year_entry.get().upper() + " - "
        self.new_info = {"Artist": self.artist, "Title": self.title, "Loc": self.loc, "Conf.": self.conf, "Label": self.label, "Label #": self.label_num, "Notes": self.year}
        self.master.update_row(self.idx + 2, self.new_info)
        self.data.update(self.new_info)
        self.row = self.xl_read.iloc[self.idx]
        self.display_info()
    
    def start(self):
        self.addit_info = {}
        self.selected_highlights = []

        ctk.CTkLabel(self, text="Choose 2 - 3 / Limit 5", font=("Lucida Sans", 25)).grid(row=3, column=0, columnspan = 8, sticky="nsew")
        '''ctk.CTkLabel(self, text="Limit 5", font=("Lucida Sans", 20)).grid(row=4, column=2, columnspan = 3, sticky="sw")'''

        '''self.master.clear()
        self.master.display_sidebar()'''
        self.curr_info()
        def years():
            self.year2_text.grid(row=0, column=3, pady=20, padx=2)
            self.year2.grid(row=0, column=4, columnspan=3, pady=20, padx=2)

        self.year_label_2 = ctk.CTkLabel(self.hl, text="Original Year: " + str(self.year), font=("Courier New Greek", 22), anchor="center", width=200)
        self.year_label_2.grid(row=0, column=0, pady=10, padx=15, sticky='nsew') 
            
        reissue_text = ctk.CTkLabel(self.hl,
                                    text="Reissue", font=("Courier New Greek", 22))
        reissue_text.grid(row=0, column=1, padx=(20,0), pady=20)
        self.reissue_var = ctk.BooleanVar(self.hl)
        self.reissue_checkb = ctk.CTkCheckBox(self.hl, variable=self.reissue_var, text="", onvalue=True, offvalue=False)
        self.reissue_checkb.grid(row=0, column=2, sticky="ew", padx=10, pady=20)

        def toggle_reissue_addition():
            if self.reissue_var.get():
                years()
            else:
                self.year2.grid_forget()
                self.year2_text.grid_forget()

        self.reissue_checkb.bind("<Button-1>", lambda _: toggle_reissue_addition())

        self.year2_text = ctk.CTkLabel(self.hl, text="Year:", font=("Courier New Greek", 22))
        self.year2 = ctk.CTkEntry(self.hl, width=100, height=5, font=("Courier New Greek", 18))

        self.unique_var = ctk.StringVar()

        self.unique_fill_in_opt = ctk.CTkCheckBox(self.highlight_entry_frame, text="", onvalue="unique", offvalue="None", width=10)
        unique_fill_in_opt_text = ctk.CTkEntry(self.highlight_entry_frame, textvariable=self.unique_var, placeholder_text="Write Your Own", placeholder_text_color=["#000000", "#FFFFFF"], font=("Courier New Greek", 18), width=750)

        self.unique_fill_in_opt.grid(row=15, column=0, pady=5, padx=(5,0), sticky="")
        unique_fill_in_opt_text.grid(row=15, column=1, columnspan=16, pady=5, padx=(0,10), sticky="w")

        self.first_set = {
            "New / Factory Sealed": ctk.StringVar(),
            "180g": ctk.StringVar(),
            "Colored Wax": ctk.StringVar(),
            "(Insert edit) Colored Wax": ctk.StringVar(),
            "2xLP": ctk.StringVar(),
            "3xLP": ctk.StringVar(),
            "4xLP": ctk.StringVar(),
            "5xLP": ctk.StringVar(),
            "Box Set": ctk.StringVar(),
            "7\" 45 RPM": ctk.StringVar(),
            "10\"": ctk.StringVar(),
            "12\" Single": ctk.StringVar(),
            "EP": ctk.StringVar(),
            "Picture Disc": ctk.StringVar()
        }
        self.second_set = {
            "(Insert edit) Exclusive": ctk.StringVar(),
            "Limited Edition": ctk.StringVar(),
            "LTD ED": ctk.StringVar(),
            "Original Issue": ctk.StringVar(),
            "1st Issue": ctk.StringVar(),
            "Rare": ctk.StringVar(),
            "Rare-1st Issue": ctk.StringVar(),
            "Out of Print": ctk.StringVar(),
            "Remastered": ctk.StringVar(),
            "Numbered": ctk.StringVar(),
            "Monaural": ctk.StringVar(),
            "Quadrasonic": ctk.StringVar(),
            "Import": ctk.StringVar(),
            "(Insert edit) Import": ctk.StringVar()
        }
        
        self.third_set = {
            "Includes Inserts": ctk.StringVar(),
            "Includes Poster": ctk.StringVar(),
            "Includes All inserts": ctk.StringVar(),
            "Includes (Insert edit)": ctk.StringVar(),
            "Audiophile": ctk.StringVar(),
            "Laser Etched": ctk.StringVar(),
            "Unauthorized": ctk.StringVar(),
            "Bootleg": ctk.StringVar(),
            "White Label Promo": ctk.StringVar(),
            "Promo": ctk.StringVar(),
            "Promotional": ctk.StringVar()
        }
        self.fourth_set = {
            "Original Gatefold Jacket": ctk.StringVar(),
            "Uni-Pack Jacket": ctk.StringVar(),
            "Tri Fold Jacket": ctk.StringVar(),
            "Textured Jacket": ctk.StringVar(),
            "Die-Cut Jacket": ctk.StringVar(),
            "Embossed Jacket": ctk.StringVar(),
            "Laminated Jacket": ctk.StringVar(),
            "Original Factory Shrink-wrap": ctk.StringVar(),
            "Autographed": ctk.StringVar()
        }

        i = 0

        self.labels = {}
        
        # place the checkboxes in the frame for the first set
        for item, var in self.first_set.items():
            if "(Insert edit)" in item:
                insert_edit_checkb = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                insert_edit_checkb.grid(row=i, column=0, pady=3, padx=(5,0), sticky="")
                insert_edit_checkb.bind("<Button-1>", lambda event, var=var, item=item: self.open_insert_edit_window(event, var, item))
            else:
                first = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                first.grid(row=i, column=0, pady=3, padx=(5,0), sticky="")
            
            
            label = ctk.CTkLabel(self.highlight_entry_frame, text = item,  font=("Arial", 18), compound="left", width = 200, anchor="w")
            self.labels[item] = label
            label.grid(row=i, column=1, columnspan=3, pady=3, padx=(0,10), sticky="w")  
            i += 1

        i = 0
        for item, var in self.second_set.items():
            #print(item)
            if "(Insert edit)" in item:
                insert_edit_checkb = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                insert_edit_checkb.grid(row=i, column=4, pady=3, padx=(5,0), sticky="")
                insert_edit_checkb.bind("<Button-1>", lambda event, var=var, item=item: self.open_insert_edit_window(event, var, item))
            else:
                second = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                second.grid(row=i, column=4, pady=3, padx=(5,0), sticky="") 
            label = ctk.CTkLabel(self.highlight_entry_frame, text = item,  font=("Arial", 18), compound="left", width = 200, anchor="w")
            self.labels[item] = label
            label.grid(row=i, column=5, columnspan=2, pady=3, padx=(0,10), sticky="w")  
            i += 1

        i = 0
        for item, var in self.third_set.items():
            #print(item)
            if "(Insert edit)" in item:
                insert_edit_checkb = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                insert_edit_checkb.grid(row=i, column=8, pady=3, padx=(5,0), sticky="")
                insert_edit_checkb.bind("<Button-1>", lambda event, var=var, item=item: self.open_insert_edit_window(event, var, item))
            else:
                third = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                third.grid(row=i, column=8, pady=3, padx=(5,0), sticky="")   
            
            label = ctk.CTkLabel(self.highlight_entry_frame, text = item,  font=("Arial", 18), compound="left", width = 200, anchor="w")
            self.labels[item] = label
            label.grid(row=i, column=9, columnspan=3, pady=3, padx=(0,10), sticky="w")  
            i += 1

        i = 0
        for item, var in self.fourth_set.items():
            #print(item)
            if "(Insert edit)" in item:
                insert_edit_checkb = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                insert_edit_checkb.grid(row=i, column=12, pady=3, padx=(5,0), sticky="")
                insert_edit_checkb.bind("<Button-1>", lambda event, var=var, item=item: self.open_insert_edit_window(event, var, item))
            else:
                fourth = ctk.CTkCheckBox(self.highlight_entry_frame, text="", variable=var, onvalue=item, offvalue="None", width=10)
                fourth.grid(row=i, column=12, pady=3, padx=(5,0), sticky="")
            label = ctk.CTkLabel(self.highlight_entry_frame, text = item,  font=("Arial", 18), compound="left", width = 200, anchor="w")
            self.labels[item] = label
            label.grid(row=i, column=13, columnspan=3, pady=3, padx=(0,10), sticky="w")  
            i += 1
        
        save_button = ctk.CTkButton(self, text="save", command=self.save, font=("Courier New Greek", 22))
        save_button.grid(row=15, column=7, columnspan=1, pady=20, padx=20, sticky="e")

    def open_insert_edit_window(self, event, var, item):
        if var.get() == "None":
            self.labels[item].configure(text=item)
            return
        self.top = ctk.CTkToplevel(self)
        self.top.title("Insert Edit")
        self.top.attributes("-topmost", True)  # Set the toplevel window to stay in front
        self.top.grab_set()
        self.top.resizable(False, False)

        self.entry_var = ctk.StringVar()

        self.entry = ctk.CTkEntry(self.top, font=("Courier New Greek", 22), width=200, textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, pady=10, padx=15, sticky='nsew')
        self.entry.focus_set()


        save_btn = ctk.CTkButton(self.top, text="Save", command=lambda var=var, item=item: self.save_insert_edit(var, item), font=("Courier New Greek", 22))
        save_btn.grid(row=1, column=0, pady=10, padx=15, sticky='nsew')

        self.top.bind("<Return>", lambda event: save_btn.invoke())  # Bind the Return key to the save button

    def save_insert_edit(self, var, item):
        value = self.entry_var.get()
        #print(value)
        var.set(item.replace("(Insert edit)", value))
        #self.selected_highlights.append(item.replace("(Insert edit)", value))
        #print(item.replace("(Insert edit)", value))
        for widget in self.highlight_entry_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                if widget.cget("text") == item:
                    widget.configure(text=item.replace("(Insert edit)", value))
        for widget in self.top.winfo_children():
            widget.destroy()
        self.top.destroy()
        

    def save(self):
        if self.reissue_var.get():
            self.addit_info['Notes'] = f"{str(self.row['Notes'])} / {str(self.year2.get())} REISSUE - "
        else:
            if 'Notes' not in self.addit_info:
                self.addit_info['Notes'] = str(self.row['Notes']) + " - "

        if self.unique_fill_in_opt.get() != "None":
            self.selected_highlights.append(self.unique_var.get())

        for set in [self.first_set, self.second_set, self.third_set, self.fourth_set]:
            for item, var in set.items():
                value = var.get()
                if value != "None" and value != "":
                    if value.endswith ("xLP"):
                        self.selected_highlights.append(value)
                    else:
                        self.selected_highlights.append(value.upper())

        #print("Highlights: " + str(self.selected_highlights))

        for highlight in self.selected_highlights:
            self.addit_info['Notes'] += highlight + " "
        self.addit_info['Qty'] = "Intro"
        # Update the corresponding row in the DataFrame (self.xl_read)
        self.master.update_row(self.idx, self.addit_info)

        self.curr_idx +=  1
        self.reset_fields()

        if self.curr_idx < len(self.indexes):
            self.idx = self.indexes[self.curr_idx]
            self.row = self.xl_read.iloc[self.idx]
            self.curr_info()
            self.year2_text.grid_remove()
            self.year2.grid_remove()  # Hide the year entry widget
            self.start()
        else:
            self.master.start()

    def empty_fields(self):
        if self.reissue_var.get() and not self.year2.get():
            self.year2.configure(bg_color="red")
        else:
            self.year2.configure(bg_color=self.border_color)
        if not self.highlight_entry.get():
            self.highlight_entry.configure(bg_color="red")
        else:
            self.highlight_entry.configure(bg_color=self.border_color)
    

    def get_addit_data(self):
        return self.addit_info
    
    def reset_fields(self):
        #print("Cleared entries")
        # clear all checkboxes
        for set in [self.first_set, self.second_set, self.third_set, self.fourth_set]:
            for item, var in set.items():
                var.set("None")

        self.year2.delete(0, ctk.END)
        self.reissue_checkb.deselect()
