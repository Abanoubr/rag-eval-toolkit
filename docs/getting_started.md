# Getting Started with rag-eval-toolkit
    
    ## Installation
    
    ```bash
    pip install rag-eval-toolkit
    ```
    
    Or from source:
    
    ```bash
    git clone https://github.com/Abanoubr/rag-eval-toolkit
    cd rag-eval-toolkit
    pip install -e .
    ```
    
    ## Quick Start
    
    ```python
    from rag_eval.evaluator import RAGEvaluator
    from rag_eval.backends.anthropic_backend import AnthropicBackend
    from rag_eval.metrics.faithfulness import FaithfulnessMetric
    from rag_eval.metrics.relevancy import AnswerRelevancyMetric
    
    # Initialize backend
    backend = AnthropicBackend(model="claude-sonnet-4-20250514")
    
    # Set up evaluator
    evaluator = RAGEvaluator(backend=backend)
    evaluator.add_metric(FaithfulnessMetric())
    evaluator.add_metric(AnswerRelevancyMetric())
    
    # Your dataset
    dataset = [
        {
            "question": "What is RAG?",
            "context": "RAG stands for Retrieval-Augmented Generation...",
            "answer": "RAG is a technique that...",
        }
    ]
    
    # Evaluate
    results = evaluator.evaluate(dataset)
    print(results)
    ```
    
    ## Available Metrics
    
    | Metric | Description |
    |--------|-------------|
    | `FaithfulnessMetric` | Does the answer stay grounded in the context? |
    | `AnswerRelevancyMetric` | Does the answer address the question? |
    | `ContextPrecisionMetric` | Is the retrieved context relevant? |
    | `ContextRecallMetric` | Does context cover the ground truth? |
    
    ## Backends
    
    - `AnthropicBackend` — Uses Claude (requires `ANTHROPIC_API_KEY`)
    - `OpenAIBackend` — Uses GPT-4 (requires `OPENAI_API_KEY`)
    
    ## CLI Usage
    
    ```bash
    rag-eval --help
    ```
    
    ## Creating Custom Metrics
    
    See `examples/custom_metrics.py` for how to build your own metric by extending `BaseMetric`.
    
