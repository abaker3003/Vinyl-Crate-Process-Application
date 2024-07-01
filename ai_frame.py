from urllib import response
import customtkinter as ctk
import os
import xlfile as xl
import json

from llamaapi import LlamaAPI



class AI_Frame(ctk.CTkFrame):
    def  __init__(self, master, intros_outros=None, condition=None, **kwargs):
        super().__init__(master, **kwargs)

        self.configure( width=900, height=600)
        self._condition = condition
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

        '''api_key_file = os.path.join(current_dir, 'api_key.json')
        with open(api_key_file) as f:
            keys = json.load(f)
            LLAMA_API_KEY = keys['LLAMA_API_KEY']

        llama = LlamaAPI(LLAMA_API_KEY)

        api_request_json = {
            "messages": [
                {"role": "user", "content": "Please revise / modify the following two sentences for grammar correctiveness:\n" + "\"" + self.vinyl_sentence + " " + self.jacket_sentence},
            ],
            "stream": False,
            "function_call": "generate_text",
        }

        response = llama.run(api_request_json)'''

        response = "Please revise / modify the following two sentences for grammar correctiveness:\n\"" + self.vinyl_sentence + " " + self.jacket_sentence
        
        self.AIDescriptionDiag = ctk.CTkFrame(self, height=600, width=900)
        self.AIDescriptionDiag.grid(row=0, column=5, columnspan=5, rowspan=3, sticky='nsew', padx=10, pady=10)
        self.AIDescriptionDiag.columnconfigure(0, weight=1)
        self.AIDescriptionDiag.rowconfigure(0, weight=1)

        self.AIDescription_label = ctk.CTkLabel(self.AIDescriptionDiag, text="LLAMA Description", font=("Courier New Greek", 22))

        self.AIDescription_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky='e')

        AIDescription_text = ctk.CTkTextbox(self.AIDescriptionDiag,
                                            height=300,
                                            width=425, wrap="word", font=("Courier New Greek", 20))
        AIDescription_text.configure(state="normal")
        AIDescription_text.delete("0.0", ctk.END)


    ## ---> need to fix AI response <--- ##
        '''AIDescription_text.insert("0.0", response.text)'''

    ## ---> TESTING PURPOSES <--- ##
        AIDescription_text.insert("0.0", response)

        AIDescription_text.grid(row=1, column=0, columnspan=3, pady=20, padx=20, sticky='nsew')
        self.AIDescriptionDiag.columnconfigure(0, weight=1)
        self.AIDescriptionDiag.rowconfigure(1, weight=1)
        self.responses.append(AIDescription_text)




    def get_data(self):
        return self.responses[self.ai_decision.get()].get("0.0", ctk.END)
    
    @property
    def intros_outros(self):
        return self._intros_outros

    @property
    def condition(self):
        return self._condition
    
    @intros_outros.setter
    def intros_outros(self, io):
        self._intros_outros = io

    @condition.setter
    def condition(self, cnd):
        self._condition = cnd


