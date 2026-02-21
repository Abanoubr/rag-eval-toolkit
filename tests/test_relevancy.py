import unittest
    from unittest.mock import MagicMock
    from rag_eval.metrics.relevancy import AnswerRelevancyMetric
    
    class TestAnswerRelevancyMetric(unittest.TestCase):
        def setUp(self):
            self.metric = AnswerRelevancyMetric()
            self.mock_backend = MagicMock()
    
        def test_high_relevancy_score(self):
            self.mock_backend.generate.return_value = "0.92"
            row = {"question": "What is the capital of France?", "answer": "The capital of France is Paris."}
            score = self.metric.score(row, self.mock_backend)
            self.assertAlmostEqual(score, 0.92)
    
        def test_score_clamped_between_zero_and_one(self):
            self.mock_backend.generate.return_value = "0.75"
            row = {"question": "test", "answer": "test"}
            score = self.metric.score(row, self.mock_backend)
            self.assertGreaterEqual(score, 0.0)
            self.assertLessEqual(score, 1.0)
    
    if __name__ == "__main__":
        unittest.main()
    
