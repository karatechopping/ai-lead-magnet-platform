"""
Assessment Questionnaire Module

This module provides the core functionality for the flexible assessment system
that determines the most appropriate lead magnet type for any business.

The questionnaire is designed to be industry-agnostic and adaptable to any business type.
"""

import json
from typing import Dict, List, Any, Optional

class Question:
    """Base class for assessment questions."""
    
    def __init__(self, id: str, text: str, category: str, weight: float = 1.0):
        """
        Initialize a question.
        
        Args:
            id: Unique identifier for the question
            text: The question text to display
            category: Category this question belongs to (business_profile, customer_journey, etc.)
            weight: Importance weight of this question (default: 1.0)
        """
        self.id = id
        self.text = text
        self.category = category
        self.weight = weight
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert question to dictionary representation."""
        return {
            "id": self.id,
            "text": self.text,
            "category": self.category,
            "weight": self.weight,
            "type": self.__class__.__name__
        }


class MultipleChoiceQuestion(Question):
    """Multiple choice question with predefined options."""
    
    def __init__(self, id: str, text: str, category: str, options: List[Dict[str, Any]], 
                 weight: float = 1.0, allow_multiple: bool = False):
        """
        Initialize a multiple choice question.
        
        Args:
            id: Unique identifier for the question
            text: The question text to display
            category: Category this question belongs to
            options: List of option dictionaries with 'value' and 'text' keys
            weight: Importance weight of this question
            allow_multiple: Whether multiple options can be selected
        """
        super().__init__(id, text, category, weight)
        self.options = options
        self.allow_multiple = allow_multiple
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert question to dictionary representation."""
        result = super().to_dict()
        result.update({
            "options": self.options,
            "allow_multiple": self.allow_multiple
        })
        return result


class TextQuestion(Question):
    """Free text input question."""
    
    def __init__(self, id: str, text: str, category: str, weight: float = 1.0, 
                 max_length: Optional[int] = None):
        """
        Initialize a text question.
        
        Args:
            id: Unique identifier for the question
            text: The question text to display
            category: Category this question belongs to
            weight: Importance weight of this question
            max_length: Maximum length of the answer (optional)
        """
        super().__init__(id, text, category, weight)
        self.max_length = max_length
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert question to dictionary representation."""
        result = super().to_dict()
        if self.max_length:
            result["max_length"] = self.max_length
        return result


class ScaleQuestion(Question):
    """Numeric scale question (e.g., 1-5, 1-10)."""
    
    def __init__(self, id: str, text: str, category: str, min_value: int, max_value: int, 
                 weight: float = 1.0, labels: Optional[Dict[int, str]] = None):
        """
        Initialize a scale question.
        
        Args:
            id: Unique identifier for the question
            text: The question text to display
            category: Category this question belongs to
            min_value: Minimum value on the scale
            max_value: Maximum value on the scale
            weight: Importance weight of this question
            labels: Optional dictionary mapping scale values to label text
        """
        super().__init__(id, text, category, weight)
        self.min_value = min_value
        self.max_value = max_value
        self.labels = labels or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert question to dictionary representation."""
        result = super().to_dict()
        result.update({
            "min_value": self.min_value,
            "max_value": self.max_value,
            "labels": self.labels
        })
        return result


