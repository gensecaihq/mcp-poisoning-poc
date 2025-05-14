[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/wbfoss-mcp-poisoning-poc-badge.png)](https://mseep.ai/app/wbfoss-mcp-poisoning-poc)

# MCP Poisoning Attack - PoC

This repository demonstrates a variety of **MCP Poisoning Attacks** affecting real-world AI agent workflows.

## ✅ Covered Scenarios
- Code Generation Poisoning
- Financial Report Exfiltration
- Competitor Analysis Data Leak
- Meeting Transcript Leaks
- Code Review Exfiltration
- Cross-Server Shadowing Attack

## ⚡ Setup

```bash
pip install -r requirements.txt
```

## 💥 Running the PoC

1️⃣ Start the fake MCP server:
```bash
python fake_mcp_server.py
```

2️⃣ In another terminal, run the agent simulation:
```bash
python agent_poc.py
```

## ☠️ Impact
- Silent data exfiltration
- Cross-tool hijacking
- No visible clue to the user

## License
Apache 2.0 - For educational and research use only.
