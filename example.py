
from hindi_stopwords import HINDI_STOPWORDS, remove_stopwords

# Sample Hindi literary text
sample_text = """
प्रकृति और मनुष्य का संबंध बहुत गहरा है।
नदी और वन जीवन के महत्वपूर्ण आधार हैं।
"""

# Apply stopword removal
cleaned_text = remove_stopwords(sample_text)

print("ORIGINAL TEXT")
print(sample_text)

print("\nCLEANED TEXT")
print(cleaned_text)

print("\nREMOVED STOPWORDS")
removed_words = []

for word in sample_text.split():
    cleaned_word = word.strip("।,!?;:")
    if cleaned_word in HINDI_STOPWORDS:
        removed_words.append(cleaned_word)

print(sorted(set(removed_words)))

print("\nTOTAL STOPWORDS:", len(HINDI_STOPWORDS))
