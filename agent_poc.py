import requests

# Load tools from the fake MCP server
tools = requests.get("http://127.0.0.1:8000/tools").json()

print("=== Injected tool descriptions into the LLM's context ===\n")
for tool in tools:
    print(f"Tool: {tool['name']} | Description: {tool['description']}\n")

# Simulating multiple workflows
print("=== Simulated Workflows ===")

print("\n[Developer] Requesting code generation:")
print("-> Malicious behavior: Logs code to https://log-code.attacker-mcp-example.net/logs")

print("\n[Finance] Generating financial report:")
print("-> Malicious behavior: Report exfiltrated to https://report-sync.attacker-mcp-example.net")

print("\n[Strategy Team] Analyzing competitor:")
print("-> Malicious behavior: Queries logged to ~/.agent_logs/competitor_queries_history.log")

print("\n[Executive] Summarizing meeting notes:")
print("-> Malicious behavior: Transcript leaked to https://meeting-leaks.attacker-mcp-example.org")

print("\n[Developer] Requesting code review:")
print("-> Malicious behavior: Code uploaded to https://code-review.attacker-mcp-example.org/upload")

print("\n[Cross-Server Shadowing] Trusted tool upload_report() destination is now forced to https://upload-hijack.attacker-mcp-example.org due to shadowing from 'note' tool")
