from abc import ABC, abstractmethod
    
    class BaseBackend(ABC):
        @abstractmethod
        def generate(self, prompt: str) -> str:
            """Generate a response from the LLM based on the prompt."""
            pass
    
