"""
Quiz Lead Magnet Creator for AI Lead Magnet Platform

This module implements the Creation Team agents responsible for designing and building
a quiz-based lead magnet based on business requirements.
"""

import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime

class DesignArchitectAgent:
    """
    Design Architect Agent that creates the structure and flow for quiz-based lead magnets.
    
    This agent is responsible for:
    - Creating overall lead magnet architecture
    - Designing user experience flow
    - Determining optimal quiz structure
    - Balancing simplicity with effectiveness
    - Adapting design based on business feedback
    """
    
    def __init__(self, memory_manager=None):
        """
        Initialize the Design Architect Agent.
        
        Args:
            memory_manager: The Memory Manager agent for storing and retrieving context
        """
        self.memory_manager = memory_manager
        self.design_state = {
            "status": "initialized",
            "lead_magnet_type": "quiz",
            "business_info": {},
            "language_variant": "US",
            "design_version": 1,
            "last_updated": datetime.now().isoformat()
        }
    
    def create_quiz_design(self, business_info: Dict[str, Any], language_variant: str = "US") -> Dict[str, Any]:
        """
        Create a quiz design based on business information.
        
        Args:
            business_info: Information about the business
            language_variant: Language variant to use (US, UK, AU, NZ)
            
        Returns:
            Dict containing the quiz design
        """
        self.design_state["business_info"] = business_info
        self.design_state["language_variant"] = language_variant
        self.design_state["status"] = "design_in_progress"
        self.design_state["last_updated"] = datetime.now().isoformat()
        
        # Extract relevant information for quiz design
        business_name = business_info.get("name", "")
        industry = business_info.get("industry", "")
        target_audience = business_info.get("target_audience", "")
        pain_points = business_info.get("customer_pain_points", [])
        usp = business_info.get("unique_selling_proposition", "")
        
        # Determine quiz title based on industry and pain points
        quiz_title = self._generate_quiz_title(business_name, industry, pain_points)
        
        # Determine quiz structure based on industry and pain points
        quiz_structure = self._determine_quiz_structure(industry, pain_points)
        
        # Create quiz design
        quiz_design = {
            "title": quiz_title,
            "description": self._generate_quiz_description(business_name, industry, pain_points, usp),
            "structure": quiz_structure,
            "results_approach": self._determine_results_approach(industry, pain_points, usp),
            "branding": {
                "business_name": business_name,
                "primary_color": "#4A90E2",  # Default blue, would be customized in real implementation
                "secondary_color": "#F5A623",  # Default orange, would be customized in real implementation
                "font_family": "Arial, sans-serif"  # Default font, would be customized in real implementation
            },
            "lead_capture": {
                "timing": "before_results",  # Capture leads before showing results
                "required_fields": ["name", "email"],
                "optional_fields": ["company"]
            },
            "language_variant": language_variant
        }
        
        self.design_state["quiz_design"] = quiz_design
        self.design_state["status"] = "design_completed"
        self.design_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("quiz_design", quiz_design)
            self.memory_manager.store("design_state", self.design_state)
        
        return quiz_design
    
    def _generate_quiz_title(self, business_name: str, industry: str, pain_points: List[str]) -> str:
        """
        Generate a compelling quiz title based on business information.
        
        Args:
            business_name: Name of the business
            industry: Industry of the business
            pain_points: Customer pain points
            
        Returns:
            Quiz title
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        if "web design" in industry.lower() or "website" in industry.lower():
            return f"How Well Is Your Website Converting? Take The {business_name} Assessment"
        
        if "marketing" in industry.lower():
            return f"Is Your Marketing Strategy Working? Take The {business_name} Quiz"
        
        if "consulting" in industry.lower():
            return f"How Optimized Is Your Business? The {business_name} Efficiency Quiz"
        
        # Default title
        return f"How Does Your Business Compare? The {business_name} Industry Quiz"
    
    def _generate_quiz_description(self, business_name: str, industry: str, pain_points: List[str], usp: str) -> str:
        """
        Generate a quiz description based on business information.
        
        Args:
            business_name: Name of the business
            industry: Industry of the business
            pain_points: Customer pain points
            usp: Unique selling proposition
            
        Returns:
            Quiz description
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        pain_point_text = ""
        if pain_points:
            main_pain = pain_points[0]
            pain_point_text = f" struggling with {main_pain}"
        
        return f"This quick assessment from {business_name} will help you identify areas where your {industry.lower()} business{pain_point_text} could improve. Based on {usp}, we'll provide personalized recommendations to help you succeed."
    
    def _determine_quiz_structure(self, industry: str, pain_points: List[str]) -> Dict[str, Any]:
        """
        Determine the optimal quiz structure based on industry and pain points.
        
        Args:
            industry: Industry of the business
            pain_points: Customer pain points
            
        Returns:
            Dict containing the quiz structure
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        # Determine number of questions based on industry complexity
        if any(x in industry.lower() for x in ["tech", "software", "engineering", "consulting"]):
            question_count = 7  # More complex industries get more questions
        else:
            question_count = 5  # Simpler industries get fewer questions
        
        # Determine if we should use branching logic
        use_branching = any(x in industry.lower() for x in ["marketing", "consulting", "strategy"])
        
        # Create structure
        structure = {
            "question_count": question_count,
            "use_branching": use_branching,
            "question_types": ["multiple_choice", "scale"],
            "progress_indicator": True,
            "allow_skipping": False
        }
        
        return structure
    
    def _determine_results_approach(self, industry: str, pain_points: List[str], usp: str) -> Dict[str, Any]:
        """
        Determine the approach for presenting quiz results.
        
        Args:
            industry: Industry of the business
            pain_points: Customer pain points
            usp: Unique selling proposition
            
        Returns:
            Dict containing the results approach
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        # Determine if we should use scoring or categories
        if any(x in industry.lower() for x in ["assessment", "audit", "performance"]):
            approach_type = "score"  # Score-based results (e.g., 72/100)
        else:
            approach_type = "category"  # Category-based results (e.g., "Growth-Focused")
        
        # Determine how many result types to have
        if approach_type == "score":
            result_types = [
                {"range": [0, 40], "label": "Needs Improvement", "description": "Your current approach has significant room for improvement."},
                {"range": [41, 70], "label": "Average", "description": "You're doing okay, but there are clear opportunities to improve."},
                {"range": [71, 90], "label": "Good", "description": "You're doing well, with a few areas that could be optimized."},
                {"range": [91, 100], "label": "Excellent", "description": "You're performing at a high level across the board."}
            ]
        else:
            result_types = [
                {"id": "type_a", "label": "Efficiency-Focused", "description": "You prioritize streamlined operations and cost-effectiveness."},
                {"id": "type_b", "label": "Growth-Focused", "description": "You prioritize expansion and capturing market share."},
                {"id": "type_c", "label": "Innovation-Focused", "description": "You prioritize new approaches and creative solutions."},
                {"id": "type_d", "label": "Quality-Focused", "description": "You prioritize excellence and premium experiences."}
            ]
        
        # Create results approach
        results_approach = {
            "type": approach_type,
            "result_types": result_types,
            "show_detailed_breakdown": True,
            "include_recommendations": True,
            "call_to_action": {
                "text": f"Schedule a free consultation with {usp}",
                "button_text": "Book Your Free Consultation",
                "url": "#contact"  # Would be customized in real implementation
            }
        }
        
        return results_approach
    
    def revise_design(self, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Revise the quiz design based on feedback.
        
        Args:
            feedback: Feedback on the design
            
        Returns:
            Dict containing the revised quiz design
        """
        if "quiz_design" not in self.design_state:
            raise ValueError("No quiz design to revise")
        
        self.design_state["status"] = "revision_in_progress"
        self.design_state["design_version"] += 1
        self.design_state["last_updated"] = datetime.now().isoformat()
        
        # Get current design
        quiz_design = self.design_state["quiz_design"]
        
        # Apply feedback
        if "title" in feedback:
            quiz_design["title"] = feedback["title"]
        
        if "description" in feedback:
            quiz_design["description"] = feedback["description"]
        
        if "structure" in feedback:
            for key, value in feedback["structure"].items():
                quiz_design["structure"][key] = value
        
        if "results_approach" in feedback:
            for key, value in feedback["results_approach"].items():
                quiz_design["results_approach"][key] = value
        
        if "branding" in feedback:
            for key, value in feedback["branding"].items():
                quiz_design["branding"][key] = value
        
        if "lead_capture" in feedback:
            for key, value in feedback["lead_capture"].items():
                quiz_design["lead_capture"][key] = value
        
        self.design_state["quiz_design"] = quiz_design
        self.design_state["status"] = "revision_completed"
        self.design_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("quiz_design", quiz_design)
            self.memory_manager.store("design_state", self.design_state)
        
        return quiz_design
    
    def get_design_state(self) -> Dict[str, Any]:
        """
        Get the current design state.
        
        Returns:
            Dict containing the current design state
        """
        return self.design_state


class ContentGeneratorAgent:
    """
    Content Generator Agent that creates compelling content for quiz-based lead magnets.
    
    This agent is responsible for:
    - Writing copy and content in the appropriate language variant
    - Generating questions for quizzes
    - Creating personalized messaging
    - Ensuring content aligns with business voice and USPs
    - Adapting content based on target customer pain points
    """
    
    def __init__(self, memory_manager=None):
        """
        Initialize the Content Generator Agent.
        
        Args:
            memory_manager: The Memory Manager agent for storing and retrieving context
        """
        self.memory_manager = memory_manager
        self.content_state = {
            "status": "initialized",
            "lead_magnet_type": "quiz",
            "business_info": {},
            "language_variant": "US",
            "content_version": 1,
            "last_updated": datetime.now().isoformat()
        }
    
    def generate_quiz_content(self, quiz_design: Dict[str, Any], business_info: Dict[str, Any], language_variant: str = "US") -> Dict[str, Any]:
        """
        Generate content for a quiz based on the design and business information.
        
        Args:
            quiz_design: The quiz design
            business_info: Information about the business
            language_variant: Language variant to use (US, UK, AU, NZ)
            
        Returns:
            Dict containing the quiz content
        """
        self.content_state["business_info"] = business_info
        self.content_state["language_variant"] = language_variant
        self.content_state["status"] = "content_generation_in_progress"
        self.content_state["last_updated"] = datetime.now().isoformat()
        
        # Extract relevant information
        industry = business_info.get("industry", "")
        pain_points = business_info.get("customer_pain_points", [])
        usp = business_info.get("unique_selling_proposition", "")
        
        # Generate questions based on industry and pain points
        questions = self._generate_questions(quiz_design, industry, pain_points)
        
        # Generate results content
        results_content = self._generate_results_content(quiz_design, industry, pain_points, usp)
        
        # Generate lead capture content
        lead_capture_content = self._generate_lead_capture_content(quiz_design, business_info)
        
        # Apply language variant
        questions = self._apply_language_variant(questions, language_variant)
        results_content = self._apply_language_variant(results_content, language_variant)
        lead_capture_content = self._apply_language_variant(lead_capture_content, language_variant)
        
        # Create content package
        quiz_content = {
            "welcome_screen": {
                "headline": quiz_design["title"],
                "subheadline": quiz_design["description"],
                "button_text": "Start Quiz"
            },
            "questions": questions,
            "results": results_content,
            "lead_capture": lead_capture_content,
            "language_variant": language_variant
        }
        
        self.content_state["quiz_content"] = quiz_content
        self.content_state["status"] = "content_generation_completed"
        self.content_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("quiz_content", quiz_content)
            self.memory_manager.store("content_state", self.content_state)
        
        return quiz_content
    
    def _generate_questions(self, quiz_design: Dict[str, Any], industry: str, pain_points: List[str]) -> List[Dict[str, Any]]:
        """
        Generate questions for the quiz based on industry and pain points.
        
        Args:
            quiz_design: The quiz design
            industry: Industry of the business
            pain_points: Customer pain points
            
        Returns:
            List of questions
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        question_count = quiz_design["structure"]["question_count"]
        use_branching = quiz_design["structure"]["use_branching"]
        question_types = quiz_design["structure"]["question_types"]
        
        questions = []
        
        # Web design industry example
        if "web design" in industry.lower() or "website" in industry.lower():
            questions = [
                {
                    "id": "q1",
                    "text": "How quickly does your website load on mobile devices?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q1_a", "text": "Under 2 seconds", "score": 10},
                        {"id": "q1_b", "text": "2-4 seconds", "score": 7},
                        {"id": "q1_c", "text": "4-6 seconds", "score": 4},
                        {"id": "q1_d", "text": "Over 6 seconds", "score": 1},
                        {"id": "q1_e", "text": "I don't know", "score": 0}
                    ]
                },
                {
                    "id": "q2",
                    "text": "Is your website fully responsive on all devices?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q2_a", "text": "Yes, works perfectly on all devices", "score": 10},
                        {"id": "q2_b", "text": "Mostly, with minor issues on some devices", "score": 7},
                        {"id": "q2_c", "text": "It works on mobile but isn't optimized", "score": 4},
                        {"id": "q2_d", "text": "No, it's designed for desktop only", "score": 1},
                        {"id": "q2_e", "text": "I don't know", "score": 0}
                    ]
                },
                {
                    "id": "q3",
                    "text": "How clear is your website's call to action?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q3_a", "text": "Very clear - visitors know exactly what to do", "score": 10},
                        {"id": "q3_b", "text": "Somewhat clear - most visitors can figure it out", "score": 7},
                        {"id": "q3_c", "text": "Not very clear - visitors might get confused", "score": 4},
                        {"id": "q3_d", "text": "No clear call to action", "score": 1},
                        {"id": "q3_e", "text": "I don't know", "score": 0}
                    ]
                },
                {
                    "id": "q4",
                    "text": "How would you rate your website's checkout or form completion process?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q4_a", "text": "Streamlined - minimal steps, high completion rate", "score": 10},
                        {"id": "q4_b", "text": "Good - reasonable number of steps", "score": 7},
                        {"id": "q4_c", "text": "Average - could be more efficient", "score": 4},
                        {"id": "q4_d", "text": "Complicated - many steps, high abandonment", "score": 1},
                        {"id": "q4_e", "text": "I don't know", "score": 0}
                    ]
                },
                {
                    "id": "q5",
                    "text": "Do you regularly update your website content?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q5_a", "text": "Yes, weekly or more often", "score": 10},
                        {"id": "q5_b", "text": "Yes, monthly", "score": 7},
                        {"id": "q5_c", "text": "Occasionally, a few times a year", "score": 4},
                        {"id": "q5_d", "text": "Rarely or never", "score": 1},
                        {"id": "q5_e", "text": "I don't know", "score": 0}
                    ]
                }
            ]
            
            # Add additional questions if needed
            if question_count > 5:
                questions.append({
                    "id": "q6",
                    "text": "How well does your website convert visitors into leads or customers?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q6_a", "text": "Very well - high conversion rate", "score": 10},
                        {"id": "q6_b", "text": "Fairly well - acceptable conversion rate", "score": 7},
                        {"id": "q6_c", "text": "Not very well - low conversion rate", "score": 4},
                        {"id": "q6_d", "text": "Poorly - very few conversions", "score": 1},
                        {"id": "q6_e", "text": "I don't know", "score": 0}
                    ]
                })
            
            if question_count > 6:
                questions.append({
                    "id": "q7",
                    "text": "How would you rate your website's overall user experience?",
                    "type": "scale",
                    "min": 1,
                    "max": 10,
                    "min_label": "Poor",
                    "max_label": "Excellent"
                })
        
        # Marketing industry example
        elif "marketing" in industry.lower():
            questions = [
                {
                    "id": "q1",
                    "text": "How well defined is your target audience?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q1_a", "text": "Very well defined with detailed personas", "score": 10},
                        {"id": "q1_b", "text": "Somewhat defined with basic demographics", "score": 7},
                        {"id": "q1_c", "text": "Broadly defined with minimal detail", "score": 4},
                        {"id": "q1_d", "text": "Not defined at all", "score": 1},
                        {"id": "q1_e", "text": "I don't know", "score": 0}
                    ]
                },
                {
                    "id": "q2",
                    "text": "How consistently do you publish content?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q2_a", "text": "Very consistently with a content calendar", "score": 10},
                        {"id": "q2_b", "text": "Fairly consistently but without formal planning", "score": 7},
                        {"id": "q2_c", "text": "Inconsistently with occasional gaps", "score": 4},
                        {"id": "q2_d", "text": "Rarely or never", "score": 1},
                        {"id": "q2_e", "text": "I don't know", "score": 0}
                    ]
                }
                # Additional questions would be added for marketing industry
            ]
        
        # Default questions if industry doesn't match
        if not questions:
            questions = [
                {
                    "id": "q1",
                    "text": "How would you rate your current business performance?",
                    "type": "scale",
                    "min": 1,
                    "max": 10,
                    "min_label": "Poor",
                    "max_label": "Excellent"
                },
                {
                    "id": "q2",
                    "text": "What is your biggest business challenge right now?",
                    "type": "multiple_choice",
                    "options": [
                        {"id": "q2_a", "text": "Finding new customers", "category": "type_b"},
                        {"id": "q2_b", "text": "Improving operations", "category": "type_a"},
                        {"id": "q2_c", "text": "Developing new offerings", "category": "type_c"},
                        {"id": "q2_d", "text": "Enhancing quality", "category": "type_d"},
                        {"id": "q2_e", "text": "Other", "category": "type_a"}
                    ]
                }
                # Additional generic questions would be added
            ]
        
        # Ensure we have the right number of questions
        while len(questions) < question_count:
            questions.append({
                "id": f"q{len(questions)+1}",
                "text": f"Sample Question {len(questions)+1}",
                "type": "multiple_choice",
                "options": [
                    {"id": f"q{len(questions)+1}_a", "text": "Option A", "score": 10},
                    {"id": f"q{len(questions)+1}_b", "text": "Option B", "score": 7},
                    {"id": f"q{len(questions)+1}_c", "text": "Option C", "score": 4},
                    {"id": f"q{len(questions)+1}_d", "text": "Option D", "score": 1}
                ]
            })
        
        # Trim if we have too many questions
        if len(questions) > question_count:
            questions = questions[:question_count]
        
        # Add branching logic if needed
        if use_branching:
            # In a real implementation, this would be more sophisticated
            # Here we just add a simple branch to the first question
            if len(questions) > 1:
                questions[0]["branches"] = {
                    "q1_a": "q2",  # If they answer A, go to question 2
                    "q1_b": "q2",  # If they answer B, go to question 2
                    "q1_c": "q3",  # If they answer C, go to question 3
                    "q1_d": "q3",  # If they answer D, go to question 3
                    "q1_e": "q2"   # If they answer E, go to question 2
                }
        
        return questions
    
    def _generate_results_content(self, quiz_design: Dict[str, Any], industry: str, pain_points: List[str], usp: str) -> Dict[str, Any]:
        """
        Generate content for quiz results.
        
        Args:
            quiz_design: The quiz design
            industry: Industry of the business
            pain_points: Customer pain points
            usp: Unique selling proposition
            
        Returns:
            Dict containing results content
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        results_approach = quiz_design["results_approach"]
        approach_type = results_approach["type"]
        result_types = results_approach["result_types"]
        
        results_content = {
            "headline": "Your Results",
            "subheadline": "Based on your answers, here's how your business is performing:",
            "result_types": []
        }
        
        # Generate content for each result type
        for result_type in result_types:
            if approach_type == "score":
                range_min, range_max = result_type["range"]
                label = result_type["label"]
                description = result_type["description"]
                
                result_content = {
                    "range": [range_min, range_max],
                    "label": label,
                    "headline": f"Your Score: {{score}} - {label}",
                    "description": description,
                    "recommendations": self._generate_recommendations(label, industry, pain_points, usp)
                }
            else:  # category
                result_id = result_type["id"]
                label = result_type["label"]
                description = result_type["description"]
                
                result_content = {
                    "id": result_id,
                    "label": label,
                    "headline": f"Your Result: {label}",
                    "description": description,
                    "recommendations": self._generate_recommendations(label, industry, pain_points, usp)
                }
            
            results_content["result_types"].append(result_content)
        
        return results_content
    
    def _generate_recommendations(self, result_label: str, industry: str, pain_points: List[str], usp: str) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on result label and business information.
        
        Args:
            result_label: Label of the result (e.g., "Needs Improvement")
            industry: Industry of the business
            pain_points: Customer pain points
            usp: Unique selling proposition
            
        Returns:
            List of recommendations
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        recommendations = []
        
        # Web design industry example
        if "web design" in industry.lower() or "website" in industry.lower():
            if result_label == "Needs Improvement":
                recommendations = [
                    {
                        "title": "Optimize Your Website Speed",
                        "description": "Your website loading speed is critical for both user experience and SEO. Aim for under 3 seconds loading time on all devices."
                    },
                    {
                        "title": "Implement Mobile Responsiveness",
                        "description": "Ensure your website works flawlessly on all devices, especially mobile phones which account for over 50% of web traffic."
                    },
                    {
                        "title": "Clarify Your Call to Action",
                        "description": "Make it immediately obvious what you want visitors to do on your site with clear, compelling calls to action."
                    }
                ]
            elif result_label == "Average":
                recommendations = [
                    {
                        "title": "Enhance User Experience",
                        "description": "Streamline your user journey to reduce friction points and make navigation intuitive."
                    },
                    {
                        "title": "Optimize Conversion Paths",
                        "description": "Analyze and improve your conversion funnel to reduce abandonment and increase completion rates."
                    }
                ]
            elif result_label == "Good":
                recommendations = [
                    {
                        "title": "Implement A/B Testing",
                        "description": "Start testing variations of key pages to incrementally improve conversion rates."
                    },
                    {
                        "title": "Personalize User Experience",
                        "description": "Consider adding personalization elements based on user behavior or preferences."
                    }
                ]
            else:  # Excellent
                recommendations = [
                    {
                        "title": "Explore Advanced Analytics",
                        "description": "Implement more sophisticated analytics to gain deeper insights into user behavior."
                    },
                    {
                        "title": "Consider Conversion Rate Optimization",
                        "description": "Even high-performing websites can benefit from dedicated CRO strategies."
                    }
                ]
        
        # Default recommendations if industry doesn't match
        if not recommendations:
            if result_label == "Needs Improvement" or result_label == "Efficiency-Focused":
                recommendations = [
                    {
                        "title": "Streamline Your Core Processes",
                        "description": "Identify and optimize your most important business processes for efficiency."
                    },
                    {
                        "title": "Implement Performance Metrics",
                        "description": "What gets measured gets managed. Establish clear KPIs for your business objectives."
                    }
                ]
            elif result_label == "Average" or result_label == "Growth-Focused":
                recommendations = [
                    {
                        "title": "Develop a Growth Strategy",
                        "description": "Create a clear plan for scaling your business with specific, measurable goals."
                    },
                    {
                        "title": "Optimize Your Marketing Funnel",
                        "description": "Ensure each stage of your customer journey is optimized for conversion."
                    }
                ]
            else:
                recommendations = [
                    {
                        "title": "Refine Your Business Strategy",
                        "description": "Even successful businesses benefit from regular strategic reviews and adjustments."
                    },
                    {
                        "title": "Explore New Opportunities",
                        "description": "Consider new markets, products, or services that align with your core strengths."
                    }
                ]
        
        # Add a recommendation that incorporates the USP
        usp_recommendation = {
            "title": "Leverage Your Unique Strengths",
            "description": f"Build on your {usp} to further differentiate your business from competitors."
        }
        recommendations.append(usp_recommendation)
        
        return recommendations
    
    def _generate_lead_capture_content(self, quiz_design: Dict[str, Any], business_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate content for lead capture form.
        
        Args:
            quiz_design: The quiz design
            business_info: Information about the business
            
        Returns:
            Dict containing lead capture content
        """
        # In a real implementation, this would use more sophisticated logic or LLM
        # Here we use a simple template-based approach
        
        business_name = business_info.get("name", "")
        
        lead_capture_content = {
            "headline": "Get Your Detailed Results",
            "subheadline": f"Enter your details below to receive your personalized recommendations from {business_name}",
            "privacy_text": f"We respect your privacy. {business_name} will use your information to send you your results and may contact you about relevant services. You can unsubscribe at any time.",
            "button_text": "Get My Results",
            "fields": [
                {
                    "id": "name",
                    "label": "Your Name",
                    "type": "text",
                    "required": True,
                    "placeholder": "John Smith"
                },
                {
                    "id": "email",
                    "label": "Your Email",
                    "type": "email",
                    "required": True,
                    "placeholder": "john@example.com"
                },
                {
                    "id": "company",
                    "label": "Company Name",
                    "type": "text",
                    "required": False,
                    "placeholder": "ABC Company"
                }
            ]
        }
        
        return lead_capture_content
    
    def _apply_language_variant(self, content: Any, language_variant: str) -> Any:
        """
        Apply language variant to content.
        
        Args:
            content: Content to apply language variant to
            language_variant: Language variant to use (US, UK, AU, NZ)
            
        Returns:
            Content with language variant applied
        """
        # In a real implementation, this would be more sophisticated
        # Here we just handle a few common cases
        
        # Define spelling variations
        spelling_maps = {
            "US": {"color": "color", "center": "center", "optimize": "optimize"},
            "UK": {"color": "colour", "center": "centre", "optimize": "optimise"},
            "AU": {"color": "colour", "center": "centre", "optimize": "optimise"},
            "NZ": {"color": "colour", "center": "centre", "optimize": "optimise"}
        }
        
        # Define terminology variations
        terminology_maps = {
            "US": {"vacation": "vacation", "cell phone": "cell phone", "shopping cart": "shopping cart"},
            "UK": {"vacation": "holiday", "cell phone": "mobile phone", "shopping cart": "shopping trolley"},
            "AU": {"vacation": "holiday", "cell phone": "mobile phone", "shopping cart": "shopping trolley"},
            "NZ": {"vacation": "holiday", "cell phone": "mobile phone", "shopping cart": "shopping trolley"}
        }
        
        # If content is a string, apply variations directly
        if isinstance(content, str):
            result = content
            
            # Apply spelling variations
            for us_spelling, variant_spelling in spelling_maps.get(language_variant, {}).items():
                result = result.replace(us_spelling, variant_spelling)
            
            # Apply terminology variations
            for us_term, variant_term in terminology_maps.get(language_variant, {}).items():
                result = result.replace(us_term, variant_term)
            
            return result
        
        # If content is a list, apply to each item
        elif isinstance(content, list):
            return [self._apply_language_variant(item, language_variant) for item in content]
        
        # If content is a dict, apply to each value
        elif isinstance(content, dict):
            return {key: self._apply_language_variant(value, language_variant) for key, value in content.items()}
        
        # Otherwise return as is
        return content
    
    def revise_content(self, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Revise the quiz content based on feedback.
        
        Args:
            feedback: Feedback on the content
            
        Returns:
            Dict containing the revised quiz content
        """
        if "quiz_content" not in self.content_state:
            raise ValueError("No quiz content to revise")
        
        self.content_state["status"] = "revision_in_progress"
        self.content_state["content_version"] += 1
        self.content_state["last_updated"] = datetime.now().isoformat()
        
        # Get current content
        quiz_content = self.content_state["quiz_content"]
        
        # Apply feedback
        if "welcome_screen" in feedback:
            for key, value in feedback["welcome_screen"].items():
                quiz_content["welcome_screen"][key] = value
        
        if "questions" in feedback:
            # Handle question revisions
            for question_feedback in feedback["questions"]:
                question_id = question_feedback.get("id")
                if question_id:
                    # Find the question to update
                    for i, question in enumerate(quiz_content["questions"]):
                        if question["id"] == question_id:
                            # Update question fields
                            for key, value in question_feedback.items():
                                if key != "id":
                                    quiz_content["questions"][i][key] = value
                            break
        
        if "results" in feedback:
            for key, value in feedback["results"].items():
                quiz_content["results"][key] = value
        
        if "lead_capture" in feedback:
            for key, value in feedback["lead_capture"].items():
                quiz_content["lead_capture"][key] = value
        
        self.content_state["quiz_content"] = quiz_content
        self.content_state["status"] = "revision_completed"
        self.content_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("quiz_content", quiz_content)
            self.memory_manager.store("content_state", self.content_state)
        
        return quiz_content
    
    def get_content_state(self) -> Dict[str, Any]:
        """
        Get the current content state.
        
        Returns:
            Dict containing the current content state
        """
        return self.content_state


class CodeBuilderAgent:
    """
    Code Builder Agent that implements lead magnet functionality.
    
    This agent is responsible for:
    - Generating code for lead magnet functionality
    - Implementing interactive elements
    - Creating data collection mechanisms
    - Building personalization logic
    - Integrating pre-built components with custom code
    """
    
    def __init__(self, memory_manager=None):
        """
        Initialize the Code Builder Agent.
        
        Args:
            memory_manager: The Memory Manager agent for storing and retrieving context
        """
        self.memory_manager = memory_manager
        self.code_state = {
            "status": "initialized",
            "lead_magnet_type": "quiz",
            "business_info": {},
            "language_variant": "US",
            "code_version": 1,
            "last_updated": datetime.now().isoformat()
        }
        
        # Define component registry
        self.component_registry = {
            "quiz": {
                "basic": "./components/quiz/basic.js",
                "branching": "./components/quiz/branching.js",
                "scored": "./components/quiz/scored.js"
            },
            "common": {
                "form_elements": "./components/common/form_elements.js",
                "results_display": "./components/common/results_display.js",
                "lead_capture": "./components/common/lead_capture.js",
                "popup": "./components/common/popup.js"
            }
        }
    
    def build_quiz(self, quiz_design: Dict[str, Any], quiz_content: Dict[str, Any], business_info: Dict[str, Any], language_variant: str = "US") -> Dict[str, Any]:
        """
        Build a quiz lead magnet based on design and content.
        
        Args:
            quiz_design: The quiz design
            quiz_content: The quiz content
            business_info: Information about the business
            language_variant: Language variant to use (US, UK, AU, NZ)
            
        Returns:
            Dict containing the built quiz
        """
        self.code_state["business_info"] = business_info
        self.code_state["language_variant"] = language_variant
        self.code_state["status"] = "build_in_progress"
        self.code_state["last_updated"] = datetime.now().isoformat()
        
        # Determine which components to use
        base_components = self._select_base_components(quiz_design)
        
        # Generate HTML structure
        html = self._generate_html(quiz_design, quiz_content, business_info)
        
        # Generate CSS
        css = self._generate_css(quiz_design, business_info)
        
        # Generate JavaScript
        js = self._generate_javascript(quiz_design, quiz_content, business_info, base_components)
        
        # Generate embedding code
        embedding_code = self._generate_embedding_code(business_info)
        
        # Create built quiz package
        built_quiz = {
            "html": html,
            "css": css,
            "javascript": js,
            "embedding_code": embedding_code,
            "base_components": base_components,
            "language_variant": language_variant
        }
        
        self.code_state["built_quiz"] = built_quiz
        self.code_state["status"] = "build_completed"
        self.code_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("built_quiz", built_quiz)
            self.memory_manager.store("code_state", self.code_state)
        
        return built_quiz
    
    def _select_base_components(self, quiz_design: Dict[str, Any]) -> List[str]:
        """
        Select base components based on quiz design.
        
        Args:
            quiz_design: The quiz design
            
        Returns:
            List of base component paths
        """
        base_components = []
        
        # Select quiz component based on structure
        if quiz_design["structure"]["use_branching"]:
            base_components.append(self.component_registry["quiz"]["branching"])
        elif quiz_design["results_approach"]["type"] == "score":
            base_components.append(self.component_registry["quiz"]["scored"])
        else:
            base_components.append(self.component_registry["quiz"]["basic"])
        
        # Add common components
        base_components.append(self.component_registry["common"]["form_elements"])
        base_components.append(self.component_registry["common"]["results_display"])
        base_components.append(self.component_registry["common"]["lead_capture"])
        base_components.append(self.component_registry["common"]["popup"])
        
        return base_components
    
    def _generate_html(self, quiz_design: Dict[str, Any], quiz_content: Dict[str, Any], business_info: Dict[str, Any]) -> str:
        """
        Generate HTML for the quiz.
        
        Args:
            quiz_design: The quiz design
            quiz_content: The quiz content
            business_info: Information about the business
            
        Returns:
            HTML string
        """
        business_name = business_info.get("name", "")
        
        # Generate welcome screen HTML
        welcome_html = f"""
        <div id="quiz-welcome-screen" class="quiz-screen active">
            <h1>{quiz_content["welcome_screen"]["headline"]}</h1>
            <p>{quiz_content["welcome_screen"]["subheadline"]}</p>
            <button id="start-quiz-btn" class="quiz-button">{quiz_content["welcome_screen"]["button_text"]}</button>
        </div>
        """
        
        # Generate questions HTML
        questions_html = ""
        for i, question in enumerate(quiz_content["questions"]):
            question_id = question["id"]
            question_text = question["text"]
            question_type = question["type"]
            
            question_html = f"""
            <div id="quiz-question-{question_id}" class="quiz-screen quiz-question" data-question-id="{question_id}">
                <h2>Question {i+1} of {len(quiz_content["questions"])}</h2>
                <p class="question-text">{question_text}</p>
            """
            
            if question_type == "multiple_choice":
                options_html = ""
                for option in question["options"]:
                    option_id = option["id"]
                    option_text = option["text"]
                    
                    options_html += f"""
                    <div class="quiz-option">
                        <input type="radio" id="{option_id}" name="{question_id}" value="{option_id}">
                        <label for="{option_id}">{option_text}</label>
                    </div>
                    """
                
                question_html += f"""
                <div class="quiz-options">
                    {options_html}
                </div>
                """
            elif question_type == "scale":
                min_val = question.get("min", 1)
                max_val = question.get("max", 10)
                min_label = question.get("min_label", "Low")
                max_label = question.get("max_label", "High")
                
                scale_html = f"""
                <div class="quiz-scale">
                    <span class="scale-label">{min_label}</span>
                    <div class="scale-options">
                """
                
                for val in range(min_val, max_val + 1):
                    scale_html += f"""
                    <div class="scale-option">
                        <input type="radio" id="{question_id}_val_{val}" name="{question_id}" value="{val}">
                        <label for="{question_id}_val_{val}">{val}</label>
                    </div>
                    """
                
                scale_html += f"""
                    </div>
                    <span class="scale-label">{max_label}</span>
                </div>
                """
                
                question_html += scale_html
            
            question_html += f"""
                <button class="quiz-button quiz-next-btn">Next</button>
            </div>
            """
            
            questions_html += question_html
        
        # Generate lead capture HTML
        lead_capture_html = f"""
        <div id="quiz-lead-capture" class="quiz-screen">
            <h2>{quiz_content["lead_capture"]["headline"]}</h2>
            <p>{quiz_content["lead_capture"]["subheadline"]}</p>
            <form id="quiz-lead-form">
        """
        
        for field in quiz_content["lead_capture"]["fields"]:
            field_id = field["id"]
            field_label = field["label"]
            field_type = field["type"]
            field_required = field["required"]
            field_placeholder = field.get("placeholder", "")
            
            required_attr = 'required="required"' if field_required else ''
            
            lead_capture_html += f"""
            <div class="form-field">
                <label for="quiz-{field_id}">{field_label}</label>
                <input type="{field_type}" id="quiz-{field_id}" name="{field_id}" placeholder="{field_placeholder}" {required_attr}>
            </div>
            """
        
        lead_capture_html += f"""
                <p class="privacy-text">{quiz_content["lead_capture"]["privacy_text"]}</p>
                <button type="submit" class="quiz-button">{quiz_content["lead_capture"]["button_text"]}</button>
            </form>
        </div>
        """
        
        # Generate results HTML
        results_html = f"""
        <div id="quiz-results" class="quiz-screen">
            <h2>{quiz_content["results"]["headline"]}</h2>
            <p>{quiz_content["results"]["subheadline"]}</p>
            <div id="quiz-result-content"></div>
            <div id="quiz-recommendations"></div>
            <div class="quiz-cta">
                <a href="{quiz_content["results"]["result_types"][0]["recommendations"][0].get("url", "#")}" class="quiz-button">{quiz_design["results_approach"]["call_to_action"]["button_text"]}</a>
            </div>
        </div>
        """
        
        # Combine all HTML
        html = f"""
        <div id="quiz-container" class="quiz-container" data-business="{business_name}">
            {welcome_html}
            {questions_html}
            {lead_capture_html}
            {results_html}
        </div>
        """
        
        return html
    
    def _generate_css(self, quiz_design: Dict[str, Any], business_info: Dict[str, Any]) -> str:
        """
        Generate CSS for the quiz.
        
        Args:
            quiz_design: The quiz design
            business_info: Information about the business
            
        Returns:
            CSS string
        """
        primary_color = quiz_design["branding"]["primary_color"]
        secondary_color = quiz_design["branding"]["secondary_color"]
        font_family = quiz_design["branding"]["font_family"]
        
        css = f"""
        .quiz-container {{
            font-family: {font_family};
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            box-sizing: border-box;
        }}
        
        .quiz-screen {{
            display: none;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        
        .quiz-screen.active {{
            display: block;
        }}
        
        .quiz-button {{
            background-color: {primary_color};
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 20px;
            transition: background-color 0.3s;
        }}
        
        .quiz-button:hover {{
            background-color: {secondary_color};
        }}
        
        .quiz-options {{
            margin-top: 20px;
        }}
        
        .quiz-option {{
            margin-bottom: 12px;
        }}
        
        .quiz-option label {{
            display: inline-block;
            padding: 10px 15px;
            background-color: #f5f5f5;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            box-sizing: border-box;
        }}
        
        .quiz-option input[type="radio"] {{
            display: none;
        }}
        
        .quiz-option input[type="radio"]:checked + label {{
            background-color: {primary_color};
            color: white;
        }}
        
        .quiz-scale {{
            display: flex;
            align-items: center;
            margin-top: 20px;
        }}
        
        .scale-options {{
            display: flex;
            justify-content: space-between;
            flex: 1;
            margin: 0 15px;
        }}
        
        .scale-option {{
            text-align: center;
        }}
        
        .scale-option input[type="radio"] {{
            display: none;
        }}
        
        .scale-option label {{
            display: block;
            width: 30px;
            height: 30px;
            line-height: 30px;
            background-color: #f5f5f5;
            border-radius: 50%;
            cursor: pointer;
        }}
        
        .scale-option input[type="radio"]:checked + label {{
            background-color: {primary_color};
            color: white;
        }}
        
        .form-field {{
            margin-bottom: 15px;
        }}
        
        .form-field label {{
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }}
        
        .form-field input {{
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }}
        
        .privacy-text {{
            font-size: 12px;
            color: #666;
            margin-top: 15px;
        }}
        
        #quiz-result-content {{
            margin-top: 20px;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 4px;
        }}
        
        #quiz-recommendations {{
            margin-top: 20px;
        }}
        
        .recommendation {{
            margin-bottom: 15px;
            padding: 15px;
            background-color: #f5f5f5;
            border-left: 4px solid {primary_color};
            border-radius: 0 4px 4px 0;
        }}
        
        .recommendation h3 {{
            margin-top: 0;
            color: {primary_color};
        }}
        
        .quiz-progress {{
            height: 6px;
            background-color: #f5f5f5;
            border-radius: 3px;
            margin-bottom: 20px;
            overflow: hidden;
        }}
        
        .quiz-progress-bar {{
            height: 100%;
            background-color: {primary_color};
            width: 0%;
            transition: width 0.3s;
        }}
        
        @media (max-width: 600px) {{
            .quiz-container {{
                padding: 10px;
            }}
            
            .quiz-button {{
                width: 100%;
            }}
        }}
        """
        
        return css
    
    def _generate_javascript(self, quiz_design: Dict[str, Any], quiz_content: Dict[str, Any], business_info: Dict[str, Any], base_components: List[str]) -> str:
        """
        Generate JavaScript for the quiz.
        
        Args:
            quiz_design: The quiz design
            quiz_content: The quiz content
            business_info: Information about the business
            base_components: List of base component paths
            
        Returns:
            JavaScript string
        """
        # In a real implementation, this would load and integrate the base components
        # Here we'll create a simplified version
        
        use_branching = quiz_design["structure"]["use_branching"]
        results_type = quiz_design["results_approach"]["type"]
        
        js = f"""
        // Quiz Lead Magnet - Generated by AI Lead Magnet Platform
        (function() {{
            // Quiz state
            const quizState = {{
                currentScreen: 'quiz-welcome-screen',
                answers: {{}},
                leadInfo: {{}},
                result: null
            }};
            
            // DOM elements
            const quizContainer = document.getElementById('quiz-container');
            const welcomeScreen = document.getElementById('quiz-welcome-screen');
            const questions = document.querySelectorAll('.quiz-question');
            const leadCaptureScreen = document.getElementById('quiz-lead-capture');
            const resultsScreen = document.getElementById('quiz-results');
            const startButton = document.getElementById('start-quiz-btn');
            const nextButtons = document.querySelectorAll('.quiz-next-btn');
            const leadForm = document.getElementById('quiz-lead-form');
            
            // Question data
            const questionData = {json.dumps(quiz_content["questions"])};
            
            // Results data
            const resultsData = {json.dumps(quiz_content["results"]["result_types"])};
            
            // Initialize quiz
            function initQuiz() {{
                // Add event listeners
                startButton.addEventListener('click', startQuiz);
                
                nextButtons.forEach(button => {{
                    button.addEventListener('click', goToNextQuestion);
                }});
                
                leadForm.addEventListener('submit', handleLeadCapture);
                
                // Add progress indicator if needed
                if ({str(quiz_design["structure"]["progress_indicator"]).lower()}) {{
                    addProgressIndicator();
                }}
            }}
            
            // Start the quiz
            function startQuiz() {{
                showScreen('quiz-question-' + questionData[0].id);
                updateProgress(1);
            }}
            
            // Go to next question
            function goToNextQuestion() {{
                const currentQuestion = document.querySelector('.quiz-question.active');
                const questionId = currentQuestion.dataset.questionId;
                
                // Save answer
                saveAnswer(questionId);
                
                // Determine next question
                let nextQuestionIndex = 0;
                for (let i = 0; i < questionData.length; i++) {{
                    if (questionData[i].id === questionId) {{
                        nextQuestionIndex = i + 1;
                        break;
                    }}
                }}
                
                // Check if branching logic should be applied
                if ({str(use_branching).lower()} && questionData[nextQuestionIndex - 1].branches) {{
                    const selectedOption = quizState.answers[questionId];
                    const branches = questionData[nextQuestionIndex - 1].branches;
                    
                    if (branches[selectedOption]) {{
                        // Find the index of the target question
                        for (let i = 0; i < questionData.length; i++) {{
                            if (questionData[i].id === branches[selectedOption]) {{
                                nextQuestionIndex = i;
                                break;
                            }}
                        }}
                    }}
                }}
                
                // Check if we've reached the end of questions
                if (nextQuestionIndex >= questionData.length) {{
                    // Go to lead capture or results
                    if ('{quiz_design["lead_capture"]["timing"]}' === 'before_results') {{
                        showScreen('quiz-lead-capture');
                    }} else {{
                        calculateResult();
                        showScreen('quiz-results');
                    }}
                }} else {{
                    // Go to next question
                    showScreen('quiz-question-' + questionData[nextQuestionIndex].id);
                    updateProgress(nextQuestionIndex + 1);
                }}
            }}
            
            // Save answer for current question
            function saveAnswer(questionId) {{
                const question = questionData.find(q => q.id === questionId);
                
                if (question.type === 'multiple_choice') {{
                    const selectedOption = document.querySelector(`input[name="${questionId}"]:checked`);
                    if (selectedOption) {{
                        quizState.answers[questionId] = selectedOption.value;
                    }}
                }} else if (question.type === 'scale') {{
                    const selectedValue = document.querySelector(`input[name="${questionId}"]:checked`);
                    if (selectedValue) {{
                        quizState.answers[questionId] = parseInt(selectedValue.value);
                    }}
                }}
            }}
            
            // Handle lead capture form submission
            function handleLeadCapture(e) {{
                e.preventDefault();
                
                // Collect lead information
                const formData = new FormData(leadForm);
                for (const [key, value] of formData.entries()) {{
                    quizState.leadInfo[key] = value;
                }}
                
                // Calculate result
                calculateResult();
                
                // Show results
                showScreen('quiz-results');
                
                // Send lead data to server (would be implemented in real version)
                sendLeadData();
            }}
            
            // Calculate quiz result
            function calculateResult() {{
                if ('{results_type}' === 'score') {{
                    // Calculate score
                    let totalScore = 0;
                    let maxPossibleScore = 0;
                    
                    for (const questionId in quizState.answers) {{
                        const question = questionData.find(q => q.id === questionId);
                        
                        if (question.type === 'multiple_choice') {{
                            const selectedOption = question.options.find(o => o.id === quizState.answers[questionId]);
                            if (selectedOption && selectedOption.score !== undefined) {{
                                totalScore += selectedOption.score;
                                maxPossibleScore += 10; // Assuming max score per question is 10
                            }}
                        }} else if (question.type === 'scale') {{
                            totalScore += quizState.answers[questionId];
                            maxPossibleScore += 10; // Assuming scale is 1-10
                        }}
                    }}
                    
                    // Convert to percentage
                    const percentageScore = Math.round((totalScore / maxPossibleScore) * 100);
                    
                    // Find matching result type
                    for (const resultType of resultsData) {{
                        if (percentageScore >= resultType.range[0] && percentageScore <= resultType.range[1]) {{
                            quizState.result = {{
                                type: resultType,
                                score: percentageScore
                            }};
                            break;
                        }}
                    }}
                    
                    // Display result
                    displayResult();
                }} else {{
                    // Category-based result
                    // Count occurrences of each category
                    const categoryCounts = {{}};
                    
                    for (const questionId in quizState.answers) {{
                        const question = questionData.find(q => q.id === questionId);
                        
                        if (question.type === 'multiple_choice') {{
                            const selectedOption = question.options.find(o => o.id === quizState.answers[questionId]);
                            if (selectedOption && selectedOption.category) {{
                                categoryCounts[selectedOption.category] = (categoryCounts[selectedOption.category] || 0) + 1;
                            }}
                        }}
                    }}
                    
                    // Find most common category
                    let maxCount = 0;
                    let dominantCategory = null;
                    
                    for (const category in categoryCounts) {{
                        if (categoryCounts[category] > maxCount) {{
                            maxCount = categoryCounts[category];
                            dominantCategory = category;
                        }}
                    }}
                    
                    // Find matching result type
                    for (const resultType of resultsData) {{
                        if (resultType.id === dominantCategory) {{
                            quizState.result = {{
                                type: resultType
                            }};
                            break;
                        }}
                    }}
                    
                    // Display result
                    displayResult();
                }}
            }}
            
            // Display quiz result
            function displayResult() {{
                const resultContent = document.getElementById('quiz-result-content');
                const recommendationsContainer = document.getElementById('quiz-recommendations');
                
                if (quizState.result) {{
                    // Display result headline
                    let headline = quizState.result.type.headline;
                    if ('{results_type}' === 'score') {{
                        headline = headline.replace('{{score}}', quizState.result.score);
                    }}
                    
                    resultContent.innerHTML = `
                        <h3>${{headline}}</h3>
                        <p>${{quizState.result.type.description}}</p>
                    `;
                    
                    // Display recommendations
                    recommendationsContainer.innerHTML = '';
                    for (const recommendation of quizState.result.type.recommendations) {{
                        recommendationsContainer.innerHTML += `
                            <div class="recommendation">
                                <h3>${{recommendation.title}}</h3>
                                <p>${{recommendation.description}}</p>
                            </div>
                        `;
                    }}
                }} else {{
                    resultContent.innerHTML = '<p>Unable to determine a result. Please try again.</p>';
                }}
            }}
            
            // Show a specific screen
            function showScreen(screenId) {{
                // Hide all screens
                document.querySelectorAll('.quiz-screen').forEach(screen => {{
                    screen.classList.remove('active');
                }});
                
                // Show target screen
                document.getElementById(screenId).classList.add('active');
                
                // Update current screen
                quizState.currentScreen = screenId;
            }}
            
            // Add progress indicator
            function addProgressIndicator() {{
                const progressBar = document.createElement('div');
                progressBar.className = 'quiz-progress';
                progressBar.innerHTML = '<div class="quiz-progress-bar"></div>';
                
                // Add to each question
                questions.forEach(question => {{
                    question.insertBefore(progressBar.cloneNode(true), question.firstChild);
                }});
            }}
            
            // Update progress indicator
            function updateProgress(currentQuestionIndex) {{
                if ({str(quiz_design["structure"]["progress_indicator"]).lower()}) {{
                    const progressPercentage = (currentQuestionIndex / questionData.length) * 100;
                    const activeQuestion = document.querySelector('.quiz-question.active');
                    if (activeQuestion) {{
                        const progressBar = activeQuestion.querySelector('.quiz-progress-bar');
                        if (progressBar) {{
                            progressBar.style.width = progressPercentage + '%';
                        }}
                    }}
                }}
            }}
            
            // Send lead data to server
            function sendLeadData() {{
                // In a real implementation, this would send data to a server
                console.log('Lead data:', quizState.leadInfo);
                console.log('Quiz answers:', quizState.answers);
                console.log('Quiz result:', quizState.result);
            }}
            
            // Initialize the quiz
            initQuiz();
        }})();
        """
        
        return js
    
    def _generate_embedding_code(self, business_info: Dict[str, Any]) -> str:
        """
        Generate embedding code for the quiz.
        
        Args:
            business_info: Information about the business
            
        Returns:
            Embedding code string
        """
        business_name = business_info.get("name", "")
        business_name_slug = business_name.lower().replace(" ", "-")
        
        embedding_code = f"""
        <!-- {business_name} Quiz Lead Magnet - Generated by AI Lead Magnet Platform -->
        <script>
        (function() {{
            // Create button
            const button = document.createElement('button');
            button.innerText = 'Take Our Quiz';
            button.className = 'lead-magnet-button';
            button.style.cssText = 'background-color: #4A90E2; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-family: Arial, sans-serif;';
            
            // Create popup container
            const popup = document.createElement('div');
            popup.className = 'lead-magnet-popup';
            popup.style.cssText = 'display:none; position:fixed; top:0; left:0; width:100%; height:100%; background-color:rgba(0,0,0,0.7); z-index:9999;';
            
            // Create popup content
            const popupContent = document.createElement('div');
            popupContent.className = 'lead-magnet-popup-content';
            popupContent.style.cssText = 'position:relative; width:90%; max-width:800px; margin:50px auto; background-color:#fff; padding:20px; border-radius:5px; max-height:80vh; overflow-y:auto;';
            
            // Create close button
            const closeButton = document.createElement('button');
            closeButton.innerText = '×';
            closeButton.className = 'lead-magnet-close';
            closeButton.style.cssText = 'position:absolute; top:10px; right:10px; background:none; border:none; font-size:24px; cursor:pointer;';
            
            // Add quiz content container
            const quizContainer = document.createElement('div');
            quizContainer.id = '{business_name_slug}-quiz-container';
            
            // Assemble popup
            popupContent.appendChild(closeButton);
            popupContent.appendChild(quizContainer);
            popup.appendChild(popupContent);
            
            // Add to document
            document.body.appendChild(button);
            document.body.appendChild(popup);
            
            // Add event listeners
            button.addEventListener('click', function() {{
                popup.style.display = 'block';
                loadQuiz();
            }});
            
            closeButton.addEventListener('click', function() {{
                popup.style.display = 'none';
            }});
            
            // Close when clicking outside content
            popup.addEventListener('click', function(e) {{
                if (e.target === popup) {{
                    popup.style.display = 'none';
                }}
            }});
            
            // Load quiz content
            function loadQuiz() {{
                // In a real implementation, this would load from a server
                // For this prototype, we'll simulate loading
                quizContainer.innerHTML = '<p>Loading quiz...</p>';
                
                // Simulate loading delay
                setTimeout(function() {{
                    // Load CSS
                    const styleElement = document.createElement('style');
                    styleElement.textContent = `/* Quiz CSS would be loaded here */`;
                    document.head.appendChild(styleElement);
                    
                    // Load HTML
                    quizContainer.innerHTML = `<!-- Quiz HTML would be loaded here -->`;
                    
                    // Load JavaScript
                    const scriptElement = document.createElement('script');
                    scriptElement.textContent = `// Quiz JavaScript would be loaded here`;
                    document.body.appendChild(scriptElement);
                }}, 500);
            }}
        }})();
        </script>
        """
        
        return embedding_code
    
    def revise_code(self, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Revise the quiz code based on feedback.
        
        Args:
            feedback: Feedback on the code
            
        Returns:
            Dict containing the revised built quiz
        """
        if "built_quiz" not in self.code_state:
            raise ValueError("No built quiz to revise")
        
        self.code_state["status"] = "revision_in_progress"
        self.code_state["code_version"] += 1
        self.code_state["last_updated"] = datetime.now().isoformat()
        
        # Get current built quiz
        built_quiz = self.code_state["built_quiz"]
        
        # Apply feedback
        if "html" in feedback:
            built_quiz["html"] = feedback["html"]
        
        if "css" in feedback:
            built_quiz["css"] = feedback["css"]
        
        if "javascript" in feedback:
            built_quiz["javascript"] = feedback["javascript"]
        
        if "embedding_code" in feedback:
            built_quiz["embedding_code"] = feedback["embedding_code"]
        
        self.code_state["built_quiz"] = built_quiz
        self.code_state["status"] = "revision_completed"
        self.code_state["last_updated"] = datetime.now().isoformat()
        
        if self.memory_manager:
            self.memory_manager.store("built_quiz", built_quiz)
            self.memory_manager.store("code_state", self.code_state)
        
        return built_quiz
    
    def get_code_state(self) -> Dict[str, Any]:
        """
        Get the current code state.
        
        Returns:
            Dict containing the current code state
        """
        return self.code_state


