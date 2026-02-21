"""
    Basic example: Evaluate a RAG pipeline using rag-eval-toolkit.
    
    Usage:
        export ANTHROPIC_API_KEY=your_key_here
        python examples/basic_evaluation.py
    """
    
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
    
    from rag_eval.evaluator import RAGEvaluator
    from rag_eval.backends.anthropic_backend import AnthropicBackend
    from rag_eval.metrics.faithfulness import FaithfulnessMetric
    from rag_eval.metrics.relevancy import AnswerRelevancyMetric
    from rag_eval.metrics.context_precision import ContextPrecisionMetric
    from rag_eval.utils.helpers import save_results_to_csv
    
    # Sample dataset: question, retrieved context, generated answer
    SAMPLE_DATASET = [
        {
            "question": "What is retrieval-augmented generation?",
            "context": "Retrieval-Augmented Generation (RAG) is a technique that combines information retrieval with language model generation. It retrieves relevant documents from a knowledge base and uses them to ground the model's response.",
            "answer": "RAG is a technique that retrieves relevant documents and uses them to generate more accurate, grounded responses.",
            "ground_truth": "Retrieval-Augmented Generation combines retrieval and generation to produce factually grounded answers."
        },
        {
            "question": "What programming language is commonly used for ML?",
            "context": "Python is the dominant language in machine learning and AI research. Libraries like PyTorch, TensorFlow, and scikit-learn are all Python-based.",
            "answer": "Python is the most commonly used language for machine learning.",
            "ground_truth": "Python is the dominant language in ML, supported by libraries like PyTorch and TensorFlow."
        },
    ]
    
    def main():
        print("=== RAG Evaluation Toolkit — Basic Example ===\n")
        
        backend = AnthropicBackend(model="claude-sonnet-4-20250514")
        evaluator = RAGEvaluator(backend=backend)
        
        evaluator.add_metric(FaithfulnessMetric())
        evaluator.add_metric(AnswerRelevancyMetric())
        evaluator.add_metric(ContextPrecisionMetric())
        
        print("Evaluating dataset...")
        results = evaluator.evaluate(SAMPLE_DATASET)
        
        print("\n=== Results ===")
        for i, result in enumerate(results):
            print(f"\nQ{i+1}: {result['question']}")
            for key, value in result.items():
                if key != "question":
                    print(f"  {key}: {value:.2f}")
        
        save_results_to_csv(results, "evaluation_results.csv")
        print("\nResults saved to evaluation_results.csv")
    
    if __name__ == "__main__":
        main()
    
