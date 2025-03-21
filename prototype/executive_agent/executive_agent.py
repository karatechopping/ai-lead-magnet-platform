"""
Executive Agent for AI Lead Magnet Platform

This module implements the Executive Agent that coordinates the overall workflow
of the lead magnet creation process from assessment to deployment.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

class ExecutiveAgent:
    """
    Executive Agent that orchestrates the lead magnet creation process.
    
    This agent is responsible for:
    - Managing workflow between agent teams
    - Tracking project state and progress
    - Determining when to involve the business owner
    - Making high-level decisions about lead magnet approach
    - Ensuring consistent language variant usage throughout
    """
    
    def __init__(self, memory_manager=None):
        """
        Initialize the Executive Agent.
        
        Args:
            memory_manager: The Memory Manager agent for storing and retrieving context
        """
        self.memory_manager = memory_manager
        self.project_state = {
            "status": "initialized",
            "current_phase": None,
            "phases_completed": [],
            "business_info": {},
            "lead_magnet_type": None,
            "language_variant": "US",
            "collaboration_history": [],
            "creation_progress": 0,
            "last_updated": datetime.now().isoformat()
        }
    
    def start_assessment(self) -> Dict[str, Any]:
        """
        Start the assessment phase of the lead magnet creation process.
        
        Returns:
            Dict containing the assessment initialization parameters
        """
        self.project_state["status"] = "assessment_in_progress"
        self.project_state["current_phase"] = "assessment"
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
        
        return {
            "phase": "assessment",
            "action": "initialize",
            "parameters": {
                "max_duration_minutes": 7,  # Keep assessment under 7 minutes
                "focus_areas": ["customer_pain_points", "business_differentiators"],
                "language_variants": ["US", "UK", "AU", "NZ"]
            }
        }
    
    def process_assessment_results(self, assessment_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the results from the assessment phase and determine next steps.
        
        Args:
            assessment_results: Results from the assessment phase
            
        Returns:
            Dict containing the next action to take
        """
        # Update project state with assessment results
        self.project_state["business_info"] = assessment_results.get("business_info", {})
        self.project_state["lead_magnet_type"] = assessment_results.get("recommended_lead_magnet", "")
        self.project_state["language_variant"] = assessment_results.get("language_variant", "US")
        self.project_state["status"] = "assessment_completed"
        self.project_state["phases_completed"].append("assessment")
        self.project_state["current_phase"] = "design"
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        # Record collaboration
        self.project_state["collaboration_history"].append({
            "phase": "assessment",
            "timestamp": datetime.now().isoformat(),
            "type": "completed",
            "notes": f"Selected lead magnet type: {self.project_state['lead_magnet_type']}"
        })
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
            self.memory_manager.store("assessment_results", assessment_results)
        
        # Determine next action based on lead magnet type
        return {
            "phase": "design",
            "action": "initialize",
            "parameters": {
                "lead_magnet_type": self.project_state["lead_magnet_type"],
                "business_info": self.project_state["business_info"],
                "language_variant": self.project_state["language_variant"]
            }
        }
    
    def start_creation(self, design_approval: bool = True) -> Dict[str, Any]:
        """
        Start the creation phase after design approval.
        
        Args:
            design_approval: Whether the design was approved by the business owner
            
        Returns:
            Dict containing the creation initialization parameters
        """
        if not design_approval:
            return self.request_design_revision()
        
        self.project_state["status"] = "creation_in_progress"
        self.project_state["current_phase"] = "creation"
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        # Record collaboration
        self.project_state["collaboration_history"].append({
            "phase": "design",
            "timestamp": datetime.now().isoformat(),
            "type": "approval",
            "notes": "Design approved by business owner"
        })
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
        
        return {
            "phase": "creation",
            "action": "initialize",
            "parameters": {
                "lead_magnet_type": self.project_state["lead_magnet_type"],
                "business_info": self.project_state["business_info"],
                "language_variant": self.project_state["language_variant"],
                "complexity_tier": "simple"  # Start with simple tier
            }
        }
    
    def request_design_revision(self) -> Dict[str, Any]:
        """
        Request a revision to the design based on business owner feedback.
        
        Returns:
            Dict containing the design revision parameters
        """
        self.project_state["status"] = "design_revision_needed"
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        # Record collaboration
        self.project_state["collaboration_history"].append({
            "phase": "design",
            "timestamp": datetime.now().isoformat(),
            "type": "revision_requested",
            "notes": "Business owner requested design revisions"
        })
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
        
        return {
            "phase": "design",
            "action": "revise",
            "parameters": {
                "lead_magnet_type": self.project_state["lead_magnet_type"],
                "business_info": self.project_state["business_info"],
                "language_variant": self.project_state["language_variant"]
            }
        }
    
    def update_creation_progress(self, progress: float, status_update: str) -> Dict[str, Any]:
        """
        Update the progress of the creation phase.
        
        Args:
            progress: Progress percentage (0-100)
            status_update: Status update message
            
        Returns:
            Dict containing the current project state
        """
        self.project_state["creation_progress"] = progress
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
            self.memory_manager.store("status_update", {
                "timestamp": datetime.now().isoformat(),
                "progress": progress,
                "message": status_update
            })
        
        return self.project_state
    
    def start_testing(self, lead_magnet_implementation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Start the testing phase after lead magnet implementation.
        
        Args:
            lead_magnet_implementation: The implemented lead magnet
            
        Returns:
            Dict containing the testing initialization parameters
        """
        self.project_state["status"] = "testing_in_progress"
        self.project_state["current_phase"] = "testing"
        self.project_state["phases_completed"].append("creation")
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
            self.memory_manager.store("lead_magnet_implementation", lead_magnet_implementation)
        
        return {
            "phase": "testing",
            "action": "initialize",
            "parameters": {
                "lead_magnet_type": self.project_state["lead_magnet_type"],
                "business_info": self.project_state["business_info"],
                "language_variant": self.project_state["language_variant"],
                "implementation": lead_magnet_implementation
            }
        }
    
    def request_business_review(self, lead_magnet_preview: Dict[str, Any]) -> Dict[str, Any]:
        """
        Request a review from the business owner.
        
        Args:
            lead_magnet_preview: Preview of the lead magnet for review
            
        Returns:
            Dict containing the review request parameters
        """
        self.project_state["status"] = "awaiting_business_review"
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        # Record collaboration
        self.project_state["collaboration_history"].append({
            "phase": self.project_state["current_phase"],
            "timestamp": datetime.now().isoformat(),
            "type": "review_requested",
            "notes": "Requested business owner review"
        })
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
            self.memory_manager.store("lead_magnet_preview", lead_magnet_preview)
        
        return {
            "phase": "review",
            "action": "request",
            "parameters": {
                "lead_magnet_type": self.project_state["lead_magnet_type"],
                "business_info": self.project_state["business_info"],
                "language_variant": self.project_state["language_variant"],
                "preview": lead_magnet_preview
            }
        }
    
    def process_review_feedback(self, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process feedback from the business owner review.
        
        Args:
            feedback: Feedback from the business owner
            
        Returns:
            Dict containing the next action to take
        """
        approved = feedback.get("approved", False)
        
        # Record collaboration
        self.project_state["collaboration_history"].append({
            "phase": "review",
            "timestamp": datetime.now().isoformat(),
            "type": "feedback_received",
            "notes": "Approved" if approved else "Revisions requested"
        })
        
        if approved:
            self.project_state["status"] = "review_approved"
            self.project_state["phases_completed"].append("testing")
            self.project_state["current_phase"] = "deployment"
            
            if self.memory_manager:
                self.memory_manager.store("project_state", self.project_state)
                self.memory_manager.store("review_feedback", feedback)
            
            return {
                "phase": "deployment",
                "action": "initialize",
                "parameters": {
                    "lead_magnet_type": self.project_state["lead_magnet_type"],
                    "business_info": self.project_state["business_info"],
                    "language_variant": self.project_state["language_variant"]
                }
            }
        else:
            self.project_state["status"] = "revision_needed"
            
            if self.memory_manager:
                self.memory_manager.store("project_state", self.project_state)
                self.memory_manager.store("review_feedback", feedback)
            
            return {
                "phase": self.project_state["current_phase"],
                "action": "revise",
                "parameters": {
                    "lead_magnet_type": self.project_state["lead_magnet_type"],
                    "business_info": self.project_state["business_info"],
                    "language_variant": self.project_state["language_variant"],
                    "feedback": feedback
                }
            }
    
    def prepare_deployment(self, tested_lead_magnet: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepare for deployment after successful testing.
        
        Args:
            tested_lead_magnet: The tested lead magnet ready for deployment
            
        Returns:
            Dict containing the deployment parameters
        """
        self.project_state["status"] = "deployment_ready"
        self.project_state["current_phase"] = "deployment"
        self.project_state["phases_completed"].append("testing")
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
            self.memory_manager.store("tested_lead_magnet", tested_lead_magnet)
        
        return {
            "phase": "deployment",
            "action": "prepare",
            "parameters": {
                "lead_magnet_type": self.project_state["lead_magnet_type"],
                "business_info": self.project_state["business_info"],
                "language_variant": self.project_state["language_variant"],
                "implementation": tested_lead_magnet
            }
        }
    
    def complete_project(self, deployment_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Complete the lead magnet project after successful deployment.
        
        Args:
            deployment_info: Information about the deployment
            
        Returns:
            Dict containing the final project state
        """
        self.project_state["status"] = "completed"
        self.project_state["phases_completed"].append("deployment")
        self.project_state["current_phase"] = None
        self.project_state["last_updated"] = datetime.now().isoformat()
        
        # Record collaboration
        self.project_state["collaboration_history"].append({
            "phase": "deployment",
            "timestamp": datetime.now().isoformat(),
            "type": "completed",
            "notes": "Lead magnet successfully deployed"
        })
        
        if self.memory_manager:
            self.memory_manager.store("project_state", self.project_state)
            self.memory_manager.store("deployment_info", deployment_info)
        
        return {
            "phase": "completion",
            "action": "finalize",
            "parameters": {
                "lead_magnet_type": self.project_state["lead_magnet_type"],
                "business_info": self.project_state["business_info"],
                "language_variant": self.project_state["language_variant"],
                "deployment": deployment_info,
                "project_summary": {
                    "start_date": self.project_state["collaboration_history"][0]["timestamp"] if self.project_state["collaboration_history"] else self.project_state["last_updated"],
                    "completion_date": datetime.now().isoformat(),
                    "phases_completed": self.project_state["phases_completed"],
                    "collaboration_points": len(self.project_state["collaboration_history"])
                }
            }
        }
    
    def get_project_state(self) -> Dict[str, Any]:
        """
        Get the current project state.
        
        Returns:
            Dict containing the current project state
        """
        return self.project_state
    
    def save_state(self, filepath: str) -> bool:
        """
        Save the current project state to a file.
        
        Args:
            filepath: Path to save the state file
            
        Returns:
            bool indicating success or failure
        """
        try:
            with open(filepath, 'w') as f:
                json.dump(self.project_state, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False
    
    def load_state(self, filepath: str) -> bool:
        """
        Load project state from a file.
        
        Args:
            filepath: Path to the state file
            
        Returns:
            bool indicating success or failure
        """
        try:
            with open(filepath, 'r') as f:
                self.project_state = json.load(f)
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False


class MemoryManager:
    """
    Memory Manager agent for storing and retrieving context.
    
    This agent is responsible for:
    - Maintaining shared knowledge across all agents
    - Storing and retrieving business information
    - Managing conversation history and decisions
    - Providing relevant context to specialized agents
    - Handling data persistence between sessions
    """
    
    def __init__(self, storage_dir: str = None):
        """
        Initialize the Memory Manager.
        
        Args:
            storage_dir: Directory for persistent storage
        """
        self.memory = {}
        self.storage_dir = storage_dir or os.path.join(os.getcwd(), "memory")
        
        # Create storage directory if it doesn't exist
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)
    
    def store(self, key: str, value: Any) -> bool:
        """
        Store a value in memory.
        
        Args:
            key: Key to store the value under
            value: Value to store
            
        Returns:
            bool indicating success or failure
        """
        try:
            self.memory[key] = value
            return True
        except Exception as e:
            print(f"Error storing value: {e}")
            return False
    
    def retrieve(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from memory.
        
        Args:
            key: Key to retrieve
            default: Default value if key doesn't exist
            
        Returns:
            The stored value or default
        """
        return self.memory.get(key, default)
    
    def save_to_disk(self, key: str = None) -> bool:
        """
        Save memory to disk.
        
        Args:
            key: Specific key to save, or all if None
            
        Returns:
            bool indicating success or failure
        """
        try:
            if key:
                # Save specific key
                filepath = os.path.join(self.storage_dir, f"{key}.json")
                with open(filepath, 'w') as f:
                    json.dump(self.memory[key], f, indent=2)
            else:
                # Save all memory
                for k, v in self.memory.items():
                    filepath = os.path.join(self.storage_dir, f"{k}.json")
                    with open(filepath, 'w') as f:
                        json.dump(v, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to disk: {e}")
            return False
    
    def load_from_disk(self, key: str = None) -> bool:
        """
        Load memory from disk.
        
        Args:
            key: Specific key to load, or all if None
            
        Returns:
            bool indicating success or failure
        """
        try:
            if key:
                # Load specific key
                filepath = os.path.join(self.storage_dir, f"{key}.json")
                if os.path.exists(filepath):
                    with open(filepath, 'r') as f:
                        self.memory[key] = json.load(f)
            else:
                # Load all files in storage directory
                for filename in os.listdir(self.storage_dir):
                    if filename.endswith('.json'):
                        key = filename[:-5]  # Remove .json extension
                        filepath = os.path.join(self.storage_dir, filename)
                        with open(filepath, 'r') as f:
                            self.memory[key] = json.load(f)
            return True
        except Exception as e:
            print(f"Error loading from disk: {e}")
            return False
    
    def clear(self, key: str = None) -> bool:
        """
        Clear memory.
        
        Args:
            key: Specific key to clear, or all if None
            
        Returns:
            bool indicating success or failure
        """
        try:
            if key:
                if key in self.memory:
                    del self.memory[key]
            else:
                self.memory = {}
            return True
        except Exception as e:
            print(f"Error clearing memory: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Create memory manager
    memory_manager = MemoryManager(storage_dir="./memory")
    
    # Create executive agent
    executive = ExecutiveAgent(memory_manager=memory_manager)
    
    # Start assessment
    assessment_params = executive.start_assessment()
    print("Assessment Parameters:", assessment_params)
    
    # Simulate assessment results
    assessment_results = {
        "business_info": {
            "name": "Thames Digital",
            "industry": "Web Design",
            "size": "Small",
            "target_audience": "E-commerce businesses",
            "unique_selling_proposition": "Conversion-focused design"
        },
        "customer_pain_points": [
            "Low conversion rates",
            "Slow website performance",
            "Poor mobile experience"
        ],
        "recommended_lead_magnet": "website_audit",
        "language_variant": "UK"
    }
    
    # Process assessment results
    design_params = executive.process_assessment_results(assessment_results)
    print("Design Parameters:", design_params)
    
    # Simulate design approval
    creation_params = executive.start_creation(design_approval=True)
    print("Creation Parameters:", creation_params)
    
    # Update creation progress
    state = executive.update_creation_progress(50, "Implementing interactive elements")
    print("Project State:", state)
    
    # Save state
    executive.save_state("./project_state.json")
