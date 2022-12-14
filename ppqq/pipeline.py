"""Basic text preprocessing class."""

import re
import string
import unicodedata
from typing import Any, Iterable, List

from ppqq.exceptions import UndefinedTokenizerStep
from ppqq.settings import EMAIL_REGEX, NUMBER_REGEX, PREPROCESSING_STEPS, URL_REGEX
from sklearn.base import BaseEstimator, TransformerMixin


class Cleaner(BaseEstimator, TransformerMixin):
    """Text normalization."""

    def __init__(self) -> None:
        """Initialize preprocessor for the given language."""
        self.__name__: str = type(self).__name__
        try:
            self.tokenizer_steps = []
            for step in PREPROCESSING_STEPS:
                self.tokenizer_steps.append(getattr(self, step))
        except AttributeError as exce:
            raise UndefinedTokenizerStep(step) from exce

    def fit(self, X: Any, y: Any = None) -> "Cleaner":  # pylint: disable=W0613
        """Fit the transformer."""
        return self

    def transform(self, X: Iterable, y: Iterable = None) -> List[str]:  # pylint: disable=W0613
        """Apply in a composed fashion all the defined tokenizers."""

        outputs = []
        for text in X:
            for func in self.tokenizer_steps:
                text = func(text)
            outputs.append(text)

        return outputs

    @staticmethod
    def unicode_decomposition(text: str) -> str:
        """Decompose unicode characters into their most cannonical form."""
        return unicodedata.normalize("NFD", text)

    @staticmethod
    def ascii_filter(text: str) -> str:
        """Filter text by keeping only unicode characters with ord less than 128 (ascii)."""
        return text.encode("ascii", errors="ignore").decode("utf-8")

    @staticmethod
    def lowercase(text: str) -> str:
        """Convert text to lowercase characters."""
        return text.lower()

    @staticmethod
    def remove_punctuation(text: str) -> str:
        """Remove punctuation characters."""
        return text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))

    @staticmethod
    def trim_spaces(text: str) -> str:
        """Remove spaces, tabs and other identation characters."""
        return " ".join(text.split())

    @staticmethod
    def tokenize_numbers(text: str) -> Any:
        """Replace numbers with a token."""
        return re.sub(NUMBER_REGEX, " numbertk ", text)

    @staticmethod
    def tokenize_urls(text: str) -> Any:
        """Replace urls with a token."""
        return re.sub(URL_REGEX, " urltk ", text)

    @staticmethod
    def tokenize_emails(text: str) -> Any:
        """Replace emails with a token."""
        return re.sub(EMAIL_REGEX, " emailtk ", text)
