
# Methodology: Hindi Literary Stopwords

## 1. Project Objective

This project develops an experimental, curated Hindi stopword resource for literary text analysis. It explores how common grammatical words can be filtered while preserving meaningful literary vocabulary.

## 2. What Are Stopwords?

Stopwords are frequently occurring words that may contribute less to certain text-processing tasks. Examples include conjunctions, postpositions and auxiliary verbs.

However, a word is not universally unimportant. Its relevance depends on the research question and textual context.

## 3. Selection Criteria

The initial list was organised into the following categories:

- Conjunctions: और, तथा, लेकिन
- Relative words: जो, जिसे, जिसका
- Postpositions: का, की, के, में, से
- Auxiliary verbs: है, हैं, था, थी

Words were selected based on their grammatical function and expected usefulness for literary text processing.

## 4. Preservation of Meaningful Words

Words such as प्रकृति, नदी, वन, जल, मनुष्य and मन were excluded from the stopword list because they may carry thematic and symbolic significance in poetry.

Negation words such as नहीं and न are also preserved because removing them may reverse or alter a sentence's meaning.

## 5. Implementation

The project uses Python to:

1. Store a curated set of Hindi stopwords.
2. Normalize text using Unicode NFC normalization.
3. Tokenize text using whitespace separation.
4. Identify and remove selected stopwords.
5. Display the original and processed text.

## 6. Limitations

- The current list is small and experimental.
- It is not a universal Hindi stopword standard.
- Context-dependent words may have literary significance.
- Whitespace tokenization does not handle every Hindi linguistic variation.
- The list requires testing on a larger and more diverse Hindi poetry corpus.

## 7. Future Improvements

- Validate the list against selected Hindi poems.
- Compare it with existing Hindi NLP stopword resources.
- Add linguistic and contextual evaluation.
- Improve tokenization and punctuation handling.
- Document additions and exclusions with examples.

## 8. Research Ethics

The project uses original implementation and curated word selection. Literary texts used for evaluation will be checked for copyright and source attribution before redistribution.
