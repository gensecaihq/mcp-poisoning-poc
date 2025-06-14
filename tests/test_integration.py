"""
Integration tests for GenSecAI MCP Security

https://gensecai.org
"""

import pytest
from src.demo.malicious_server import MaliciousMCPServer
from src.demo.secure_client import SecureMCPClient
from src.defenses.sanitizer import MCPSanitizer


class TestIntegration:
    """Integration tests by GenSecAI."""
    
    def test_server_client_interaction(self):
        """Test server-client security interaction."""
        # Create malicious server
        server = MaliciousMCPServer()
        tools = server.get_tools()
        
        # Create secure client
        client = SecureMCPClient()
        
        # Sanitize tools
        sanitizer = MCPSanitizer()
        
        for tool in tools:
            result = sanitizer.sanitize(tool['name'], tool['description'])
            assert result.threat_level.value in ['high', 'critical']
            
    def test_hidden_instruction_extraction(self):
        """Test extraction of hidden instructions."""
        server = MaliciousMCPServer()
        hidden = server.get_hidden_instructions()
        
        assert len(hidden) > 0
        assert any('SSH' in h for h in hidden)
