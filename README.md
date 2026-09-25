# Coirei Internship - Task 1

# AI API using FastAPI and Ollama

# Introduction

This is my Task 1 project for the Coirei GenAI Internship.
In this project, I created a simple AI API using **FastAPI** and connected it with **Ollama**. The API takes user input and gives an AI-generated response.

# Technologies Used

* Python
* FastAPI
* Uvicorn
* Ollama
* Postman

# API

POST/generate`

Example input:
{
    "user_input": "Explain machine learning concepts"
}
The API sends the input to the Ollama AI model and returns the response.

# How to Run

Install the required packages:
uv pip install -r requirements.txt

Run the API:
uv run uvicorn main:app --reload

API URL:
http://127.0.0.1:8000

For API testing:
http://127.0.0.1:8000/docs

I also tested the API using **Postman**.

# What I Learned

* Basics of API and REST API
* GET and POST methods
* Request and response
* JSON
* FastAPI and Uvicorn
* Connecting an AI model with an API
* Testing API using Postman

# Conclusion
This task helped me understand how to create a simple API and connect an AI model with it.
