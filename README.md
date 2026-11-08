
# Hindi Literary Stopwords

A beginner-friendly Python project that explores stopword removal in Hindi literary text.

## Project Overview

This project develops an experimental, curated Hindi stopword list for processing Hindi literary and poetic texts.

It identifies and removes selected grammatical words while preserving meaningful vocabulary such as प्रकृति, नदी, वन, जल and मनुष्य.

## Objectives

- Create a curated Hindi stopword list.
- Implement stopword removal using Python.
- Preserve meaningful literary vocabulary.
- Examine the limitations of stopword removal in literary analysis.

## Project Structure

- `hindi_stopwords.py` — Python implementation.
- `stopwords.txt` — Curated list of 39 Hindi stopwords.
- `example.py` — Demonstration using sample Hindi sentences.
- `methodology.md` — Selection criteria, methodology and limitations.

## Methodology

The project uses Unicode NFC normalization and whitespace-based tokenization.

Stopwords are loaded directly from `stopwords.txt`. Selected words are removed while retaining punctuation and other vocabulary.

## Example

Original:

प्रकृति और मनुष्य का संबंध बहुत गहरा है।

Processed:

प्रकृति मनुष्य संबंध बहुत गहरा।

## Testing

The implementation was tested using four Hindi sentences.

The tests examined:
- Removal of selected grammatical words.
- Preservation of meaningful vocabulary.
- Preservation of negation words such as नहीं.
- Preservation of sentence-ending punctuation.

## Limitations

- The list is experimental, not a universal Hindi NLP standard.
- The list contains only 39 selected words.
- Whitespace-based tokenization has linguistic limitations.
- Context-dependent words may carry literary meaning.
- Further evaluation on a larger poetry corpus is required.

## Future Scope

- Test the resource on a larger Hindi poetry corpus.
- Compare with existing Hindi NLP resources.
- Improve linguistic tokenization.
- Evaluate how stopword removal affects literary interpretation.

## Course Information

DH Lab 2 — Monsoon Semester 2026  
Department of Humanities and Social Sciences  
IIT (ISM) Dhanbad
