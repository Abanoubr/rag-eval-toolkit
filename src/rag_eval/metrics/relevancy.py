"""Answer relevancy metric -- measures how well the answer addresses the question."""
import logging
from typing import Any, Dict

from .base import BaseMetric

logger = logging.getLogger(__name__)


class AnswerRelevancyMetric(BaseMetric):
    """Evaluates how relevant the generated answer is to the user's question.

    A score of 1.0 means the answer perfectly addresses the question.
    A score of 0.0 means the answer is completely off-topic or irrelevant.
    """

    def __init__(self) -> None:
        """Initialise AnswerRelevancyMetric with its canonical name."""
        super().__init__(name="answer_relevancy")

    def score(self, row: Dict[str, Any], backend: Any) -> float:
        """Score how relevant the answer is to the question.

        Uses an LLM-as-judge approach: the backend rates whether the generated
        answer directly and completely addresses the user's question.

        Args:
            row: Must contain 'question' and 'answer' keys.
            backend: LLM backend instance with a ``generate(prompt: str) -> str``
                method.

        Returns:
            Float in [0.0, 1.0].  Returns 0.0 on parse or runtime errors.
        """
        question = row.get("question")
        answer = row.get("answer")

        prompt = f"""
Given the following question and answer, evaluate how relevant the answer is
to the question.

Question: {question}
Answer: {answer}

How relevant is the answer to the question?
Respond with a single float score between 0.0 and 1.0.
0.0 = completely irrelevant
1.0 = perfectly answers the question
Only return the number, nothing else.
"""
        try:
            response = backend.generate(prompt)
            return max(0.0, min(1.0, float(response.strip())))
        except ValueError:
            logger.warning("AnswerRelevancyMetric: could not parse backend response as float.")
            return 0.0
        except Exception as exc:
            logger.error("AnswerRelevancyMetric: unexpected error during scoring: %s", exc)
            return 0.0
