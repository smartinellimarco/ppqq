"""Library configurations."""

# Steps of the preprocessor in order.
PREPROCESSING_STEPS = [
    "unicode_decomposition",
    "tokenize_emails",
    "tokenize_urls",
    "tokenize_numbers",
    "ascii_filter",
    "lowercase",
    "remove_punctuation",  # Removing punctuation is tricky since its
    "trim_spaces",  # hard to know which character to use as replacement.
]

# Regex used to detect urls.
URL_REGEX = r"(?=http|www)[^\s]+"

# Regex used to detect emails.
EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Regex used to detect numbers.
NUMBER_REGEX = r"\d+"
