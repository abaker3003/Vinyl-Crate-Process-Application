import customtkinter as ctk
import os
import xlfile as xl
import json

import google.generativeai as genai



class AI_Frame(ctk.CTkFrame):
    def  __init__(self, master, intros_outros=None, condition=None, vinyl_dmg=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure( width=900, height=600)
        self._condition = condition
        self._vinyl_dmg = vinyl_dmg
        self._intros_outros = intros_outros
        self.ai_decision = ctk.IntVar()
        self.master = master
        self.responses = []
        


    def desc(self):
        self.display_text = "Condition: " + str(self._condition)
        self.display_text += "\nVinyl Damage Dict: " + str(self._vinyl_dmg)
        #print("Vinyl: " + str(self._vinyl_dmg))
        self.intro = self._intros_outros[0]
        self.outro = self._intros_outros[1]
        self.display_text += "\nIntro: " + self.intro

        
        

        # ---> FILE HANDLING <--- #
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Book1.xlsx')

        xl_file = xl.open_excel_file(file_path)

        self.xl_read = xl_file.read_into_dataframe_ai()

        filtered_xl_read = self.xl_read[self.xl_read['Cond'] == self._condition]
        filtered_xl_read['Description'] = filtered_xl_read['Description'].str.lower()

        filtered_xl_read['Description'] = filtered_xl_read['Description'].astype(str)
        description_list = filtered_xl_read['Description'].tolist()
        self.description_list = ", ".join(description_list)


        options = [
            "traces", "handling traces", "hairline", "hairlines", "sleeve dust",
            "sleeve rubs", "scuffings", "scuffs", "markings", "marks",
            "blemishing", "blemishes", "prints", "spindle marks", "ring wear",
            "corner wear", "NO DAMAGE"
        ]
        

        # Load the API key from the JSON file
        with open('api_key.json') as f:
            keys = json.load(f)
            GOOGLE_API_KEY = keys['GOOGLE_API_KEY']

        # Configure the genai with the API key
        genai.configure(api_key=GOOGLE_API_KEY)

        # Create a generative model
        model = genai.GenerativeModel('gemini-1.5-pro-latest')

        # -->--> Prompt usng the common words/phrases <--<-- #

        prompt = "PLEASE LEAVE DESCRIPTION IN 1 SENTENCE AND ONLY USE THE DAMAGES/SEVERITIES PROVIDED IN THE DICTIONARY: Based on the list of example descriptions in the dataset for the condition " + str(self._condition) + ": " + self.description_list + ", please modify the following stentence templates and replace the parentheses and the text within with the corresponding damage:severity dictionaries:\n"

        prompt += "\"" + self.intro + "\" : " + str(self._vinyl_dmg) + "\n"

        '''prompt += "Also, revise the following jacket sentence and edit as needed:\n"

        prompt += "\"" + self.outro + "\"\n"
        
        prompt += "Please put the two final sentences together with proper grammer and punctuation. No extra characters. This needs to be displayed as a Vynil description ready to print.\n**Also** please review the resulting description and clean it up and necessary"'''

        
        self.response_google = model.generate_content(prompt)  # Replace max_tokens with max_length
        self.AIDescriptionDiag_googleai = ctk.CTkFrame(self, height=600, width=900)
        self.AIDescriptionDiag_googleai.grid(row=0, column=5, columnspan=5, rowspan=3, sticky='nsew', padx=10, pady=10)
        self.AIDescriptionDiag_googleai.columnconfigure(0, weight=1)
        self.AIDescriptionDiag_googleai.rowconfigure(0, weight=1)
        self.ai_description(self.response_google, self.AIDescriptionDiag_googleai)
        
        
    def ai_description(self, message, frame):

        self.AIDescription_label = ctk.CTkLabel(frame, text="GoogleAI Description", font=("Courier New Greek", 22))

        self.AIDescription_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky='e')

        AIDescription_text = ctk.CTkTextbox(frame,
                                            height=300,
                                            width=425, wrap="word", font=("Courier New Greek", 20))
        AIDescription_text.configure(state="normal")
        AIDescription_text.delete("0.0", ctk.END)
        
        AIDescription_text.insert("0.0", message.text + self.outro)

        #insert self.outro on next line
        '''AIDescription_text.insert("4.0", self.outro)'''

        AIDescription_text.grid(row=1, column=0, columnspan=3, pady=20, padx=20, sticky='nsew')
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        self.responses.append(AIDescription_text)



    def get_data(self):
        return self.responses[self.ai_decision.get()].get("0.0", ctk.END)
    
    @property
    def intros_outros(self):
        return self._intros_outros

    @property
    def condition(self):
        return self._condition
    
    @property
    def vinyl_dmg(self):
        return self._vinyl_dmg
    
    @intros_outros.setter
    def intros_outros(self, io):
        self._intros_outros = io

    @condition.setter
    def condition(self, cnd):
        self._condition = cnd

    @vinyl_dmg.setter
    def vinyl_dmg(self, vnyl):
        self._vinyl_dmg = vnyl

