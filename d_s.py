import customtkinter as ctk
from tkinter import ttk

class DmgSvr(ctk.CTkFrame):
    def __init__(self, master, dmgs, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.dmgs = dmgs

        self.dmg_vars = {dmg:ctk.StringVar() for dmg, l in self.dmgs.items()}
        self.dmg_dict = {}
        self.dmgs_cnt = 0
        var = None
        self.checkboxes = []
        self.selected_damages = [] 
        self.last_row = 0
        self.last_column = 0

        col = 0
        subtract_row = 0


        # List of checkboxes with damage labels/entry
        for i, (dmg, svrty_lst) in enumerate(self.dmgs.items()):
            if i > 0 and i % 11 == 0 :
                subtract_row -= 11
                col += 2

            var=self.dmg_vars[dmg]
            dmg_bx = ctk.CTkCheckBox(self, text="", variable=var, onvalue=dmg, offvalue="None", width=2, height=1)
            #print(dmg + " - row: " + str(i + subtract_row))
            dmg_bx.grid(row=i + subtract_row, column=col, pady=3, padx=(10,0), sticky="e")
            self.checkboxes.append(dmg_bx)
            
            self.label = None

            if dmg == "Other":
                self.label = ctk.CTkEntry(self, textvariable=var, placeholder_text="Other", font=("Arial", 18))                
                self.checkboxes.append(self.label)

            else:
                
                self.label = ctk.CTkLabel(self, text=dmg, font=("Arial", 18))

            self.label.grid(row=i + subtract_row, column= col+ 1, pady=3, padx=(0,10), sticky="w")

            # Bind / Toggle Function
            dmg_bx.bind("<Button-1>", lambda event, dmg=dmg, var=var, svrty=svrty_lst, entry=self.label: self.toggle_severity_selection(event, svrty, dmg, var, entry))
        
        self.last_row = i + subtract_row + 1
        self.last_column =  col + 1
             

    def toggle_severity_selection(self, event, svrty, dmg, var, entry=None):
        #print("selected widget: ", dmg)
        #print("current widget value: ", var.get())+
        
        #print(self.dmg_dict)

        self.var = var

        if self.var.get() != "None":

            if len(svrty) == 0:
                self.selected_damages.append(dmg)
                self.update_damages_count()
                return

            self.update_damages_count()
            
            
            if self.var.get() != dmg:
                #print("Empty widget value")
                self.var.set("None")
            elif self.var.get() == "NO DAMAGE":
                self.add_svrty_to_dmg(dmg, "NO DAMAGE")
            else:
                if self.var.get() not in self.selected_damages:
                    self.selected_damages.append(self.var.get())
                self.display(event, dmg, self.var, svrty)

        elif self.var.get() == "None" or self.var.get() in self.dmg_dict.keys():
            if dmg in self.dmg_dict.keys():
                #print("Removing the following DAMAGE:SEVERITIES from dictionary: ")
                #print(dmg + ":" + str(self.dmg_dict[dmg]))
                del self.dmg_dict[dmg]

            if dmg in self.selected_damages:
                self.selected_damages.remove(dmg)
            
            self.master.remove_unselected_flaw(dmg, list(self.dmg_dict.keys()))

            self.enable_widgets()
        #print(self.dmg_dict)


    def update_damages_count(self):
        self.dmgs_cnt = len(self.dmg_dict.keys())

        #print(str(self.dmgs_cnt) + " DAMAGES")


        if self.dmgs_cnt >= 3:
            self.disable_widgets()
        else:
            
            self.enable_widgets()

    def uncheck_current_dmg(self, dmg):
        self.close_svrity_frame()
        if dmg in self.dmg_dict.keys():
                #print("Removing the following DAMAGE:SEVERITIES from dictionary: ")
                #print(dmg + ":" + str(self.dmg_dict[dmg]))
                del self.dmg_dict[dmg]

        if dmg in self.selected_damages:
            self.selected_damages.remove(dmg)
        
        self.master.remove_unselected_flaw(dmg, list(self.dmg_dict.keys()))

        self.enable_widgets()
    
    ## 2nd-2nd
    def close_svrity_frame(self):
        for wdgt in self.svrty_frame.winfo_children():
            wdgt.grid_remove()
        for checkbox in self.checkboxes:
            checkbox.configure(state='normal')
            if isinstance(checkbox, ctk.CTkEntry):
                checkbox.delete(0, 'end')

    ## 2nd-1st
    def display(self, event, dmg, var, svrty):
        #print("Disabling widgets")
        
        self.disable_widget(event, dmg, var)
        self.svrty_frame = Sev_List(self, svrty, dmg, var)

    
    def disable_widgets(self):
        color = ""
        if ctk.get_appearance_mode() == 'Light':
            color = '#9D9C9D'
        else:
            color = 'black'
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                if widget.cget("onvalue") in self.dmg_dict.keys():
                    widget.configure(state='normal')
                else:
                    widget.configure(state='disabled')
            if isinstance(widget, ctk.CTkLabel):
                if widget.cget("text") not in self.dmg_dict.keys():
                    widget.configure(text_color=color)
        

    def disable_widget(self, event, dmg, var):
        color = ""
        if ctk.get_appearance_mode() == 'Light':
            color = '#9D9C9D'
        else:
            color = 'black'
        #count = 1
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                if widget.cget("onvalue") != dmg:
                    #print(count)
                    #count += 1
                    widget.configure(state='disabled')
                    #print(str(type(widget)) + " " + str(widget.cget("onvalue")) +  " " + str(widget.cget("state")))
            if isinstance(widget, ctk.CTkLabel):
                if widget.cget("text") != dmg or widget.cget("text") not in self.dmg_dict.keys():
                    #print(count)
                    #count += 1
                    widget.configure(text_color=color)
                    #print(str(type(widget)) + " " + str(widget.cget("text")) +  " " + str(widget.cget("text_color")))
              
    
    def enable_widgets(self):
        if ctk.get_appearance_mode() == 'Light':
            color = 'black'
        else:
            color = 'white'

        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(text_color=color)
            if isinstance(widget, ctk.CTkCheckBox) or isinstance(widget, ctk.CTkEntry):
                widget.configure(state='normal')

    def set_dict(self, dmg, svrty):
        #print("Set button Activated..")
            
        #print("Current damage: " + dmg) 

        if dmg:
            var = ctk.StringVar(self, value=dmg)  
            checkbox = ctk.CTkCheckBox(self, text="", variable=var, onvalue=dmg, offvalue="None", font=("Arial", 15), width=2, height=1)
            checkbox.grid(row=self.last_row, column=self.last_column - 1, pady=3, padx=(10,0), sticky="e")
            label = ctk.CTkLabel(self, text=dmg, font=("Arial", 15))
            label.grid(row=self.last_row, column=self.last_column, pady=3, padx=(0,10), sticky="w")
            # Bind / Toggle Function
            #print("line 118 executed ")
            checkbox.bind("<Button-1>", lambda event, svrty=svrty, dmg=dmg, var=var: self.toggle_severity_selection(event, svrty, dmg, var))
            self.checkboxes.append(checkbox)
            self.dmg_vars[dmg] = var
            # Clear the CTkEntry widget
            self.label.delete(0, 'end')
            # Uncheck the "Other" checkbox
            self.dmg_vars["Other"].set("None")
            self.update_dict(dmg)
            #print("Current severity dict in severity class ...." )
            #print(self.svrty_frame.get_selected_severity())
            self.last_row += 1
        else:
            self.update_dict(self.var.get())
            
        #print(self.dmg_dict)
        self.update_damages_count()
        

    def update_dict(self, dmg):
        if self.dmg_vars[dmg].get() == "None":
            self.dmg_dict.pop(dmg, None)  # Remove the damage from the dictionary
            self.master.remove_unselected_flaw(dmg, list(self.dmg_dict.keys()))
        else:
            self.dmg_dict[dmg] = self.svrty_frame.get_selected_severity()
        self.close_svrity_frame()
        self.enable_widgets()



    def add_svrty_to_dmg(self, dmg, svrty):
        self.dmg_dict[dmg] = svrty
        self.master.add_selected_flaws(dmg, svrty)

    def add_svrty_to_dmg_new_checkbox(self, dmg, svrty):
        self.set_dict(dmg, svrty)
        self.master.add_selected_flaws(dmg, svrty)


    
    def get_dmg_dict(self):
        return self.dmg_dict



class Sev_List(ctk.CTkToplevel):
    def __init__(self, parent, svrty=None, dmg=None, var=None, this_selection=None):
        super().__init__(parent)
        self.parent = parent
        self.configure(height=100)
        self.title("")
        self.attributes("-topmost", True)
        self.resizable(False, False)
        if dmg != "Other":
            self.grab_set()
        self.svrty = svrty
        self.dmg = dmg
        self.var = var
        self.this_selection = this_selection
        self.selected_svrties = []
        self.checked_amt = 0

        self.display_list()

    def handle_key_event(self, event):
        if event.keysym == "Escape":
            self.var.set("None")
            self.parent.uncheck_current_dmg(self.dmg)
            self.destroy()
        
    def display_list(self):

        self.bind("<Key>", self.handle_key_event)

        for widget in self.winfo_children():
            widget.grid_forget()
        self.reset_selections()
        
        ctk.CTkLabel(self, text="Severity", font=("Lucida Sans", 20)).grid(row=0, column=0, columnspan=2, sticky="snew")
    
        if self.dmg == "Other":
            ctk.CTkLabel(self, text="Choose 1 / Limit 2\nMake sure to fill out Entry Box \nBEFORE htting \"Set\"", font=("Lucida Sans", 15)).grid(row=1, column=0, columnspan=2,  sticky="snew")

        else:
            ctk.CTkLabel(self, text="Choose 1 / Limit 2", font=("Lucida Sans", 15)).grid(row=1, column=0, columnspan=2,  sticky="snew")

        # ttk seperater going horizontal
        sep = ttk.Separator(self, orient="horizontal")
        sep.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

        for widget in self.parent.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                if widget.cget("onvalue") != self.dmg:
                    widget.configure(state='disabled')
        
        self.scroll_frame = ctk.CTkScrollableFrame(self, height=475)
        self.scroll_frame.grid(row=3, column=0, columnspan=3, rowspan=4, sticky="snew")

        for j, svrty in enumerate(self.svrty):
            severity_var = ctk.StringVar()
            severity = ctk.CTkCheckBox(self.scroll_frame, text=f'{svrty}', variable=severity_var, onvalue=svrty, offvalue="None", font=("Arial", 18), width=2, height=1)
            severity.grid(row=j, column=1, pady=5, padx=(5,50), sticky="snew")
            severity.bind("<Button-1>", lambda event, svrty=svrty, var=severity_var: self.check_limit(event, svrty, var))

        self.cancel_btn = ctk.CTkButton(self, text="Cancel", command=lambda:self.cancel(), font=("Lucida Sans", 17))
        self.cancel_btn.grid(row=len(self.svrty) + 2, column=0, columnspan=1, padx=10, pady=10)

        self.set_btn = ctk.CTkButton(self, text="Set", command=lambda: self.set_dict(), font=("Lucida Sans", 17))
        self.set_btn.grid(row=len(self.svrty) + 2, column=1, columnspan=1, padx=10, pady=10)

    
    def set_dict(self):
        if self.dmg == "Other":
            self.parent.add_svrty_to_dmg_new_checkbox(self.parent.label.get(), self.selected_svrties)
        else:
            self.parent.add_svrty_to_dmg(self.dmg, self.selected_svrties)
        self.parent.update_damages_count()
        self.destroy()

    def update_checked_amount(self):
        self.checked_amt = len(self.selected_svrties)

    # ----> PRINT STATEMENTS FOR DEBUGGING <---- #
    def check_limit(self, event, svrty, var):
        clicked_widget = event.widget

        if var.get() != "None" and var.get() != svrty:
            #print("Empty widget value")
            var.set("None")
            return
         
        #print("selected widget: ", svrty)
        #print("current widget value: ", var.get())

        
        if var.get() == "None" and svrty in self.selected_svrties:
            #print("Removing activated")
            self.selected_svrties.remove(svrty)
        elif var.get() != "None" and svrty not in self.selected_svrties:
            #print("Adding activated")
            self.selected_svrties.append(svrty)

        self.update_checked_amount()
        #print("update of checked amount: ", self.checked_amt)

        if self.checked_amt < 2:
            #print("Normalizing all widgets...")
            for widget in self.scroll_frame.winfo_children():
                if isinstance(widget, ctk.CTkCheckBox):
                    widget.configure(state='normal')
        elif self.checked_amt >= 2:
            #print("Disabling the following unchecked widgets...")
            for widget in self.scroll_frame.winfo_children():
                if isinstance(widget, ctk.CTkCheckBox):
                     if widget.cget("onvalue") not in self.selected_svrties:
                        widget.configure(state='disabled')

    def reset_selections(self):
        self.selected_svrties = []
        self.update_checked_amount()
            

    def get_selected_severity(self):
        return self.selected_svrties
    
    def cancel(self):
        self.var.set("None")
        self.parent.uncheck_current_dmg(self.dmg)
        self.destroy()
