"""Context recall metric -- measures coverage of ground-truth information in the context."""
import logging
from typing import Any, Dict

from .base import BaseMetric

logger = logging.getLogger(__name__)


class ContextRecallMetric(BaseMetric):
    """Evaluates how much of the ground-truth answer is covered by the context.

    A score of 1.0 means every piece of ground-truth information appears in
    the retrieved context.  A score of 0.0 means none of the required
    information is present.

    Note:
        This metric requires a 'ground_truth' key in the input row.
        If absent, an empty string is used which may produce unreliable scores.
    """

    def __init__(self) -> None:
        """Initialise ContextRecallMetric with its canonical name."""
        super().__init__(name="context_recall")

    def score(self, row: Dict[str, Any], backend: Any) -> float:
        """Score how much ground-truth information is covered by the context.

        Uses an LLM-as-judge approach: the backend estimates what fraction of
        the ground-truth reference answer can be found in the retrieved context.

        Args:
            row: Must contain 'question' and 'context' keys.  Optionally
                includes a 'ground_truth' key for the reference answer.
            backend: LLM backend instance with a ``generate(prompt: str) -> str``
                method.

        Returns:
            Float in [0.0, 1.0].  Returns 0.0 on parse or runtime errors.
        """
        question = row.get("question")
        context = row.get("context")
        ground_truth = row.get("ground_truth", "")

        prompt = f"""
Given a question, context, and ground truth answer, evaluate how much of the
ground truth is covered by the context.

Question: {question}
Context: {context}
Ground Truth: {ground_truth}

What fraction of the ground truth information is present in the context?
Respond with a single float between 0.0 and 1.0.
0.0 = none of the ground truth is in the context
1.0 = all ground truth information is present in the context
Only return the number, nothing else.
"""
        try:
            response = backend.generate(prompt)
            return max(0.0, min(1.0, float(response.strip())))
        except ValueError:
            logger.warning("ContextRecallMetric: could not parse backend response as float.")
            return 0.0
        except Exception as exc:
            logger.error("ContextRecallMetric: unexpected error during scoring: %s", exc)
            return 0.0
