import os
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents.structured_output import ToolStrategy
from langchain.agents.structured_output import ProviderStrategy
from tavily import TavilyClient

load_dotenv()

class Source(BaseModel):
    """ Schema for a source used by the agent """
    title: str | None = Field(description="The title of the source")
    url: str | None = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """ Schema for the agent's response with answer and sources"""
    answer: str | None = Field(description="The answer to the query")
    sources: list[Source] | None = Field(default_factory=list, description="List of sources used to generate the answer")

tavily = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

@tool
def search(query: str) -> str:
    """
    Tool that searches for information based on a query from the internet
    
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    # Placeholder for search functionality
    return tavily.search(query=query, max_results=3)

llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE"),openai_api_key=os.environ.get("OPENAI_API_KEY"),
                    model_name="openai/gpt-oss-20b", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools, response_format=ToolStrategy(AgentResponse)) #, agent_type="react-search")

def main():
    print("This is a placeholder for react_search_agent.py")
    """
     result = agent.invoke(
        {"messages":HumanMessage(content="Who is the current president of the United States?")}
    )
    """
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="Search for 3 job postings for LLM expert in the Malmö area on google and list their details."
            )
        }
    )
    result["structured_response"]


if __name__ == "__main__":
    main()
