from abc import ABC, abstractmethod
    from typing import Dict, Any
    
    class BaseMetric(ABC):
        def __init__(self, name: str):
            self.name = name
    
        @abstractmethod
        def score(self, row: Dict[str, Any], backend) -> float:
            """Calculate the score for a single row of data."""
            pass
    
