"""
Lead Magnet Generator Module

This module generates customized lead magnets based on assessment results.
It uses templates and AI-driven personalization to create lead magnets
that are tailored to both the business and their individual customers.
"""

import json
import os
from typing import Dict, List, Any, Optional

class LeadMagnetTemplate:
    """Base class for lead magnet templates."""

    def __init__(self, id: str, name: str, description: str, structure: Dict[str, Any]):
        """
        Initialize a lead magnet template.

        Args:
            id: Unique identifier for this template
            name: Display name of the template
            description: Description of what this template creates
            structure: Dictionary defining the structure of the lead magnet
        """
        self.id = id
        self.name = name
        self.description = description
        self.structure = structure

    def to_dict(self) -> Dict[str, Any]:
        """Convert template to dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "structure": self.structure,
            "type": self.__class__.__name__
        }

    def generate(self, business_profile: Dict[str, Any],
                customer_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate a lead magnet based on this template.

        Args:
            business_profile: Dictionary containing business information
            customer_data: Optional dictionary containing customer-specific data

        Returns:
            Dictionary containing the generated lead magnet
        """
        # Base implementation - should be overridden by subclasses
        return {
            "template_id": self.id,
            "template_name": self.name,
            "business_profile": business_profile,
            "customer_data": customer_data or {},
            "content": {}
        }


