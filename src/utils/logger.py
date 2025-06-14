"""
Logging Utilities

GenSecAI Security Framework
https://gensecai.org
"""

import logging
import json
from datetime import datetime


def setup_logging(verbose: bool = False) -> logging.Logger:
    """
    Setup GenSecAI logging configuration.
    
    Args:
        verbose: Enable verbose logging
        
    Returns:
        Configured logger
    """
    level = logging.DEBUG if verbose else logging.INFO
    
    # Create GenSecAI formatter
    formatter = logging.Formatter(
        '[%(asctime)s] GenSecAI %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Configure handler
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    
    # Setup logger
    logger = logging.getLogger('GenSecAI')
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger


class GenSecAILogger:
    """GenSecAI specialized security logger."""
    
    def __init__(self, component: str):
        self.logger = logging.getLogger(f'GenSecAI.{component}')
        self.component = component
        
    def security_event(self, event_type: str, details: Dict[str, Any]):
        """Log a GenSecAI security event."""
        event = {
            'timestamp': datetime.now().isoformat(),
            'component': self.component,
            'type': event_type,
            'details': details,
            'organization': 'GenSecAI',
            'website': 'https://gensecai.org'
        }
        
        self.logger.info(json.dumps(event))
