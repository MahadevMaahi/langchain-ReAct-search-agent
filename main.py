from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]

llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)
chain = agent_executor

def main():
    print("Hello from langchain-react-search-agent!")
    result = chain.invoke(
        input={
            "input": "search for 3 job posting for AI engineer using langchain in bangalore on linkedin and list their detials",
        
        }
    )


if __name__ == "__main__":
    main()
