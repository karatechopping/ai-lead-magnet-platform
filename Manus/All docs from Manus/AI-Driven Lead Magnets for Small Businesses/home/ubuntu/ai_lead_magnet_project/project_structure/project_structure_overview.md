# Project Structure and Documentation

This document provides an overview of the AI Lead Magnet Platform project structure, explaining the purpose of each component and how they work together.

## Project Overview

The AI Lead Magnet Platform is organized into the following main components:

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

## Component Descriptions

### Documentation (`docs/`)

Contains all project documentation:

- `concept_overview.md` - High-level overview of the AI Lead Magnet concept
- `ai_agent_architecture.md` - Detailed architecture of the AI agent system
- `conversational_assessment_system_design.md` - Design of the assessment system
- `implementation_roadmap_detailed.md` - Phased implementation plan
- `technical_architecture.md` - Technical architecture and components
- `industry_specific_lead_magnets.md` - Examples of lead magnets by industry
- `lead_magnet_assessment_system.md` - Assessment system design
- `lead_magnet_concept_analysis.md` - Analysis of the lead magnet concept
- `revised_concept_analysis.md` - Updated concept analysis
- `ai_agent_frameworks_research.md` - Research on AI agent frameworks

### Prototype Implementation (`prototype/`)

#### Executive Agent (`prototype/executive_agent/`)

The Executive Agent coordinates the overall workflow and manages the project state:

- `executive_agent.py` - Main Executive Agent implementation
- Contains the `ExecutiveAgent` class that orchestrates the entire lead magnet creation process

#### Assessment Team (`prototype/assessment/`)

Handles the conversational assessment of businesses:

- `engine.py` - Assessment engine that processes business information
- `questionnaire.py` - Manages the conversational questionnaire flow

#### Creation Team (`prototype/creation_team/`)

Responsible for designing and building lead magnets:

- `quiz_lead_magnet_creator.py` - Implementation for quiz-based lead magnets
- Contains `DesignArchitectAgent`, `ContentGeneratorAgent`, and `CodeBuilderAgent` classes

#### Deployment (`prototype/deployment/`)

Handles the deployment and embedding of lead magnets:

- `deployment.py` - Manages the deployment process and embedding code generation

#### Generator (`prototype/generator/`)

Generates lead magnet content and structure:

- `generator.py` - Core generator functionality for lead magnets

#### Utils (`prototype/utils/`)

Utility functions and helper classes:

- `memory_manager.py` - Manages memory and context sharing between agents

#### Main Application (`prototype/main.py`)

The entry point for the application that ties all components together.

## Code Organization

The codebase follows these organizational principles:

1. **Agent-Based Architecture**: The system is organized around specialized agents with clear responsibilities
2. **Separation of Concerns**: Each component handles a specific aspect of the lead magnet creation process
3. **Modular Design**: Components are designed to be modular and reusable
4. **Memory Management**: A central memory system enables context sharing between agents

## Key Workflows

### Lead Magnet Creation Workflow

1. **Assessment**: The Executive Agent initiates the assessment process
   - Conversation Manager Agent guides the overall flow
   - Business Profiler Agent gathers business information
   - Customer Insight Agent explores customer pain points
   - Lead Magnet Recommender Agent suggests appropriate lead magnets

2. **Creation**: The Creation Team builds the lead magnet
   - Design Architect Agent creates the structure and flow
   - Content Generator Agent creates the content
   - Code Builder Agent implements the functionality

3. **Quality Assurance**: The lead magnet is tested and refined
   - Testing Agent verifies functionality
   - Refinement Agent incorporates feedback
   - User Experience Agent ensures usability

4. **Deployment**: The lead magnet is prepared for deployment
   - Integration Agent generates embedding code
   - Analytics Agent sets up performance tracking

## Development Guidelines

1. **Code Style**: Follow PEP 8 guidelines for Python code
2. **Documentation**: Document all classes and methods with docstrings
3. **Testing**: Write unit tests for all components
4. **Error Handling**: Implement robust error handling throughout the codebase
5. **Logging**: Use the logging module for debugging and monitoring

## Future Development

The codebase is designed to be extended with:

1. Additional lead magnet types beyond quizzes
2. Enhanced personalization capabilities
3. More sophisticated AI models for content generation
4. Advanced analytics and optimization features

For more detailed information, refer to the implementation roadmap in `docs/implementation_roadmap_detailed.md`.
