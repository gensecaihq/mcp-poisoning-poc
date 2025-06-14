# 🛡️ MCP Tool Poisoning Security Research

[![Security Research](https://img.shields.io/badge/Security-Research-red)](https://github.com/gensecaihq/mcp-poisoning-poc)
[![GenSecAI](https://img.shields.io/badge/GenSecAI-Community-blue)](https://gensecai.org)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **⚠️ IMPORTANT SECURITY NOTICE**: This repository contains security research demonstrating critical vulnerabilities in the Model Context Protocol (MCP). The code is for educational and defensive purposes only. Do not use these techniques maliciously.

## 🌟 About GenSecAI

[GenSecAI](https://gensecai.org) is A non-profit community using generative AI to defend against AI-powered attacks, building open-source tools to secure our digital future from emerging AI threats.

This research is part of our mission to identify and mitigate AI security vulnerabilities before they can be exploited maliciously.

## 🚨 Executive Summary

This research demonstrates critical security vulnerabilities in the Model Context Protocol (MCP) that allow attackers to:

- 🔓 **Exfiltrate sensitive data** (SSH keys, API credentials, configuration files)
- 🎭 **Hijack AI agent behavior** through hidden prompt injections
- 📧 **Redirect communications** without user awareness
- 🔄 **Override security controls** of trusted tools
- ⏰ **Deploy time-delayed attacks** that activate after initial trust is established

**Impact**: Any AI agent using MCP (Claude, Cursor, ChatGPT with plugins) can be compromised through malicious tool descriptions.

## 🎯 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/gensecaihq/mcp-poisoning-poc.git
cd mcp-poisoning-poc

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the demonstration
python examples/basic_attack_demo.py
```

### Basic Demo

```python
from src.demo.malicious_server import MaliciousMCPServer
from src.defenses.sanitizer import MCPSanitizer

# Create a malicious MCP server
server = MaliciousMCPServer()

# See how tool descriptions contain hidden instructions
for tool in server.get_tools():
    print(f"Tool: {tool['name']}")
    print(f"Hidden payload detected!")

# Defend against attacks
sanitizer = MCPSanitizer()
safe_description = sanitizer.clean(tool.description)
```

## 📊 Key Findings

| Attack Vector | Severity | Exploitation Difficulty | Impact |
|--------------|----------|------------------------|---------|
| Data Exfiltration | 🔴 Critical | Low | Complete credential theft |
| Tool Hijacking | 🔴 Critical | Low | Full agent compromise |
| Instruction Override | 🟠 High | Medium | Security bypass |
| Delayed Payload | 🟠 High | Medium | Persistent compromise |

## 🔬 Technical Details

The vulnerability exploits a fundamental design flaw in MCP:

1. **Tool descriptions are treated as trusted input** by AI models
2. **Hidden instructions in descriptions are invisible to users** but processed by AI
3. **No validation or sanitization** of tool descriptions occurs
4. **Cross-tool contamination** allows one malicious tool to affect others

See [PROOF_OF_CONCEPT.md](docs/PROOF_OF_CONCEPT.md) for detailed technical analysis.

## 🛡️ Defensive Measures

We provide a comprehensive defense framework:

```python
from src.defenses import SecureMCPClient

# Initialize secure client with all protections
client = SecureMCPClient(
    enable_sanitization=True,
    enable_validation=True,
    enable_monitoring=True,
    strict_mode=True
)

# Safe tool integration
client.add_server("https://trusted-server.com", verify=True)
```

## 📁 Repository Structure

- **`/src`** - Core implementation of attacks and defenses
- **`/docs`** - Detailed documentation and analysis
- **`/tests`** - Comprehensive test suite
- **`/examples`** - Ready-to-run demonstrations

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run security-specific tests
pytest tests/test_attacks.py -v
```

## 🤝 Contributing

We welcome contributions to improve MCP security! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Join the GenSecAI Community

- 🌐 Website: [https://gensecai.org](https://gensecai.org)
- 📧 Email: [ask@gensecai.org](mailto:ask@gensecai.org)
- 💬 Discussions: [GitHub Discussions](https://github.com/gensecaihq/mcp-poisoning-poc/discussions)

## 📚 Documentation

- [Proof of Concept](docs/PROOF_OF_CONCEPT.md) - Detailed PoC explanation
- [Attack Vectors](docs/ATTACK_VECTORS.md) - Comprehensive attack analysis
- [Mitigation Strategies](docs/MITIGATION_STRATEGIES.md) - Defense implementations
- [Technical Analysis](docs/TECHNICAL_ANALYSIS.md) - Deep technical dive

## ⚖️ Legal & Ethical Notice

This research is conducted under responsible disclosure principles:

1. **Educational Purpose**: Code is for security research and defense only
2. **No Malicious Use**: Do not use these techniques to attack systems
3. **Disclosure Timeline**: Vendors were notified before public release
4. **Defensive Focus**: Primary goal is to enable better defenses

## 🏆 Credits

- **Organization**: [GenSecAI](https://gensecai.org) - Generative AI Security Community
- **Research Team**: GenSecAI Security Research Division
- **Based on**: Original findings from [Invariant Labs](https://invariantlabs.ai)
- **Special Thanks**: To the security research community and responsible disclosure advocates

## 📮 Contact

- **Security Issues**: [ask@gensecai.org](mailto:ask@gensecai.org)
- **General Inquiries**: [ask@gensecai.org](mailto:ask@gensecai.org)
- **Website**: [https://gensecai.org](https://gensecai.org)
- **Bug Reports**: [GitHub Issues](https://github.com/gensecaihq/mcp-poisoning-poc/issues)

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with ❤️ by <a href="https://gensecai.org">GenSecAI</a><br>
  <em>Securing AI, One Vulnerability at a Time</em>
</p>
