Python
from pydantic import BaseModel, Field
from typing import List

class DetailedResponse(BaseModel):
    summary: str = Field(description="A concise summary of the answer.")
    key_points: List[str] = Field(description="Bullet points highlighting key facts or steps.")
    actionable_advice: str = Field(description="A single clear takeaway or recommended action.")
