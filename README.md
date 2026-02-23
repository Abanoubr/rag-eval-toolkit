# rag-eval-toolkit
    
    [![CI](https://github.com/Abanoubr/rag-eval-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Abanoubr/rag-eval-toolkit/actions/workflows/ci.yml)
    [![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
    [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
    
    A lightweight, extensible Python framework for evaluating Retrieval-Augmented Generation (RAG) pipelines. Uses LLM-as-judge to score faithfulness, relevancy, and context quality.
    
    ## Why rag-eval-toolkit?
    
    | Feature | rag-eval-toolkit | Ragas |
    |---------|-----------------|-------|
    | Setup complexity | ✅ Minimal | ⚠️ Moderate |
    | Custom metrics | ✅ Simple class inheritance | ⚠️ More complex |
    | Backend support | ✅ OpenAI + Anthropic | ✅ Multiple |
    | HTML reports | ✅ Built-in | ❌ External |
    | CLI tool | ✅ Built-in | ❌ Not included |
    
    ## Installation
    
    ```bash
    pip install rag-eval-toolkit
    ```
    
    ## Quick Start (5 lines)
    
    ```python
    from rag_eval import RAGEvaluator, AnthropicBackend, FaithfulnessMetric
    
    evaluator = RAGEvaluator(backend=AnthropicBackend())
    evaluator.add_metric(FaithfulnessMetric())
    results = evaluator.evaluate(your_dataset)
    ```
    
    ## Available Metrics
    
    - **FaithfulnessMetric** — Does the answer stick to the retrieved context?
    - **AnswerRelevancyMetric** — Does the answer address the actual question?
    - **ContextPrecisionMetric** — Is the retrieved context relevant to the question?
    - **ContextRecallMetric** — Does the context cover the ground truth answer?
    
    ## Dataset Format
    
    ```python
    dataset = [
        {
            "question": "What is RAG?",
            "context": "RAG stands for Retrieval-Augmented Generation...",
            "answer": "RAG is a technique that combines retrieval with generation.",
            "ground_truth": "RAG combines document retrieval with LLM generation."  # optional
        }
    ]
    ```
    
    ## Backends
    
    ```python
    from rag_eval.backends import AnthropicBackend, OpenAIBackend
    
    # Claude (recommended)
    backend = AnthropicBackend(model="claude-sonnet-4-20250514")
    
    # GPT-4
    backend = OpenAIBackend(model="gpt-4-turbo-preview")
    ```
    
    ## Custom Metrics
    
    ```python
    from rag_eval.metrics.base import BaseMetric
    
    class MyMetric(BaseMetric):
        def __init__(self):
            super().__init__(name="my_metric")
        
        def score(self, row, backend) -> float:
            # Your evaluation logic here
            return 0.95
    ```
    
    ## CLI
    
    ```bash
    rag-eval --help
    ```
    
    
## Architecture

```
rag_eval/
├── backends/          # LLM backends (Anthropic, OpenAI)
├── metrics/           # Evaluation metrics
│   ├── faithfulness.py
│   ├── relevancy.py
│   ├── context_precision.py
│   └── context_recall.py
├── report/            # HTML report generation
├── evaluator.py       # Core evaluation engine
└── cli.py             # Command-line interface
```

## HTML Reports

```python
# Generate a full HTML report with per-question breakdowns
evaluator.generate_report(results, output="eval_report.html")
```

## Author

**Abanoub Rodolf Boctor** — [LinkedIn](https://linkedin.com/in/abanoubrodolf) · [GitHub](https://github.com/Abanoubr)

## Contributing
    
    PRs welcome. Please open an issue first to discuss major changes.
    
    ## License
    
    MIT
    
