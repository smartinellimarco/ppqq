"""Library custom exceptions."""


class UndefinedTokenizerStep(Exception):
    """Tokenizer step is not defined."""

    def __init__(self, step: str):
        """Raise exception for unknown tokenizer step."""
        super().__init__(f"Tokenizer step '{step}' is not defined.")
