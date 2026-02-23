"""Faithfulness metric -- measures whether the answer is grounded in the context."""
import logging
from typing import Any, Dict

from .base import BaseMetric

logger = logging.getLogger(__name__)


class FaithfulnessMetric(BaseMetric):
    """Evaluates whether the generated answer is faithful to the retrieved context.

    A faithfulness score of 1.0 means every claim in the answer is supported
    by the context.  A score of 0.0 indicates the answer is entirely
    hallucinated or unsupported.
    """

    def __init__(self) -> None:
        """Initialise FaithfulnessMetric with its canonical name."""
        super().__init__(name="faithfulness")

    def score(self, row: Dict[str, Any], backend: Any) -> float:
        """Score how faithful the answer is to the provided context.

        Uses an LLM-as-judge approach: the backend is prompted to rate
        whether every claim in the generated answer can be traced back to
        the supplied context.

        Args:
            row: Must contain 'question', 'context', and 'answer' keys.
            backend: LLM backend instance with a ``generate(prompt: str) -> str``
                method.

        Returns:
            Float in [0.0, 1.0].  Returns 0.0 on parse or runtime errors.
        """
        question = row.get("question")
        context = row.get("context")
        answer = row.get("answer")

        prompt = f"""
Given the following context, question, and answer, evaluate whether the answer
is faithful to the context. The answer should not contain any information that
is not present in the context.

Context: {context}
Question: {question}
Answer: {answer}

Is the answer completely faithful to the context?
Respond with a single float score between 0.0 and 1.0.
0.0 = completely hallucinated/unfaithful
1.0 = completely faithful
Only return the number, nothing else.
"""
        try:
            response = backend.generate(prompt)
            return max(0.0, min(1.0, float(response.strip())))
        except ValueError:
            logger.warning("FaithfulnessMetric: could not parse backend response as float.")
            return 0.0
        except Exception as exc:
            logger.error("FaithfulnessMetric: unexpected error during scoring: %s", exc)
            return 0.0
