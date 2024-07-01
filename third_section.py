import re
import customtkinter as ctk
import condition_frame as cf
import vinyl_damage_frame as vdf
import jacket_flaws as jf
import ai_frame as ai

class Frame2(ctk.CTkFrame):
    def __init__(self, master, indexes, xl_read, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.indexes = indexes
        self.xl_read = xl_read.read_into_dataframe()
        self.master = master
        self.curr_idx = 0
        self.idx = indexes[self.curr_idx]
        self.info = ctk.CTkFrame(self)
        self.info.grid(row=0, column=0, columnspan=3, rowspan=3, sticky='nsew', padx=10, pady=7)
        self.row = self.xl_read.loc[self.idx]       
        self.data = {}
        self.selected_intro = []    
        self.start()

    def clear_display(self):
        for widget in self.info.winfo_children():
            widget.grid_forget()
        self.info.grid(row=0, column=0, columnspan=5, rowspan=2, sticky='nsew', padx=10, pady=10)
        #print("cleared display")

    def curr_info(self):
        self.row = self.xl_read.loc[self.idx]    
        self.artist = self.row['Artist']
        self.title = self.row['Title']
        self.loc = self.row['Loc']
        self.conf = self.row['Conf.']
        self.label = self.row['Label']
        self.label_num = self.row['Label #']
        self.year = self.row['Notes']
        self.display_info()

    def display_info(self):

        self.clear_display()
        self.artist_label = ctk.CTkLabel(self.info, height=15, text="Artist: " + self.artist, font=("Courier New Greek", 18), anchor="center", width=200)
        self.artist_label.grid(row=0, column=0, columnspan=2, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self.info, height=15, text="Title: " + self.title, font=("Courier New Greek", 18), anchor="center", width=200)
        self.title_label.grid(row=1, column=0, columnspan=2, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(0, weight=1)

        self.loc_label = ctk.CTkLabel(self.info, height=15, text="Genre: " + self.loc, font=("Courier New Greek", 18), anchor="center", width=200)
        self.loc_label.grid(row=0, column=2, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(2, weight=1)

        self.conf_label = ctk.CTkLabel(self.info, height=15, text="Type: " + self.conf, font=("Courier New Greek", 18), anchor="center", width=200)
        self.conf_label.grid(row=1, column=2, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(2, weight=1)

        self.label_label = ctk.CTkLabel(self.info, height=15, text="Label: " + self.label, font=("Courier New Greek", 18), width=200, anchor="center")
        self.label_label.grid(row=0, column=3, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(3, weight=1)

        self.label_num_label = ctk.CTkLabel(self.info, height=15, text="Label #: " + self.label_num, width=200, font=("Courier New Greek", 18), anchor="center")
        self.label_num_label.grid(row=1, column=3, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(3, weight=1)

        self.year_label = ctk.CTkLabel(self.info, height=15, text="Year: " + str(self.year), font=("Courier New Greek", 18), anchor="center", width=200)
        self.year_label.grid(row=0, column=4, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(4, weight=1)

        edit = ctk.CTkButton(self.info, height=15, text="Edit", command=lambda: self.edit(), font=("Courier New Greek", 18))
        edit.grid(row=1, column=4, pady=10, padx=15, sticky='nsew')
        self.info.columnconfigure(4, weight=1)
    
    def edit(self):
        self.clear_display()

        self.artist_entry = ctk.CTkEntry(self.info, height=15, font=("Courier New Greek", 18))
        self.artist_entry.insert(0, self.artist)
        self.artist_entry.grid(row=0, column=0, columnspan = 2, pady=5, padx=15)
        
        self.title_entry = ctk.CTkEntry(self.info, height=15, font=("Courier New Greek", 18))
        self.title_entry.insert(0, self.title)
        self.title_entry.grid(row=1, column=0, columnspan = 2, pady=5, padx=15)
        
        loc_list = ["PRL", "RBL", "MTL", "FKL", "API",   "SGCL", "SNTL", "JZL", "VNL", "BLL", "CLL", "CML", "CSL", "CWL", "DDL", "HOL", "HHL", "HSL", "HWL", "INL", 
                     "MTL", "NAL", "RGL", "RPL", "SPL", "SLA", "STCL", "STL",
                    "SYL", "SWL", "WOL", "ZZL"]
        self._loc = ctk.StringVar(value=self.loc)
        self.loc_option = ctk.CTkComboBox(self.info, height=15, variable=self._loc, font=("Courier New Greek", 18), state="readonly", values=loc_list, hover=True, dropdown_font=("Courier New Greek", 15), width=200)
        self.loc_option.grid(row=0, column=2, pady=5, padx=25)
        
        
        self.conf_entry = ctk.CTkEntry(self.info, height=15, font=("Courier New Greek", 18), width=200)
        self.conf_entry.insert(0, self.conf)
        self.conf_entry.grid(row=1, column=2, pady=5, padx=25)
        
        self.label_entry = ctk.CTkEntry(self.info, height=15, font=("Courier New Greek", 18), width=200)
        self.label_entry.insert(0, self.label)
        self.label_entry.grid(row=0, column=3, pady=5, padx=15)
        
        self.label_num_entry = ctk.CTkEntry(self.info, height=15, font=("Courier New Greek", 18), width=200)
        self.label_num_entry.insert(0, self.label_num)
        self.label_num_entry.grid(row=1, column=3, pady=5, padx=15)
        
        self.year_entry = ctk.CTkEntry(self.info, height=15, font=("Courier New Greek", 18), width=200)
        self.year_entry.insert(0, self.year)
        self.year_entry.grid(row=0, column=4, pady=5, padx=15)
        
        save_btn = ctk.CTkButton(self.info, height=15, text="Save", command=self.save_edited_info, font=("Courier New Greek", 18))
        save_btn.grid(row=1, column=4, pady=5, padx=15)

    def save_edited_info(self):
        self.artist = self.artist_entry.get()
        self.title = self.title_entry.get()
        self.loc = self._loc.get()
        self.conf = self.conf_entry.get()
        self.label = self.label_entry.get()
        self.label_num = self.label_num_entry.get()
        self.year = self.year_entry.get()
        self.addit_info = {"Artist": self.artist, "Title": self.title, "Loc": self.loc, "Conf.": self.conf, "Label": self.label, "Label #": self.label_num, "Notes": self.year}
        self.master.update_row(self.idx + 2, self.addit_info)
        self.row = self.xl_read.iloc[self.idx]
        self.display_info()
    
    def start(self):
        self.addit_info = {}
        self.data = {}
        self.idx = self.indexes[self.curr_idx]
        
        self.curr_info()

        self.condition = cf.Condition(self)
        self.condition.grid(row=4, column=0, columnspan=5, rowspan=2, padx=10, pady=7, sticky='nsew')

        self.back_btn = ctk.CTkButton(self, text="Back", command=lambda: self.master.start_new_vinyl(), font=("Courier New Greek", 18), width=100)
        self.back_btn.grid(row=6, column=0, columnspan=2, pady=20, padx=25, sticky="w")

        self.next_btn = ctk.CTkButton(self, text="Next", command=self.save_first_info, font=("Courier New Greek", 18), width=100)
        self.next_btn.grid(row=6, column=4, columnspan=2, pady=20, padx=25, sticky="e")

    
    def save_first_info(self):
        if not self.condition.check_fields():
            return
        self.data["Con"] = self.condition.get_condition()
        self.cond = self.condition.get_condition()
        self.clear()

#### ----> NEED TEMPLATE FOR NEW GRADE <----- #####
        if self.condition.get_condition() == "New":
            self.data["Damages"] = "{\"NO DAMAGE\":\"NO DAMAGE\"} - {\"NO DAMAGE\":\"NO DAMAGE\"}"
            self.data["Qty"] = "Highlights"
            # save the damages dictionaries into the ["Damages"] column
            self.master.update_row(self.idx, self.data)
            self.curr_idx += 1
            if self.curr_idx >= len(self.indexes):
                self.master.start()
            else:
                self.idx = self.indexes[self.curr_idx]
                self.clear()
                self.display_info()
                self.start()
#### ----> NEED TEMPLATE FOR NEW GRADE <----- #####

        else:
            self.damage_frame()
    
    def clear(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        self.display_info()
    
    def back(self):
        self.clear()
        self.display_info()
        self.start()
        
    def damage_frame(self):

        
        self.second_section = vdf.Vinyl_Damages(self)
        self.third_section = Intros(self, self.curr_idx, self.xl_read, self.cond)
        self.fourth_section = jf.Jacket_Flaws(self)
        

        self.back_btn = ctk.CTkButton(self, text="Back", command=self.back, font=("Courier New Greek", 18))

        self.next_btn = ctk.CTkButton(self, text="Next", font=("Courier New Greek", 18))

        self.vinyl_dmg()
        

    def vinyl_dmg(self):
        
        self.clear()

        self.back_btn.configure(command=lambda:self.back())
        
        self.next_btn.configure(command=lambda:self.show_intros())

        self.second_section.grid(row=2, column=0, columnspan=5, rowspan=3, sticky='nsew', padx=10, pady=7)

        self.back_btn.grid(row=6, column=0, columnspan=1, pady=20, padx=20, sticky='w')

        self.next_btn.grid(row=6, column=4, columnspan=1, pady=20, padx=20, sticky='e')


    def show_intros(self):
        
        self.clear()

        self.back_btn.configure(command=lambda:self.vinyl_dmg())
        
        self.next_btn.configure(command=lambda:self.jacket_string())

        self.third_section.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky='nsew')
        
        self.back_btn.grid(row=6, column=0, columnspan=1, pady=20, padx=20, sticky='w')

        self.next_btn.grid(row=6, column=4, columnspan=1, pady=20, padx=20, sticky='e')


    def jacket_string(self):
        self.vinyl_sentence = self.third_section.get_ai_response()

        if not self.vinyl_sentence:
            return

        self.clear()
        self.curr_info()

        damages_dict = self.second_section.get_selection()
        damages_content = ', '.join([f"{key}: {value}" for key, value in damages_dict.items()])
        print("Vinyl: " + str(damages_content))

        pattern = r"\((.*?)\)"
        self.vinyl_sentence = re.sub(pattern, damages_content, self.vinyl_sentence)

        print("Vinyl Sentence: " + str(self.vinyl_sentence))

        self.back_btn.configure(command=lambda:self.intros())
        self.next_btn.configure(command=lambda:self.to_ai_frame(), text="Generate AI")

        self.back_btn.grid(row=6, column=0, columnspan=1, pady=20, padx=20, sticky='w')
        self.next_btn.grid(row=6, column=4, columnspan=1, pady=20, padx=20, sticky='e')
        self.fourth_section.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky='nsew')

    def to_ai_frame(self):

        self.jacket_sentence = self.fourth_section.get_jacket_string()

        if not self.jacket_sentence:
            return
        
        self.next_btn.configure(state="disable")

        self.clear()
        self.curr_info()


        # find the radio button that was selected
        self.selected_intro.append(self.vinyl_sentence)
        self.selected_intro.append(self.jacket_sentence)

        self.back_btn.configure(command=lambda:self.intros())
        self.next_btn.configure(command=lambda:self.to_ai_frame(), text="Generate AI")

        self.back_btn.grid(row=6, column=0, columnspan=1, pady=20, padx=20, sticky='w')

        self.next_btn.grid(row=6, column=4, columnspan=1, pady=20, padx=20, sticky='e')

         #self.scroll_outros.grid_forget()
        self.next_btn.grid_forget()
        self.ai_desc()

    def ai_desc(self):
        self.ai_frame = ai.AI_Frame(self)
        self.master.title("AI DESCRIPTION")
        self.ai_frame.condition = self.cond
        self.ai_frame.intros_outros = self.selected_intro
        self.ai_frame.desc()
        self.next_btn = ctk.CTkButton(self, text="Save", command=lambda: self.save_damage_info, font=("Courier New Greek", 18))
        self.ai_frame.grid(row=3, column=0, columnspan=3, sticky='nsew', padx=10, pady=7)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.next_btn.grid(row=12, column=2, columnspan=1, pady=20, padx=20, sticky='e')

    def save_damage_info(self):
        self.data["Damages"] = str(self.second_section.get_selection()) + " - " + self.fourth_section.get_jacket_string()
        self.data["Qty"] = "Highlights"
        # save the damages dictionaries into the ["Damages"] column
        self.master.update_row(self.idx, self.data)
        self.curr_idx += 1
        if self.curr_idx >= len(self.indexes):
            self.master.start()
        else:
            self.idx = self.indexes[self.curr_idx]
            self.clear()
            self.display_info()
            self.start()


class Intros(ctk.CTkScrollableFrame):

    def __init__(self, master, curr_idx, xl_read, cond, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.xl_read = xl_read
        self.cond = cond
        self.master = master
        self.curr_idx = 0
        self.idx = curr_idx
        self.row = self.xl_read.loc[self.idx]       
        self.data = {}
        self.selected_intro = []        
        self.intro_opt = {
            "New" : [
                ["Vinyl is new, never been played in its original factory shrink-wrap."], 
                ["Vinyl is BRAND NEW in original factory shrink wrap."]
                ],
            "Very Good": [
                ["Vinyl appears new or unplayed, totally clean with its original brilliant shine."],
                ["Vinyl appears like-new or unplayed with its original factory shine.",
                "Vinyl appears like-new, unplayed & very clean with a glassy shine."],
                ["Vinyl appears like-new, possibly unplayed but no evidence of usage or wear. Maintains its original factory shine.",
                "Vinyl appears like-new, possibly unplayed, with (only subtle handling traces) but overall clean with its original factory shine."],
                ["Vinyl appears like-new, likely once-played with (very subtle handling traces), maintains its original factory shine.",
                "Vinyl appears like-new, likely once-played and carefully-handled but little evidence of usage or wear.",
                "Vinyl appears like-new, likely once-played, (faint and stray handling traces) but sustaining its original factory gloss."],
                ["Vinyl appears like-new, likely once or twice-played, with stray and faint handling traces, maintains its original factory shine.",
                "Vinyl appears like-new, likely once or twice-played, with (stray usage and handling traces), maintains its original factory shine."],
                ["Vinyl appears very minimally-played w/ (very faint handling traces), very clean with its original glossy shine.",
                "Vinyl appears very minimally-played w/ (very faint handling traces), very clean with a high shine.",
                "Vinyl appears very minimally-played w/ (very faint handling traces & storage blemishing), very clean overall."],
                ["Vinyl appears minimally-played with (very faint handling traces), very clean with a glassy shine.",
                "Vinyl appears minimally-played with (minor blemishing from storage), otherwise very clean."]
                ],
            "Good": [
                ["Vinyl appears like-new, likely once or twice-played but little evidence of usage or wear. Mostly clean with a brilliant shine.", 
                "Vinyl appears like-new, likely once-played with (stray usage & handling traces). Maintains its factory shine.", 
                "Vinyl appears like-new, likely once or twice-played with (scattered usage & handling traces). Maintains its factory shine."], 
                ["Vinyl appears minimally played with (light handling traces), otherwise clean and bright.", 
                "Vinyl appears minimally played with (very subtle usage & handling traces) while maintaining its original shine.", 
                "Vinyl appears minimally-played with (minor usage traces), retains its original brilliant shine.", 
                "Vinyl appears minimally-played, (faint & stray usage and handling traces), maintains its original factory shine.", 
                "Vinyl appears minimally-played, (faint & stray usage and handling traces), maintains its original glossy factory-shine.", 
                "Vinyl appears minimally-played with (faint but mild usage & handling traces), mostly clean & bright.", 
                "Vinyl appears minimally played with (light usage and handling traces), otherwise bright and clean.", 
                "Vinyl appears minimally-played, (faint & stray sleeve rubs and usage traces), retains its original factory shine."], 
                ["Vinyl appears minimally-played, (scattered usage & handling traces), maintains its original factory shine.", 
                "Vinyl appears minimally-played and carefully-handled with (very light handling-prints & sleeve-markings from storage), overall clean with a glossy-shine.", 
                "Vinyl appears minimally-played w/ (faint usage & handling markings), mostly clean & bright", 
                "Vinyl appears minimally-played w/ (faint usage & storage-related sleeve rubs), mostly clean & bright."], 
                ["Vinyl appears minimally-played with (scattered usage & handling traces), maintains most of its original factory shine.", 
                "Vinyl appears minimally-played with (mild storage markings) with its original glossy-shine.", 
                "Vinyl appears nominally-played with (mild usage-markings & handling-prints), retains its shiny-gloss.", 
                "Vinyl appears nominally-played with (mild handling-traces & usage-markings), retains its original shine.", 
                "Vinyl appears (mild usage-markings & handling-prints), overall appears minimally-played."], 
                ["Vinyl appears (mild sleeve-marks & a few usage & handling-markings), but free from excessive wear.", 
                "Vinyl appears (light surface-marks & handling-prints), overall appears carefully-played with its original shine.", 
                "Vinyl appears (minimally-played, stray and light handling & usage markings) while retaining its original factory shine.", 
                "Vinyl appears (light handling-prints & stray surface-blemishing), yet free from heavy wear from minimal play.", 
                "Vinyl appears (occasionally-played with stray usage & handling markings) but overall acceptable & respectable."]
                ],
            "Fairly Good": [
                ["Vinyl appears minimally played, (light and stray usage & handling traces), still maintains its original factory shine."], 
                ["Vinyl appears occasionally-played with (light, stray, typical handling traces), retains most of its original factory gloss.", 
                "Vinyl appears occasionally-played, (typical usage and handling traces), maintains some of its original factory shine.", 
                "Vinyl appears occasionally-played with (typical but faint usage traces), yet maintains its original factory shine.", 
                "Vinyl appears occasionally-played with (faint usage traces & handling prints), retains its original glossy-shine.", 
                "Vinyl appears occasionally-played, (stray, light, & typical usage traces), retains some of its original factory shine."], 
                ["Vinyl appears occasionally-played, with (light, scattered, and typical usage & handling traces), maintains some of its original factory shine.", 
                "Vinyl appears occasionally-played, with (stray and scattered usage traces), maintains its original factory shine.", 
                "Vinyl appears occasionally-played, with (mild and typical usage traces), yet retains some of its original glassy factory finish.", 
                "Vinyl appears occasionally-played, with (scattered, typical handling traces), retains most of its original factory gloss."], 
                ["Vinyl appears occasionally-played, (mild, typical, and scattered usage and handling traces), still retains some of its original factory shine.", 
                "Vinyl appears occasionally-played, (mild and scattered handling traces), maintains its original factory shine.", 
                "Vinyl appears occasionally-played, (mild, typical, and scattered usage & handling traces), yet retains some of its original glassy factory finish."], 
                ["Vinyl appears moderately-played with (faint usage & handling blemishing), remains respectable.", 
                "Vinyl appears moderately-played with (faint markings & handling blemishes), retains some shine.", 
                "Vinyl appears moderately-played with (faint usage markings, handling blemishes), retains some shine, overall respectable.",  
                "Vinyl appear moderately-played with (faint usage markings and handling blemishes), overall respectable."], 
                ["Vinyl appears moderately-played with (faint hairlines, markings & handling blemishes), retains some shine.", 
                "Vinyl appears moderately-played with (faint hairline-type wear and usage markings), overall respectable.", 
                "Vinyl appears moderately-played with (scattered, stray markings & hairlines), but overall respectable.", 
                "Vinyl appears moderately-played (scattered usage & handling markings).  Remains respectable for playback.", 
                "Vinyl appears moderately-played, with (scattered usage & handling markings and stray and hairlines) visible with a close up view."], 
                ["Vinyl appears moderately-played with (mild usage & handling markings, namely hairline-type wear), remains respectable for playback.", 
                "Vinyl appears moderately-played (scattered usage & markings).  Remains respectable for playback.", 
                "Vinyl appears moderately-played, (mild usage blemishes, mostly handling blemishes), still maintains most of its original factory brilliance."], 
                ["Vinyl appears moderately-played, (scattered usage and handling traces, typical hairlines), retains some of its original factory glossy finish.", 
                "Vinyl appears moderately-played, (mild and typical handling markings), yet retains some of its original factory shine.", 
                "Vinyl appears moderately-played, (typical and light usage traces, light hairlines), retains some of its original factory shine."], 
                ["Vinyl appears regularly-played with (typical usage & handling markings) but overall respectable."]
                ],
            "Fair": [
                ["Vinyl appears minimally-played with (mild handling traces & storage-related sleeve rub blemishing).",
                "Vinyl appears minimally-played with (stray, careless scuffing markings)."], 
                ["Vinyl appears frequently-played, with stray usage and handling traces), retains some of its factory shine.", 
                "Vinyl appears frequently-played with (light but faint hairline-type wear).  Remains respectable for playback.",   
                "Vinyl appears frequently-played with (multiple hairlines and handling prints).", 
                "Vinyl appears frequently-played with (scattered usage & handling blemishes and surface markings.",
                "Vinyl appears frequently-played with, (mild usage & handling markings and hairline-type wear).",
                "Vinyl appears frequently-played with (faint, scattered scuffs & other markings, otherwise acceptable for playback."],
                [
                "Vinyl appears regularly-played with (visible hairline-wear and handling traces).",
                "Vinyl appears regularly-played with (scattered hairline-type wear), otherwise respectable for playback.",
                "Vinyl appears regularly-played with (faint scattered markings, usage traces, & handling blemishes).",
                "Vinyl appears regularly-played, (scattered usage & handling traces, mild sleeve rub blemishing), otherwise retains most of its original shine.",
                "Vinyl appears regularly-played with (scattered scuffing, hairlines and usage markings), but remains respectable for playback.",
                "Vinyl appears regularly-played with (scattered usage & handling markings). Remains respectable for playback.",
                "Vinyl appears regularly-played with (noticeable scuffs and marks), but remains respectable for playback.",
                "Vinyl appears regularly played has (multiple, visible usage marks), but remains respectable for playback.",
                "Vinyl appears regularly-played with (notable handling & usage traces and scattered surface markings) but acceptable for playback.",
                "Vinyl appears regularly-played with (hairline-type wear and scattered scuffing from usage and handling). Respectable for playback.",
                "Vinyl appears regularly played with (namely hairline-type wear and scattered usage markings). Vinyl is respectable but playback.",
                "Vinyl appears regularly-played with (heavy, noticeable scuffing and other marks), but remains respectable for playback.",
                "Vinyl Appears regularly-played with (scattered marks, prints and mild groove wear), yet retains some of its original gloss.",
                "Vinyl Appears regularly-played with (scuffing and heavy wear) but still acceptable for playback."
                ],
                ["Vinyl appears heavily played with (handling prints and minor scuffing marks).",
                "Vinyl appears heavily-played with (scattered usage & handling markings, namely hairline-type wear). Remains respectable for playback.",
                "Vinyl appears heavily-played with (scattered surface scuffs from careless handling). Remains respectable for playback.",
                "Vinyl appears heavily played with (multiple surface markings) and light wear from typical usage, remains acceptable for playback.",
                "Vinyl appears heavily-played with (numerous hairlines and few scuffing marks).",
                "Vinyl appears heavily-played with (scattered hairlines & usage markings but overall acceptable).",
                "Vinyl appears heavily played with (mild groove-wear, surface-marks & prints), remains acceptable.",
                "Vinyl appears heavily-played with (multiple scuffing marks and other blemishes).",
                "Vinyl appears heavily-played and well worn with (multiple scuff marks), but still playable.",
                "Vinyl appears heavily played with (scattered usage markings) throughout. Remains acceptable for playback.",
                "Vinyl appears heavily played with (heavy groove wear and usage markings).",
                "Vinyl appears heavily-played wear with (scattered surface markings & blemishes), remains acceptable for playback.",
                "Vinyl appears heavily played with (heavy groove-wear with significant surface-marks), remains acceptable for playback",
                "Vinyl appears heavily played with significant marks and wear, noisy playback can be expected.",
                "Vinyl appears heavily played with (multiple surface marks) & groove wear from generous usage, noisy playback can be expected."
                ]
                ]
        }

        self.start()

        self.configure()

        self.configure(height=400, width=600)
 
    def start(self):

        self.intro_var = ctk.StringVar(value=None)

        i = 1
        letter = 0
        ascii_A = ord('A') 
        for sentences in self.intro_opt[self.cond]:
            label_letter = chr(ascii_A + letter)
            ctk.CTkLabel(self, text=label_letter, font=("Courier New Greek", 20)).grid(row=i, column=0, pady=1, padx=10, sticky='nsew')
            letter += 1
            i += 1

            for line in sentences:
                rdio = ctk.CTkRadioButton(self, text=line, variable=self.intro_var, value=line, font=("Courier New Greek", 16))
                rdio.grid(row=i, column=1, pady=5, padx=10, sticky='nsew')
                i += 1
            ctk.CTkLabel(self, text="").grid(row=i, column=0, pady=1, padx=10, sticky='nsew')
            i += 1

    def get_ai_response(self):
        return self.intro_var.get()
    
    
    def clear(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        self.display_info()
