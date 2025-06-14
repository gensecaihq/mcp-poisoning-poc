"""
Setup configuration for GenSecAI MCP Tool Poisoning PoC
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gensecai-mcp-poisoning-poc",
    version="1.0.0",
    author="GenSecAI",
    author_email="ask@gensecai.org",
    description="MCP Tool Poisoning Security Research by GenSecAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gensecaihq/mcp-poisoning-poc",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "aiohttp>=3.9.0",
        "pydantic>=2.0.0",
        "pytest>=7.4.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research", 
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    project_urls={
        "GenSecAI": "https://gensecai.org",
        "Bug Reports": "https://github.com/gensecaihq/mcp-poisoning-poc/issues",
        "Source": "https://github.com/gensecaihq/mcp-poisoning-poc",
    },
)
