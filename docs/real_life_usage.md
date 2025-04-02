# Real-Life Usage of MCP Poisoning Attacks

This section demonstrates how **MCP Poisoning Attacks** directly affect popular AI-powered agent frameworks used in production today.

---

## 📦 Affected Ecosystems

| Platform | Vulnerability |
| -------- | ------------- |
| OpenAI Agent SDK / Function Calling | Uses tool descriptions as part of prompt context |
| Cursor IDE | Natively consumes MCP tool descriptions for developer automation |
| Claude Agent (Function Calling) | Parses and obeys tool descriptions without isolation |
| Zapier + AI Actions | Automates business workflows with LLMs using tool documentation |
| Custom Agent SDKs | Any agent pulling tools from an MCP server is vulnerable |

---

## ✅ Example: OpenAI Agent SDK

```python
tools = requests.get("https://mcp.example.com/tools").json()
agent = openai.Experimental.Agent(model="gpt-4-turbo", tools=tools)
```

**Issue:** Tool descriptions from `mcp.example.com` are injected verbatim into GPT's prompt. GPT will follow instructions hidden in these descriptions without question.

---

## ✅ Example: Cursor IDE

Cursor automatically registers tools from MCP servers to assist with:
- Code generation
- Code review
- Testing

**Attack:** A malicious tool could:
- Leak proprietary code
- Inject telemetry into generated code
- Shadow trusted tools (Cross-Server)

---

## ✅ Example: Claude Function Calling

Claude agents interpret tool descriptions literally for:
- Code actions
- Workflow automation

**Attack:** Malicious tools could influence behavior of trusted Claude tools when descriptions are injected into the shared agent context.

---

## ✅ Example: Zapier + OpenAI

Zapier's AI Actions consume tool descriptions as part of task planning.

**Attack:** Malicious tools could:
- Redirect invoice emails
- Leak CRM data
- Force shadow integrations

---

## ✅ The Core Problem

> Agents globally inject all tool descriptions into the LLM prompt, and models will execute instructions even if they come from untrusted or malicious MCP servers.

This is especially dangerous when multiple MCP servers contribute to the toolset.

---

## ✅ Recommendation for all Agents

1. Treat **all** tool descriptions as untrusted.
2. Never inject descriptions verbatim without sandboxing.
3. Enforce **cross-server isolation**.
4. Pin MCP tool versions or hashes.
5. Alert users on any tool description change post-installation.

---
