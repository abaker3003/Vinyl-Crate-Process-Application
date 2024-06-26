from tkinter import UNDERLINE
import customtkinter as ctk

class DescriptionInputFrame(ctk.CTkFrame):

    def __init__(self, master, next_idx = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.desc_data = {}
        self._page = 1
        self.next_idx = next_idx

        self.curr_qty_val = "_"

        self.artist_title = ctk.CTkFrame(self)
        self.artist_title.grid(row=0,
                            column=0,
                            columnspan=6,
                            rowspan=3,
                            sticky='nsew',
                            pady=20, padx=20)

        # ---> ARTIST INPUT <--- #
        artist_label = ctk.CTkLabel(self.artist_title, text="Artist", font=("Courier New Greek", 22, "bold"))
        #artist_label.grid(row=1, column=2, padx=5, pady=10)
        artist_label.grid(row=0, column=0, padx=5)

        self.artist_text = ctk.CTkEntry(self.artist_title, height=1, width=300, font=("Arial Greek", 18))
        self.artist_text.grid(row=0, column=1, padx=10, pady=20, columnspan=3)
        self.artist_text.focus_set()

        for i in range(3):
            self.artist_title.rowconfigure(i, weight=1)
        for i in range(6):
            self.artist_title.columnconfigure(i, weight=0)

        self.border_color = self.artist_text.cget("bg_color")


        # ---> TITLE INPUT <--- #
        title_label = ctk.CTkLabel(self.artist_title, text="Title", font=("Courier New Greek", 22, "bold"))
        #title_label.grid(row=2, column=2, padx=5, pady=10)
        title_label.grid(row=1, column=0, padx=5)

        self.title_text = ctk.CTkEntry(self.artist_title, height=1, width=300, font=("Arial Greek", 18))
        self.title_text.grid(row=1, column=1, padx=10, pady=20, columnspan=3)

        label_text = ctk.CTkLabel(self.artist_title, text="Label", font=("Courier New Greek", 22, "bold"))
        self.label = ctk.CTkEntry(self.artist_title, width=130, height=5, font=("Arial Greek", 18))
        label_text.grid(row=0, column=6, padx=20, pady=20)
        self.label.grid(row=0, column=7, columnspan=2, pady=20)

        label_number_text = ctk.CTkLabel(self.artist_title, text="Label #", font=("Courier New Greek", 22, "bold"))
        self.label_number = ctk.CTkEntry(self.artist_title, width=130, height=5, font=("Arial Greek", 18))
        label_number_text.grid(row=1, column=6, padx=20, pady=20)
        self.label_number.grid(row=1, column=7, columnspan=2, pady=20)

        # ---> TYPE RADIO BUTTONS <--- #

        self.type_frame = ctk.CTkFrame(self)
        self.type_frame.grid(row=3,
                            column=0,
                            columnspan=4,
                            rowspan=4,
                            sticky='nsew',
                            pady=20, padx=20)
        self.type_label = ctk.CTkLabel(self.type_frame, text="Type", font=("Courier New Greek", 22, "bold"))
        self.type_label.grid(row=0, column=2, padx=20, pady = 20, sticky='nsew')
        
        clear_btn = ctk.CTkButton(self.type_frame, text="clear", font=("Courier New Greek", 15), height=5, width=50, command=lambda: self.unselect_radiobutton())
        clear_btn.grid(row=0, column=3, padx=15, pady=20, sticky="ne")

        types_list = [
            "LP", "7\"- Single", "CD", "2xLP", "7\" EP", "DVD", "3xLP", "10\" LP", "BR", "4xLP", "10\" EP", "Book", "_xLP BOX", "12\" Single","BOX", "OTHER" 
        ]
        self.types = ctk.StringVar(self.type_frame, "Type")
        self.type_entry = ctk.CTkEntry(self.type_frame, width=100, height=5, font=("Arial Greek", 18))

        r, c = 1, 0
        self.border = None
        self.type_bts = []
        for i, type in enumerate(types_list):
            if i % 3 == 0:
                r += 1
                c = 0
            type_opt = ctk.CTkRadioButton(self.type_frame,
                                            text=type,
                                            variable=self.types,
                                            value=type, font=("Courier New Greek", 19), command=lambda: self.close_entry())
            self.type_bts.append(type_opt)
            self.border = type_opt.cget("text_color")
            type_opt.grid(row=r, column=c + 1, padx=15, pady=20)
            if type == "OTHER":
                type_opt.configure(command=lambda event=None, r=r, c=c+2: self.open_entry(event, r, c))
            elif type == "_xLP BOX":
                type_opt.configure(command=lambda: self.open_entry_qty())
            c += 1
            
        

        loc_frame = ctk.CTkFrame(self)
        loc_frame.grid(row=3, column=4, rowspan=2, columnspan=2, sticky='nsew', pady=20, padx=20)
        loc_text = ctk.CTkLabel(loc_frame, text="LOC", font=("Courier New Greek", 22, "bold"))
        loc_text.grid(row=0, column=0, columnspan=3, padx=20, pady=(30, 15), sticky='nsew')

        loc_list = ["PRL", "RBL", "MTL", "FKL", "API",   "SGCL", "SNTL", "JZL", "VNL", "BLL", "CLL", "CML", "CSL", "CWL", "DDL", "HOL", "HHL", "HSL", "HWL", "INL", 
                     "MTL", "NAL", "RGL", "RPL", "SPL", "SLA", "STCL", "STL",
                    "SYL", "SWL", "WOL", "ZZL"]
        self._loc = ctk.StringVar()
        self.loc_option = ctk.CTkComboBox(loc_frame, variable=self._loc, font=("Courier New Greek", 22),  state="readonly", values=loc_list, hover=True, dropdown_font=("Courier New Greek", 15))
        self.loc_option.grid(row=1, column=0, columnspan=3, padx=20, pady=(15,30), sticky='nsew')

        

        self.year_frame = ctk.CTkFrame(self)
        self.year_frame.grid(row=5, column=4, columnspan=2, rowspan=2, sticky='nsew', pady=20, padx=20)

        year_label = ctk.CTkLabel(self.year_frame, text="Original\nIssue Year", font=("Courier New Greek", 22, "bold"))
        year_label.grid(row=0, column=0, columnspan=3, padx=20, pady=(30, 15), sticky='nsew')

        self.year_entry = ctk.CTkEntry(self.year_frame, width=130, height=5, font=("Arial Greek", 18))
        self.year_entry.grid(row=1, column=0, columnspan=3, padx=20, pady=(15,30), sticky='nsew')


        save_button = ctk.CTkButton(self, text="Next Record\nIn Crate", command=self.save, font=("Courier New Greek", 22))
        save_button.grid(row=15, column=6, columnspan=1, pady=20, padx=10, sticky="ew")

        done_button = ctk.CTkButton(self, text="End Pre-Prep\nStart Grading", command=self.done, font=("Courier New Greek", 22))
        done_button.grid(row=15, column=4, columnspan=1, pady=20, padx=(30, 0), sticky="ew")
    
    def close_entry(self):
        self.type_entry.grid_remove()

    def open_entry(self, event, r, c):
        
        self.type_entry.grid(row=r, column=c, columnspan=2, padx=20, pady=(15,30), sticky='nsew')

    def open_entry_qty(self):

        self.close_entry()

        self.type_qty = Enter_QTY(self, self.curr_qty_val)

    
    def unselect_radiobutton(self):
        self.close_entry()
        self.types.set("None")
        self.curr_qty_val = "_"
        for widget in self.type_frame.winfo_children():
            if isinstance(widget, ctk.CTkRadioButton) and widget.cget("text").endswith("LP BOX"):
                widget.configure(text= str(self.curr_qty_val) + "xLP BOX")
            

    def set_qty(self, qty):
        self.curr_qty_val = str(qty)
        for widget in self.type_frame.winfo_children():
            if isinstance(widget, ctk.CTkRadioButton) and widget.cget("text").endswith("LP BOX"):
                widget.configure(text= str(self.curr_qty_val) + "xLP BOX")


    def save(self):
        if not self.check_fields_finishing(): 
            self.empty_fields()
            return
        self.desc_data["Assignment"] = "Crate " + str(self.master.current_crate_num)
        self.desc_data['Artist'] = self.artist_text.get()
        self.desc_data['Title'] = self.title_text.get()
        if self.types.get() == "OTHER":
            self.desc_data['Conf.'] = self.type_entry.get()
        else:
            self.desc_data['Conf.'] = self.types.get()
        self.desc_data["Label"] = self.label.get()
        self.desc_data["Label #"] = self.label_number.get()
        self.desc_data["Loc"] = self._loc.get()
        self.desc_data["Notes"] = str(self.year_entry.get())
        self.desc_data["Qty"] = "Grading"
        if self.next_idx is not None:
            self.master.save_data(self.desc_data, row = self.next_idx)
            self.next_idx += 1
        else:
            self.master.save_data(self.desc_data, current_section = 1)
        self.master.new_crate = False
        self.reset_fields()

    def done(self):
        filled, unfilled = self.count_filled_and_unfilled_entries()

        if self.master.new_crate and (not self.check_fields_finishing() or self.all_fields_empty()): 
            self.empty_fields()
            print("nEW cRATE: " + str(self.master.new_crate))
            return
        
        if unfilled == 0:
            self.save()
        elif filled == 0:
            self.master.start()
        else:
            self.empty_fields()
            print("SOME NOT FILLED OUT!")
            return

        self.master.new_crate = False
        self.master.start()

    def count_filled_and_unfilled_entries(self):
        filled = 0
        unfilled = 0
        if len(self.artist_text.get()) >= 1:
            filled += 1
        else:
            unfilled += 1
        if len(self.title_text.get()) >=1:
            filled += 1 
        else:
            unfilled += 1 
        if self.types.get() != "None":
            filled += 1 
        else: 
            unfilled += 1 
        if self.types.get() == "OTHER":
            if len(self.type_entry.get()) >= 1:
                filled += 1 
            else: 
                unfilled += 1 
        if len(self.label.get()) >= 1:
            filled += 1 
        else: 
            unfilled += 1 
        if len(self.label_number.get()) >= 1:
            filled += 1
        else:
            unfilled += 1
        if len(self._loc.get()) >= 1:
            filled += 1 
        else: 
            unfilled += 1 
        if len(self.year_entry.get()) >= 1:
            filled += 1
        else:
            unfilled += 1
        return filled, unfilled
    
    def empty_fields(self):
        
        if not self.artist_text.get():
            self.artist_text.configure(bg_color="red", border_width=2)
        else:
            self.artist_text.configure(bg_color=self.border_color)
        if not self.title_text.get():
            self.title_text.configure(bg_color="red", border_width=2)
        else:
            self.title_text.configure(bg_color=self.border_color)
        for widget in self.type_frame.winfo_children():
            if isinstance(widget, ctk.CTkRadioButton):
                
                if not self.types.get():
                
                    widget.configure(border_color="FF0000", border_width=3)    
                else:
                    widget.configure(border_color=self.border)
        if self.types.get() == "OTHER" and len(self.type_entry.get()) < 1:
            self.type_entry.configure(bg_color="red", border_width=2) 
        else:
            self.type_entry.configure(bg_color=self.border_color)
        if not self.label.get():
            self.label.configure(bg_color="red", border_width=2)
        else:
            self.label.configure(bg_color=self.border_color)
        if not self.label_number.get():
            self.label_number.configure(bg_color="red", border_width=2)
        else:
            self.label_number.configure(bg_color=self.border_color)
        if not self._loc.get():
            self.loc_option.configure(bg_color="red", border_width=2)
        else:
            self.loc_option.configure(bg_color=self.border_color)
        if not self.year_entry.get():
            self.year_entry.configure(bg_color="red", border_width=2)
        else:
            self.year_entry.configure(bg_color=self.border_color)

    def all_fields_empty(self):
        if not (len(self.artist_text.get()) >= 1 or len(self.title_text.get()) >= 1 or self.types.get() != "None" or len(self.label.get()) >= 1 or len(self.label_number.get()) >= 1 or len(self._loc.get()) >= 1 or len(self.year_entry.get()) >= 1): 
            return True
        return False
    
    def check_fields_finishing(self):
        self.empty_fields()
        if len(self.artist_text.get()) >= 1 and len(self.title_text.get()) >=1 and self.types.get() != "None" and len(self.label.get()) >= 1 and len(self.label_number.get()) >= 1 and len(self._loc.get()) >= 1 and len(self.year_entry.get()) >= 1:
            if self.types.get() == "OTHER" and len(self.type_entry.get()) <= 1:
                return False
            return True
        # check if all fields aren't filled out
        
        return False
    
    def check_empty_finishing(self):
        print("Artist: " + self.artist_text.get())
        print("Title: " + self.title_text.get())
        print("Type: " + self.types.get())
        print("Label: " + self.label.get())
        print("Label #: " + self.label_number.get())
        print("LOC: " + self._loc.get())
        print("Year: " + self.year_entry.get())
        
        self.empty_fields()
        if len(self.artist_text.get()) >= 1 and len(self.title_text.get()) >=1 and self.types.get() != "None" and len(self.label.get()) >= 1 and len(self.label_number.get()) >= 1 and len(self._loc.get()) >= 1 and len(self.year_entry.get()) >= 1:
            if self.types.get() == "OTHER" and len(self.type_entry.get()) <= 1:
                return False
            return True
        # check if all fields aren't filled out
        
        return False

    def get_desc_data(self):
        return self.desc_data
    
    def reset_fields(self):
        self.artist_text.delete(0, ctk.END)
        self.title_text.delete(0, ctk.END)
        self.label.delete(0, ctk.END)
        self.label_number.delete(0, ctk.END)
        self._loc.set("")
        self.types.set(None)
        self.type_entry.delete(0, ctk.END)
        self.year_entry.delete(0, ctk.END)

class Enter_QTY(ctk.CTkToplevel):
    def __init__(self, parent, current_value="_", flaw="xLP BOX"):
        super().__init__(parent)
        self.parent = parent
        self.configure(height=100)
        self.title("")
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.grab_set()
        self.flaw = flaw
        self.current_value = current_value

        self.display()

    def handle_key_event(self, event):
        if event.keysym == "Escape":
            self.parent.unselect_radiobutton()
            self.destroy()

    def display(self):
        print("TOP LEVEL WINDOW QTY START")

        self.bind("<Key>", self.handle_key_event)


        for widget in self.winfo_children():
            widget.grid_forget()


        ctk.CTkLabel(self, text= self.current_value + self.flaw,  font=("Lucida Sans", 17)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.qty_entry = ctk.CTkEntry(self, placeholder_text="Enter Number")
        if self.current_value != "_":
            self.qty_entry.insert(0, self.current_value)
        self.qty_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.qty_entry.bind('<KeyRelease>', self.update_qty)


        self.cancel_btn = ctk.CTkButton(self, text="Cancel", command=lambda:self.cancel(), font=("Lucida Sans", 17))
        self.cancel_btn.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

        self.set_btn = ctk.CTkButton(self, text="Set", command=lambda: self.set_qty(), font=("Lucida Sans", 17))
        self.set_btn.grid(row=2, column=1, columnspan=1, padx=10, pady=10)
    
    def update_qty(self, event):
        if self.qty_entry.get() == "":
            self.current_value = "_"
        else:
            self.current_value = self.qty_entry.get()
        
        for widget in list(self.winfo_children()):
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(text=self.current_value + "xLP BOX")

    def set_qty(self):
        
        self.parent.set_qty(self.qty_entry.get())
        self.destroy()

    def cancel(self):
        self.parent.unselect_radiobutton()
        self.destroy()

