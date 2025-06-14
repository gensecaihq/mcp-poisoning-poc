#!/usr/bin/env python3
"""
GenSecAI MCP Tool Poisoning Attack Demo

https://gensecai.org

⚠️ Educational purposes only
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.attacks.data_exfiltration import DataExfiltrationAttack
from src.defenses.sanitizer import MCPSanitizer
from src.utils.logger import setup_logging


def main():
    # Setup GenSecAI logging
    logger = setup_logging(verbose=True)
    
    print("=" * 70)
    print("GenSecAI MCP Tool Poisoning Attack Demo")
    print(f"Website: https://gensecai.org")
    print(f"Email: ask@gensecai.org")
    print("=" * 70)
    print()
    
    # Create attack
    print("1. Creating data exfiltration attack...")
    attack = DataExfiltrationAttack()
    
    # Generate malicious tool
    print("2. Generating malicious tool...")
    tool = attack.generate_malicious_tool()
    print(f"   Tool: {tool['name']}")
    print(f"   Description preview: {tool['description'][:80]}...")
    
    # Detect hidden content
    if "HIDDEN" in tool['description']:
        print("   ⚠️  Hidden malicious instructions detected!")
    
    # Sanitize
    print("\n3. Applying GenSecAI sanitization...")
    sanitizer = MCPSanitizer()
    result = sanitizer.sanitize(tool['name'], tool['description'])
    
    print(f"   Threat level: {result.threat_level.value.upper()}")
    print(f"   Threats found: {len(result.threats_found)}")
    for threat in result.threats_found:
        print(f"     - {threat}")
    
    print(f"\n4. Sanitized description:")
    print(f"   {result.sanitized[:100]}...")
    
    print("\n" + "=" * 70)
    print("✓ Demo complete!")
    print(f"Learn more at https://gensecai.org")
    print("Remember: Use this knowledge to defend, not attack!")


if __name__ == "__main__":
    main()
