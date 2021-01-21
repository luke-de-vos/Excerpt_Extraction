# Excerpt_Extraction

Excerpt Extractor: Creates directory splitDoc.py and populates with excerpts of specified word count range from passed file
Excerpts begin and end with the beginning and ends of sentences respectively.
If a sentence begins before the minLength and persists through the maxLength, the excerpt is deleted.

To use:
  ```
	python3 splitDoc.py [filePath] [minLength] [maxLength]
  ```
