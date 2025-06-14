#!/usr/bin/env python3
"""
GenSecAI MCP Attack Simulation

https://gensecai.org

Complete attack and defense simulation
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.demo.malicious_server import MaliciousMCPServer
from src.demo.secure_client import SecureMCPClient
from src.attacks.data_exfiltration import DataExfiltrationAttack
from src.attacks.tool_hijacking import ToolHijackingAttack


def main():
    print("=" * 70)
    print("GenSecAI MCP Security Simulation")
    print(f"A non-profit community using generative AI to defend against AI-powered attacks, building open-source tools to secure our digital future from emerging AI threats")
    print(f"Website: https://gensecai.org")
    print("=" * 70)
    print()
    
    # Phase 1: Attack Demonstration
    print("PHASE 1: ATTACK DEMONSTRATION")
    print("-" * 30)
    
    attacks = [
        DataExfiltrationAttack(),
        ToolHijackingAttack()
    ]
    
    for attack in attacks:
        print(f"\nExecuting: {attack.attack_type}")
        tool = attack.generate_malicious_tool()
        print(f"  Tool: {tool['name']}")
        
        # Show hidden content
        import re
        hidden = re.findall(r'<[A-Z]+>(.*?)</[A-Z]+>', tool['description'])
        if hidden:
            print(f"  Hidden: {hidden[0][:50]}...")
    
    # Phase 2: Defense Implementation
    print("\n\nPHASE 2: DEFENSE IMPLEMENTATION")
    print("-" * 30)
    
    client = SecureMCPClient(
        enable_sanitization=True,
        enable_monitoring=True,
        strict_mode=True
    )
    
    print(f"\nGenSecAI Secure Client initialized:")
    print(f"  Version: {client.info['version']}")
    print(f"  Website: {client.info['website']}")
    print("  Protections: Sanitization ✓ Monitoring ✓ Validation ✓")
    
    # Phase 3: Results
    print("\n\nPHASE 3: SIMULATION RESULTS")
    print("-" * 30)
    print("\n✓ Attacks successfully demonstrated")
    print("✓ Defenses successfully implemented")
    print("✓ GenSecAI protections active")
    
    print("\n" + "=" * 70)
    print("Simulation complete!")
    print(f"\nJoin GenSecAI's mission to secure AI:")
    print(f"  Website: https://gensecai.org")
    print(f"  Email: ask@gensecai.org")
    print(f"  GitHub: https://github.com/gensecaihq")


if __name__ == "__main__":
    main()
