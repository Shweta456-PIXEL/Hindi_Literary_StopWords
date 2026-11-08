
from pathlib import Path
import unicodedata


def normalize_text(text):
    """Normalize Hindi text using Unicode NFC."""
    return unicodedata.normalize("NFC", text)


# Load stopwords directly from stopwords.txt
STOPWORDS_FILE = Path(__file__).with_name("stopwords.txt")

with open(STOPWORDS_FILE, "r", encoding="utf-8") as file:
    HINDI_STOPWORDS = {
        normalize_text(line.strip())
        for line in file
        if line.strip()
    }


def remove_stopwords(text, stopwords=None):
    """
    Remove selected Hindi stopwords while preserving
    punctuation and meaningful literary vocabulary.
    """

    if stopwords is None:
        stopwords = HINDI_STOPWORDS

    stopwords = {normalize_text(word) for word in stopwords}

    punctuation = "।॥,!?;:()[]{}\"'“”‘’"
    cleaned_tokens = []

    for token in normalize_text(text).split():

        word = token.strip(punctuation)
        normalized_word = normalize_text(word)

        if normalized_word in stopwords:

            # Preserve trailing punctuation after removing a word.
            trailing_punctuation = token[len(token.rstrip(punctuation)):]

            if trailing_punctuation and cleaned_tokens:
                cleaned_tokens[-1] += trailing_punctuation

            elif trailing_punctuation:
                cleaned_tokens.append(trailing_punctuation)

        else:
            cleaned_tokens.append(token)

    return " ".join(cleaned_tokens)


if __name__ == "__main__":

    sample_text = "प्रकृति और मनुष्य का संबंध बहुत गहरा है।"

    print("Original:", sample_text)
    print("Cleaned:", remove_stopwords(sample_text))
    print("Total stopwords:", len(HINDI_STOPWORDS))
