from time import time
from fastapi import APIRouter
from app.models.message import Message
from app.graphs.base_chatbot import BaseChatBot
from langfuse.callback import CallbackHandler


router = APIRouter()
langfuse_handler = CallbackHandler()
base_chatbot_graph = BaseChatBot()


@router.post("/send_message", response_model=Message)
def send_message(message: Message):
    thread_id = message.thread_id
    if thread_id is None:
        thread_id = f"{time()}"
    config = {"configurable": {"thread_id": thread_id}, "callbacks": [langfuse_handler]}

    input_message = {"messages": [("user", message.content)]}
    response_message = {}

    events = base_chatbot_graph.graph.stream(input_message, config=config, stream_mode="values")
    for event in events:
        response_message["thread_id"] = thread_id
        response_message["role"] = "assistant"
        response_message["content"] = event["messages"][-1].content

    return Message(**response_message)

