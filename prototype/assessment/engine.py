"""
Assessment Engine Module

This module processes assessment questionnaire responses and determines
the most appropriate lead magnet type for a business based on their answers.

The engine is designed to be industry-agnostic and adaptable to any business type.
"""

import json
from typing import Dict, List, Any, Optional
from .questionnaire import Questionnaire

class LeadMagnetType:
    """Represents a type of lead magnet that can be recommended."""
    
    def __init__(self, id: str, name: str, description: str, 
                 business_types: List[str], customer_needs: List[str],
                 technical_level: int, example: str):
        """
        Initialize a lead magnet type.
        
        Args:
            id: Unique identifier for this lead magnet type
            name: Display name of the lead magnet type
            description: Detailed description of what this lead magnet is
            business_types: List of business types this is suitable for
            customer_needs: List of customer needs this addresses
            technical_level: Technical complexity level (1-5)
            example: Example description of this lead magnet type
        """
        self.id = id
        self.name = name
        self.description = description
        self.business_types = business_types
        self.customer_needs = customer_needs
        self.technical_level = technical_level
        self.example = example
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert lead magnet type to dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "business_types": self.business_types,
            "customer_needs": self.customer_needs,
            "technical_level": self.technical_level,
            "example": self.example
        }


class AssessmentEngine:
    """
    Engine that processes assessment responses and recommends lead magnet types.
    
    This engine uses a scoring algorithm to match business characteristics
    with appropriate lead magnet types.
    """
    
    def __init__(self, lead_magnet_types: Optional[List[LeadMagnetType]] = None):
        """
        Initialize the assessment engine.
        
        Args:
            lead_magnet_types: Optional list of lead magnet types to use
        """
        self.lead_magnet_types = lead_magnet_types or []
    
    def add_lead_magnet_type(self, lead_magnet_type: LeadMagnetType) -> None:
        """
        Add a lead magnet type to the engine.
        
        Args:
            lead_magnet_type: LeadMagnetType object to add
        """
        self.lead_magnet_types.append(lead_magnet_type)
    
    def process_responses(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process questionnaire responses and recommend lead magnet types.
        
        Args:
            responses: Dictionary of question IDs to response values
            
        Returns:
            Dictionary containing recommendations and analysis
        """
        # Extract key business characteristics from responses
        business_profile = self._extract_business_profile(responses)
        customer_needs = self._extract_customer_needs(responses)
        technical_capability = self._extract_technical_capability(responses)
        marketing_goals = self._extract_marketing_goals(responses)
        
        # Score each lead magnet type based on fit
        scored_types = []
        for lm_type in self.lead_magnet_types:
            score = self._calculate_score(
                lm_type, 
                business_profile, 
                customer_needs, 
                technical_capability,
                marketing_goals
            )
            scored_types.append({
                "lead_magnet_type": lm_type,
                "score": score,
                "fit_analysis": self._analyze_fit(
                    lm_type, 
                    business_profile, 
                    customer_needs, 
                    technical_capability
                )
            })
        
        # Sort by score (descending)
        scored_types.sort(key=lambda x: x["score"], reverse=True)
        
        # Prepare recommendations
        recommendations = []
        for item in scored_types[:3]:  # Top 3 recommendations
            lm_type = item["lead_magnet_type"]
            recommendations.append({
                "id": lm_type.id,
                "name": lm_type.name,
                "description": lm_type.description,
                "score": item["score"],
                "fit_analysis": item["fit_analysis"],
                "example": lm_type.example
            })
        
        return {
            "business_profile": business_profile,
            "customer_needs": customer_needs,
            "technical_capability": technical_capability,
            "marketing_goals": marketing_goals,
            "recommendations": recommendations
        }
    
    def _extract_business_profile(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Extract business profile information from responses."""
        return {
            "business_type": responses.get("business_type"),
            "business_size": responses.get("business_size"),
            "business_description": responses.get("business_description"),
            "target_audience": responses.get("target_audience")
        }
    
    def _extract_customer_needs(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Extract customer needs information from responses."""
        return {
            "pain_points": responses.get("customer_pain_points", []),
            "sales_cycle_length": responses.get("sales_cycle_length"),
            "common_questions": responses.get("customer_questions")
        }
    
    def _extract_technical_capability(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Extract technical capability information from responses."""
        return {
            "website_platform": responses.get("website_platform"),
            "technical_resources": responses.get("technical_resources"),
            "tech_comfort": responses.get("tech_comfort", 3)
        }
    
    def _extract_marketing_goals(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Extract marketing goals information from responses."""
        return {
            "primary_goals": responses.get("marketing_goals", []),
            "lead_quality_importance": responses.get("lead_quality_importance", 3)
        }
    
    def _calculate_score(self, lead_magnet_type: LeadMagnetType, 
                         business_profile: Dict[str, Any],
                         customer_needs: Dict[str, Any],
                         technical_capability: Dict[str, Any],
                         marketing_goals: Dict[str, Any]) -> float:
        """
        Calculate a score representing how well a lead magnet type fits the business.
        
        Higher scores indicate better fit.
        """
        score = 0.0
        
        # Business type fit
        if business_profile.get("business_type") in lead_magnet_type.business_types:
            score += 2.0
        elif "any" in lead_magnet_type.business_types:
            score += 1.0
        
        # Customer needs fit
        pain_points = customer_needs.get("pain_points", [])
        for need in lead_magnet_type.customer_needs:
            if need in pain_points:
                score += 1.5
        
        # Technical capability fit
        tech_comfort = technical_capability.get("tech_comfort", 3)
        if lead_magnet_type.technical_level <= tech_comfort:
            score += 1.0
        else:
            # Penalize if technical requirements exceed capability
            score -= 0.5 * (lead_magnet_type.technical_level - tech_comfort)
        
        # Marketing goals fit
        primary_goals = marketing_goals.get("primary_goals", [])
        if "leads" in primary_goals:
            score += 1.0
        if "conversion" in primary_goals:
            score += 0.5
        if "authority" in primary_goals:
            score += 0.5
        
        # Lead quality vs quantity preference
        lead_quality_importance = marketing_goals.get("lead_quality_importance", 3)
        if lead_quality_importance >= 4 and "quality" in lead_magnet_type.id:
            score += 1.0
        elif lead_quality_importance <= 2 and "quantity" in lead_magnet_type.id:
            score += 1.0
        
        return score
    
    def _analyze_fit(self, lead_magnet_type: LeadMagnetType,
                    business_profile: Dict[str, Any],
                    customer_needs: Dict[str, Any],
                    technical_capability: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze why a lead magnet type fits or doesn't fit the business.
        
        Returns a dictionary with strengths and potential issues.
        """
        strengths = []
        issues = []
        
        # Business type fit
        if business_profile.get("business_type") in lead_magnet_type.business_types:
            strengths.append(f"Well-suited for your business type")
        elif "any" in lead_magnet_type.business_types:
            strengths.append(f"Adaptable to various business types including yours")
        else:
            issues.append(f"Not typically used by your business type, but can be adapted")
        
        # Customer needs fit
        pain_points = customer_needs.get("pain_points", [])
        matching_needs = [need for need in lead_magnet_type.customer_needs if need in pain_points]
        if matching_needs:
            strengths.append(f"Addresses key customer pain points: {', '.join(matching_needs)}")
        else:
            issues.append("May not directly address your customers' main pain points")
        
        # Technical capability fit
        tech_comfort = technical_capability.get("tech_comfort", 3)
        if lead_magnet_type.technical_level <= tech_comfort:
            strengths.append(f"Matches your technical capabilities")
        else:
            issues.append(f"May require more technical expertise than you currently have")
        
        return {
            "strengths": strengths,
            "potential_issues": issues
        }


def create_default_lead_magnet_types() -> List[LeadMagnetType]:
    """
    Create a default set of lead magnet types.
    
    Returns:
        List of LeadMagnetType objects
    """
    return [
        LeadMagnetType(
            id="interactive_assessment",
            name="Interactive Assessment Tool",
            description="An interactive tool that evaluates the user's current situation and provides personalized recommendations.",
            business_types=["service", "hybrid", "content"],
            customer_needs=["knowledge", "complexity", "risk"],
            technical_level=3,
            example="A website performance analyzer that evaluates loading speed, mobile optimization, and provides specific improvement recommendations."
        ),
        
        LeadMagnetType(
            id="calculator",
            name="Value Calculator",
            description="A calculator that helps users quantify potential savings, ROI, or other valuable metrics.",
            business_types=["service", "product", "hybrid"],
            customer_needs=["cost", "complexity", "risk"],
            technical_level=3,
            example="A savings calculator that shows how much money a customer could save by switching to your product or service."
        ),
        
        LeadMagnetType(
            id="personalized_plan",
            name="Personalized Plan Generator",
            description="A tool that creates a custom plan or roadmap based on the user's specific situation.",
            business_types=["service", "hybrid", "content"],
            customer_needs=["knowledge", "complexity", "support"],
            technical_level=4,
            example="A marketing plan generator that creates a customized strategy based on business goals, target audience, and budget."
        ),
        
        LeadMagnetType(
            id="diagnostic_tool",
            name="Problem Diagnostic Tool",
            description="A tool that helps users identify and diagnose specific problems or issues they're facing.",
            business_types=["service", "product", "hybrid"],
            customer_needs=["knowledge", "complexity", "support"],
            technical_level=3,
            example="A home plumbing diagnostic tool that helps identify potential issues based on symptoms and provides recommendations."
        ),
        
        LeadMagnetType(
            id="interactive_quiz",
            name="Interactive Quiz or Survey",
            description="An engaging quiz that helps users learn something about themselves or their situation.",
            business_types=["any"],
            customer_needs=["knowledge", "complexity"],
            technical_level=2,
            example="A 'What type of [product/service] is right for you?' quiz that recommends specific options based on preferences."
        ),
        
        LeadMagnetType(
            id="template_library",
            name="Template or Resource Library",
            description="A collection of templates, checklists, or resources tailored to the user's specific needs.",
            business_types=["any"],
            customer_needs=["time", "knowledge", "access"],
            technical_level=2,
            example="A customized collection of templates or resources based on the user's industry, role, or specific challenges."
        ),
        
        LeadMagnetType(
            id="comparison_tool",
            name="Comparison or Selection Tool",
            description="A tool that helps users compare options or make a selection based on their criteria.",
            business_types=["product", "hybrid", "content"],
            customer_needs=["complexity", "knowledge", "risk"],
            technical_level=3,
            example="A product comparison tool that helps users find the right option based on their specific requirements and preferences."
        ),
        
        LeadMagnetType(
            id="mini_course",
            name="Personalized Mini-Course",
            description="A short educational course with content tailored to the user's specific needs or level.",
            business_types=["service", "content", "nonprofit"],
            customer_needs=["knowledge", "support", "access"],
            technical_level=3,
            example="A 5-day email course with content adapted to the user's experience level, industry, or specific challenges."
        ),
        
        LeadMagnetType(
            id="free_consultation",
            name="Automated Consultation Scheduler",
            description="A tool that qualifies leads and automatically schedules a personalized consultation.",
            business_types=["service", "hybrid"],
            customer_needs=["support", "knowledge", "complexity"],
            technical_level=2,
            example="A consultation booking tool that gathers information about the user's needs and schedules a call with the right expert."
        ),
        
        LeadMagnetType(
            id="configurator",
            name="Product or Service Configurator",
            description="A tool that allows users to customize a product or service to their specific needs.",
            business_types=["product", "hybrid"],
            customer_needs=["complexity", "quality", "access"],
            technical_level=4,
            example="A custom solution builder that allows users to configure a product or service package based on their specific requirements."
        )
    ]


if __name__ == "__main__":
    # Example usage
    engine = AssessmentEngine(create_default_lead_magnet_types())
    
    # Sample responses
    sample_responses = {
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
    
    # Process responses
    results = engine.process_responses(sample_responses)
    
    # Print recommendations
    print(json.dumps(results["recommendations"], indent=2))
