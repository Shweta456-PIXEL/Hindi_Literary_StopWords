
import re
import unicodedata

# Curated initial stopword list for Hindi literary text.
# This is an experimental list, not a universal Hindi NLP standard.

HINDI_STOPWORDS = {
    # Conjunctions
    "और", "तथा", "एवं", "या", "अथवा",
    "लेकिन", "मगर", "किंतु", "परंतु", "क्योंकि",
    "यदि", "अगर", "कि", "जबकि",

    # Relative and connective words
    "जो", "जिस", "जिसे", "जिसका", "जिसकी", "जिसके",

    # Postpositions
    "का", "की", "के", "को", "से", "में",
    "पर", "तक", "द्वारा", "हेतु", "साथ", "बिना",

    # Common auxiliary forms
    "है", "हैं", "था", "थी", "थे", "हूँ", "हो",
}


def normalize_text(text):
    """Normalize Unicode text to NFC form."""
    return unicodedata.normalize("NFC", text)


def remove_stopwords(text, stopwords=None):
    """
    Remove selected Hindi stopwords while preserving
    the original spelling and punctuation of retained words.
    """
    if stopwords is None:
        stopwords = HINDI_STOPWORDS

    text = normalize_text(text)
    cleaned_tokens = []

    for token in text.split():
        # Ignore punctuation at the beginning/end for matching.
       word = token.strip("।॥,!?;:()[]{}\"'“”‘’")
        normalized_word = normalize_text(word)

        if not normalized_word or normalized_word not in stopwords:
            cleaned_tokens.append(token)

    return " ".join(cleaned_tokens)


if __name__ == "__main__":
    sample_text = "प्रकृति और मनुष्य का संबंध बहुत गहरा है।"

    print("Original text:")
    print(sample_text)

    print("\nAfter stopword removal:")
    print(remove_stopwords(sample_text))
