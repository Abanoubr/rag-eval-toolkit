from typing import Dict, Any
    from .base import BaseMetric
    
    class FaithfulnessMetric(BaseMetric):
        def __init__(self):
            super().__init__(name="faithfulness")
    
        def score(self, row: Dict[str, Any], backend) -> float:
            question = row.get("question")
            context = row.get("context")
            answer = row.get("answer")
            
            prompt = f"""
            Given the following context, question, and answer, evaluate whether the answer is faithful to the context.
            The answer should not contain any information that is not present in the context.
            
            Context: {context}
            Question: {question}
            Answer: {answer}
            
            Is the answer completely faithful to the context? Respond with a single float score between 0.0 and 1.0.
            0.0 = completely hallucinated/unfaithful
            1.0 = completely faithful
            Only return the number, nothing else.
            """
            response = backend.generate(prompt)
            try:
                return float(response.strip())
            except ValueError:
                return 0.0
