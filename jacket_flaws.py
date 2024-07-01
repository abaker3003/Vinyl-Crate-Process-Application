from tkinter import ttk
import customtkinter as ctk
import enter_measurement as em


class Jacket_Flaws(ctk.CTkFrame):

    def __init__(self, master, *args,**kwargs):

        super().__init__(master, *args, **kwargs)

        self.selected_flaws = []

        self.flaws_cnt = 0
        self.sentence_cnt = 0

        self.selected_flaws_sentences = []

        self.checkboxes = []

        self.flaw_vars = {}

        self.flaw_dict = {}

        self.master = master

        self.display_flaws()

    def display_flaws(self):
        self.general_dict = {
            "like new": "is",
            "excellent": "is",
            "minimal wear": "has",
            "moderate wear": "has",
            "worn": "is",
            "well worn": "is",
            "heavily worn": "is",
            "fragile": "is"
        }

        # Jacket Label
        ctk.CTkLabel(self, text="Jacket Flaws / Severity", font=("Lucida Sans", 25)).grid(row=0, column=0, columnspan=6, sticky='nsew')

        ctk.CTkLabel(self, text="Choose Up To 3", font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')

        self.general_frame = ctk.CTkTabview(self, width=200, height=475)
        self.general_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

        self.general_frame.add("General")
        ctk.CTkLabel(self.general_frame.tab("General"), text="GENERAL", width=200, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="nsew")


        self.general_var = ctk.StringVar()

        for i, general in enumerate(self.general_dict.keys()):
            self.general_frame.columnconfigure(0, minsize=1, pad=0)
            # radiobuttons 
            ctk.CTkRadioButton(self.general_frame.tab("General"), text=general, variable=self.general_var, value=self.general_dict.get(general) + " " + general, font=("Lucida Sans", 14)).grid(row=i + 2, column=0, sticky='nsew', padx=10, pady=10)



        self.sections_tab = ctk.CTkTabview(self, width=500, height=475)
        self.sections_tab.grid(row=3, column=1, columnspan=4, sticky='nsew', padx=10, pady=10)


        ## --->> MAIN <<--- ##
        self.sections_tab.add("Main")
        ctk.CTkLabel(self.sections_tab.tab("Main"), text="MAIN", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="nsew")

        self.main_dict = {
            "shelf wear": {
                "has": [
                    "light", "slight", "noticeable", "minimal", "generalized", "mild", "moderate", "typical", "pronounced", "heavy", "significant"
                ]
            },
            "ring wear": { 
                "has": [
                    "light", "slight", "noticeable", "minimal", "generalized", "mild", "moderate", "typical", "pronounced", "heavy", "significant"
                ]
            }
        }

        for i, (flaw, sevrty) in enumerate(self.main_dict.items()):
            self.flaw_vars[flaw] = ctk.StringVar()
            var = self.flaw_vars[flaw]
            first_word = list(sevrty.keys())[0]
            svrty = sevrty.get(first_word)
            #print(flaw)
            flaw_box = ctk.CTkCheckBox(self.sections_tab.tab("Main"), text=flaw, onvalue=flaw, variable=var, offvalue="None", width=2, height=1, font=("Lucida Sans", 14))
            self.checkboxes.append(flaw_box)
            flaw_box.grid(row=i + 2, column=0, sticky='nsew', padx=10, pady=10)
            flaw_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, svrty=svrty, first_word=first_word: self.toggle_severity_selection(event, svrty, flaw, var, first_word))


    ## --->> ORIGINAL <<--- ##
        self.sections_tab.add("Original")
        ctk.CTkLabel(self.sections_tab.tab("Original"), text="ORIGINAL", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="nsew")
    
        self.orig_dict = [
            [
                ["original factory shrink-wrap", "has"]
            ],
            [
                ["saw cut", "has"],
                ["cut corner", "has"],
                ["drill hole", "has"],
                ["hole-punch", "has"],
                ["slightly bowed", "is"]
            ],
            [
                ["promotional hole punch", "has"],
                ["promotional gold stamp", "has"],
                ["promotional stamp", "has"],
                ["promotional sticker", "has"],
                ["promotional hype-sticker", "has"]
            ]
        ]

        for j, section in enumerate(self.orig_dict):
            for i, flaws in enumerate(section):
                flaw_name = flaws[0]
                self.flaw_vars[flaw_name] = ctk.StringVar()
                var = self.flaw_vars[flaw_name]
                flaw_box = ctk.CTkCheckBox(self.sections_tab.tab("Original"), text=flaw_name, onvalue=flaw_name, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                flaw_box.grid(row=i + 2, column=j, sticky='nsew', padx=10, pady=10)
                flaw_box.bind("<Button-1>", lambda event, flaw_name=flaw_name, flaw_details=flaws[1], var=var: self.add_to_list(event,  flaw_details, flaw_name, var))
                self.checkboxes.append(flaw_box)


    ## --->> FLAW A <<--- ##
        self.sections_tab.add("Flaw A")
        ctk.CTkLabel(self.sections_tab.tab("Flaw A"), text="FLAW A", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="nsew")

        self.flaw_a_dict= [
            {"frayed": {
                "is": [
                        "mildly", "moderately", "heavily", "lightly"
                ]
            }},
            {"fraying": {
                "has": [
                    "light", "slight", "mild", "heavy", "significant", "severe"
                ]
            }},
            {"crease": {
                "has": [
                    "subtle", "faint", "tiny", "small", "light", "noticeable", "mild", "moderate", "large", "significant"
                ]
            }},
            {"creases": {
                "has": [
                    "subtle", "faint", "stray", "tiny", "small", "light", "minor", "noticeable", "occasional", "scattered", "mild", "large", "heavy", "significant", "considerable"
                ]
            }},
            {"creasing": {
                "has": [
                    "faint", "stray", "tiny", "small", "light", "minor", "noticeable", "occasional", "scattered", "mild", "moderate", "pronounced", "heavy", "significant", "considerable"
                ]
            }},
            {"creased": {
                "is": [
                    "mildly", "heavily", "lightly"
                ]
            }},
            {"tear": {
                "has": [
                    "tiny", "small", "minor", "noticeable", "mild", "visible", "large" "significant"
                ]
            }},
            {"tears": {
                "has": [
                    "tiny", "small", "minor", "noticeable", "scattered", "mild", "multiple", "pronounced", "large", "significant", "considerable"
                ]
            }},
            {"torn": {
                "is": [
                    "mildly" "heavily"
                ]
            }},
            ["partially-torn", "is"],
            {"cracked": {
                "is": [
                    "light", "noticeable", "mildly", "heavily"
                ]
            }},
            {"scrape": {
                "has": [
                    "faint", "insignificant", "tiny", "small", "light", "minor", "slight", "noticeable", "occasional", "mild", "visible", "pronounced", "large", "heavy", "significant", "considerable", "severe"
                ]
            }},
            {"scrapes": {
                "has": [
                    "faint", "stray", "tiny", "small", "light", "minor", "slight", "noticeable", "occasional", "mild", "multiple", "visible", "pronounced", "large", "heavy", "significant", "considerable" "severe"
                ]
            }},
            {"scraping": {
                "has": [
                    "stray", "small", "light", "minor", "slight", "occasional", "scattered", "mild", "visible", "pronounced", "heavy", "significant", "considerable"
                ]
            }},
            {"stain": {
                "has": [
                    "subtle", "faint", "insignificant", "tiny", "small", "light", "minor", "obvious", "noticeable", "occasional", "mild", "visible", "pronounced", "large", "heavy", "significant", "considerable"
                ]
            }},
            {"stained": {
                "has": [
                    "mildly", "heavily", "slightly"
                ]
            }},
            {"staining": {
                "has": [
                    "subtle", "faint", "stray", "tiny", "isolated", "light", "minor", "obvious", "noticeable", "occasional", "generalized", "scattered", "mild", "moderate", "visible", "pronounced", "significant", "considerable"
                ]
            }},
            {"wrinkled": {
                "has": [
                    "mildly", "moderately", "heavily", "lightly", "slightly"
                ]
            }},
            {"faded": {
                "has": [
                    "mildly", "moderately", "heavily", "lightly", "slightly"
                ]
            }},
            {"fading": {
                "has": [
                    "subtle", "minor", "slight", "obvious", "noticeable", "generalized", "mild", "heavy", "significant"
                ]
            }},
            {"age-related fading": {
                "has": [
                    "subtle", "minor", "slight", "obvious", "noticeable", "generalized", "mild", "heavy", "significant"
                ]
            }},
            {"yellowed": {
                "has": [
                    "mildly", "moderately", "heavily", "lightly", "slightly"
                ]
            }},
            {"yellowed from age": {
                "has": [
                    "mildly", "moderately", "heavily", "lightly", "slightly"
                ]
            }},
            {"age-related yellowing": {
                "has": [
                    "subtle", "faint", "light", "minor", "noticeable", "generalized", "mildly", "heavy", "significant"
                ]
            }},
            {"discolored": {
                "has": [
                    "mildly", "heavily", "lightly", "slightly"
                ]
            }},
            {"discoloration": {
                "has": [
                    "subtle", "faint", "minor", "slight", "noticeable", "generalized", "mild", "visible", "heavy", "significant"
                ]
            }},
            {"bowed": {
                "has": [
                    "mildly", "heavily", "lightly", "slightly"
                ]
            }},
            ["slightly bowed", "has"]
        ]

        add_col = 0
        sub_row = 0

        for i, section in enumerate(self.flaw_a_dict):
            if i != 0 and i % 11 == 0:
                add_col += 1
                sub_row -= 11
            if isinstance(section, list):
                flaw_name = section[0]
                #print(flaw_name)
                self.flaw_vars[flaw_name] = ctk.StringVar()
                var = self.flaw_vars[flaw_name]
                flaw_box = ctk.CTkCheckBox(self.sections_tab.tab("Flaw A"), text=flaw_name, onvalue=flaw_name, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                flaw_box.grid(row=i + 2 + sub_row, column=0 + add_col, sticky='nsew', padx=10, pady=10)
                flaw_box.columnconfigure(0 + add_col, minsize=1, pad=0)

                flaw_box.bind("<Button-1>", lambda event, flaw_name=flaw_name, flaw_details=section[1], var=var: self.add_to_list(event,  flaw_details, flaw_name, var))
                self.checkboxes.append(flaw_box)

            else:
                flaw = list(section.keys())[0]
                details = list(section.values())[0]
                #print("ELSE!! Flaw: " + flaw + "\tDetails: " + str(details))
                first_word = list(details.keys())[0]
                svrty = details[first_word]
                #print(flaw)
                self.flaw_vars[flaw] = ctk.StringVar()
                var = self.flaw_vars[flaw]
                self.sections_tab.columnconfigure(0, minsize=1, pad=0)
                flaw_a_box = ctk.CTkCheckBox(self.sections_tab.tab("Flaw A"), text=flaw, onvalue=flaw, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                self.checkboxes.append(flaw_a_box)
                flaw_a_box.grid(row=i + 2 + sub_row, column=0 + add_col, sticky='nsew', padx=10, pady=10)
                flaw_box.columnconfigure(0 + add_col, minsize=1, pad=0)

                #print("first_word: " + first_word + "\t" + "svrty: " + str(svrty))

                if len(svrty) > 0:
                    flaw_a_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, first_word=first_word, severity=svrty: self.toggle_severity_selection(event, severity, flaw, var, first_word))
                else:
                    flaw_a_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, first_word=first_word: self.toggle_severity_selection_toplevel(event, flaw, var, first_word))


    ## --->> FLAW B <<--- ##
        self.sections_tab.add("Flaw B")
        ctk.CTkLabel(self.sections_tab.tab("Flaw B"), text="FLAW B", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="nsew")


        self.flaw_b_dict = [
            [
                [
                "stick-on label", "has a"
                ],
                [
                "label adhered to cover", "has a"
                ]
            ],
            [
                [
                "adhesive residue", "has"
                ],
                [
                "sticker peel blemish", "has"
                ],
                ["sticker peel damage", "has"
                ]
            ],
            [
                ["tape repair", "has"],
                ["repaired with tape","is"],
                ["tape reinforced", "is"],
                ["taped reinforced seams", "has"],
                ["seams reinforced with tape", "has"]
            ]
        ]

        for j, section in enumerate(self.flaw_b_dict):
            for i, flaws in enumerate(section):
                flaw_name = flaws[0]
                self.flaw_vars[flaw_name] = ctk.StringVar()
                var = self.flaw_vars[flaw_name]
                flaw_box = ctk.CTkCheckBox(self.sections_tab.tab("Flaw B"), text=flaw_name, onvalue=flaw_name, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                flaw_box.grid(row=i + 2, column=j, sticky='nsew', padx=10, pady=10)
                flaw_box.bind("<Button-1>", lambda event, flaw_name=flaw_name, flaw_details=flaws[1], var=var: self.add_to_list(event,  flaw_details, flaw_name, var))
                self.checkboxes.append(flaw_box)


    ## --->> FLAW C <<--- ##
        self.sections_tab.add("Flaw C")
        ctk.CTkLabel(self.sections_tab.tab("Flaw C"), text="FLAW C", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="nsew")

        self.flaw_c_dict = [
            [
                {"writing on cover": {
                    "has": [
                        "faint", "insignificant", "tiny", "light", "minor", "obvious", "noticeable", "sporatic", "scattered", "mild", "visible", "pronounced", "heavy", "significant", "considerable"]
                }},
                {"writing on rear cover": {
                    "has": [
                        "faint", "insignificant", "tiny", "light", "minor", "obvious", "noticeable", "sporatic", "scattered", "mild", "visible", "pronounced", "heavy", "significant", "considerable"
                    ]
                }},
                {"writing on front & rear": {
                    "has": [
                        "faint", "insignificant", "tiny", "light", "minor", "obvious", "noticeable", "sporatic", "scattered", "mild", "visible", "pronounced", "significant", "considerable"
                    ]
                }},
                {"ink stamp": {
                    "has": [
                        "faint", "tiny", "small", "light", "mild", "visible", "large"
                    ]
                }},
                {"ink notations": {
                    "has": [
                        "faint", "stray", "tiny", "small", "isolated", "light", "minor", "noticeable", "scattered", "mild", "multiple", "visible", "pronounced", "large", "heavy", "significant", "considerable"
                    ]
                }},
                {"owner ID in pen": {
                    "has": [
                        "faint", "small", "light", "obvious", "noticeable", "mild", "visible", "pronounced"
                    ]
                }},
                {"owner ID in sharpie": {
                    "has": [
                        "small", "light", "obvious", "noticeable", "mild", "visible", "pronounced"
                    ]
                }}
            ],
            [
                {"evidence of moisture exposure": {
                    "has": [
                        "faint", "stray", "isolated", "light", "minor", "obvious", "noticeable", "generalized", "scattered", "mild", "moderate", "typical", "visible", "pronounced", "heavy", "significant", "considerable", "severe"
                    ]
                }},
                {"staining from moisture exposure": {
                    "has": [
                        "faint", "stray", "isolated", "light", "minor", "obvious", "noticeable", "generalized", "scattered", "mild", "moderate", "typical", "visible", "pronounced", "heavy", "significant", "considerable", "severe"
                    ]
                }},
                {"water marks": {
                    "has": [
                        "faint", "isolated", "light", "minor", "noticeable", "scattered", "mild", "visible",  "heavy", "significant", "considerable"
                    ]
                }},
                {"moisture staining": {
                    "has": [
                        "faint", "isolated", "light", "minor", "obvious", "noticeable", "occasional", "generalized", "scattered", "mild", "moderate", "typical", "visible", "pronounced", "heavy", "significant", "considerable", "severe"
                    ]
                }},
                {"water damage": {
                    "has": [
                        "subtle", "faint", "fragile", "insignificant", "stray", "tiny", "small", "isolated", "light", "minor", "slight", "obvious", "noticeable", "few", "minimal", "minimally", "occasional", "average", "general", "generalized", "sporatic", "scattered", "mild", "mildly", "moderate", "moderately", "multiple", "storage-related", "normal", "typical", "visible", "pronounced", "large", "heavy", "heavily", "significant", "considerable", "feelable", "excessive", "severe"
                    ]
                }},
                {"wrinkling from moisture exposure": {
                    "has": [
                        "subtle", "faint", "stray", "tiny", "isolated", "light", "minor", "slight", "obvious", "noticeable", "generalized", "sporatic", "scattered", "mild", "moderate", "typical", "visible", "pronounced", "heavy", "significant", "considerable", "severe"
                    ]
                }},
                {"fused scraping damage from moisture": {
                    "has": [
                        "small", "light", "minor", "noticeable", "generalized", "sporatic", "mild", "moderate", "visible", "heavy", "significant"
                    ]
                }},
                {"sticker peel residue": {
                    "has": [
                        "light", "mild", "heavy"
                    ]
                }}
            ],
            [
                {"mold": {
                    "has" : [
                        "light", "noticable", "scattered", "visible"
                    ]
                }},
                {"moldy": {
                    "is" : [
                        "slightly", "lightly", "mildly", "moderately", "heavily"
                    ]
                }}
            ]
        ]

        for i, section in enumerate(self.flaw_c_dict):

            for j, part in enumerate(section):

                flaw = list(part.items())[0][0]
                details = list(part.items())[0][1]
                #print("ELSE!! Flaw: " + flaw + "\tDetails: " + str(details))
                first_word = list(details.items())[0][0]
                svrty = list(details.items())[0][1]
                #print(flaw)
                self.flaw_vars[flaw] = ctk.StringVar()
                var = self.flaw_vars[flaw]
                self.sections_tab.columnconfigure(0, minsize=1, pad=0)
                flaw_a_box = ctk.CTkCheckBox(self.sections_tab.tab("Flaw C"), text=flaw, onvalue=flaw, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                self.checkboxes.append(flaw_a_box)
                flaw_a_box.grid(row= j + 2, column=i, sticky='nsew', padx=10, pady=10)
                flaw_box.columnconfigure(0 + add_col, minsize=1, pad=0)
                flaw_a_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, svrty=svrty, first_word=first_word: self.toggle_severity_selection(event, svrty, flaw, var, first_word))


    ## --->> SPINE <<--- ##
        self.sections_tab.add("Spine")
        ctk.CTkLabel(self.sections_tab.tab("Spine"), text="SPINE", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="nsew")

        self.spine_dict = [
            [
                {"spine-wear":  {
                    "has": [
                        "light", "slight", "noticeable", "minimal", "generalized", "mild", "moderate", "typical", "pronounced", "heavy", "significant", "considerable"
                    ]
                }},
                {"spine split":  {
                    "has": [
                        "tiny", "small", "large", "partial", "totally"
                    ]
                }},
                {"partial spine split": {
                    "has": []
                }},
                {"partially split spine": {
                    "has": []
                }}
            ],
            [
                {"spine & seam flaking": {
                    "has": [
                        "stray", "light", "minor", "slight", "obvious", "noticeable", "generalized", "mild", "typical", "heavy", "considerable"
                    ]
                }},
                {"flaking wear along spine ": {
                    "has": [
                        "light", "slight", "typical"
                    ]
                }},
                {"flaking along spine & seams": {
                    "has": [
                        "light", "minor", "slight", "noticeable", "occasional", "generalized", "sporatic", "scattered", "mild", "moderate", "typical", "visible", "pronounced", "heavy", "significant", "considerable", "excessive", "severe"
                    ]
                }}
            ],
            [
                {"cracked spine": {
                    "has": []
                }},
                {"crack along spine": {
                    "has": []
                }},
                {"cracking along spine": {
                    "has": [
                    "light", "slight", "generalized", "mild", "moderate" "pronounced", "heavy", "significant", "considerable", "severe"
                ]
                }}
            ]
        ]
        
        for i, section in enumerate(self.spine_dict):

            for j, part in enumerate(section):

                flaw = list(part.items())[0][0]
                details = list(part.items())[0][1]
                #print("ELSE!! Flaw: " + flaw + "\tDetails: " + str(details))
                first_word = list(details.items())[0][0]
                svrty = list(details.items())[0][1]
                #print(flaw)
                self.flaw_vars[flaw] = ctk.StringVar()
                var = self.flaw_vars[flaw]
                self.sections_tab.columnconfigure(0, minsize=1, pad=0)
                flaw_a_box = ctk.CTkCheckBox(self.sections_tab.tab("Spine"), text=flaw, onvalue=flaw, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                self.checkboxes.append(flaw_a_box)
                flaw_a_box.grid(row=i + 2, column=j, sticky='nsew', padx=10, pady=10)
                flaw_box.columnconfigure(0 + add_col, minsize=1, pad=0)
                if len(svrty) > 0:
                    flaw_a_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, svrty=svrty, first_word=first_word: self.toggle_severity_selection(event, svrty, flaw, var, first_word))
                else:
                    flaw_a_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, first_word=first_word: self.toggle_severity_selection_toplevel(event, flaw, var, first_word))


    ## --->> CORNERS <<--- ##
        self.sections_tab.add("Corners")
        ctk.CTkLabel(self.sections_tab.tab("Corners"), text="CORNERS", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 4, sticky="nsew")

        self.corners_dict = [
            {"corner wear": {
                "has": [
                    "light", "minor", "noticeable", "minimal", "generalized", "mild", "moderate", "pronounced", "heavy", "significant", "considerable", "severe"
                ]
            }},
            {"bent corner": {
                "has": [
                    "stray", "minor", "slight", "mild", "pronounced", "significant"
                ]
            }},
            {"bent corners": {
                "has": [
                    "small", "minor", "slight", "noticeable", "minimal", "mild" "pronounced", "significant"
                ]
            }},
            {"corner dents": {
                "has": [
                    "tiny", "small", "light", "minor", "slight", "noticeable", "minimal", "generalized", "mild", "typical", "pronounced", "heavy", "significant"
                ]
            }},
            {"dented corners": {
                "has": [
                    "tiny", "small", "light" "slight", "slightly", "noticeable", "minimal", "generalized", "mildly", "typical", "pronounced", "heavy", "significant"
                ]
            }},
            {"creased corner": {
                "has": [
                    "faint", "insignificant", "tiny", "small", "light", "slight", "obvious", "noticeable", "minimally", "mildly", "heavily"
                ]
            }},
            {"creased corners": {
                "has": [
                    "tiny", "small", "light", "slight", "noticeable", "minimally", "mildly", "heavily"
                ]
            }},
            {"cut corner": {
                "has" : [
                ]
            }}
        ]

        for i, section in enumerate(self.corners_dict):
            flaw = list(section.keys())[0]
            details = list(section.values())[0]
            #print("ELSE!! Flaw: " + flaw + "\tDetails: " + str(details))
            first_word = list(details.keys())[0]
            svrty = details[first_word]
            #print(flaw)
            self.flaw_vars[flaw] = ctk.StringVar()
            var = self.flaw_vars[flaw]
            self.sections_tab.columnconfigure(0, minsize=1, pad=0)
            flaw_a_box = ctk.CTkCheckBox(self.sections_tab.tab("Corners"), text=flaw, onvalue=flaw, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
            self.checkboxes.append(flaw_a_box)
            flaw_a_box.grid(row=i + 2, column=0, sticky='nsew', padx=10, pady=10)
            flaw_box.columnconfigure(0 + add_col, minsize=1, pad=0)
            #print("first_word: " + first_word + "\t" + "svrty: " + str(svrty))
            if len(svrty) > 0:
                flaw_a_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, severity=svrty, first_word=first_word: self.toggle_severity_selection(event, severity, flaw, var, first_word))
            else:
                flaw_a_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, first_word=first_word: self.toggle_severity_selection_toplevel(event, flaw, var, first_word))

        self.sections_tab.add("Seams")
        ctk.CTkLabel(self.sections_tab.tab("Seams"), text="SEAMS", width=500, font=("Lucida Sans", 18)).grid(row=1, column=0, columnspan = 3, sticky="e")

        self.seams_dict = [
            [
                {
                    "unglued seams": {
                        "has": [
                        ]
                    }
                },
                {
                    "cracking along seams": {
                        "has": [
                            "light", "noticeable", "occasional", "generalized", "scattered", "mild", "heavy", "significant", "considerable", "severe"
                        ]
                    }
                },
                {
                    "flaking along seams": {
                        "has": [
                            "faint", "stray", "tiny" "isolated", "light", "noticeable", "generalized", "scattered", "mild", "moderate", "significant", "considerable"
                            ]
                    }
                },
                [
                    "seams totally split", "has"
                ]
            ],
            [
                {
                    "flaking wear": {
                        "has": [
                            "light", "minor", "generalized", "scattered", "mild", "moderate", "typical", "significant", "considerable", "severe"
                        ]
                    }
                },
                {    "flaking wear along both seams": {
                        "has": [
                            "light", "noticeable", "mild", "heavy"
                        ]
                    }
                },
                {    "flaking along top seam": {
                        "has": [
                            "light", "noticeable", "scattered", "mild", "heavy"
                        ]
                    }
                },
                {    "flaking along bottom seam": {
                        "has": [
                            "light", "minor",  "noticeable", "scattered", "mild"
                        ]
                    }
                },
                {   "seam & spine flaking": {
                        "has": [
                            "light", "minor",  "noticeable", "scattered", "mild"
                        ]
                    }
                }
            ],
            [
                [
                    "top seam split", "has a"
                ],
                {
                    "partial-split on top seam": {
                        "has a": [
                        ]
                    }
                },
                {
                    "partially-split top seam": {
                        "has a": [
                        ]
                    }
                },
                [
                "unglued top seam", "has"],
                {
                    "crack on top seam": {
                        "has a": [
                        ]
                    }
                },
                [
                "small crack on top seam", "has a"
                ],
                [
                "totally split top seam", "has a"
                ]
            ],
            [
                [
                "bottom seam split", "has"
                ],
                [
                "partial split on bottom seam", "has"
                ],
                [
                "partially-split bottom seam", "has"
                ],
                {    
                    "crack on the bottom seam": {
                        "has": [
                            "small", "minor", "large"
                        ]
                    }
                },
                [
                "small crack on bottom seam", "has"
                ],
                [
                "totally split bottom seam", "has"
                ],
                [
                "totally split top & bottom seems", "has"
                ]
            ],
            [
                [
                "top & bottom seam splits", "has"
                ],
                [
                "top & bottom unglued seams", "has"
                ]
            ]
        ]



        for i, section in enumerate(self.seams_dict):
            add = 0
            for j, parts in enumerate(section):
                if isinstance(parts, list):
                    flaw_name = parts[0]
                    print(flaw_name, end=" ")
                    if flaw_name.startswith("top & bottom"):
                        i = 0
                        add = 6
                    self.flaw_vars[flaw_name] = ctk.StringVar()
                    var = self.flaw_vars[flaw_name]
                    flaw_box = ctk.CTkCheckBox(self.sections_tab.tab("Seams"), text=flaw_name, onvalue=flaw_name, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                    flaw_box.grid(row=j + 4 + add, column=i, sticky='nsew', padx=10, pady=10)
                    print(" - ROW: " + str(j + 4 + add) + "COL: " + str(i))
                    flaw_box.bind("<Button-1>", lambda event, flaw_name=flaw_name, flaw_details=parts[1], var=var: self.add_to_list(event,  flaw_details, flaw_name, var))
                    self.checkboxes.append(flaw_box)
                else:
                    flaw = list(parts.items())[0][0]
                    print(flaw, end=" ")
                    details = list(parts.items())[0][1]
                    if isinstance(details, dict):
                        first_word = list(details.keys())[0]
                        svrty = list(details.values())[0]
                        self.flaw_vars[flaw] = ctk.StringVar()
                        var = self.flaw_vars[flaw]
                        seams_box = ctk.CTkCheckBox(self.sections_tab.tab("Seams"), text=flaw, onvalue=flaw, offvalue="None", width=2, height=1, font=("Lucida Sans", 14), variable=var)
                        self.checkboxes.append(seams_box)
                        seams_box.grid(row=j + 4, column=i, sticky='nsew', padx=10, pady=10)
                        print(" - ROW: " + str(j + 4) + "COL: " + str(i))
                        if len(svrty) > 0:
                            seams_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, svrty=svrty, first_word=first_word: self.toggle_severity_selection(event, svrty, flaw, var, first_word))
                        else:
                            seams_box.bind("<Button-1>", lambda event, flaw=flaw, var=var, first_word=first_word: self.toggle_severity_selection_toplevel(event, flaw, var, first_word))


    ## --->> OTHERWISE <<-- ##
        self.otherwise_frame = ctk.CTkTabview(self, width=200, height=475)
        self.otherwise_frame.grid(row=3, column=5, sticky='nsew', padx=10, pady=10)

        self.otherwise_frame.add("Otherwise")
        ctk.CTkLabel(self.otherwise_frame.tab("Otherwise"), text="OTHERWISE", width=200, font=("Lucida Sans", 18)).grid(row=1, column=0, sticky="ew")
        
        self.otherwise_frame.columnconfigure(0, minsize=1, pad=0)

        self.otherwise_list = [
            "jacket is clean & solid.",
            "jacket is clean.",
            "jacket is in excellent condition.",
            "jacket is in good, clean, acceptable condition." ,
            "jacket is in good, clean, respectable condition." ,
            "jacket is in good condition.",
            "jacket is in respectable condition.",
            "jacket is in acceptable condition."
        ]

        self.otherwise_var = ctk.StringVar()

        for i, last in enumerate(self.otherwise_list):
            ctk.CTkRadioButton(self.otherwise_frame.tab("Otherwise"), text=last, variable=self.otherwise_var, value=", otherwise " + last, font=("Lucida Sans", 14)).grid(row=i + 2, column=0, sticky='nsew', padx=10, pady=10)

        generate_btn = ctk.CTkButton(self, text="GENERATE", command=lambda: self.verify_selected_options())
        generate_btn.grid(row=4, column=0, columnspan=6)
        self.sentence_display = ctk.CTkLabel(self, text="", font=("Courier New Greek", 16))
        self.sentence_display.grid(row=5, column=0, columnspan=6, sticky="nsew")

    def verify_selected_options(self):

        current_sentences = self.selected_flaws_sentences.copy()

        if self.general_var.get() and self.otherwise_var.get() and len(self.selected_flaws) != 0:
            self.jacket_string = "Jacket " + self.general_var.get()
            
            if current_sentences[0] == "original factory shrink-wrap":
                self.jacket_string +=" in " + current_sentences.pop(0)
                
            else: 
                self.jacket_string += " with " + current_sentences.pop(0)

            if len(current_sentences) == 1:
                self.jacket_string += " and " + current_sentences[0]
            elif len(current_sentences) == 2:
                self.jacket_string += ", " + current_sentences[0] + " and " + current_sentences[1]

            self.jacket_string += self.otherwise_var.get()
            self.display_sentence()
    
        else:
            self.display_sentence("Need to select BOTH general and otherwise AS WELL AS up to 3 flaws and hit \"Generate\" again")
    
    def toggle_severity_selection_toplevel(self, event, flaw, var, first_word):

        #print("TOP LEVEL WINDOW MEASUREMENT START")
        
        self.var = var

        if self.var.get() != "None":
            self.update_flaws_count()

            if self.var.get() != flaw:
                #print("Empty widget value")
                self.var.set("None")

            else:
                if self.var.get() not in self.selected_flaws:
                    self.selected_flaws.append(self.var.get())

                self.display_measurement(event, flaw, self.var, first_word)

        elif self.var.get() == "None" or self.var.get() in self.flaw_dict.keys():
            if flaw in self.flaw_dict.keys():
                #print("Removing the following DAMAGE:SEVERITIES from dictionary: ")
                #print(flaw + ":" + str(self.flaw_dict[flaw]))
                del self.flaw_dict[flaw]

            if flaw in self.selected_flaws:
                self.selected_flaws.remove(flaw)

            for i in range(len(self.selected_flaws_sentences)):
                if self.selected_flaws_sentences[i].endswith(flaw):
                    self.selected_flaws_sentences.pop(i)

            self.enable_widgets()
            
    def display_sentence(self, new_sentence = None):
        if not new_sentence:
            self.sentence_display.configure(text=self.jacket_string)
        else:
            self.sentence_display.configure(text=new_sentence)

    def get_jacket_string(self):
        return self.jacket_string

    def toggle_severity_selection(self, event, svrty, flaw, var, first_word):
        #print("selected widget: ", flaw)
        #print("current widget value: ", var.get())+
        
        #print(self.flaw_dict)

        self.var = var

        if self.var.get() != "None":

            self.update_flaws_count()
            
            if self.var.get() != flaw:
                #print("Empty widget value")
                self.var.set("None")
            else:
                if self.var.get() not in self.selected_flaws:
                    self.selected_flaws.append(self.var.get())
                self.display(event, flaw, self.var, svrty, first_word)

        elif self.var.get() == "None" or self.var.get() in self.flaw_dict.keys():
            if flaw in self.flaw_dict.keys():
                #print("Removing the following DAMAGE:SEVERITIES from dictionary: ")
                #print(flaw + ":" + str(self.flaw_dict[flaw]))
                del self.flaw_dict[flaw]

            if flaw in self.selected_flaws:
                self.selected_flaws.remove(flaw)
            
            for i in range(len(self.selected_flaws_sentences)):
                if self.selected_flaws_sentences[i].endswith(flaw):
                    self.selected_flaws_sentences.pop(i)
  
            self.enable_widgets()
        #print(self.flaw_dict)

    def update_flaws_count(self):
        self.flaws_cnt = len(self.flaw_dict.keys())
        #print(str(self.flaws_cnt) + " flaws")

        if self.flaws_cnt >= 3:
            self.disable_widgets()
        else:
            
            self.enable_widgets()

    def uncheck_current_flaw(self, flaw):
        self.close_svrity_frame()
        if flaw in self.flaw_dict.keys():
                #print("Removing the following DAMAGE:SEVERITIES from dictionary: ")
                #print(flaw + ":" + str(self.flaw_dict[flaw]))
                del self.flaw_dict[flaw]

        if flaw in self.selected_flaws:
            self.selected_flaws.remove(flaw)
        
        for i, sentences in enumerate(self.selected_flaws_sentences):
            if self.selected_flaws_sentences[i].endswith(flaw):
                self.selected_flaws_sentences.pop(i)

        self.enable_widgets()
    
    ## 2nd-2nd
    def close_svrity_frame(self):
        for wdgt in self.svrty_frame.winfo_children():
            wdgt.grid_remove()
        for checkbox in self.checkboxes:
            checkbox.configure(state='normal')

    ## 2nd-1st
    def display(self, event, flaw, var, svrty, first_word):
        #print("Disabling widgets")
        
        self.disable_widget(event, flaw, var)
        self.svrty_frame = Severity(self, first_word, svrty, flaw, var)


    def display_measurement(self, event, flaw, var, first_word, current_value="__"):
        self.disable_widget(event, flaw, var)
        self.measurement_frame = em.Enter_Measurement(self, first_word, flaw, var, current_value)

    
    def disable_widgets(self):
        for widget in self.sections_tab.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                if widget.cget("onvalue") in self.selected_flaws:
                    widget.configure(state='normal')
                else:
                    widget.configure(state='disabled')
        

    def disable_widget(self, event, flaw, var):
        for widget in self.sections_tab.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                if widget.cget("text") != flaw:
                    #print(count)
                    #count += 1
                    widget.configure(state='disabled')
                    #print(str(type(widget)) + " " + str(widget.cget("onvalue")) +  " " + str(widget.cget("state")))
              
    
    def enable_widgets(self):
        for widget in self.sections_tab.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                widget.configure(state='normal')

    def set_dict(self, flaw):
        #print("Set button Activated..")
            
        #print("Current damage: " + flaw) 

        if flaw:
            var = ctk.StringVar(self, value=flaw)  
            checkbox = ctk.CTkCheckBox(self, text="", variable=var, onvalue=flaw, offvalue="None", font=("Arial", 15), width=2, height=1)
            checkbox.grid(row=len(self.flaws), column=0, pady=3, padx=(10,0), sticky="e")
            label = ctk.CTkLabel(self, text=flaw, font=("Arial", 15))
            label.grid(row=len(self.flaws), column=1, pady=3, padx=(0,10), sticky="w")
            # Bind / Toggle Function
            #print("line 118 executed ")
            checkbox.bind("<Button-1>", lambda event, flaw=flaw, var=var: self.toggle_severity_selection(event, flaw, var))
            self.checkboxes.append(checkbox)
            self.flaws.append(flaw)
            self.flaw_vars[flaw] = var
            # Clear the CTkEntry widget
            self.label.delete(0, 'end')
            # Uncheck the "Other" checkbox
            self.flaw_vars["Other"].set("None")
            self.update_dict(flaw)
            #print("Current severity dict in severity class ...." )
            #print(self.svrty_frame.get_selected_severity())
        else:
            self.update_dict(self.var.get())
            
        #print(self.flaw_dict)
        #self.update_flaws_count()
        

    def update_dict(self, flaw):
        if self.flaw_vars[flaw].get() == "None":
            self.flaw_dict.pop(flaw, None)  # Remove the damage from the dictionary
            self.master.remove_unselected_flaw(flaw, list(self.flaw_dict.keys()))
        else:
            self.flaw_dict[flaw] = self.svrty_frame.get_selected_severity()

        self.close_svrity_frame()
        self.enable_widgets()



    def add_svrty_to_flaw(self, flaw, svrty):
        self.flaw_dict[flaw] = svrty
        self.add_selected_flaws(flaw, svrty)

    def add_selected_flaws(self, dmg, svrty):
        s = ""
        for sev in svrty:
            s += sev + ", "
        s = s[:-2]
        s = s + " " + dmg
        self.selected_flaws_sentences.append(s)
        self.sentence_cnt += 1

    def add_to_list(self, event, first_word, flaw, var):
        print(var.get())
        if var.get() == "None":
            self.selected_flaws.remove(flaw)
            self.sentence_cnt -= 0
            for i in range(len(self.selected_flaws_sentences)):
                if self.selected_flaws_sentences[i].endswith(flaw):
                    self.selected_flaws_sentences.pop(i)
                    break
        else:
            self.selected_flaws.append(flaw)
            self.selected_flaws_sentences.append(first_word + " " + flaw)
            self.sentence_cnt += 1


    def remove_unselected_flaw(self, removed_dmg):
        was_there = False
        for i in len(self.selected_flaws_sentences):
            if self.selected_flaws_sentences[i].endswith(removed_dmg):
                self.selected_flaws_sentences.pop(i)
                was_there = True
                break

        if was_there:
            self.sentence_cnt += 1


    
    def get_flaw_dict(self):
        return self.flaw_dict

