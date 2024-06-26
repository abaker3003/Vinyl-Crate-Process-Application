import customtkinter as ctk

class Progress(ctk.CTkFrame):
    def __init__(self, master, crate_num, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.crate_num = crate_num
        if str(self.crate_num).isdigit():
            label = ctk.CTkLabel(self, text="Crate " + str(self.crate_num), font=("Courier New Greek", 18, "bold"), anchor="center")
        else:
            label = ctk.CTkLabel(self, text=self.crate_num, font=("Courier New Greek", 20, "bold"), anchor="center")
        label.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        self.curr_progress = ctk.StringVar(value="Pre Prep")

        self.progress = ctk.CTkSegmentedButton(self, values=["PRE\nPREP", "  GRADING  ", "  HIGHLIGHTS  ", "   INTRO  ", "RSL /\nPRICE", "  PRINT  "], variable=self.curr_progress, font=("Courier New Greek", 19), state="disabled", width=350)
        self.progress.grid(row=0, column=1, columnspan=4, sticky='nsew', padx=20, pady=20)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.home_btn = ctk.CTkButton(self, text="Home", command=lambda: master.start_app(), font=("Courier New Greek", 19), width=95, height=10)
        self.home_btn.grid(row=0, column=8, columnspan=2, padx=10, pady=10, sticky="nsew")
    
    def set_progress(self, progress):
        self.curr_progress.set(progress)