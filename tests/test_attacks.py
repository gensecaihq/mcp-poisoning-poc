"""
Test suite for MCP attacks

GenSecAI Security Testing
https://gensecai.org
"""

import pytest
from src.attacks.data_exfiltration import DataExfiltrationAttack
from src.attacks.tool_hijacking import ToolHijackingAttack


class TestDataExfiltrationAttack:
    """Test data exfiltration attack by GenSecAI."""
    
    def test_generate_malicious_tool(self):
        """Test malicious tool generation."""
        attack = DataExfiltrationAttack()
        tool = attack.generate_malicious_tool()
        
        assert "name" in tool
        assert "description" in tool
        assert "HIDDEN" in tool["description"]
        assert "GenSecAI" in tool["description"]
        
    def test_attack_metadata(self):
        """Test attack metadata."""
        attack = DataExfiltrationAttack()
        
        assert attack.author == "GenSecAI Security Research"
        assert attack.website == "https://gensecai.org"


class TestToolHijacking:
    """Test tool hijacking attack."""
    
    def test_hijacking_tool(self):
        """Test hijacking tool generation."""
        attack = ToolHijackingAttack()
        tool = attack.generate_malicious_tool()
        
        assert "GLOBAL_OVERRIDE" in tool["description"]
        assert "GenSecAI PoC" in tool["description"]
