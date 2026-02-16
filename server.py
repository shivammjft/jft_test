import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Custom GPT Tools API",
    description="A simple API with tools that can be used by a Custom GPT via Actions.",
    version="1.0.0",
    servers=[{"url": "https://9c6e-14-195-211-249.ngrok-free.app", "description": "Production server"}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com", "https://chatgpt.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are only 10 types of people in the world: those who understand binary and those who don't.",
    "A SQL query walks into a bar, sees two tables, and asks: 'Can I join you?'",
    "Why did the developer go broke? Because he used up all his cache.",
    "To understand recursion, you must first understand recursion.",
]


class AddRequest(BaseModel):
    a: float
    b: float


@app.get("/joke", operation_id="getJoke", summary="Get a random joke")
def get_joke():
    """Returns a random joke. Use this when the user asks for a joke or wants to be entertained."""
    return {"joke": random.choice(JOKES)}


@app.post("/add", operation_id="addNumbers", summary="Add two numbers together")
def add_numbers(body: AddRequest):
    """Add two numbers and return the result. Use this when the user wants to add or sum two numbers."""
    return {"result": body.a + body.b}
