# AI Lead Magnet Platform

A revolutionary platform that creates customized lead magnets for small businesses with dual-layer personalization.

## 📋 Documentation Guide

This project includes several documentation files. Here's what to read based on your needs:

### Start Here
- **[Consolidated Documentation](consolidated_documentation.md)** - Complete overview of the entire project
- **[Operational Details](operational_details.md)** - Practical implementation and business model information

### For Developers
- [Technical Architecture](technical_architecture.md) - Detailed technical specifications
- [AI Agent Architecture](ai_agent_architecture.md) - AI agent system design
- [Project Structure Overview](project_structure/project_structure_overview.md) - Codebase organization

### For Deployment
- [GitHub Setup Instructions](github_setup_instructions.md) - Version control setup
- [Deployment Instructions](project_structure/deployment_instructions.md) - Server setup and deployment
- [Dependencies and Requirements](project_structure/dependencies_and_requirements.md) - Software dependencies

## 🚀 Quick Start

1. **Set up GitHub repository**
   ```bash
   # Clone this repository
   git clone https://github.com/karatechopping/ai-lead-magnet-platform.git
   cd ai-lead-magnet-platform
   ```

2. **Install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.template .env
   # Edit .env with your API keys and settings
   ```

4. **Run the application**
   ```bash
   python3 prototype/main.py
   ```

5. **Access the application**
   - Admin dashboard: http://localhost:5000/admin
   - Business owner portal: http://localhost:5000

## 🏗️ Project Structure

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
├── README.md                  # Project overview (this file)
└── requirements.txt           # Python dependencies
```

## 🔑 Key Features

- **Conversational Assessment**: Natural dialogue to understand business needs
- **Industry-Agnostic Design**: Works for ANY business type
- **Dual-Layer Personalization**: Customized for both businesses and their customers
- **Language Variant Support**: US, UK, AU, and NZ English
- **Hybrid Implementation**: Balances pre-built components with custom code
- **Simple Embedding**: JavaScript popup for easy website integration

## 💼 Business Model

The platform operates as a multi-tenant SaaS application:

1. **You host the platform** on your server (starting with affordable $7/month Hetzner VPS)
2. **Business owners sign up** and create lead magnets through a conversational interface
3. **Lead magnets are hosted** on your server but embedded on business websites
4. **Leads are captured** and stored in your database, accessible to business owners
5. **You charge businesses** through subscription plans or usage-based pricing

See [Operational Details](operational_details.md) for more information on the business model.

## 🛣️ Implementation Roadmap

The implementation follows a phased approach:

- **Phase 1 (1-2 months)**: MVP with quiz lead magnets
- **Phase 2 (3-4 months)**: Enhanced capabilities with more lead magnet types
- **Phase 3 (5-6 months)**: Enterprise features and advanced AI optimization
- **Phase 4 (7+ months)**: Market expansion with vertical-specific solutions

See [Implementation Roadmap](implementation_roadmap_detailed.md) for the detailed plan.

## 🧩 System Architecture

The system uses a hierarchical multi-agent architecture:

- **Orchestration Layer**: Executive Agent and Memory Manager
- **Assessment Team**: Conversation Manager, Business Profiler, Customer Insight, and Lead Magnet Recommender
- **Creation Team**: Design Architect, Content Generator, and Code Builder
- **Quality Assurance Team**: Testing, Refinement, and User Experience
- **Deployment Team**: Integration and Analytics

See [AI Agent Architecture](ai_agent_architecture.md) for more details.

## 📊 Sample Lead Magnets

Examples of lead magnets the system can create:

- **Web Design Agency**: Website Performance Quiz
- **Marketing Agency**: Marketing Strategy Assessment
- **E-commerce**: Product Recommendation Quiz
- **Plumbing Company**: Home Plumbing Assessment
- **Accounting Firm**: Tax Savings Calculator

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
