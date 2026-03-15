from pydantic import BaseModel
from typing import List

class ResumeAnalysis(BaseModel): 
    resume_summary: str 
    skills_detected: List[str] 
    missing_skills: List[str]   
    suggestions: List[str] 