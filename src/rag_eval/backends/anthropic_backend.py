import os
    try:
        from anthropic import Anthropic
    except ImportError:
        Anthropic = None
    
    from .base import BaseBackend
    
    class AnthropicBackend(BaseBackend):
        def __init__(self, model: str = "claude-3-opus-20240229"):
            if Anthropic is None:
                raise ImportError("Please install anthropic: pip install anthropic")
                
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY environment variable is not set.")
                
            self.client = Anthropic(api_key=api_key)
            self.model = model
    
        def generate(self, prompt: str) -> str:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                temperature=0.0,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
    
