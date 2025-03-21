"""
Deployment Module

This module handles the embedding and deployment of lead magnets on client websites.
It provides simple integration options for businesses to add lead magnets to their sites.
"""

import json
from typing import Dict, Any, Optional


class EmbedGenerator:
    """
    Generator for embed codes that businesses can use to add lead magnets to their websites.
    """
    
    def __init__(self, base_url: str = "https://leadmagnet.example.com"):
        """
        Initialize the embed generator.
        
        Args:
            base_url: Base URL for the lead magnet service
        """
        self.base_url = base_url
    
    def generate_embed_code(self, lead_magnet_id: str, business_id: str,
                           options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate embed code for a lead magnet.
        
        Args:
            lead_magnet_id: ID of the lead magnet to embed
            business_id: ID of the business
            options: Optional dictionary of configuration options
            
        Returns:
            Dictionary containing embed codes and instructions
        """
        options = options or {}
        
        # Default options
        default_options = {
            "width": "100%",
            "height": "600px",
            "theme": "light",
            "button_text": "Start Now",
            "button_color": "#4A90E2",
            "modal": False
        }
        
        # Merge default options with provided options
        merged_options = {**default_options, **options}
        
        # Create options string for iframe URL
        options_params = "&".join([f"{k}={v}" for k, v in merged_options.items() 
                                  if k not in ["width", "height", "modal"]])
        
        # Generate iframe embed code
        iframe_url = f"{self.base_url}/embed/{lead_magnet_id}?business={business_id}&{options_params}"
        iframe_code = f'<iframe src="{iframe_url}" width="{merged_options["width"]}" height="{merged_options["height"]}" frameborder="0" allowtransparency="true"></iframe>'
        
        # Generate JavaScript embed code for modal option
        js_code = ""
        if merged_options["modal"]:
            js_code = f"""
<script src="{self.base_url}/js/leadmagnet-embed.js"></script>
<script>
  LeadMagnet.init({{
    lead_magnet_id: "{lead_magnet_id}",
    business_id: "{business_id}",
    button_text: "{merged_options["button_text"]}",
    button_color: "{merged_options["button_color"]}",
    theme: "{merged_options["theme"]}"
  }});
</script>
<button onclick="LeadMagnet.open()">{merged_options["button_text"]}</button>
"""
        
        # Generate WordPress shortcode
        wp_shortcode = f'[leadmagnet id="{lead_magnet_id}" business="{business_id}" theme="{merged_options["theme"]}" button_text="{merged_options["button_text"]}" button_color="{merged_options["button_color"]}"]'
        
        return {
            "iframe": iframe_code,
            "javascript": js_code,
            "wordpress": wp_shortcode,
            "options": merged_options,
            "preview_url": f"{self.base_url}/preview/{lead_magnet_id}?business={business_id}"
        }


class DeploymentManager:
    """
    Manager for deploying and managing lead magnets.
    """
    
    def __init__(self, base_url: str = "https://leadmagnet.example.com"):
        """
        Initialize the deployment manager.
        
        Args:
            base_url: Base URL for the lead magnet service
        """
        self.base_url = base_url
        self.embed_generator = EmbedGenerator(base_url)
    
    def create_deployment(self, lead_magnet_id: str, business_id: str,
                         settings: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a deployment for a lead magnet.
        
        Args:
            lead_magnet_id: ID of the lead magnet to deploy
            business_id: ID of the business
            settings: Optional dictionary of deployment settings
            
        Returns:
            Dictionary containing deployment information
        """
        settings = settings or {}
        
        # Default settings
        default_settings = {
            "active": True,
            "collect_email": True,
            "redirect_url": "",
            "custom_css": "",
            "theme": "light",
            "button_text": "Start Now",
            "button_color": "#4A90E2",
            "thank_you_message": "Thank you for completing this assessment!"
        }
        
        # Merge default settings with provided settings
        merged_settings = {**default_settings, **settings}
        
        # Generate embed codes
        embed_codes = self.embed_generator.generate_embed_code(
            lead_magnet_id, 
            business_id,
            {
                "theme": merged_settings["theme"],
                "button_text": merged_settings["button_text"],
                "button_color": merged_settings["button_color"],
                "modal": False
            }
        )
        
        # Generate modal embed codes
        modal_embed_codes = self.embed_generator.generate_embed_code(
            lead_magnet_id, 
            business_id,
            {
                "theme": merged_settings["theme"],
                "button_text": merged_settings["button_text"],
                "button_color": merged_settings["button_color"],
                "modal": True
            }
        )
        
        # Create deployment object
        deployment = {
            "id": f"dep_{lead_magnet_id}_{business_id}",
            "lead_magnet_id": lead_magnet_id,
            "business_id": business_id,
            "settings": merged_settings,
            "embed_codes": {
                "inline": embed_codes,
                "modal": modal_embed_codes
            },
            "status": "active" if merged_settings["active"] else "inactive",
            "created_at": "2025-03-20T12:00:00Z",  # Example timestamp
            "updated_at": "2025-03-20T12:00:00Z",  # Example timestamp
            "public_url": f"{self.base_url}/public/{lead_magnet_id}?business={business_id}"
        }
        
        return deployment
    
    def generate_installation_guide(self, deployment: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate an installation guide for a deployment.
        
        Args:
            deployment: Deployment object
            
        Returns:
            Dictionary containing installation instructions
        """
        lead_magnet_id = deployment["lead_magnet_id"]
        business_id = deployment["business_id"]
        
        # Generate installation instructions
        instructions = {
            "title": "Installation Guide",
            "description": "Follow these steps to add your lead magnet to your website:",
            "options": [
                {
                    "title": "Option 1: Embed directly in your page",
                    "description": "Copy and paste this code into your HTML where you want the lead magnet to appear:",
                    "code": deployment["embed_codes"]["inline"]["iframe"],
                    "difficulty": "easy"
                },
                {
                    "title": "Option 2: Add as a popup/modal",
                    "description": "Copy and paste this code into your HTML to add a button that opens the lead magnet in a popup:",
                    "code": deployment["embed_codes"]["modal"]["javascript"],
                    "difficulty": "medium"
                }
            ]
        }
        
        # Add WordPress-specific instructions if applicable
        instructions["options"].append({
            "title": "Option 3: WordPress Shortcode",
            "description": "If you're using WordPress, add this shortcode to any page or post:",
            "code": deployment["embed_codes"]["inline"]["wordpress"],
            "difficulty": "easy"
        })
        
        # Add testing instructions
        instructions["testing"] = {
            "title": "Testing Your Lead Magnet",
            "steps": [
                "After installation, visit your page to ensure the lead magnet appears correctly.",
                f"You can preview your lead magnet directly at: {deployment['public_url']}",
                "Complete the lead magnet yourself to test the user experience.",
                "Check your dashboard to confirm that test submissions are being recorded."
            ]
        }
        
        return instructions


if __name__ == "__main__":
    # Example usage
    deployment_manager = DeploymentManager()
    
    # Create a sample deployment
    deployment = deployment_manager.create_deployment(
        lead_magnet_id="lm_123",
        business_id="bus_456",
        settings={
            "theme": "dark",
            "button_text": "Take Assessment",
            "button_color": "#FF6600"
        }
    )
    
    # Generate installation guide
    installation_guide = deployment_manager.generate_installation_guide(deployment)
    
    # Print the deployment and installation guide
    print(json.dumps(deployment, indent=2))
    print("\nInstallation Guide:")
    print(json.dumps(installation_guide, indent=2))
