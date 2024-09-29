import functools
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langgraph.graph import START, END
from langgraph.checkpoint.memory import MemorySaver
from app.agents.agent import create_agent_without_tools
from app.agents.state import AgentState


def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {"messages": [result]}


class BaseChatBot:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-2024-08-06")
        self.memory = MemorySaver()
        self.graph = self.set_graph()

    def set_graph(self):
        chatbot_agent = create_agent_without_tools(
            llm=self.llm,
            system_message=""
        )
        chatbot_node = functools.partial(agent_node, agent=chatbot_agent, name="chatbot")

        workflow = StateGraph(AgentState)
        workflow.add_node("chatbot", chatbot_node)
        workflow.add_edge(START, "chatbot")
        workflow.add_edge("chatbot", END)
        return workflow.compile(checkpointer=self.memory)




