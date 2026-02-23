"""RAG Eval Toolkit — Core evaluator module."""
import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class RAGEvaluator:
    """Orchestrates RAG pipeline evaluation across one or more metrics.

    Args:
        backend: An LLM backend instance used to power LLM-as-judge evaluation.
    """

    def __init__(self, backend: Any) -> None:
        self.backend = backend
        self.metrics: List[Any] = []

    def add_metric(self, metric: Any) -> None:
        """Register a metric to be computed during evaluation.

        Args:
            metric: A metric instance implementing the BaseMetric interface.
        """
        self.metrics.append(metric)

    def evaluate(self, dataset: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Run all registered metrics over the provided dataset.

        Args:
            dataset: List of dicts, each containing 'question', 'context',
                     and 'answer' keys. 'ground_truth' is optional.

        Returns:
            Dictionary mapping metric names to their average scores and
            per-sample results.

        Raises:
            ValueError: If the dataset is empty or no metrics are registered.
        """
        if not dataset:
            raise ValueError("Dataset must not be empty.")
        if not self.metrics:
            raise ValueError("No metrics registered. Call add_metric() first.")

        per_metric_scores: Dict[str, List[float]] = {m.name: [] for m in self.metrics}

        for item in dataset:
            for metric in self.metrics:
                try:
                    score = metric.score(item, self.backend)
                    score = max(0.0, min(1.0, float(score)))
                    per_metric_scores[metric.name].append(score)
                except (ValueError, TypeError) as e:
                    logger.warning("Failed to parse score for %s: %s. Using 0.0.", metric.name, e)
                    per_metric_scores[metric.name].append(0.0)
                except Exception as e:
                    logger.error("Backend call failed for %s: %s", metric.name, e)
                    raise

        averages = {
            name: round(sum(scores) / len(scores), 4)
            for name, scores in per_metric_scores.items()
            if scores
        }

        return {"averages": averages, "per_sample": per_metric_scores}

    def generate_report(
        self, results: Dict[str, Any], output: str = "eval_report.html"
    ) -> str:
        """Generate an HTML evaluation report.

        Args:
            results: Output from evaluate(), containing averages and per-sample scores.
            output: File path for the generated HTML report.

        Returns:
            Path to the generated report file.
        """
        try:
            from rag_eval.report.generator import generate_html_report
            generate_html_report(results, output)
            logger.info("Report saved to %s", output)
        except ImportError:
            logger.warning("Report generator not available. Install with: pip install rag-eval-toolkit[report]")
        return output