class ConditionalQuestion(Question):
    """Question that is only shown based on previous answers."""
    
    def __init__(self, id: str, text: str, category: str, condition: Dict[str, Any], 
                 weight: float = 1.0):
        """
        Initialize a conditional question.
        
        Args:
            id: Unique identifier for the question
            text: The question text to display
            category: Category this question belongs to
            condition: Dictionary with question_id and expected value(s)
            weight: Importance weight of this question
        """
        super().__init__(id, text, category, weight)
        self.condition = condition
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert question to dictionary representation."""
        result = super().to_dict()
        result["condition"] = self.condition
        return result


class Questionnaire:
    """Manages a collection of questions for the assessment."""
    
    def __init__(self):
        """Initialize an empty questionnaire."""
        self.questions = []
        self.categories = set()
    
    def add_question(self, question: Question) -> None:
        """
        Add a question to the questionnaire.
        
        Args:
            question: Question object to add
        """
        self.questions.append(question)
        self.categories.add(question.category)
    
    def get_questions_by_category(self, category: str) -> List[Question]:
        """
        Get all questions in a specific category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of questions in the specified category
        """
        return [q for q in self.questions if q.category == category]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert questionnaire to dictionary representation."""
        return {
            "questions": [q.to_dict() for q in self.questions],
            "categories": list(self.categories)
        }
    
    def to_json(self) -> str:
        """Convert questionnaire to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Questionnaire':
        """
        Create a questionnaire from a dictionary representation.
        
        Args:
            data: Dictionary containing questionnaire data
            
        Returns:
            New Questionnaire instance
        """
        questionnaire = cls()
        
        for q_data in data.get("questions", []):
            q_type = q_data.get("type")
            
            if q_type == "MultipleChoiceQuestion":
                question = MultipleChoiceQuestion(
                    id=q_data["id"],
                    text=q_data["text"],
                    category=q_data["category"],
                    options=q_data["options"],
                    weight=q_data.get("weight", 1.0),
                    allow_multiple=q_data.get("allow_multiple", False)
                )
            elif q_type == "TextQuestion":
                question = TextQuestion(
                    id=q_data["id"],
                    text=q_data["text"],
                    category=q_data["category"],
                    weight=q_data.get("weight", 1.0),
                    max_length=q_data.get("max_length")
                )
            elif q_type == "ScaleQuestion":
                question = ScaleQuestion(
                    id=q_data["id"],
                    text=q_data["text"],
                    category=q_data["category"],
                    min_value=q_data["min_value"],
                    max_value=q_data["max_value"],
                    weight=q_data.get("weight", 1.0),
                    labels=q_data.get("labels", {})
                )
            elif q_type == "ConditionalQuestion":
                question = ConditionalQuestion(
                    id=q_data["id"],
                    text=q_data["text"],
                    category=q_data["category"],
                    condition=q_data["condition"],
                    weight=q_data.get("weight", 1.0)
                )
            else:
                # Default to base Question class
                question = Question(
                    id=q_data["id"],
                    text=q_data["text"],
                    category=q_data["category"],
                    weight=q_data.get("weight", 1.0)
                )
                
            questionnaire.add_question(question)
            
        return questionnaire
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Questionnaire':
        """
        Create a questionnaire from a JSON string.
        
        Args:
            json_str: JSON string containing questionnaire data
            
        Returns:
            New Questionnaire instance
        """
        data = json.loads(json_str)
        return cls.from_dict(data)


def create_default_questionnaire() -> Questionnaire:
    """
    Create a default questionnaire with industry-agnostic questions.
    
    Returns:
        Questionnaire with default questions
    """
    questionnaire = Questionnaire()
    
    # Business Profile questions
    questionnaire.add_question(MultipleChoiceQuestion(
        id="business_type",
        text="Which of the following best describes your business?",
        category="business_profile",
        options=[
            {"value": "service", "text": "Service-based business"},
            {"value": "product", "text": "Product-based business"},
            {"value": "hybrid", "text": "Both services and products"},
            {"value": "content", "text": "Content or information business"},
            {"value": "nonprofit", "text": "Nonprofit organization"}
        ],
        weight=1.5
    ))
    
    questionnaire.add_question(MultipleChoiceQuestion(
        id="business_size",
        text="How many people work in your business?",
        category="business_profile",
        options=[
            {"value": "solo", "text": "Just me"},
            {"value": "micro", "text": "2-5 people"},
            {"value": "small", "text": "6-20 people"},
            {"value": "medium", "text": "21-100 people"},
            {"value": "large", "text": "More than 100 people"}
        ]
    ))
    
    questionnaire.add_question(TextQuestion(
        id="business_description",
        text="In a few sentences, describe what your business does and who you serve:",
        category="business_profile",
        weight=1.8
    ))
    
    questionnaire.add_question(MultipleChoiceQuestion(
        id="target_audience",
        text="Who is your primary target audience?",
        category="business_profile",
        options=[
            {"value": "b2c", "text": "Individual consumers (B2C)"},
            {"value": "b2b_small", "text": "Small businesses (B2B)"},
            {"value": "b2b_enterprise", "text": "Large enterprises (B2B)"},
            {"value": "b2g", "text": "Government or public sector"},
            {"value": "mixed", "text": "Mixed audience"}
        ],
        weight=1.3
    ))
    
    # Customer Journey questions
    questionnaire.add_question(MultipleChoiceQuestion(
        id="customer_pain_points",
        text="What are the main pain points your customers experience? (Select up to 3)",
        category="customer_journey",
        options=[
            {"value": "time", "text": "Lack of time"},
            {"value": "knowledge", "text": "Lack of knowledge or expertise"},
            {"value": "cost", "text": "High costs or budget constraints"},
            {"value": "complexity", "text": "Complexity or confusion"},
            {"value": "quality", "text": "Poor quality alternatives"},
            {"value": "access", "text": "Limited access to resources"},
            {"value": "risk", "text": "Risk or uncertainty"},
            {"value": "support", "text": "Lack of support or guidance"}
        ],
        allow_multiple=True,
        weight=1.7
    ))
    
    questionnaire.add_question(ScaleQuestion(
        id="sales_cycle_length",
        text="How long is your typical sales cycle?",
        category="customer_journey",
        min_value=1,
        max_value=5,
        labels={
            1: "Very short (immediate purchase)",
            2: "Short (days)",
            3: "Medium (weeks)",
            4: "Long (months)",
            5: "Very long (6+ months)"
        },
        weight=1.2
    ))
    
    questionnaire.add_question(TextQuestion(
        id="customer_questions",
        text="What are the top 3 questions potential customers ask before buying?",
        category="customer_journey",
        weight=1.6
    ))
    
    # Value Proposition questions
    questionnaire.add_question(TextQuestion(
        id="unique_value",
        text="What makes your business different from competitors?",
        category="value_proposition",
        weight=1.5
    ))
    
    questionnaire.add_question(MultipleChoiceQuestion(
        id="customer_value",
        text="Which of these do your customers value most about your business?",
        category="value_proposition",
        options=[
            {"value": "quality", "text": "Quality of products/services"},
            {"value": "price", "text": "Competitive pricing"},
            {"value": "expertise", "text": "Expertise and knowledge"},
            {"value": "convenience", "text": "Convenience or ease of use"},
            {"value": "support", "text": "Customer service and support"},
            {"value": "results", "text": "Proven results or outcomes"},
            {"value": "innovation", "text": "Innovation or unique approach"}
        ],
        weight=1.4
    ))
    
    # Technical Capability questions
    questionnaire.add_question(MultipleChoiceQuestion(
        id="website_platform",
        text="What platform is your website built on?",
        category="technical_capability",
        options=[
            {"value": "wordpress", "text": "WordPress"},
            {"value": "shopify", "text": "Shopify"},
            {"value": "wix", "text": "Wix"},
            {"value": "squarespace", "text": "Squarespace"},
            {"value": "custom", "text": "Custom-built website"},
            {"value": "other", "text": "Other platform"},
            {"value": "none", "text": "Don't have a website yet"}
        ]
    ))
    
    questionnaire.add_question(MultipleChoiceQuestion(
        id="technical_resources",
        text="Who manages your website and digital marketing?",
        category="technical_capability",
        options=[
            {"value": "self", "text": "I do it myself"},
            {"value": "internal", "text": "Internal team member"},
            {"value": "freelancer", "text": "Freelancer or contractor"},
            {"value": "agency", "text": "External agency"},
            {"value": "nobody", "text": "Nobody currently"}
        ]
    ))
    
    questionnaire.add_question(ScaleQuestion(
        id="tech_comfort",
        text="How comfortable are you with implementing new technologies?",
        category="technical_capability",
        min_value=1,
        max_value=5,
        labels={
            1: "Not comfortable at all",
            2: "Slightly comfortable",
            3: "Moderately comfortable",
            4: "Very comfortable",
            5: "Extremely comfortable"
        }
    ))
    
    # Marketing Goals questions
    questionnaire.add_question(MultipleChoiceQuestion(
        id="marketing_goals",
        text="What are your primary marketing goals? (Select up to 3)",
        category="marketing_goals",
        options=[
            {"value": "awareness", "text": "Increase brand awareness"},
            {"value": "leads", "text": "Generate more leads"},
            {"value": "conversion", "text": "Improve conversion rates"},
            {"value": "retention", "text": "Increase customer retention"},
            {"value": "upsell", "text": "Upsell or cross-sell to existing customers"},
            {"value": "authority", "text": "Establish industry authority"},
            {"value": "engagement", "text": "Increase audience engagement"}
        ],
        allow_multiple=True,
        weight=1.6
    ))
    
    questionnaire.add_question(ScaleQuestion(
        id="lead_quality_importance",
        text="How important is lead quality vs. lead quantity for your business?",
        category="marketing_goals",
        min_value=1,
        max_value=5,
        labels={
            1: "Quantity is much more important",
            3: "Both are equally important",
            5: "Quality is much more important"
        },
        weight=1.3
    ))
    
    return questionnaire


if __name__ == "__main__":
    # Example usage
    questionnaire = create_default_questionnaire()
    print(questionnaire.to_json())
