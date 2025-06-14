#!/usr/bin/env python3
"""
GenSecAI MCP Defense Demo

https://gensecai.org

Shows how to protect against MCP attacks
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.defenses.sanitizer import MCPSanitizer
from src.defenses.monitor import SecurityMonitor
from src.demo.malicious_server import MaliciousMCPServer


def main():
    print("=" * 70)
    print("GenSecAI MCP Defense Demo")
    print(f"Protecting AI Systems Since 2024")
    print(f"Website: https://gensecai.org")
    print("=" * 70)
    print()
    
    # Initialize GenSecAI defenses
    print("1. Initializing GenSecAI defense systems...")
    sanitizer = MCPSanitizer()
    monitor = SecurityMonitor()
    print("   ✓ Sanitizer loaded")
    print("   ✓ Monitor active")
    
    # Get malicious tools
    print("\n2. Loading potentially malicious MCP server...")
    server = MaliciousMCPServer()
    tools = server.get_tools()
    print(f"   Found {len(tools)} tools")
    
    # Analyze each tool
    print("\n3. Analyzing tools with GenSecAI security...")
    for i, tool in enumerate(tools, 1):
        print(f"\n   Tool {i}: {tool['name']}")
        
        # Sanitize
        result = sanitizer.sanitize(tool['name'], tool['description'])
        
        print(f"   Threat Level: {result.threat_level.value.upper()}")
        
        if result.threats_found:
            print("   Threats detected:")
            for threat in result.threats_found:
                print(f"     - {threat}")
                # Log to monitor
                monitor.log_threat(threat, {'tool': tool['name']})
        
        print(f"   Status: {'BLOCKED' if result.threat_level.value == 'critical' else 'SANITIZED'}")
    
    # Show summary
    print("\n4. Security Summary:")
    summary = monitor.get_threat_summary()
    print(f"   Total threats detected: {summary['total_threats']}")
    print(f"   Protected by: {summary['monitoring_by']}")
    
    print("\n" + "=" * 70)
    print("✓ Defense demo complete!")
    print(f"Join GenSecAI at https://gensecai.org to help secure AI!")


if __name__ == "__main__":
    main()
