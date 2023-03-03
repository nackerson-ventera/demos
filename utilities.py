import openai
import config

class GPT_utilities:
    
    def __init__(self):
        openai.api_key = config.openai_api_key
        
        self.char_to_token = 4 # approximatly four characters is 1 token
        self.default_gpt_config = {
            "model": "text-davinci-003",
            "temperature": 0.7,
            "max_length":200,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        self.gpt_config = self.default_gpt_config.copy()