class AssessmentTemplate(LeadMagnetTemplate):
    """Template for interactive assessment lead magnets."""

    def __init__(self, id: str, name: str, description: str,
                 questions: List[Dict[str, Any]],
                 result_categories: List[Dict[str, Any]],
                 structure: Optional[Dict[str, Any]] = None):
        """
        Initialize an assessment template.

        Args:
            id: Unique identifier for this template
            name: Display name of the template
            description: Description of what this template creates
            questions: List of assessment questions
            result_categories: List of possible result categories
            structure: Optional dictionary defining additional structure
        """
        structure = structure or {}
        structure.update({
            "questions": questions,
            "result_categories": result_categories
        })
        super().__init__(id, name, description, structure)

    def generate(self, business_profile: Dict[str, Any],
                customer_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generate an assessment lead magnet."""
        customer_data = customer_data or {}

        # Personalize questions for the business
        personalized_questions = self._personalize_questions(
            self.structure["questions"],
            business_profile
        )

        # Personalize result categories for the business
        personalized_results = self._personalize_result_categories(
            self.structure["result_categories"],
            business_profile
        )

        # Create the assessment content
        assessment = {
            "template_id": self.id,
            "template_name": self.name,
            "business_name": business_profile.get("business_name", "Your Business"),
            "title": self._generate_title(business_profile),
            "introduction": self._generate_introduction(business_profile),
            "questions": personalized_questions,
            "result_categories": personalized_results,
            "call_to_action": self._generate_call_to_action(business_profile),
            "branding": {
                "primary_color": business_profile.get("brand_color", "#4A90E2"),
                "logo_url": business_profile.get("logo_url", ""),
                "font": business_profile.get("brand_font", "Arial, sans-serif")
            }
        }

        # If customer data is provided, pre-fill some fields
        if customer_data:
            assessment["customer_name"] = customer_data.get("name", "")
            assessment["customer_email"] = customer_data.get("email", "")
            # Add any other customer-specific customizations here

        return assessment

    def _personalize_questions(self, questions: List[Dict[str, Any]],
                              business_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Personalize assessment questions for the business."""
        business_type = business_profile.get("business_type", "")
        business_name = business_profile.get("business_name", "our")
        industry = business_profile.get("industry", "your industry")

        personalized_questions = []
        for question in questions:
            # Create a copy of the question to modify
            personalized_question = question.copy()

            # Replace placeholders in the question text
            text = personalized_question["text"]
            text = text.replace("[BUSINESS_NAME]", business_name)
            text = text.replace("[INDUSTRY]", industry)
            text = text.replace("[BUSINESS_TYPE]", business_type)
            personalized_question["text"] = text

            # Personalize options if present
            if "options" in personalized_question:
                personalized_options = []
                for option in personalized_question["options"]:
                    personalized_option = option.copy()
                    option_text = personalized_option["text"]
                    option_text = option_text.replace("[BUSINESS_NAME]", business_name)
                    option_text = option_text.replace("[INDUSTRY]", industry)
                    option_text = option_text.replace("[BUSINESS_TYPE]", business_type)
                    personalized_option["text"] = option_text
                    personalized_options.append(personalized_option)
                personalized_question["options"] = personalized_options

            personalized_questions.append(personalized_question)

        return personalized_questions

    def _personalize_result_categories(self, result_categories: List[Dict[str, Any]],
                                      business_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Personalize result categories for the business."""
        business_type = business_profile.get("business_type", "")
        business_name = business_profile.get("business_name", "our")
        industry = business_profile.get("industry", "your industry")

        personalized_categories = []
        for category in result_categories:
            # Create a copy of the category to modify
            personalized_category = category.copy()

            # Replace placeholders in the title
            title = personalized_category["title"]
            title = title.replace("[BUSINESS_NAME]", business_name)
            title = title.replace("[INDUSTRY]", industry)
            title = title.replace("[BUSINESS_TYPE]", business_type)
            personalized_category["title"] = title

            # Replace placeholders in the description
            description = personalized_category["description"]
            description = description.replace("[BUSINESS_NAME]", business_name)
            description = description.replace("[INDUSTRY]", industry)
            description = description.replace("[BUSINESS_TYPE]", business_type)
            personalized_category["description"] = description

            # Replace placeholders in the recommendations
            if "recommendations" in personalized_category:
                personalized_recommendations = []
                for recommendation in personalized_category["recommendations"]:
                    personalized_recommendation = recommendation.replace("[BUSINESS_NAME]", business_name)
                    personalized_recommendation = personalized_recommendation.replace("[INDUSTRY]", industry)
                    personalized_recommendation = personalized_recommendation.replace("[BUSINESS_TYPE]", business_type)
                    personalized_recommendations.append(personalized_recommendation)
                personalized_category["recommendations"] = personalized_recommendations

            personalized_categories.append(personalized_category)

        return personalized_categories

    def _generate_title(self, business_profile: Dict[str, Any]) -> str:
        """Generate a personalized title for the assessment."""
        business_name = business_profile.get("business_name", "Our")
        industry = business_profile.get("industry", "")

        if "website" in self.id.lower():
            return f"{business_name} Website Performance Assessment"
        elif "marketing" in self.id.lower():
            return f"{business_name} Marketing Strategy Assessment"
        elif "financial" in self.id.lower():
            return f"{business_name} Financial Health Assessment"
        else:
            return f"{business_name} {industry} Assessment"

    def _generate_introduction(self, business_profile: Dict[str, Any]) -> str:
        """Generate a personalized introduction for the assessment."""
        business_name = business_profile.get("business_name", "our")
        business_description = business_profile.get("business_description", "")

        intro = f"Welcome to {business_name}'s assessment tool. "

        if business_description:
            intro += f"As {business_description}, we understand the challenges you face. "

        intro += "This assessment will help us understand your specific needs and provide personalized recommendations."

        return intro

    def _generate_call_to_action(self, business_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a personalized call to action."""
        business_name = business_profile.get("business_name", "us")

        return {
            "heading": f"Ready to take the next step with {business_name}?",
            "button_text": "Contact Us Now",
            "description": "Get personalized assistance based on your assessment results."
        }


class CalculatorTemplate(LeadMagnetTemplate):
    """Template for calculator lead magnets."""

    def __init__(self, id: str, name: str, description: str,
                 inputs: List[Dict[str, Any]],
                 calculations: Dict[str, str],
                 results: List[Dict[str, Any]],
                 structure: Optional[Dict[str, Any]] = None):
        """
        Initialize a calculator template.

        Args:
            id: Unique identifier for this template
            name: Display name of the template
            description: Description of what this template creates
            inputs: List of calculator input fields
            calculations: Dictionary of calculation formulas
            results: List of result display configurations
            structure: Optional dictionary defining additional structure
        """
        structure = structure or {}
        structure.update({
            "inputs": inputs,
            "calculations": calculations,
            "results": results
        })
        super().__init__(id, name, description, structure)

    def generate(self, business_profile: Dict[str, Any],
                customer_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generate a calculator lead magnet."""
        customer_data = customer_data or {}

        # Personalize inputs for the business
        personalized_inputs = self._personalize_inputs(
            self.structure["inputs"],
            business_profile
        )

        # Personalize results for the business
        personalized_results = self._personalize_results(
            self.structure["results"],
            business_profile
        )

        # Create the calculator content
        calculator = {
            "template_id": self.id,
            "template_name": self.name,
            "business_name": business_profile.get("business_name", "Your Business"),
            "title": self._generate_title(business_profile),
            "introduction": self._generate_introduction(business_profile),
            "inputs": personalized_inputs,
            "calculations": self.structure["calculations"],
            "results": personalized_results,
            "call_to_action": self._generate_call_to_action(business_profile),
            "branding": {
                "primary_color": business_profile.get("brand_color", "#4A90E2"),
                "logo_url": business_profile.get("logo_url", ""),
                "font": business_profile.get("brand_font", "Arial, sans-serif")
            }
        }

        # If customer data is provided, pre-fill some fields
        if customer_data:
            calculator["customer_name"] = customer_data.get("name", "")
            calculator["customer_email"] = customer_data.get("email", "")

            # Pre-fill input values if available
            for input_field in calculator["inputs"]:
                field_id = input_field["id"]
                if field_id in customer_data:
                    input_field["default_value"] = customer_data[field_id]

        return calculator

    def _personalize_inputs(self, inputs: List[Dict[str, Any]],
                           business_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Personalize calculator inputs for the business."""
        business_type = business_profile.get("business_type", "")
        business_name = business_profile.get("business_name", "our")
        industry = business_profile.get("industry", "your industry")

        personalized_inputs = []
        for input_field in inputs:
            # Create a copy of the input to modify
            personalized_input = input_field.copy()

            # Replace placeholders in the label
            label = personalized_input["label"]
            label = label.replace("[BUSINESS_NAME]", business_name)
            label = label.replace("[INDUSTRY]", industry)
            label = label.replace("[BUSINESS_TYPE]", business_type)
            personalized_input["label"] = label

            # Replace placeholders in the help text if present
            if "help_text" in personalized_input:
                help_text = personalized_input["help_text"]
                help_text = help_text.replace("[BUSINESS_NAME]", business_name)
                help_text = help_text.replace("[INDUSTRY]", industry)
                help_text = help_text.replace("[BUSINESS_TYPE]", business_type)
                personalized_input["help_text"] = help_text

            personalized_inputs.append(personalized_input)

        return personalized_inputs

    def _personalize_results(self, results: List[Dict[str, Any]],
                            business_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Personalize calculator results for the business."""
        business_type = business_profile.get("business_type", "")
        business_name = business_profile.get("business_name", "our")
        industry = business_profile.get("industry", "your industry")

        personalized_results = []
        for result in results:
            # Create a copy of the result to modify
            personalized_result = result.copy()

            # Replace placeholders in the label
            label = personalized_result["label"]
            label = label.replace("[BUSINESS_NAME]", business_name)
            label = label.replace("[INDUSTRY]", industry)
            label = label.replace("[BUSINESS_TYPE]", business_type)
            personalized_result["label"] = label

            # Replace placeholders in the description if present
            if "description" in personalized_result:
                description = personalized_result["description"]
                description = description.replace("[BUSINESS_NAME]", business_name)
                description = description.replace("[INDUSTRY]", industry)
                description = description.replace("[BUSINESS_TYPE]", business_type)
                personalized_result["description"] = description

            personalized_results.append(personalized_result)

        return personalized_results

    def _generate_title(self, business_profile: Dict[str, Any]) -> str:
        """Generate a personalized title for the calculator."""
        business_name = business_profile.get("business_name", "Our")

        if "roi" in self.id.lower():
            return f"{business_name} ROI Calculator"
        elif "savings" in self.id.lower():
            return f"{business_name} Savings Calculator"
        elif "cost" in self.id.lower():
            return f"{business_name} Cost Calculator"
        else:
            return f"{business_name} Value Calculator"

    def _generate_introduction(self, business_profile: Dict[str, Any]) -> str:
        """Generate a personalized introduction for the calculator."""
        business_name = business_profile.get("business_name", "our")
        business_description = business_profile.get("business_description", "")

        intro = f"Welcome to {business_name}'s calculator tool. "

        if business_description:
            intro += f"As {business_description}, we understand the importance of making informed decisions. "

        intro += "This calculator will help you quantify the potential value and make the right choice for your needs."

        return intro

    def _generate_call_to_action(self, business_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a personalized call to action."""
        business_name = business_profile.get("business_name", "us")

        return {
            "heading": f"Ready to realize these benefits with {business_name}?",
            "button_text": "Contact Us Now",
            "description": "Get a personalized consultation based on your calculator results."
        }


class LeadMagnetGenerator:
    """
    Generator that creates customized lead magnets based on templates.

    This generator uses templates and business/customer data to create
    personalized lead magnets.
    """

    def __init__(self, templates: Optional[List[LeadMagnetTemplate]] = None):
        """
        Initialize the lead magnet generator.

        Args:
            templates: Optional list of lead magnet templates to use
        """
        self.templates = templates or []

    def add_template(self, template: LeadMagnetTemplate) -> None:
        """
        Add a template to the generator.

        Args:
            template: LeadMagnetTemplate object to add
        """
        self.templates.append(template)

    def get_template_by_id(self, template_id: str) -> Optional[LeadMagnetTemplate]:
        """
        Get a template by its ID.

        Args:
            template_id: ID of the template to retrieve

        Returns:
            LeadMagnetTemplate if found, None otherwise
        """
        for template in self.templates:
            if template.id == template_id:
                return template
        return None

    def get_templates_by_type(self, lead_magnet_type: str) -> List[LeadMagnetTemplate]:
        """
        Get all templates matching a lead magnet type.

        Args:
            lead_magnet_type: Type of lead magnet to filter by

        Returns:
            List of matching LeadMagnetTemplate objects
        """
        return [t for t in self.templates if lead_magnet_type.lower() in t.id.lower()]

    def generate_lead_magnet(self, template_id: str, business_profile: Dict[str, Any],
                            customer_data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Generate a lead magnet using the specified template.

        Args:
            template_id: ID of the template to use
            business_profile: Dictionary containing business information
            customer_data: Optional dictionary containing customer-specific data

        Returns:
            Dictionary containing the generated lead magnet, or None if template not found
        """
        template = self.get_template_by_id(template_id)
        if not template:
            return None

        return template.generate(business_profile, customer_data)

    def recommend_and_generate(self, lead_magnet_type: str, business_profile: Dict[str, Any],
                              customer_data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Recommend and generate a lead magnet based on the lead magnet type.

        Args:
            lead_magnet_type: Type of lead magnet to generate
            business_profile: Dictionary containing business information
            customer_data: Optional dictionary containing customer-specific data

        Returns:
            Dictionary containing the generated lead magnet, or None if no suitable template
        """
        matching_templates = self.get_templates_by_type(lead_magnet_type)
        if not matching_templates:
            return None

        # For now, just use the first matching template
        # In a more sophisticated version, we could score templates based on fit
        template = matching_templates[0]

        return template.generate(business_profile, customer_data)


def create_default_templates() -> List[LeadMagnetTemplate]:
    """
    Create a default set of lead magnet templates.

    Returns:
        List of LeadMagnetTemplate objects
    """
    templates = []

    # Website Assessment Template
    website_assessment = AssessmentTemplate(
        id="website_performance_assessment",
        name="Website Performance Assessment",
        description="An assessment that evaluates website performance and provides recommendations.",
        questions=[
            {
                "id": "website_speed",
                "text": "How would you rate your website's loading speed?",
                "type": "multiple_choice",
                "options": [
                    {"value": "very_slow", "text": "Very slow (5+ seconds)"},
                    {"value": "slow", "text": "Somewhat slow (3-5 seconds)"},
                    {"value": "average", "text": "Average (2-3 seconds)"},
                    {"value": "fast", "text": "Fast (1-2 seconds)"},
                    {"value": "very_fast", "text": "Very fast (under 1 second)"}
                ]
            },
            {
                "id": "mobile_friendly",
                "text": "Is your website optimized for mobile devices?",
                "type": "multiple_choice",
                "options": [
                    {"value": "not_at_all", "text": "Not at all"},
                    {"value": "somewhat", "text": "Somewhat, but needs improvement"},
                    {"value": "mostly", "text": "Mostly optimized"},
                    {"value": "fully", "text": "Fully optimized"},
                    {"value": "unsure", "text": "I'm not sure"}
                ]
            },
            {
                "id": "content_quality",
                "text": "How would you rate the quality and relevance of your website content?",
                "type": "multiple_choice",
                "options": [
                    {"value": "poor", "text": "Poor - outdated or minimal content"},
                    {"value": "fair", "text": "Fair - some good content but inconsistent"},
                    {"value": "good", "text": "Good - mostly relevant and up-to-date"},
                    {"value": "excellent", "text": "Excellent - comprehensive and engaging"}
                ]
            },
            {
                "id": "conversion_elements",
                "text": "Does your website have clear calls-to-action (CTAs) and conversion elements?",
                "type": "multiple_choice",
                "options": [
                    {"value": "none", "text": "No CTAs or conversion elements"},
                    {"value": "few", "text": "A few basic CTAs"},
                    {"value": "some", "text": "Some CTAs but not strategically placed"},
                    {"value": "many", "text": "Multiple strategic CTAs throughout the site"}
                ]
            },
            {
                "id": "seo_status",
                "text": "How would you describe your website's SEO (Search Engine Optimization)?",
                "type": "multiple_choice",
                "options": [
                    {"value": "none", "text": "No SEO work has been done"},
                    {"value": "basic", "text": "Basic SEO elements are in place"},
                    {"value": "moderate", "text": "Moderate SEO work with some keyword targeting"},
                    {"value": "advanced", "text": "Advanced SEO strategy with regular updates"},
                    {"value": "unsure", "text": "I'm not sure"}
                ]
            }
        ],
        result_categories=[
            {
                "id": "needs_improvement",
                "title": "Your Website Needs Significant Improvements",
                "description": "Based on your responses, your website has several areas that need attention to effectively attract and convert visitors.",
                "score_range": [0, 10],
                "recommendations": [
                    "Improve your website's loading speed to reduce bounce rates",
                    "Optimize your website for mobile devices",
                    "Develop a content strategy with relevant, engaging content",
                    "Implement clear calls-to-action throughout your site",
                    "Develop a basic SEO strategy to improve search visibility"
                ]
            },
            {
                "id": "average_performance",
                "title": "Your Website Has Average Performance",
                "description": "Your website has some strong elements but also opportunities for improvement to maximize its effectiveness.",
                "score_range": [11, 15],
                "recommendations": [
                    "Fine-tune your website's loading speed for optimal performance",
                    "Enhance mobile responsiveness across all pages",
                    "Expand your content to address customer pain points more effectively",
                    "Optimize placement and design of conversion elements",
                    "Develop a more comprehensive SEO strategy"
                ]
            },
            {
                "id": "high_performance",
                "title": "Your Website Is Performing Well",
                "description": "Congratulations! Your website is performing well in most areas, with just a few opportunities for enhancement.",
                "score_range": [16, 20],
                "recommendations": [
                    "Consider advanced performance optimizations for even faster loading",
                    "Implement A/B testing to further improve conversion rates",
                    "Develop more personalized content for different audience segments",
                    "Explore advanced SEO techniques to dominate your niche",
                    "Consider adding interactive elements to increase engagement"
                ]
            }
        ]
    )
    templates.append(website_assessment)

    # ROI Calculator Template
    roi_calculator = CalculatorTemplate(
        id="roi_calculator",
        name="ROI Calculator",
        description="A calculator that helps users estimate the return on investment.",
        inputs=[
            {
                "id": "current_cost",
                "label": "Current Monthly Cost",
                "type": "number",
                "min": 0,
                "default_value": 1000,
                "help_text": "Enter your current monthly spending in this area"
            },
            {
                "id": "expected_savings",
                "label": "Expected Savings Percentage",
                "type": "number",
                "min": 0,
                "max": 100,
                "default_value": 20,
                "help_text": "Estimated percentage savings with our solution"
            },
            {
                "id": "implementation_cost",
                "label": "Implementation Cost",
                "type": "number",
                "min": 0,
                "default_value": 5000,
                "help_text": "One-time cost to implement our solution"
            },
            {
                "id": "time_period",
                "label": "Time Period (Months)",
                "type": "number",
                "min": 1,
                "max": 60,
                "default_value": 12,
                "help_text": "Number of months to calculate ROI"
            }
        ],
        calculations={
            "monthly_savings": "current_cost * (expected_savings / 100)",
            "total_savings": "monthly_savings * time_period",
            "net_savings": "total_savings - implementation_cost",
            "roi_percentage": "(net_savings / implementation_cost) * 100",
            "break_even_months": "implementation_cost / monthly_savings"
        },
        results=[
            {
                "id": "monthly_savings",
                "label": "Estimated Monthly Savings",
                "format": "currency",
                "description": "Your estimated monthly savings with our solution"
            },
            {
                "id": "total_savings",
                "label": "Total Savings Over Time Period",
                "format": "currency",
                "description": "Your total savings over the selected time period"
            },
            {
                "id": "net_savings",
                "label": "Net Savings (After Implementation)",
                "format": "currency",
                "description": "Your net savings after accounting for implementation costs"
            },
            {
                "id": "roi_percentage",
                "label": "Return on Investment (ROI)",
                "format": "percentage",
                "description": "Your percentage return on investment"
            },
            {
                "id": "break_even_months",
                "label": "Break-Even Point",
                "format": "months",
                "description": "Number of months until you recover your implementation costs"
            }
        ]
    )
    templates.append(roi_calculator)

    # Add the interactive assessment template
    interactive_assessment = AssessmentTemplate(
        id="interactive_assessment",
        name="Interactive Assessment Tool",
        description="An interactive tool to assess customer needs and provide tailored recommendations.",
        questions=[
            {
                "id": "customer_needs",
                "text": "What are your customers' primary needs?",
                "type": "open_text",
            },
            {
                "id": "business_goals",
                "text": "What are your primary business goals?",
                "type": "multiple_choice",
                "options": [
                    {"value": "increase_sales", "text": "Increase sales"},
                    {"value": "generate_leads", "text": "Generate leads"},
                    {"value": "improve_engagement", "text": "Improve engagement"},
                ],
            },
        ],
        result_categories=[
            {
                "id": "growth_opportunity",
                "title": "Growth Opportunity Identified",
                "description": "Based on your responses, we have identified key areas for growth and improvement.",
                "recommendations": [
                    "Focus on improving customer engagement strategies.",
                    "Develop a targeted lead generation campaign.",
                    "Optimize your sales funnel for better conversions."
                ]
            }
        ]
    )
    templates.append(interactive_assessment)

    # Return the list of templates
    return templates

if __name__ == "__main__":
    # Example usage
    generator = LeadMagnetGenerator(create_default_templates())

    # Sample business profile
    business_profile = {
        "business_name": "WebDesign Pro",
        "business_type": "service",
        "business_description": "A web design agency specializing in small business websites",
        "industry": "web design",
        "brand_color": "#3366CC",
        "logo_url": "https://example.com/logo.png"
    }

    # Generate a website assessment lead magnet
    lead_magnet = generator.generate_lead_magnet(
        "website_performance_assessment",
        business_profile
    )

    # Print the generated lead magnet
    print(json.dumps(lead_magnet, indent=2))
