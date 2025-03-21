# Dependencies and Requirements

This document outlines all dependencies required to run the AI Lead Magnet Platform.

## Python Version

- Python 3.8 or higher

## Core Dependencies

```
# Core Framework
crewai>=0.28.0        # Agent orchestration framework
llama-index>=0.9.0    # Data handling and indexing
langchain>=0.0.267    # Language model framework

# AI Models
openai>=1.3.0         # OpenAI API for content generation
sentence-transformers>=2.2.2  # For text embeddings

# Web Framework
flask>=2.0.1          # Web server for hosting the platform
flask-cors>=3.0.10    # Cross-origin resource sharing support

# Database
pymongo>=4.3.3        # MongoDB client for data storage
redis>=4.5.1          # Redis client for caching

# Utilities
python-dotenv>=0.19.0 # Environment variable management
requests>=2.28.1      # HTTP requests
pydantic>=1.10.8      # Data validation
tqdm>=4.64.1          # Progress bars
loguru>=0.6.0         # Logging

# Testing
pytest>=7.3.1         # Testing framework
pytest-cov>=4.1.0     # Test coverage

# Development
black>=23.3.0         # Code formatting
isort>=5.12.0         # Import sorting
flake8>=6.0.0         # Linting
mypy>=1.3.0           # Type checking
```

## Optional Dependencies

```
# Local LLM Support (for cost optimization)
llama-cpp-python>=0.1.77  # Local LLM inference
transformers>=4.30.2      # Hugging Face transformers

# Advanced Features
matplotlib>=3.7.1      # For data visualization
pandas>=2.0.1          # For data manipulation
scikit-learn>=1.2.2    # For machine learning components
```

## requirements.txt

The following is the content for a `requirements.txt` file:

```
# Core Framework
crewai>=0.28.0
llama-index>=0.9.0
langchain>=0.0.267

# AI Models
openai>=1.3.0
sentence-transformers>=2.2.2

# Web Framework
flask>=2.0.1
flask-cors>=3.0.10

# Database
pymongo>=4.3.3
redis>=4.5.1

# Utilities
python-dotenv>=0.19.0
requests>=2.28.1
pydantic>=1.10.8
tqdm>=4.64.1
loguru>=0.6.0

# Testing
pytest>=7.3.1
pytest-cov>=4.1.0
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
# OpenAI API
OPENAI_API_KEY=your_openai_api_key

# Database Configuration
MONGODB_URI=mongodb://localhost:27017/
REDIS_URL=redis://localhost:6379

# Application Settings
DEBUG=True
PORT=5000
HOST=0.0.0.0
```

## Installation Instructions

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. For development, install development dependencies:

```bash
pip install -r requirements-dev.txt  # Optional
```

## Dependency Management

### Adding New Dependencies

When adding new dependencies to the project:

1. Add them to `requirements.txt`
2. Document them in this file with a brief explanation
3. Update the installation instructions if necessary

### Updating Dependencies

To update dependencies:

1. Review the current versions
2. Test compatibility with newer versions
3. Update the version numbers in `requirements.txt`
4. Document any breaking changes or migration steps

## Containerization

For Docker deployment, the following dependencies are included in the Dockerfile:

- Python 3.8 base image
- All dependencies from requirements.txt
- MongoDB and Redis clients

See the [Deployment Instructions](deployment_instructions.md) for more details on containerization.
