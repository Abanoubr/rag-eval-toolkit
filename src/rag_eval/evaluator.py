from typing import List, Dict, Any
    
    class RAGEvaluator:
        def __init__(self, backend):
            self.backend = backend
            self.metrics = []
    
        def add_metric(self, metric):
            self.metrics.append(metric)
    
        def evaluate(self, dataset: List[Dict[str, Any]]) -> Dict[str, float]:
            results = {}
            for item in dataset:
                for metric in self.metrics:
                    score = metric.score(item, self.backend)
                    # Aggregate logic here
            return results
