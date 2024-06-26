import customtkinter as ctk

class Enter_Measurement(ctk.CTkToplevel):
    def __init__(self, parent, first_word, flaw=None, var=None, current_value="__"):
        super().__init__(parent)
        self.parent = parent
        self.configure(height=100)
        self.title("")
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.grab_set()
        self.first_word = first_word
        self.flaw = flaw
        self.var = var
        self.current_value = current_value
        
        
        self.display()

    def handle_key_event(self, event):
        if event.keysym == "Escape":
            self.var.set("None")
            self.parent.uncheck_current_flaw(self.flaw)
            self.destroy()

    def display(self):
        print("TOP LEVEL WINDOW MEASUREMENT START")

        self.bind("<Key>", self.handle_key_event)


        for widget in self.winfo_children():
            widget.grid_forget()


        ctk.CTkLabel(self, text= self.current_value + "\" " + self.flaw,  font=("Lucida Sans", 17)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.measurement_entry = ctk.CTkEntry(self, placeholder_text="Enter Inches")
        if self.current_value != "__":
            self.measurement_entry.insert(0, self.current_value)
        self.measurement_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.measurement_entry.bind('<KeyRelease>', self.update_measurement)


        self.cancel_btn = ctk.CTkButton(self, text="Cancel", command=lambda:self.cancel(), font=("Lucida Sans", 17))
        self.cancel_btn.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

        self.set_btn = ctk.CTkButton(self, text="Set", command=lambda: self.set_dict(), font=("Lucida Sans", 17))
        self.set_btn.grid(row=2, column=1, columnspan=1, padx=10, pady=10)
    
    def update_measurement(self, event):
        if self.measurement_entry.get() == "":
            self.current_value = "__"
        else:
            self.current_value = self.measurement_entry.get()
        
        for widget in list(self.winfo_children()):
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(text=self.current_value + "\" " + self.flaw)

    def set_dict(self):
        
        self.parent.add_svrty_to_flaw(self.flaw, self.measurement_entry.get())
        self.destroy()

    def cancel(self):
        self.var.set("None")
        self.parent.uncheck_current_flaw(self.flaw)
        self.destroy()
