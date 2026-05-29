import os
import google.generativeai as genai

class GeminiClient:
    def __init__(self):
        # Yeh aap ki Vercel par set ki hui environment variable se key uthayega
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        self.model_name = "gemini-pro"

    def generate_pitch(self, domain: str) -> str:
        try:
            model = genai.GenerativeModel(self.model_name)
            prompt = f"Write a highly personalized, professional outreach email pitch to the website {domain} proposing a guest post trade. Keep it concise, high-converting, and friendly."
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating pitch with Gemini: {str(e)}"
          
