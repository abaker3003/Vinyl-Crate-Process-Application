from tkinter import UNDERLINE
import customtkinter as ctk
import d_s as dmgsvr

class Vinyl_Damages(ctk.CTkFrame):
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.count = 1
        self.row_start = 5

        self.dmgs = {
            'handling traces': [
                'subtle', 'faint', 'stray', 'light', 'minor', 'obvious', 'noticeable', 'few', 'occasional', 'occassionally', 'scattered', 'mild', 'typical'],
            'handling blemishes': [
                'faint', 'stray', 'tiny', 'isolated', 'light', 'minor', 'slight', 'obvious', 'noticeable', 'occasional', 'generalized', 'scattered', 'mild', 'moderate', 'multiple', 'typical', 'visible', 'significant', 'considerable'],
            'usage': [
                'light', 'minimal', 'occasional', 'mild', 'moderate', 'normal', 'typical', 'heavy', 'significant', 'considerable', 'excessive'],
            'usage traces': [
                'subtle', 'faint', 'stray', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'few', 'minimal', 'average', 'generalized', 'sporatic', 'scattered', 'mild', 'storage-related', 'typical', 'considerable'],
            'usage blemishes': [
                'faint', 'stray', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'few', 'minimal', 'generalized', 'sporatic', 'scattered', 'mild' 'multiple', 'storage-related', 'typical', 'visible', 'heavy', 'significant', 'considerable', 'excessive'],
            'usage blemishing': [
                'faint', 'stray', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'few', 'minimal', 'generalized', 'sporatic', 'scattered', 'mild',  'storage-related', 'typical', 'visible', 'pronounced', 'significant', 'considerable', 'excessive'],
            'handling & usage traces': [
                'faint', 'stray', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'minimal', 'generalized', 'sporatic', 'scattered', 'mild', 'typical', 'visible', 'pronounced', 'significant', 'considerable', 'excessive'],
            'handling & usage markings': [
                'stray', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'minimal', 'generalized', 'sporatic', 'scattered', 'mild', 'typical', 'visible', 'pronounced', 'heavy', 'significant', 'considerable', 'excessive', 'severe'],
            'prints': [
                'faint', 'stray', 'tiny', 'isolated', 'light' 'obvious', 'noticeable', 'few', 'occasional', 'scattered', 'mild', 'multiple', 'visible',],
            'handling prints': [
                'subtle', 'faint', 'stray', 'tiny', 'isolated', 'light', 'obvious', 'noticeable', 'few', 'occasional', 'scattered', 'mild', 'visible', 'pronounced'],
            'hairline': [
                'subtle', 'faint', 'insignificant', 'stray', 'tiny', 'small', 'isolated', 'light', 'occasional', 'visible'],
            'hairlines': [
                'subtle', 'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'generalized', 'scattered', 'multiple', 'storage-related'],
            'hairline-type wear': [
                'faint', 'stray', 'light', 'minor', 'noticeable', 'generalized', 'scattered', 'mild', 'moderate', 'storage-related', 'typical', 'visible', 'heavy', 'significant', 'considerable'],
            'blemishing': [
                'stray', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'minimal', 'generalized', 'scattered', 'mild', 'moderate', 'storage-related', 'visible', 'heavy', 'significant', 'considerable', 'excessive', 'severe'],
            'blemishes': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild', 'multiple', 'storage-related', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'considerable', 'excessive', 'severe'],
            'storage-related blemishing': [
                'subtle', 'faint', 'stray', 'isolated', 'light', 'minor', 'noticeable', 'minimal', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild', 'moderate', 'typical', 'heavy', 'significant', 'considerable'],
            'blemishing from storage': [
                'subtle', 'faint', 'stray', 'isolated', 'light', 'minor', 'noticeable', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild', 'moderate', 'typical'],
            'manufacturing blemish': [
                'faint', 'insignificant', 'stray', 'tiny', 'isolated', 'light', 'minor', 'noticeable', 'mild', 'pronounced', 'large', 'significant'],
            'markings': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'few', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild',  'multiple', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'considerable', 'feelable', 'excessive', 'severe'],
            'mark': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'mild', 'moderate', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'considerable', 'feelable', 'severe'],
            'marks': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'few', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild', 'moderate', 'multiple', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'considerable', 'feelable', 'excessive', 'severe'],
            'marks & prints': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'few', 'minimal', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild','multiple', 'typical', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'considerable', 'feelable', 'excessive', 'severe'],
            'marks & wear': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'few', 'minimal', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild', 'multiple', 'typical', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'considerable', 'feelable', 'excessive', 'severe'],
            'groove-wear': [
                'subtle', 'faint', 'stray', 'isolated', 'light', 'obvious', 'noticeable', 'minimal', 'generalized', 'sporatic', 'scattered', 'mild', 'moderate', 'normal', 'typical', 'visible', 'pronounced', 'significant', 'considerable', 'excessive', 'severe'],
            'surface marks': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'minimal', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild', 'moderate', 'multiple', 'normal', 'typical', 'visible', 'large', 'heavy', 'significant', 'considerable', 'feelable', 'excessive', 'severe'],
            'scuff': [
                'faint', 'insignificant', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'occasional', 'mild', 'moderate', 'typical', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'severe'],
            'scuffs': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'obvious', 'noticeable', 'occasional', 'scattered', 'mild', 'moderate', 'multiple', 'storage-related' 'typical', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'feelable', 'severe'],
            'feelable scuff': [
                'small', 'minor', 'noticeable', 'mild', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'severe'],
            'feelable scuffs': [
                'stray', 'small', 'isolated', 'obvious', 'noticeable', 'few', 'occasional', 'sporatic', 'scattered', 'mild', 'multiple', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'considerable', 'feelable', 'excessive', 'severe'],
            'scratch': [
                'faint', 'insignificant', 'stray', 'tiny', 'small', 'light', 'minor', 'obvious', 'noticeable', 'occasional', 'mild', 'visible', 'pronounced', 'large', 'heavy', 'significant', 'feelable', 'severe'],
            'wear': [
                'faint', 'light', 'minor', 'obvious', 'noticeable', 'minimal', 'generalized', 'scattered', 'mild', 'mildly', 'moderate', 'normal', 'typical', 'visible', 'pronounced', 'heavy',  'significant', 'considerable', 'excessive', 'severe'],
            
            'well-worn': [],
            'heavy wear': [
                ],
            
            'damaged': [
                'mildly', 'heavily'],
            'sleeve rub': [
                'subtle', 'faint', 'insignificant', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'noticeable', 'occasional', 'scattered', 'mild', 'multiple', 'storage-related', 'visible', 'large', 'significant'],
            'sleeve rubs': [
                'faint', 'stray', 'tiny', 'small', 'isolated', 'light', 'minor', 'noticeable', 'few', 'occasional', 'sporatic', 'scattered', 'mild', 'multiple', 'storage-related', 'typical', 'visible', 'large', 'significant'],
            'sleeve rub blemishing': [
                'subtle', 'faint' 'stray', 'isolated', 'light', 'minor', 'noticeable', 'occasional', 'generalized', 'sporatic', 'scattered', 'mild', 'typical', 'visible', 'heavy', 'significant', 'considerable', 'excessive'],
            'spindle mark on label': [
                'faint', 'insignificant', 'tiny', 'small', 'light', 'minor', 'noticeable', 'mild', 'visible', 'pronounced', 'large'],
            'spindle marks': [
                'faint', 'tiny', 'small', 'light', 'minor', 'noticeable', 'minimal', 'generalized', 'mild', 'moderate', 'multiple', 'visible', 'pronounced'],
            'spindle mark activity': [
                'faint', 'light', 'noticeable', 'minimal', 'generalized', 'sporatic', 'moderate', 'typical', 'visible', 'significant', 'considerable', 'excessive'],
            'sleeve dust': [
                'light', 'noticeable', 'sporatic', 'scattered', 'mild' 'visible', 'significant', 'considerable'],
            'record cleaner residue': [
                'faint', 'light', 'noticeable', 'generalized'],
            'bow': [
                'subtle', 'tiny', 'small', 'minor', 'slight', 'obvious', 'noticeable', 'mild', 'moderate', 'pronounced', 'significant'],
            'bowed': [
                'subtle', 'slight', 'noticeable', 'minimally', 'mildly', 'heavily',  'significant'],
            'ink writing on label': [
                'faint', 'tiny', 'small', 'light', 'minor', 'obvious', 'noticeable', 'mild', 'visible', 'heavy', 'considerable'],
            'notations on label': [
                'faint', 'tiny', 'light', 'minor', 'noticeable', 'visible'],
            'writing on label': [
                'faint', 'tiny', 'light', 'minor', 'noticeable', 'visible'],
            'name ID on label': [
                'faint', 'small', 'noticeable'],
            'stickers on label': [
                'small', 'multiple'],
            "Other" : [
                "subtle", "faint", "fragile", "insignificant", "stray", "tiny", "small", "isolated", "light", "minor", "slight", "obvious", "noticeable", "few", "minimal", "minimally", "occasional", "average", "general", "generalized", "sporatic", "scattered", "mild", "mildly", "moderate", "moderately", "multiple", "storage-related", "normal", "typical", "visible", "pronounced", "large", "heavy", "heavily", "significant", "considerable", "feelable", "excessive", "severe"]
        }
        
        
        header_label = ctk.CTkLabel(self, text="Vinyl Flaws / Severity", font=("Lucida Sans", 25))
        header_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')

        mini_label = ctk.CTkLabel(self, text="Choose Up To 3", font=("Lucida Sans", 18))
        mini_label.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')

        
        self.tree = dmgsvr.DmgSvr(self, self.dmgs)
        self.tree.grid(row=2, column=0, columnspan=6, rowspan=4, padx=5, pady=5, sticky='nsew')

        ctk.CTkLabel(self, text="Selected:", font=("Arial", 21, UNDERLINE)).grid(row=6, column=0, sticky="e", pady=5, padx=5)
      

    def add_selected_flaws(self, dmg, svrty):
        s = ""
        for sev in svrty:
            s += sev + ", "
        s = s[:-2]
        label = ctk.CTkLabel(self, text=s + " " + dmg , font=("Arial", 19))
        label.grid(row=self.row_start + self.count, column=1, columnspan=1, padx=5, pady=5, sticky='w')
        self.count += 1

    def remove_unselected_flaw(self, removed_dmg, current_dmgs):
        was_there = False
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                if widget.cget("text").endswith(removed_dmg):
                    widget.destroy()
                    was_there = True
                    break
        
        if was_there:
            self.count -= 1


        # Rearrange the damage labels to the left
        for i, dmg in enumerate(current_dmgs):
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkLabel):
                    if widget.cget("text").endswith(dmg):
                        widget.grid(row=self.row_start + 1 + i, column=1, columnspan=1, padx=5, pady=5, sticky='w')
        

    def get_selection(self):
        return self.tree.get_dmg_dict()
    