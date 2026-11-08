import unicodedata

HINDI_STOPWORDS = {
    "और", "तथा", "एवं", "या", "अथवा",
    "लेकिन", "मगर", "किंतु", "परंतु", "क्योंकि",
    "यदि", "अगर", "कि", "जबकि",

    "जो", "जिस", "जिसे", "जिसका", "जिसकी", "जिसके",

    "का", "की", "के", "को", "से", "में",
    "पर", "तक", "द्वारा", "हेतु", "साथ", "बिना",

    "है", "हैं", "था", "थी", "थे", "हूँ", "हो",
}


def normalize_text(text):
    return unicodedata.normalize("NFC", text)


def remove_stopwords(text, stopwords=None):
    if stopwords is None:
        stopwords = HINDI_STOPWORDS

    stopwords = {normalize_text(word) for word in stopwords}
    punctuation = "।॥,!?;:()[]{}\"'“”‘’"

    cleaned_tokens = []

    for token in normalize_text(text).split():
        word = token.strip(punctuation)

        if normalize_text(word) not in stopwords:
            cleaned_tokens.append(token)

    return " ".join(cleaned_tokens)


if __name__ == "__main__":
    sample_text = "प्रकृति और मनुष्य का संबंध बहुत गहरा है।"

    print("Original:", sample_text)
    print("Cleaned:", remove_stopwords(sample_text))
