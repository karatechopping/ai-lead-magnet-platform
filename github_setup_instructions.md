# GitHub Setup Instructions

This document provides step-by-step instructions for setting up version control for the AI Lead Magnet Platform using GitHub.

## Prerequisites

- GitHub account (username: karatechopping)
- Git installed on your local machine
- Basic familiarity with Git commands

## Setup Instructions

### 1. Create a New GitHub Repository

1. Log in to your GitHub account (karatechopping)
2. Click the "+" icon in the top-right corner and select "New repository"
3. Name the repository `ai-lead-magnet-platform`
4. Add a description: "AI-driven lead magnet platform for small businesses"
5. Choose "Private" for repository visibility (recommended for business projects)
6. Check "Add a README file"
7. Add a .gitignore file with "Python" template
8. Choose a license (MIT License recommended for flexibility)
9. Click "Create repository"

### 2. Clone the Repository to Your Local Machine

```bash
# Navigate to your desired directory
cd /path/to/your/projects

# Clone the repository
git clone https://github.com/karatechopping/ai-lead-magnet-platform.git

# Navigate into the project directory
cd ai-lead-magnet-platform
```

### 3. Set Up Project Structure

```bash
# Create project directories
mkdir -p prototype/{assessment,creation_team,deployment,executive_agent,generator,utils}
mkdir -p docs
```

### 4. Copy Project Files

```bash
# Copy documentation files to docs directory
cp /path/to/ai_lead_magnet_project/*.md docs/

# Copy prototype files
cp -r /path/to/ai_lead_magnet_project/prototype/* prototype/
```

### 5. Create Initial Commit

```bash
# Add all files to staging
git add .

# Commit the changes
git commit -m "Initial commit: Project structure and documentation"

# Push to GitHub
git push origin main
```

## Git Workflow for Development

### 1. Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature/new-feature-name
```

### 2. Make Changes and Commit

```bash
# Add changes to staging
git add .

# Commit changes
git commit -m "Descriptive message about the changes"
```

### 3. Push Changes to GitHub

```bash
# Push the feature branch to GitHub
git push origin feature/new-feature-name
```

### 4. Create a Pull Request

1. Go to your repository on GitHub
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select your feature branch to merge into main
5. Add a title and description
6. Click "Create pull request"

### 5. Merge the Pull Request

1. Review the changes
2. Click "Merge pull request" (if there are no conflicts)
3. Click "Confirm merge"
4. Delete the branch (optional)

## Git Best Practices

1. **Commit Often**: Make small, focused commits that address a single issue or feature
2. **Write Clear Commit Messages**: Use descriptive commit messages that explain what changes were made and why
3. **Use Branches**: Create separate branches for different features or bug fixes
4. **Pull Before Push**: Always pull the latest changes before pushing to avoid conflicts
5. **Review Changes**: Review your changes before committing to catch any issues early

## GitHub Actions (Optional)

You can set up GitHub Actions for automated testing and deployment:

1. Create a `.github/workflows` directory in your repository
2. Add workflow files (e.g., `test.yml`, `deploy.yml`) to define CI/CD pipelines
3. Configure workflows to run tests, build the application, and deploy to your hosting environment

## Additional Resources

- [GitHub Documentation](https://docs.github.com/en)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
