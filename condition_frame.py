import customtkinter as ctk


class Condition(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

        conditions_list = [
            "New", "Very Good", "Good", "Fairly Good", "Fair"
        ]
        self.condition = ctk.StringVar()

        condition_label = ctk.CTkLabel(self, text="Condition", font=("Courier New Greek", 28, "bold"))
        condition_label.grid(row=0, column=0, columnspan=6, pady=10, sticky='ew')

        for i, cond in enumerate(conditions_list):
            cond_opt = ctk.CTkRadioButton(self,
                                        text=cond,
                                        variable=self.condition,
                                        value=cond, font=("Courier New Greek", 20))
            cond_opt.grid(row=1, column=i, padx=30, pady=20)
    
    def check_fields(self):
        if self.condition.get():
            return True
        return False

    def get_condition(self):
        return self.condition.get()
    
    def clear_selection(self):
        self.condition.set("")
