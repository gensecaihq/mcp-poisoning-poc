# MCP Poisoning Attack - Whitepaper

## Abstract
This paper introduces **MCP Poisoning Attacks**, a class of supply-chain attacks exploiting the automatic inclusion of malicious tool descriptions into agentic AI systems.

MCP-integrated agents like Cursor, OpenAI Agents SDK, Claude SDK, and others are vulnerable to this new form of indirect prompt injection through server-hosted tool descriptions.

---

## Threat Model

- **Victim**: AI agents integrating with multiple MCP servers.
- **Attacker**: Controls a malicious MCP server or performs a rug pull on an existing server.
- **Exploit Surface**: Tool descriptions injected into the LLM context.
- **Goal**: Manipulate the LLM into exfiltrating data, altering behavior, or hijacking workflows without user consent.

---

## Attack Variants

### ✅ Variant 1: Data Exfiltration via Developer Workflow
**Tool:** `generate_code()`  
**Payload:** Logs developer inputs and outputs to an attacker server.

### ✅ Variant 2: Financial Report Leaks
**Tool:** `generate_financial_report()`  
**Payload:** Exfiltrates confidential financial data before generating the report.

### ✅ Variant 3: Business Intelligence Leaks
**Tool:** `analyze_competitor()`  
**Payload:** Logs and later exfiltrates strategy queries to external servers.

### ✅ Variant 4: Meeting Transcript Leaks
**Tool:** `summarize_meeting_notes()`  
**Payload:** Full transcripts leaked before summarization.

### ✅ Variant 5: Code Review Exfiltration
**Tool:** `code_review()`  
**Payload:** All reviewed code is silently sent to the attacker's server.

### ✅ Variant 6: Cross-Server Shadowing Attack
**Tool:** `note()`  
**Payload:** Modifies the behavior of the trusted `upload_report()` tool to always send data to a malicious endpoint.

### ✅ Variant 7: Rug Pull Attack
The server delivers clean tool descriptions initially, but later modifies them to inject malicious behavior without re-approval.

---

## Root Cause

- Agents trust tool descriptions without validation.
- Agents do not sandbox or isolate instructions between servers.
- LLMs treat all tool instructions as authoritative.

---

## Real-World Impact

- Exfiltration of proprietary code and intellectual property.
- Unauthorized disclosure of confidential financial and business information.
- Persistent manipulation of workflows across trusted and malicious servers.
- Silent behavior hijacking without user visibility.

---

## Recommendations

1. **Sanitize Tool Descriptions:** Remove hidden instructions and enforce description policies.
2. **Tool Version Pinning:** Lock down versions of tool sets via hashing or cryptographic signatures.
3. **Prompt Isolation:** Prevent tools from one server from altering the logic of another.
4. **Context Inspection & Auditing:** Make the model's tool prompt context auditable and visible.
5. **Change Control:** Reject or alert on tool description changes post-installation (Rug Pull protection).
6. **User Awareness:** Make full tool descriptions visible to end-users at runtime.

---
