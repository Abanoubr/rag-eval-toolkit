from typing import Dict, Any
    from .base import BaseMetric
    
    class ContextRecallMetric(BaseMetric):
        def __init__(self):
            super().__init__(name="context_recall")
    
        def score(self, row: Dict[str, Any], backend) -> float:
            question = row.get("question")
            context = row.get("context")
            ground_truth = row.get("ground_truth", "")
            
            prompt = f"""
            Given a question, context, and ground truth answer, evaluate how much of the ground truth is covered by the context.
            
            Question: {question}
            Context: {context}
            Ground Truth: {ground_truth}
            
            What fraction of the ground truth information is present in the context? 
            Respond with a single float between 0.0 and 1.0.
            0.0 = none of the ground truth is in the context
            1.0 = all ground truth information is present in the context
            Only return the number, nothing else.
            """
            response = backend.generate(prompt)
            try:
                return float(response.strip())
            except ValueError:
                return 0.0
