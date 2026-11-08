
# Methodology: Hindi Literary Stopwords

## 1. Project Objective

To develop an experimental Hindi stopword resource for processing literary and poetic texts using Python.

## 2. Stopword Selection

The initial list contains 39 words organised into four groups:

- Conjunctions: और, तथा, लेकिन, क्योंकि
- Relative words: जो, जिसे, जिसका
- Postpositions: का, की, के, में, से
- Auxiliary verbs: है, हैं, था, थी

## 3. Words Preserved

Meaningful literary vocabulary such as प्रकृति, नदी, वन, जल, जीवन and मनुष्य is excluded from the stopword list.

Negation words such as नहीं are also preserved because their removal may change sentence meaning.

## 4. Implementation

The project uses Python and the following process:

1. Load stopwords from stopwords.txt.
2. Normalize text using Unicode NFC.
3. Split text using whitespace-based tokenization.
4. Compare tokens with the curated stopword list.
5. Remove matching words.
6. Preserve punctuation and remaining vocabulary.

## 5. Testing

The function was tested on four sample Hindi sentences.

The tests checked stopword removal, meaningful-word preservation, negation preservation and punctuation preservation.

## 6. Limitations

- The list is experimental and not a universal Hindi NLP standard.
- It contains only 39 selected words.
- Whitespace tokenization cannot handle every linguistic variation.
- Some grammatical words may carry literary meaning depending on context.
- Evaluation on a larger poetry corpus is still required.

## 7. Future Scope

- Test on a larger Hindi poetry corpus.
- Compare with existing Hindi NLP resources.
- Improve tokenization.
- Study how stopword removal affects literary interpretation.

## 8. Research Ethics

Literary texts used for evaluation should be appropriately attributed. Copyright restrictions must be checked before redistributing poems.
