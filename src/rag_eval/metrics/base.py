"""Base metric interface for the RAG Eval Toolkit."""
from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseMetric(ABC):
    """Abstract base class for all RAG evaluation metrics.

    Subclasses must implement the :meth:`score` method, which evaluates
    a single dataset row against the provided LLM backend.
    """

    def __init__(self, name: str) -> None:
        """Initialise the metric with a unique identifier.

        Args:
            name: Human-readable name used for result keys and reporting.
        """
        self.name = name

    @abstractmethod
    def score(self, row: Dict[str, Any], backend: Any) -> float:
        """Compute a quality score for a single RAG sample.

        Args:
            row: Dictionary containing at minimum ``question``, ``context``,
                and ``answer`` keys.
            backend: An LLM backend instance exposing a ``generate(prompt)``
                method.

        Returns:
            A float in the range ``[0.0, 1.0]`` where higher is better.
        """
        pass
