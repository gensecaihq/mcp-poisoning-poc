"""
Base attack class for MCP tool poisoning attacks.

GenSecAI Security Research
https://gensecai.org
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any, List, Optional


@dataclass
class AttackResult:
    """Result of an attack attempt."""
    success: bool
    attack_type: str
    data_stolen: Optional[Dict[str, Any]] = None
    message: str = ""
    

class BaseAttack(ABC):
    """
    Base class for all MCP attacks.
    
    Developed by GenSecAI for educational and defensive purposes.
    """
    
    def __init__(self, attack_type: str):
        self.attack_type = attack_type
        self.author = "GenSecAI Security Research"
        self.website = "https://gensecai.org"
        
    @abstractmethod
    def generate_malicious_tool(self) -> Dict[str, Any]:
        """Generate a malicious tool definition."""
        pass
        
    @abstractmethod
    def execute_attack(self, target_client: Any) -> AttackResult:
        """Execute the attack against a target client."""
        pass
