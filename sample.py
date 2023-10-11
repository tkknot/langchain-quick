import os
import openai

from dotenv import load_dotenv
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

load_dotenv()

llm = openai.OpenAI(openai_api_key=os.environ['GPT_API_KEY'])
chat_model = ChatOpenAI(openai_api_key=os.environ['GPT_API_KEY'])

# propmt = PromptTemplate.from_template("what is a good name for a company that makes {product}?")
# print(propmt.format(product="colorful socks"))

# print(propmt)

# text = "What would be a good company name for a company that makes colorful socks?"
# messages = [HumanMessage(content=text)]

# print(llm.predict_messages(messages))
# # >> Feetful of Fun

# print(chat_model.predict_messages(messages))

# template = "You are a helpful assistant that translates {input_language} to {output_language}."
# human_template = "{text}"

# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system", template),
#     ("human", human_template),
# ])
# print(chat_prompt)

# print(chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming."))


# class CommaSeparatedListOutputParser(BaseOutputParser):
#     # """Parse the output of an LLM call to a comma-separated list."""


#     def parse(self, text: str):
#         # """Parse the output of an LLM call."""
#         return text.strip().split(", ")

# print(CommaSeparatedListOutputParser().parse("hi, bye"))