class Severity(ctk.CTkToplevel):
    def __init__(self, parent, first_word, svrty=None, flaw=None, var=None, is_list=False):
        super().__init__(parent)
        self.parent = parent
        self.configure(height=100)
        self.title("")
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.grab_set()
        self.first_word = first_word
        self.svrty = svrty
        self.flaw = flaw
        self.var = var
        self.selected_svrties = []
        self.checked_amt = 0
        self.is_list = is_list

        self.display_list()

    def handle_key_event(self, event):
        if event.keysym == "Escape":
            self.var.set("None")
            self.parent.uncheck_current_flaw(self.flaw)
            self.destroy()

    def display_list(self):

        self.bind("<Key>", self.handle_key_event)

        for widget in self.winfo_children():
            widget.grid_forget()
        self.reset_selections()
        
        ctk.CTkLabel(self, text="Severity", font=("Lucida Sans", 20)).grid(row=0, column=0, columnspan=2, sticky="snew")
        ctk.CTkLabel(self, text="Choose 1 / Limit 2", font=("Lucida Sans", 15)).grid(row=1, column=0, columnspan=2,  sticky="snew")

        # ttk seperater going horizontal
        sep = ttk.Separator(self, orient="horizontal")
        sep.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

        for widget in self.parent.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                if widget.cget("onvalue") != self.flaw:
                    widget.configure(state='disabled')
        
        self.scroll_frame = ctk.CTkScrollableFrame(self, height=525)
        self.scroll_frame.grid(row=3, column=0, columnspan=3, rowspan=4, sticky="snew")

        for j, svrty in enumerate(self.svrty):
            severity_var = ctk.StringVar()
            severity = ctk.CTkCheckBox(self.scroll_frame, text=f'{svrty}', variable=severity_var, onvalue=svrty, offvalue="None", font=("Arial", 18), width=2, height=1)
            severity.grid(row=j, column=1, pady=5, padx=(5,50), sticky="snew")
            severity.bind("<Button-1>", lambda event, svrty=svrty, var=severity_var: self.check_limit(event, svrty, var))

        self.cancel_btn = ctk.CTkButton(self, text="Cancel", command=lambda:self.cancel(), font=("Lucida Sans", 17))
        self.cancel_btn.grid(row=len(self.svrty)+2, column=0, columnspan=1, padx=10, pady=10)

        self.set_btn = ctk.CTkButton(self, text="Set", command=lambda: self.set_dict(), font=("Lucida Sans", 17))
        self.set_btn.grid(row=len(self.svrty)+2, column=1, columnspan=1, padx=10, pady=10)

    
    def set_dict(self):
        if len(self.selected_svrties) == 0:
            return
        self.parent.add_svrty_to_flaw(self.flaw, self.selected_svrties)
        self.parent.update_flaws_count()
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
        self.parent.uncheck_current_flaw(self.flaw)
        self.destroy()

class Main(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame = Jacket_Flaws(self)
        self.frame.grid(row=0, column=0, sticky="nsew")
    


if __name__ == "__main__":
    app = Main()
    app.mainloop()