Python
from langchain_core.output_parsers import StrOutputParser
from config import get_chat_model
from prompts import PERSONA_PROMPTS
from schemas import DetailedResponse

def build_text_chain(persona_key: str = "1"):
    """Builds a basic LCEL chain returning string output."""
    model = get_chat_model()
    _, prompt = PERSONA_PROMPTS.get(persona_key, PERSONA_PROMPTS["1"])
    parser = StrOutputParser()
    
    # Chain: Prompt -> Model -> String Parser
    return prompt | model | parser

def build_structured_chain(persona_key: str = "1"):
    """Builds an LCEL chain returning a Pydantic DetailedResponse object."""
    model = get_chat_model(temperature=0.2)
    _, prompt = PERSONA_PROMPTS.get(persona_key, PERSONA_PROMPTS["1"])
    structured_llm = model.with_structured_output(DetailedResponse)
    
    # Chain: Prompt -> Structured Model
    return prompt | structured_llm
