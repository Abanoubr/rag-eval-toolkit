from typing import Dict, Any
    from .base import BaseMetric
    
    class ContextPrecisionMetric(BaseMetric):
        def __init__(self):
            super().__init__(name="context_precision")
    
        def score(self, row: Dict[str, Any], backend) -> float:
            question = row.get("question")
            context = row.get("context")
            
            prompt = f"""
            Given the following question and context, evaluate how useful the context is for answering the question.
            
            Question: {question}
            Context: {context}
            
            Does the context contain the information needed to answer the question? Respond with a single float score between 0.0 and 1.0.
            0.0 = completely useless context
            1.0 = context contains the exact answer
            Only return the number, nothing else.
            """
            response = backend.generate(prompt)
            try:
                return float(response.strip())
            except ValueError:
                return 0.0
    
