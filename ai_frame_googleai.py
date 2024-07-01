import customtkinter as ctk
import os
import xlfile as xl
import json

from llamaapi import LlamaAPI



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
        
        self.vinyl_sentence = self._intros_outros[0]
        self.jacket_sentence = self._intros_outros[1]

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

        api_key_file = os.path.join(current_dir, 'api_key.json')
        with open(api_key_file) as f:
            keys = json.load(f)
            LLAMA_API_KEY = keys['LLAMA_API_KEY']

        llama = LlamaAPI(LLAMA_API_KEY)

        api_request_json = {
            "messages": [
                {"role": "user", "content": "PLEASE LEAVE DESCRIPTION IN 1 SENTENCE AND ONLY USE THE DAMAGES/SEVERITIES PROVIDED IN THE DICTIONARY: Based on the list of example descriptions in the dataset for the condition " + str(self._condition) + ": " + self.description_list + ", please modify the following stentence templates and replace the parentheses and the text within with the corresponding damage:severity dictionaries:\n"
                                               "\"" + self.vinyl_sentence + "\" : " + str(self._vinyl_dmg) + "\n"},
            ],
            "stream": False,
            "function_call": "generate_text",
        }

        response = llama.run(api_request_json)
        self.response_llama = response.json()["messages"][-1]["content"]
        self.AIDescriptionDiag_googleai = ctk.CTkFrame(self, height=600, width=900)
        self.AIDescriptionDiag_googleai.grid(row=0, column=5, columnspan=5, rowspan=3, sticky='nsew', padx=10, pady=10)
        self.AIDescriptionDiag_googleai.columnconfigure(0, weight=1)
        self.AIDescriptionDiag_googleai.rowconfigure(0, weight=1)
        self.ai_description(self.response_llama, self.AIDescriptionDiag_googleai)

        self.AIDescription_label = ctk.CTkLabel(self.AIDescriptionDiag_googleai, text="LLAMA Description", font=("Courier New Greek", 22))

        self.AIDescription_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky='e')

        AIDescription_text = ctk.CTkTextbox(self.AIDescriptionDiag_googleai,
                                            height=300,
                                            width=425, wrap="word", font=("Courier New Greek", 20))
        AIDescription_text.configure(state="normal")
        AIDescription_text.delete("0.0", ctk.END)

        AIDescription_text.insert("0.0", self.response_llama + self.outro)

        AIDescription_text.grid(row=1, column=0, columnspan=3, pady=20, padx=20, sticky='nsew')
        self.AIDescriptionDiag_googleai.columnconfigure(0, weight=1)
        self.AIDescriptionDiag_googleai.rowconfigure(1, weight=1)
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

