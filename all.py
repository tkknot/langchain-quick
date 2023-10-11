import os
import openai

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

load_dotenv()

# chat_model = ChatOpenAI(openai_api_key=os.environ['GPT_API_KEY'])

class CommaSepareatedListOutputParser(BaseOutputParser):
  
  def parse(self, text: str):
      print(text)
      return text.strip().split(",")

# system側の方には基本的にpromptの定型を入れることになりそう
template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more."""
# human_templateにユーザー側の入力文（条件）が入ってくる
human_template = "{text}"

chat_propmt = ChatPromptTemplate.from_messages([
  ("system", template),
  ("human", human_template)
])

chat_model = ChatOpenAI(openai_api_key=os.environ['GPT_API_KEY'])

# propmt | model | output parser を結び付けている
chain = chat_propmt | chat_model | CommaSepareatedListOutputParser()
print(chain.invoke({"text": "foods"}))