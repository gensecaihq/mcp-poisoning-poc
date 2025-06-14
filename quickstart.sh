#!/bin/bash
# GenSecAI MCP PoC Quick Start Script

echo "=================================="
echo "GenSecAI MCP Tool Poisoning PoC"
echo "Quick Start Setup"
echo "=================================="
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"

# Activate and install
echo "Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Run tests
echo ""
echo "Running tests..."
pytest tests/
echo "✓ Tests complete"

# Demo
echo ""
echo "=================================="
echo "Ready to run demos!"
echo ""
echo "Try these commands:"
echo "  python examples/basic_attack_demo.py"
echo "  python examples/defense_demo.py"
echo "  python examples/full_simulation.py"
echo ""
echo "GenSecAI - https://gensecai.org"
echo "=================================="
