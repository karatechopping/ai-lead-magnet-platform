import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ConversationalAssessmentAgent:
    """AI Agent for conducting dynamic business assessments."""

    def __init__(self):
        # Define the prompt template
        self.prompt_template = PromptTemplate(
            input_variables=["history", "input"],
            template=(
                "You are an AI agent helping a business owner design a lead magnet. "
                "Your primary goal is to gather detailed information about their business, "
                "industry, ideal customer profile (ICP), unique selling proposition (USP), "
                "and their customers' pain points. Do not offer solutions until you have "
                "collected all the necessary information.\n\n"
                "Conversation History:\n{history}\n\n"
                "User Input: {input}\n\n"
                "Your Response:"
            ),
        )

        # Initialize memory for context
        self.memory = ConversationBufferMemory()

        # Track the conversation stage
        self.conversation_stage = 1

    def start_conversation(self) -> str:
        """Start the conversation with the welcome message and first question."""
        # Combine the welcome message and first question
        assistant_response = (
            "Welcome to the AI Lead Magnet Platform!\n\n"
            "Let's start by learning about your business.\n\n"
            "What type of business do you run (e.g., service, product)?"
        )
        return assistant_response

    def ask_question(self, user_input: str) -> str:
        """Process user input and generate the next question or response."""
        # Validate the user's response
        if len(user_input.strip()) < 5:  # Example: Check if the response is too short
            return "Could you provide more details? Your response seems a bit brief."

        # Determine the next question based on the conversation stage
        if self.conversation_stage == 1:
            next_question = "Could you tell me more about your business and the services you offer?"
            self.conversation_stage += 1
        elif self.conversation_stage == 2:
            next_question = "What industry do your clients typically belong to?"
            self.conversation_stage += 1
        elif self.conversation_stage == 3:
            next_question = "Who is your ideal customer (ICP), and what are their key characteristics?"
            self.conversation_stage += 1
        elif self.conversation_stage == 4:
            next_question = "What is your unique selling proposition (USP)? What sets you apart from competitors?"
            self.conversation_stage += 1
        elif self.conversation_stage == 5:
            next_question = "What are the main pain points or challenges your customers face?"
            self.conversation_stage += 1
        else:
            # Once all stages are complete, generate insights
            return "Thank you! Based on what you've shared, I will now generate tailored recommendations."

        # Return the next question
        return next_question