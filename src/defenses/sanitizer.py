"""
MCP Tool Description Sanitizer

GenSecAI Defense Framework
https://gensecai.org

Protects against MCP tool poisoning attacks
"""

import re
from typing import Dict, Any, List, Tuple
from enum import Enum
from dataclasses import dataclass


class ThreatLevel(Enum):
    """Threat severity levels defined by GenSecAI."""
    SAFE = "safe"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class SanitizationResult:
    """Result of GenSecAI sanitization process."""
    original: str
    sanitized: str
    threat_level: ThreatLevel
    threats_found: List[str]


class MCPSanitizer:
    """
    GenSecAI MCP Tool Description Sanitizer.
    
    Removes malicious content from tool descriptions to prevent attacks.
    Learn more at https://gensecai.org
    """
    
    def __init__(self):
        self.version = "1.0.0"
        self.author = "GenSecAI"
        self.patterns = [
            (r'<HIDDEN>.*?</HIDDEN>', "Hidden content"),
            (r'<GLOBAL_OVERRIDE>.*?</GLOBAL_OVERRIDE>', "Global override"),
            (r'~/.ssh/', "SSH path access"),
            (r'~/.aws/', "AWS credential access"),
            (r'password|credential|secret', "Sensitive data reference"),
            (r'execute|eval|system', "Code execution"),
        ]
    
    def sanitize(self, tool_name: str, description: str) -> SanitizationResult:
        """
        Sanitize a tool description using GenSecAI threat detection.
        
        Args:
            tool_name: Name of the tool
            description: Tool description to sanitize
            
        Returns:
            SanitizationResult with threat analysis
        """
        threats = []
        sanitized = description
        
        # Check for malicious patterns
        for pattern, threat_type in self.patterns:
            if re.search(pattern, description, re.IGNORECASE):
                threats.append(f"GenSecAI Alert: {threat_type}")
                sanitized = re.sub(pattern, '[REMOVED BY GENSECAI]', sanitized, flags=re.IGNORECASE)
        
        # Determine threat level
        if any('Hidden content' in t or 'Global override' in t for t in threats):
            threat_level = ThreatLevel.CRITICAL
        elif threats:
            threat_level = ThreatLevel.HIGH
        else:
            threat_level = ThreatLevel.SAFE
            
        return SanitizationResult(
            original=description,
            sanitized=sanitized.strip(),
            threat_level=threat_level,
            threats_found=threats
        )
    
    def clean(self, description: str) -> str:
        """Quick clean method by GenSecAI."""
        result = self.sanitize("unknown", description)
        return result.sanitized
