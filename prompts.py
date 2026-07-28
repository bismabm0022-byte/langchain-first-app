from langchain_core.prompts import ChatPromptTemplate

# Persona 1: General Helpful Assistant
default_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, clear, and concise AI assistant."),
    ("human", "{user_input}")
])

# Persona 2: Software Engineer
tech_lead_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Senior Software Engineer. Provide concise, modern code solutions with best practices."),
    ("human", "{user_input}")
])

# Persona 3: Socratic Educator
teacher_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an encouraging teacher. Explain complex topics using simple analogies and step-by-step logic."),
    ("human", "{user_input}")
])

PERSONAS = {
    "1": ("General Assistant", default_prompt),
    "2": ("Tech Lead", tech_lead_prompt),
    "3": ("Teacher", teacher_prompt),
}
