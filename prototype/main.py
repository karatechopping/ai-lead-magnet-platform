"""
Main Application Module

This module ties together the assessment, generator, and deployment components
to create a complete lead magnet platform prototype.
"""

import os
import json
from typing import Dict, Any, Optional

# Import components from other modules
from assessment.engine import AssessmentEngine, create_default_lead_magnet_types
from assessment.questionnaire import Questionnaire, create_default_questionnaire
from generator.generator import LeadMagnetGenerator, create_default_templates
from deployment.deployment import DeploymentManager


class LeadMagnetPlatform:
    """
    Main platform class that integrates all components.
    
    This class provides a simplified API for the entire lead magnet platform.
    """
    
    def __init__(self, base_url: str = "https://leadmagnet.example.com"):
        """
        Initialize the lead magnet platform.
        
        Args:
            base_url: Base URL for the lead magnet service
        """
        # Initialize components
        self.assessment_engine = AssessmentEngine(create_default_lead_magnet_types())
        self.questionnaire = create_default_questionnaire()
        self.generator = LeadMagnetGenerator(create_default_templates())
        self.deployment_manager = DeploymentManager(base_url)
        
        # Storage for businesses and lead magnets (in a real implementation, this would be a database)
        self.businesses = {}
        self.lead_magnets = {}
    
    def register_business(self, business_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register a new business.
        
        Args:
            business_data: Dictionary containing business information
            
        Returns:
            Dictionary containing the registered business information
        """
        # Generate a simple business ID (in a real implementation, this would be more robust)
        business_id = f"bus_{len(self.businesses) + 1}"
        
        # Create business object
        business = {
            "id": business_id,
            "name": business_data.get("business_name", ""),
            "type": business_data.get("business_type", ""),
            "description": business_data.get("business_description", ""),
            "industry": business_data.get("industry", ""),
            "website": business_data.get("website", ""),
            "contact_email": business_data.get("contact_email", ""),
            "brand_color": business_data.get("brand_color", "#4A90E2"),
            "logo_url": business_data.get("logo_url", ""),
            "created_at": "2025-03-20T12:00:00Z",  # Example timestamp
            "lead_magnets": []
        }
        
        # Store business
        self.businesses[business_id] = business
        
        return business
    
    def assess_business(self, business_id: str, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess a business and recommend lead magnet types.
        
        Args:
            business_id: ID of the business
            responses: Dictionary of questionnaire responses
            
        Returns:
            Dictionary containing assessment results and recommendations
        """
        # Get business
        business = self.businesses.get(business_id)
        if not business:
            raise ValueError(f"Business with ID {business_id} not found")
        
        # Process responses
        results = self.assessment_engine.process_responses(responses)
        
        # Store assessment results with the business
        business["assessment_results"] = results
        
        return results
    
    def create_lead_magnet(self, business_id: str, lead_magnet_type_id: str,
                          template_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a lead magnet for a business.
        
        Args:
            business_id: ID of the business
            lead_magnet_type_id: ID of the lead magnet type
            template_id: Optional ID of the specific template to use
            
        Returns:
            Dictionary containing the created lead magnet
        """
        # Get business
        business = self.businesses.get(business_id)
        if not business:
            raise ValueError(f"Business with ID {business_id} not found")
        
        # Get business profile
        business_profile = {
            "business_name": business["name"],
            "business_type": business["type"],
            "business_description": business["description"],
            "industry": business["industry"],
            "brand_color": business["brand_color"],
            "logo_url": business["logo_url"]
        }
        
        # Generate lead magnet
        lead_magnet = None
        if template_id:
            # Use specific template
            lead_magnet = self.generator.generate_lead_magnet(template_id, business_profile)
        else:
            # Recommend and generate based on lead magnet type
            lead_magnet = self.generator.recommend_and_generate(lead_magnet_type_id, business_profile)
        
        if not lead_magnet:
            raise ValueError(f"Failed to generate lead magnet with type {lead_magnet_type_id}")
        
        # Generate a simple lead magnet ID (in a real implementation, this would be more robust)
        lead_magnet_id = f"lm_{len(self.lead_magnets) + 1}"
        
        # Add metadata
        lead_magnet["id"] = lead_magnet_id
        lead_magnet["business_id"] = business_id
        lead_magnet["created_at"] = "2025-03-20T12:00:00Z"  # Example timestamp
        
        # Store lead magnet
        self.lead_magnets[lead_magnet_id] = lead_magnet
        
        # Add to business's lead magnets
        business["lead_magnets"].append(lead_magnet_id)
        
        return lead_magnet
    
    def deploy_lead_magnet(self, lead_magnet_id: str, settings: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Deploy a lead magnet.
        
        Args:
            lead_magnet_id: ID of the lead magnet to deploy
            settings: Optional dictionary of deployment settings
            
        Returns:
            Dictionary containing deployment information
        """
        # Get lead magnet
        lead_magnet = self.lead_magnets.get(lead_magnet_id)
        if not lead_magnet:
            raise ValueError(f"Lead magnet with ID {lead_magnet_id} not found")
        
        # Get business ID
        business_id = lead_magnet["business_id"]
        
        # Create deployment
        deployment = self.deployment_manager.create_deployment(lead_magnet_id, business_id, settings)
        
        # Add deployment to lead magnet
        lead_magnet["deployment"] = deployment
        
        return deployment
    
    def get_installation_guide(self, lead_magnet_id: str) -> Dict[str, Any]:
        """
        Get installation guide for a lead magnet.
        
        Args:
            lead_magnet_id: ID of the lead magnet
            
        Returns:
            Dictionary containing installation instructions
        """
        # Get lead magnet
        lead_magnet = self.lead_magnets.get(lead_magnet_id)
        if not lead_magnet:
            raise ValueError(f"Lead magnet with ID {lead_magnet_id} not found")
        
        # Check if lead magnet has been deployed
        if "deployment" not in lead_magnet:
            raise ValueError(f"Lead magnet with ID {lead_magnet_id} has not been deployed yet")
        
        # Generate installation guide
        return self.deployment_manager.generate_installation_guide(lead_magnet["deployment"])
    
    def get_lead_magnet_preview_url(self, lead_magnet_id: str) -> str:
        """
        Get preview URL for a lead magnet.
        
        Args:
            lead_magnet_id: ID of the lead magnet
            
        Returns:
            Preview URL
        """
        # Get lead magnet
        lead_magnet = self.lead_magnets.get(lead_magnet_id)
        if not lead_magnet:
            raise ValueError(f"Lead magnet with ID {lead_magnet_id} not found")
        
        # Check if lead magnet has been deployed
        if "deployment" not in lead_magnet:
            raise ValueError(f"Lead magnet with ID {lead_magnet_id} has not been deployed yet")
        
        return lead_magnet["deployment"]["public_url"]
    
    def process_customer_interaction(self, lead_magnet_id: str, 
                                    customer_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a customer interaction with a lead magnet.
        
        This demonstrates the dual-layer personalization by customizing the lead magnet
        for a specific customer of the business.
        
        Args:
            lead_magnet_id: ID of the lead magnet
            customer_data: Dictionary containing customer information
            
        Returns:
            Dictionary containing the personalized lead magnet content
        """
        # Get lead magnet
        lead_magnet = self.lead_magnets.get(lead_magnet_id)
        if not lead_magnet:
            raise ValueError(f"Lead magnet with ID {lead_magnet_id} not found")
        
        # Get business
        business_id = lead_magnet["business_id"]
        business = self.businesses.get(business_id)
        if not business:
            raise ValueError(f"Business with ID {business_id} not found")
        
        # Get business profile
        business_profile = {
            "business_name": business["name"],
            "business_type": business["type"],
            "business_description": business["description"],
            "industry": business["industry"],
            "brand_color": business["brand_color"],
            "logo_url": business["logo_url"]
        }
        
        # Get template ID
        template_id = lead_magnet["template_id"]
        
        # Generate personalized lead magnet for this specific customer
        personalized_content = self.generator.generate_lead_magnet(
            template_id, 
            business_profile,
            customer_data
        )
        
        # In a real implementation, we would store this interaction
        # and potentially notify the business
        
        return personalized_content


def run_demo():
    """Run a demonstration of the lead magnet platform."""
    # Initialize platform
    platform = LeadMagnetPlatform()
    
    # Register a business
    business_data = {
        "business_name": "WebDesign Pro",
        "business_type": "service",
        "business_description": "A web design agency specializing in small business websites",
        "industry": "web design",
        "website": "https://webdesignpro.example.com",
        "contact_email": "info@webdesignpro.example.com",
        "brand_color": "#3366CC",
        "logo_url": "https://webdesignpro.example.com/logo.png"
    }
    business = platform.register_business(business_data)
    print(f"Registered business: {business['name']} (ID: {business['id']})")
    
    # Assess the business
    assessment_responses = {
        "business_type": "service",
        "business_size": "small",
        "business_description": "Web design agency specializing in small business websites",
        "target_audience": "b2b_small",
        "customer_pain_points": ["knowledge", "complexity", "quality"],
        "sales_cycle_length": 3,
        "customer_questions": "How much will it cost? How long will it take? Will I be able to update it myself?",
        "unique_value": "We create websites that are both beautiful and easy to update",
        "customer_value": "quality",
        "website_platform": "wordpress",
        "technical_resources": "internal",
        "tech_comfort": 4,
        "marketing_goals": ["leads", "authority", "conversion"],
        "lead_quality_importance": 4
    }
    assessment_results = platform.assess_business(business["id"], assessment_responses)
    print(f"Assessment complete. Top recommendation: {assessment_results['recommendations'][0]['name']}")
    
    # Create a lead magnet
    lead_magnet = platform.create_lead_magnet(
        business["id"],
        assessment_results["recommendations"][0]["id"]
    )
    print(f"Created lead magnet: {lead_magnet['template_name']} (ID: {lead_magnet['id']})")
    
    # Deploy the lead magnet
    deployment = platform.deploy_lead_magnet(
        lead_magnet["id"],
        {
            "theme": "light",
            "button_text": "Take Assessment",
            "button_color": "#3366CC"
        }
    )
    print(f"Deployed lead magnet. Public URL: {deployment['public_url']}")
    
    # Get installation guide
    installation_guide = platform.get_installation_guide(lead_magnet["id"])
    print(f"Generated installation guide with {len(installation_guide['options'])} options")
    
    # Process a customer interaction
    customer_data = {
        "name": "John Smith",
        "email": "john@example.com",
        "company": "Smith's Bakery",
        "website": "https://smithsbakery.example.com"
    }
    personalized_content = platform.process_customer_interaction(lead_magnet["id"], customer_data)
    print(f"Generated personalized content for customer: {customer_data['name']}")
    
    # Save demo results to file
    demo_results = {
        "business": business,
        "assessment_results": assessment_results,
        "lead_magnet": lead_magnet,
        "deployment": deployment,
        "installation_guide": installation_guide,
        "personalized_content": personalized_content
    }
    
    with open("demo_results.json", "w") as f:
        json.dump(demo_results, f, indent=2)
    
    print("Demo results saved to demo_results.json")


if __name__ == "__main__":
    run_demo()
