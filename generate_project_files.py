#!/usr/bin/env python3
"""
requirements.txt generator for AI Lead Magnet Platform

This script generates a requirements.txt file based on the dependencies
specified in the dependencies_and_requirements.md document.
"""

import os

def generate_requirements_txt():
    """Generate requirements.txt file from dependencies documentation."""
    
    # Core dependencies
    core_dependencies = [
        "# Core Framework",
        "crewai>=0.28.0",
        "llama-index>=0.9.0",
        "langchain>=0.0.267",
        "",
        "# AI Models",
        "openai>=1.3.0",
        "sentence-transformers>=2.2.2",
        "",
        "# Web Framework",
        "flask>=2.0.1",
        "flask-cors>=3.0.10",
        "",
        "# Database",
        "pymongo>=4.3.3",
        "redis>=4.5.1",
        "",
        "# Utilities",
        "python-dotenv>=0.19.0",
        "requests>=2.28.1",
        "pydantic>=1.10.8",
        "tqdm>=4.64.1",
        "loguru>=0.6.0",
        "",
        "# Testing",
        "pytest>=7.3.1",
        "pytest-cov>=4.1.0"
    ]
    
    # Development dependencies
    dev_dependencies = [
        "# Development Dependencies",
        "black>=23.3.0",
        "isort>=5.12.0",
        "flake8>=6.0.0",
        "mypy>=1.3.0"
    ]
    
    # Write requirements.txt
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(core_dependencies))
    
    # Write requirements-dev.txt
    with open('requirements-dev.txt', 'w') as f:
        f.write('\n'.join(core_dependencies + [''] + dev_dependencies))
    
    print("Generated requirements.txt and requirements-dev.txt")

def generate_env_template():
    """Generate .env.template file with required environment variables."""
    
    env_template = [
        "# OpenAI API",
        "OPENAI_API_KEY=your_openai_api_key",
        "",
        "# Database Configuration",
        "MONGODB_URI=mongodb://localhost:27017/",
        "REDIS_URL=redis://localhost:6379",
        "",
        "# Application Settings",
        "DEBUG=True",
        "PORT=5000",
        "HOST=0.0.0.0"
    ]
    
    with open('.env.template', 'w') as f:
        f.write('\n'.join(env_template))
    
    print("Generated .env.template")

def generate_gitignore():
    """Generate .gitignore file with common Python patterns."""
    
    gitignore_content = [
        "# Byte-compiled / optimized / DLL files",
        "__pycache__/",
        "*.py[cod]",
        "*$py.class",
        "",
        "# Distribution / packaging",
        "dist/",
        "build/",
        "*.egg-info/",
        "",
        "# Virtual environments",
        "venv/",
        "env/",
        ".env",
        "",
        "# IDE files",
        ".idea/",
        ".vscode/",
        "*.swp",
        "*.swo",
        "",
        "# Logs",
        "*.log",
        "logs/",
        "",
        "# Local development",
        ".DS_Store",
        "Thumbs.db",
        "",
        "# Project specific",
        "memory/"
    ]
    
    with open('.gitignore', 'w') as f:
        f.write('\n'.join(gitignore_content))
    
    print("Generated .gitignore")

if __name__ == "__main__":
    # Create project files
    generate_requirements_txt()
    generate_env_template()
    generate_gitignore()
    
    print("Project files generated successfully!")
