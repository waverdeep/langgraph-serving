from typing import List
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def create_agent_with_tools(llm, tools: List, system_message: str):
    prompt = ChatPromptTemplate(
        [
            (
                "system",
                "You are a helpful AI assistant."
                " Use the provided tools to progress towards answering the question."
                "You have access to the following tools: {tool_names}.\n{system_message}"
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    prompt = prompt.partial(system_message=system_message)
    prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
    return prompt | llm.bind_tools(tools)


def create_agent_without_tools(llm, system_message: str):
    prompt = ChatPromptTemplate(
        [
            (
                "system",
                "You are a helpful AI assistant."
                " Use the provided tools to progress towards answering the question.\n{system_message}"
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    prompt = prompt.partial(system_message=system_message)
    return prompt | llm