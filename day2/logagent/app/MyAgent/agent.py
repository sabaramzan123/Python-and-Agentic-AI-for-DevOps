from langchain_ollama import ChatOllama
from devops_tools import (
    read_log_file,
    count_log_levels,
    show_docker_containers
)
from langchain.agents import create_agent
from langchain_core.tools import tool


# ============================================================
# LLM
# ============================================================

llm = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",
    temperature=0
)


# ============================================================
# TOOLS
# ============================================================

@tool
def analyze_logs(path: str):
    """
    Analyze a log file and dynamically count all log levels
    found in the file.
    """

    log_text = read_log_file(path)

    return count_log_levels(log_text)


@tool
def get_docker_containers():
    """
    Show all Docker containers running on the host machine.
    """

    result = show_docker_containers()

    return result.stdout


# ============================================================
# AI AGENT
# ============================================================

TOOLS = [
    analyze_logs,
    get_docker_containers
]


SYSTEM_PROMPT = """
You are a DevOps Assistant.

Your job is to help users analyze log files and inspect
Docker containers running on the local machine.

You have access to two tools:

1. analyze_logs
   - Reads a log file.
   - Dynamically detects and counts the log levels present.
   - Do not assume that only INFO, WARNING, or ERROR exist.
   - New log levels such as DEBUG, CRITICAL, FATAL, SUCCESS,
     NOTICE, or custom levels may also appear.

2. get_docker_containers
   - Shows Docker containers on the local machine.

When analyzing logs, provide a concise and actionable report.

The report should include:

- Total number of log entries when possible
- Log levels found
- Count of each log level
- Important errors or warnings
- Possible troubleshooting recommendations
- Potential security concerns if visible from the available information

When discussing Docker containers, mention:

- Container name
- Container status
- Image
- Any obvious issues

Do not invent information that is not available from the tools.

Keep your response clear and beginner-friendly.
"""


agent = create_agent(
    llm,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT
)


# ============================================================
# USER INPUT
# ============================================================

question = input(
    "Enter your question for your DevOps Agent: "
)

print("\nThinking...\n")


# ============================================================
# RUN AGENT
# ============================================================

result = agent.invoke(
    {
        "messages": [
            ("user", question)
        ]
    }
)


print(result["messages"][-1].content)