from django.shortcuts import render
from rest_framework.views import APIView
from langchain_cerebras import ChatCerebras
import getpass
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class chatbot(APIView):

    def post(self, request, *args, **kwargs):
       
        if "CEREBRAS_API_KEY" not in os.environ:
            os.environ["CEREBRAS_API_KEY"] = os.getenv('CEREBRAS_API_KEY')
        llm = ChatCerebras(
            model="llama3.1-70b",
            # other params...
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant that translates {input_language} to {output_language}.",
                ),
                ("human", "{input}"),
            ]
        )

        chain = prompt | llm
        chain.invoke(
            {
                "input_language": "English",
                "output_language": "German",
                "input": "I love programming.",
            }
        )

    