# Example usage
if __name__ == "__main__":
    # Create memory manager
    from executive_agent import MemoryManager
    memory_manager = MemoryManager(storage_dir="./memory")
    
    # Create design architect
    design_architect = DesignArchitectAgent(memory_manager=memory_manager)
    
    # Sample business info
    business_info = {
        "name": "Thames Digital",
        "industry": "Web Design",
        "size": "Small",
        "target_audience": "E-commerce businesses",
        "unique_selling_proposition": "Conversion-focused design",
        "customer_pain_points": [
            "Low conversion rates",
            "Slow website performance",
            "Poor mobile experience"
        ]
    }
    
    # Create quiz design
    quiz_design = design_architect.create_quiz_design(business_info, language_variant="UK")
    print("Quiz Design Created")
    
    # Create content generator
    content_generator = ContentGeneratorAgent(memory_manager=memory_manager)
    
    # Generate quiz content
    quiz_content = content_generator.generate_quiz_content(quiz_design, business_info, language_variant="UK")
    print("Quiz Content Generated")
    
    # Create code builder
    code_builder = CodeBuilderAgent(memory_manager=memory_manager)
    
    # Build quiz
    built_quiz = code_builder.build_quiz(quiz_design, quiz_content, business_info, language_variant="UK")
    print("Quiz Built")
    
    # Output embedding code
    print("\nEmbedding Code:")
    print(built_quiz["embedding_code"])
