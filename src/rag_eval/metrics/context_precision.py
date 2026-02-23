"""Context precision metric -- measures signal-to-noise ratio of retrieved context."""
import logging
from typing import Any, Dict

from .base import BaseMetric

logger = logging.getLogger(__name__)


class ContextPrecisionMetric(BaseMetric):
    """Evaluates how precisely the retrieved context matches the information need.

    A score of 1.0 means the context contains exactly the information needed
    to answer the question with no irrelevant content.  A score of 0.0 means
    the context is entirely useless for answering the question.
    """

    def __init__(self) -> None:
        """Initialise ContextPrecisionMetric with its canonical name."""
        super().__init__(name="context_precision")

    def score(self, row: Dict[str, Any], backend: Any) -> float:
        """Score how precisely the context addresses the question's information need.

        Uses an LLM-as-judge approach: the backend rates how useful the
        retrieved context is for answering the provided question.

        Args:
            row: Must contain 'question' and 'context' keys.
            backend: LLM backend instance with a ``generate(prompt: str) -> str``
                method.

        Returns:
            Float in [0.0, 1.0].  Returns 0.0 on parse or runtime errors.
        """
        question = row.get("question")
        context = row.get("context")

        prompt = f"""
Given the following question and context, evaluate how useful the context is
for answering the question.

Question: {question}
Context: {context}

Does the context contain the information needed to answer the question?
Respond with a single float score between 0.0 and 1.0.
0.0 = completely useless context
1.0 = context contains the exact answer
Only return the number, nothing else.
"""
        try:
            response = backend.generate(prompt)
            return max(0.0, min(1.0, float(response.strip())))
        except ValueError:
            logger.warning("ContextPrecisionMetric: could not parse backend response as float.")
            return 0.0
        except Exception as exc:
            logger.error("ContextPrecisionMetric: unexpected error during scoring: %s", exc)
            return 0.0
