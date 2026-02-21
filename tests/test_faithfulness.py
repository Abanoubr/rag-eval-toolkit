import unittest
    from unittest.mock import MagicMock
    from rag_eval.metrics.faithfulness import FaithfulnessMetric
    
    class TestFaithfulnessMetric(unittest.TestCase):
        def setUp(self):
            self.metric = FaithfulnessMetric()
            self.mock_backend = MagicMock()
    
        def test_high_faithfulness_score(self):
            self.mock_backend.generate.return_value = "0.95"
            row = {"question": "What is Python?", "context": "Python is a high-level programming language.", "answer": "Python is a programming language."}
            score = self.metric.score(row, self.mock_backend)
            self.assertAlmostEqual(score, 0.95)
    
        def test_invalid_response_returns_zero(self):
            self.mock_backend.generate.return_value = "not a number"
            row = {"question": "test", "context": "test", "answer": "test"}
            score = self.metric.score(row, self.mock_backend)
            self.assertEqual(score, 0.0)
    
    if __name__ == "__main__":
        unittest.main()
    
