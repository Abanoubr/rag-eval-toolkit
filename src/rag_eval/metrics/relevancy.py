from typing import Dict, Any
    from .base import BaseMetric
    
    class AnswerRelevancyMetric(BaseMetric):
        def __init__(self):
            super().__init__(name="answer_relevancy")
    
        def score(self, row: Dict[str, Any], backend) -> float:
            question = row.get("question")
            answer = row.get("answer")
            
            prompt = f"""
            Given the following question and answer, evaluate how relevant the answer is to the question.
            
            Question: {question}
            Answer: {answer}
            
            How relevant is the answer to the question? Respond with a single float score between 0.0 and 1.0.
            0.0 = completely irrelevant
            1.0 = perfectly answers the question
            Only return the number, nothing else.
            """
            response = backend.generate(prompt)
            try:
                return float(response.strip())
            except ValueError:
                return 0.0
    
