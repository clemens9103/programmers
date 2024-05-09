from openai import OpenAI
import configparser as ConfigParser
import sys
import os

class ChatGPT:
    def __init__(self, section, config_file):
        self.cfg = ConfigParser.ConfigParser()
        self.section = section
        self.cfg.read(config_file)
        self.key = self.cfg.get('GPT','OPENAI_API_KEY')

    def GPT_Module(self):
        client = OpenAI(api_key =self.key)

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Maria DB에 데이터를 넣으려고 하는데 어떻게 하면 좋을까?"}
        ]
        )

        print(completion.choices[0].message.content)

def main():
    module = os.path.basename( sys.argv[0])
    print(f"{module} Start")
    config_file = sys.argv[1]
    section = sys.argv[2]
    
    gpt = ChatGPT(section, config_file)
    gpt.GPT_Module()

    print("END")
    

if __name__ == '__main__':
    main()