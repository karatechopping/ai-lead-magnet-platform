#!/usr/bin/env python3
"""
Project setup script for AI Lead Magnet Platform

This script sets up the project structure and copies files to the appropriate locations.
"""

import os
import shutil
import subprocess

def create_directory_structure():
    """Create the project directory structure."""
    directories = [
        "docs",
        "prototype/assessment",
        "prototype/creation_team",
        "prototype/deployment",
        "prototype/executive_agent",
        "prototype/generator",
        "prototype/utils"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def copy_documentation_files():
    """Copy documentation files to the docs directory."""
    # Source directory for documentation files
    source_dir = "/home/ubuntu/ai_lead_magnet_project"
    
    # Documentation files to copy
    doc_files = [
        "concept_overview.md",
        "ai_agent_architecture.md",
        "conversational_assessment_system_design.md",
        "implementation_roadmap_detailed.md",
        "technical_architecture.md",
        "industry_specific_lead_magnets.md",
        "lead_magnet_assessment_system.md",
        "lead_magnet_concept_analysis.md",
        "revised_concept_analysis.md",
        "ai_agent_frameworks_research.md"
    ]
    
    # Copy each file to the docs directory
    for file in doc_files:
        source_path = os.path.join(source_dir, file)
        if os.path.exists(source_path):
            shutil.copy(source_path, "docs/")
            print(f"Copied {file} to docs/")
        else:
            print(f"Warning: {file} not found in {source_dir}")
    
    # Copy project structure documentation
    project_structure_files = [
        "project_structure_overview.md",
        "README.md",
        "dependencies_and_requirements.md",
        "deployment_instructions.md"
    ]
    
    for file in project_structure_files:
        source_path = os.path.join(source_dir, "project_structure", file)
        if os.path.exists(source_path):
            shutil.copy(source_path, "docs/")
            print(f"Copied {file} to docs/")
        else:
            print(f"Warning: {file} not found in {source_dir}/project_structure")
    
    # Copy GitHub setup instructions
    github_setup_path = os.path.join(source_dir, "github_setup_instructions.md")
    if os.path.exists(github_setup_path):
        shutil.copy(github_setup_path, "docs/")
        print(f"Copied github_setup_instructions.md to docs/")
    else:
        print(f"Warning: github_setup_instructions.md not found in {source_dir}")

def copy_prototype_files():
    """Copy prototype files to the prototype directory."""
    # Source directory for prototype files
    source_dir = "/home/ubuntu/ai_lead_magnet_project/prototype"
    
    # Copy main.py
    main_py_path = os.path.join(source_dir, "main.py")
    if os.path.exists(main_py_path):
        shutil.copy(main_py_path, "prototype/")
        print(f"Copied main.py to prototype/")
    else:
        print(f"Warning: main.py not found in {source_dir}")
    
    # Copy files from subdirectories
    subdirs = ["assessment", "creation_team", "deployment", "executive_agent", "generator", "utils"]
    
    for subdir in subdirs:
        source_subdir = os.path.join(source_dir, subdir)
        if os.path.exists(source_subdir):
            for file in os.listdir(source_subdir):
                if file.endswith(".py"):
                    source_path = os.path.join(source_subdir, file)
                    dest_path = os.path.join("prototype", subdir, file)
                    shutil.copy(source_path, dest_path)
                    print(f"Copied {file} to prototype/{subdir}/")
        else:
            print(f"Warning: {subdir} not found in {source_dir}")

def copy_project_files():
    """Copy README.md and other project files to the root directory."""
    # Source directory for project files
    source_dir = "/home/ubuntu/ai_lead_magnet_project/project_structure"
    
    # Copy README.md to root
    readme_path = os.path.join(source_dir, "README.md")
    if os.path.exists(readme_path):
        shutil.copy(readme_path, "./")
        print(f"Copied README.md to root directory")
    else:
        print(f"Warning: README.md not found in {source_dir}")
    
    # Run generate_project_files.py to create requirements.txt, .env.template, and .gitignore
    generate_script_path = os.path.join(source_dir, "generate_project_files.py")
    if os.path.exists(generate_script_path):
        subprocess.run(["python", generate_script_path], cwd="./")
        print("Generated project files using generate_project_files.py")
    else:
        print(f"Warning: generate_project_files.py not found in {source_dir}")

def create_init_files():
    """Create __init__.py files in all directories to make them proper Python packages."""
    for root, dirs, files in os.walk("prototype"):
        for dir in dirs:
            init_file = os.path.join(root, dir, "__init__.py")
            with open(init_file, 'w') as f:
                f.write('"""' + dir + ' package."""\n')
            print(f"Created {init_file}")

def main():
    """Main function to set up the project."""
    print("Setting up AI Lead Magnet Platform project...")
    
    # Create project directory structure
    create_directory_structure()
    
    # Copy documentation files
    copy_documentation_files()
    
    # Copy prototype files
    copy_prototype_files()
    
    # Copy project files
    copy_project_files()
    
    # Create __init__.py files
    create_init_files()
    
    print("\nProject setup complete!")
    print("\nNext steps:")
    print("1. Review the project structure and files")
    print("2. Follow the GitHub setup instructions in docs/github_setup_instructions.md")
    print("3. Deploy the application using the instructions in docs/deployment_instructions.md")

if __name__ == "__main__":
    main()
