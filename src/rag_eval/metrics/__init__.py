"""RAG Eval Toolkit -- metrics package.

Available metrics:
    FaithfulnessMetric    -- answer grounded in context
    AnswerRelevancyMetric -- answer relevant to the question
    ContextPrecisionMetric -- context signal-to-noise ratio
    ContextRecallMetric   -- ground-truth coverage in context
    BaseMetric            -- abstract base for custom metrics
"""

from .base import BaseMetric
from .faithfulness import FaithfulnessMetric
from .relevancy import AnswerRelevancyMetric
from .context_precision import ContextPrecisionMetric
from .context_recall import ContextRecallMetric

__all__ = [
    "BaseMetric",
    "FaithfulnessMetric",
    "AnswerRelevancyMetric",
    "ContextPrecisionMetric",
    "ContextRecallMetric",
]
