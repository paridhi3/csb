from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
You are the Categorizer Agent.
Classify the content into one of: ['Research', 'Case Study', 'Article', 'Blog'].
Provide a short reasoning and confidence score.
Content: {input}
""")

agent = create_tool_calling_agent(llm=llm, tools=[], prompt=prompt)
executor = AgentExecutor(agent=agent, tools=[], verbose=True)
