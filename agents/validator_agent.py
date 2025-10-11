from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
You are the Validator Agent.
Validate metadata and category.
Return a JSON with:
{{
  "valid": true/false,
  "issues": [list of issues],
  "confidence": 0-1
}}
Input: {input}
""")

agent = create_tool_calling_agent(llm, [], prompt)
executor = AgentExecutor(agent=agent, tools=[], verbose=True)
