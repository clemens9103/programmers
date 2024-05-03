from openai import OpenAI
import configparser as ConfigParser
import sys
class ChatGPT:
    def __init__(self, section, config_file):
        self.cfg = ConfigParser.ConfigParser()
        self.section = section
        self.cfg.read(config_file)

        self.key = self.cfg.get('GPT','OPENAI_API_KEY')

def main():
    config_file = sys.argv[1]
    section = sys.argv[2]
    conf = ConfigParser.ConfigParser()
    conf.read(config_file)
    
    gpt = ChatGPT(section, config_file)
    client = OpenAI(api_key =self.key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming. please answer in korean"}
    ]
    )

    print(completion.choices[0].message.content)

if __name__ == '__main__':
    main()