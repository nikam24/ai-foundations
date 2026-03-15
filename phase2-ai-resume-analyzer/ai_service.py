from dotenv import load_dotenv 
from google import genai 
from models import ResumeAnalysis 
import json 

load_dotenv() 

client = genai.Client()

async def analyze_resume(resume_text: str) -> ResumeAnalysis:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=f"""You are an expert technical recruiter.
        Analyze the following resume:
        Return ONLY valid JSON. Do not include explanations or markdown.
        JSON format:
        {{
        "resume_summary": "...",
        "skills_detected": [],
        "missing_skills": [],
        "suggestions": []
        }}\n\nResume:\n{resume_text}"""
    )
    # print("RAW MODEL RESPONSE:")
    # print(response.text)
    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

    data = json.loads(raw_text)
    return ResumeAnalysis(**data)