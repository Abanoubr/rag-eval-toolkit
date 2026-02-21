import os
    try:
        from openai import OpenAI
    except ImportError:
        OpenAI = None
    
    from .base import BaseBackend
    
    class OpenAIBackend(BaseBackend):
        def __init__(self, model: str = "gpt-4-turbo-preview"):
            if OpenAI is None:
                raise ImportError("Please install openai: pip install openai")
            
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY environment variable is not set.")
                
            self.client = OpenAI(api_key=api_key)
            self.model = model
    
        def generate(self, prompt: str) -> str:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0
            )
            return response.choices[0].message.content
    
