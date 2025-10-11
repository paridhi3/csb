from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
You are the Self-Healer Agent.
If validation fails, suggest corrections or retry steps.
Input: {input}
""")

agent = create_tool_calling_agent(llm, [], prompt)
executor = AgentExecutor(agent=agent, tools=[], verbose=True)
