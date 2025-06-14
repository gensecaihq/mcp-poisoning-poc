"""
Real-time Security Monitor

GenSecAI Threat Detection System
https://gensecai.org
"""

import logging
from datetime import datetime
from typing import Dict, Any, List


class SecurityMonitor:
    """
    GenSecAI Real-time Security Monitor for MCP.
    
    Detects and logs potential security threats in real-time.
    """
    
    def __init__(self):
        self.logger = logging.getLogger('GenSecAI.Monitor')
        self.events = []
        
    def log_threat(self, threat_type: str, details: Dict[str, Any]):
        """Log a security threat detected by GenSecAI."""
        event = {
            'timestamp': datetime.now().isoformat(),
            'type': threat_type,
            'details': details,
            'source': 'GenSecAI Security Monitor'
        }
        
        self.events.append(event)
        self.logger.warning(f"GenSecAI Alert: {threat_type} - {details}")
        
    def get_threat_summary(self) -> Dict[str, Any]:
        """Get summary of threats detected by GenSecAI."""
        return {
            'total_threats': len(self.events),
            'monitoring_by': 'GenSecAI',
            'website': 'https://gensecai.org',
            'events': self.events[-10:]  # Last 10 events
        }
