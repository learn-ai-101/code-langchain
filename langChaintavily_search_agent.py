import os
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE"),openai_api_key=os.environ.get("OPENAI_API_KEY"),
                    model_name="openai/gpt-oss-20b", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools) #, agent_type="react-search")

def main():
    print("This is a placeholder for react_search_agent.py")
    """
     result = agent.invoke(
        {"messages":HumanMessage(content="Who is the current president of the United States?")}
    )
    """
    result = agent.invoke(
        {"messages":HumanMessage(content="Search for 3 job postings for LLM expert in the Malmö area on linkedin and list their details.")}
    )
    print(result)


if __name__ == "__main__":
    main()


"""
https://eu.smith.langchain.com/public/6a390515-5af7-4f62-a314-77a3d134ad16/r
"""