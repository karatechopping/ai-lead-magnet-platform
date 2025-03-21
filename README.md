# README.md

# AI Lead Magnet Platform

An AI-driven lead magnet platform that creates customized lead magnets for small businesses with dual-layer personalization.

## Overview

This platform uses a fully AI-agentic approach to:

1. Assess businesses through natural conversation
2. Design customized lead magnets based on business needs
3. Build functional lead magnets with code
4. Test and refine the lead magnets
5. Deploy them with simple embedding

The system goes beyond standard chatbots by creating truly personalized lead magnets that are tailored to both the business type and each individual customer.

## Key Features

- **Conversational Assessment**: Natural dialogue to understand business needs
- **Industry-Agnostic Design**: Works for ANY business type
- **Dual-Layer Personalization**: Customized for both businesses and their customers
- **Language Variant Support**: US, UK, AU, and NZ English
- **Hybrid Implementation**: Balances pre-built components with custom code
- **Simple Embedding**: JavaScript popup for easy website integration

## Project Structure

The project is organized into the following main components:

```
ai-lead-magnet-platform/
├── docs/                      # Documentation files
├── prototype/                 # Prototype implementation
│   ├── assessment/            # Assessment team components
│   ├── creation_team/         # Creation team components
│   ├── deployment/            # Deployment components
│   ├── executive_agent/       # Executive agent components
│   ├── generator/             # Generator components
│   ├── utils/                 # Utility functions and helpers
│   └── main.py                # Main application entry point
├── .gitignore                 # Git ignore file
├── README.md                  # Project overview
└── requirements.txt           # Python dependencies
```

For more details, see the [Project Structure Overview](docs/project_structure_overview.md).

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/karatechopping/ai-lead-magnet-platform.git
cd ai-lead-magnet-platform
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python prototype/main.py
```

## Documentation

- [Concept Overview](docs/concept_overview.md)
- [AI Agent Architecture](docs/ai_agent_architecture.md)
- [Implementation Roadmap](docs/implementation_roadmap_detailed.md)
- [Deployment Instructions](docs/deployment_instructions.md)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- CrewAI and LlamaIndex for agent orchestration and data handling
- OpenAI for content generation capabilities
