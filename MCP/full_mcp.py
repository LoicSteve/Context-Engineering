"""Combined MCP server: stacks tools/resources/prompts from the other
servers in this folder onto a single MCPServer instance so they can be
run as one process.

Each source module still defines its own standalone `mcp = MCPServer(...)`
(so `mcp dev calculator_server.py` etc. keep working on their own) — here
we just import the plain functions and re-register them on one combined
instance via the same decorators, used as plain calls instead of `@...`.
"""

import importlib.util
import pathlib

from mcp.server import MCPServer

import calculator_server
import documentation
import prompt_server

# file-analyzer_server.py has a hyphen in its name, so it can't be
# imported with a normal `import` statement — load it by path instead.
_here = pathlib.Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "file_analyzer_server", _here / "file-analyzer_server.py"
)
file_analyzer_server = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(file_analyzer_server)

mcp = MCPServer("full")

# --- calculator_server: tools ---
mcp.tool()(calculator_server.add)
mcp.tool()(calculator_server.subtract)
mcp.tool()(calculator_server.multiply)

# --- file-analyzer_server: tools ---
mcp.tool()(file_analyzer_server.read_file)
mcp.tool()(file_analyzer_server.count_lines)
mcp.tool()(file_analyzer_server.list_directory)

# --- documentation: resources + tool ---
mcp.resource("doc://api/overview")(documentation.api_overview)
mcp.resource("doc://api/endpoints")(documentation.api_endpoints)
mcp.tool()(documentation.get_api_status)

# --- prompt_server: prompts + tool ---
mcp.prompt()(prompt_server.code_review_prompt)
mcp.prompt()(prompt_server.security_audit_prompt)
mcp.tool()(prompt_server.get_available_prompts)

if __name__ == "__main__":
    mcp.run()
