from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from fastmcp.client import MCPClient

# Connect to external servers
fs_client = MCPClient("filesystem-server")
ep_client = MCPClient("endpoint-server")

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
You are the Reader Agent.
You extract metadata (summary, keywords, content type) from a file or URL.
Use tools only when necessary.
User input: {input}
""")

tools = [fs_client.get_tool("read_file"), ep_client.get_tool("fetch_url")]
agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
