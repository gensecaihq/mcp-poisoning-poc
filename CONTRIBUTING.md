# Contributing to GenSecAI MCP Security Research

Thank you for your interest in contributing to GenSecAI's mission of securing AI systems!

## About GenSecAI

[GenSecAI](https://gensecai.org) is A non-profit community using generative AI to defend against AI-powered attacks, building open-source tools to secure our digital future from emerging AI threats.

## How to Contribute

### Joining the Community

1. Visit [https://gensecai.org](https://gensecai.org)
2. Join our discussions on [GitHub](https://github.com/gensecaihq/mcp-poisoning-poc/discussions)
3. Contact us at ask@gensecai.org

### Reporting Security Issues

See [SECURITY.md](SECURITY.md) for security issue reporting.

### Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-attack-vector`)
3. Commit your changes (`git commit -am 'Add new attack vector'`)
4. Push to the branch (`git push origin feature/new-attack-vector`)
5. Create a Pull Request

### Contribution Guidelines

#### Code Style

- Follow PEP 8
- Use type hints
- Add docstrings to all functions/classes
- Run formatters: `black src/ tests/`

#### Testing

- Write tests for new features
- Maintain >80% code coverage
- Run tests: `pytest tests/`

#### Documentation

- Update relevant documentation
- Add examples for new features
- Keep README.md current

### Types of Contributions

#### 🔍 New Attack Vectors
- Novel exploitation techniques
- Improved evasion methods
- Real-world attack scenarios

#### 🛡️ Defense Mechanisms
- Detection algorithms
- Sanitization improvements
- Monitoring tools

#### 📚 Documentation
- Clarifications
- Additional examples
- Translation

#### 🧪 Testing
- Edge cases
- Performance tests
- Integration tests

### Pull Request Process

1. Update CHANGELOG.md
2. Pass all CI checks
3. Get review from GenSecAI maintainers
4. Squash commits if requested

### Code of Conduct

As part of the GenSecAI community, we expect:

- Respectful and inclusive behavior
- Focus on constructive criticism
- Helping others learn
- Following responsible disclosure
- Supporting our mission of AI security

### Recognition

Contributors will be:
- Added to AUTHORS.md file
- Listed on GenSecAI website
- Invited to GenSecAI events
- Eligible for GenSecAI certificates

## Development Setup

```bash
# Clone repository
git clone https://github.com/gensecaihq/mcp-poisoning-poc.git
cd mcp-poisoning-poc

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest
```

## Questions?

- Open a discussion on [GitHub](https://github.com/gensecaihq/mcp-poisoning-poc/discussions)
- Email: ask@gensecai.org
- Visit: https://gensecai.org

---

Thank you for helping GenSecAI secure our AI-powered future! 🛡️
