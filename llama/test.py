#pip install -U langchain-ollama

from langchain_ollama import OllamaLLM
import pandas as pd
llm = OllamaLLM(model="llama3.1")

data = pd.read_csv('/home/taejin/BPETL/analysis/bin/model/newsdata/test.csv')
a = data['title'][0]

response = llm.invoke(f"please translate {a} to korean. just answer the question. do not answer anything else.")
print(response)