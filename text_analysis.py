!python -m nltk.downloader punkt
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
import textstat

def analyze_text(text):
  blob = TextBlob(text)
  #polarity and subjectivity score:
  polarity_score =blob.sentiment.polarity
  subjectivity_score = blob.sentiment.subjectivity

  sentences = sent_tokenize(text)
  words = word_tokenize(text)
  #average sentence length
  avg_sentence_length = sum(len(sent.split()) for sent in sentences) / len(sentences)
  #percentage of complex words
  complex_word_count = textstat.difficult_words(text)
  percentage_complex_words = (complex_word_count / len(words)) * 100
  # Calculate FOG index
  fog_index = flesch_kincaid_grade(text)

  # Calculate average number of words per sentence
  avg_words_per_sentence = len(words) / len(sentences)

  # Count personal pronouns
  personal_pronouns = sum(1 for word in words if word.lower() in ['i', 'me', 'my', 'mine', 'myself',
                                                                    'you', 'your', 'yours', 'yourself',
                                                                    'he', 'him', 'his', 'himself',
                                                                    'she', 'her', 'hers', 'herself',
                                                                    'it', 'its', 'itself',
                                                                    'we', 'us', 'our', 'ours', 'ourselves',
                                                                    'they', 'them', 'their', 'theirs', 'themselves'])

  # Calculate average word length
  avg_word_length = sum(len(word) for word in words) / len(words)

    # Return computed metrics
  return {
        'positive_score': sum(1 for sent in blob.sentences if sent.sentiment.polarity > 0),
        'negative_score': sum(1 for sent in blob.sentences if sent.sentiment.polarity < 0),
        'polarity_score': polarity_score,
        'subjectivity_score': subjectivity_score,
        'avg_sentence_length': avg_sentence_length,
        'percentage_complex_words': percentage_complex_words,
        'fog_index': fog_index,
        'avg_words_per_sentence': avg_words_per_sentence,
        'complex_word_count': complex_word_count,
        'word_count': len(words),
        'syllable_per_word': sum(textstat.syllable_count(word) for word in words) / len(words),
        'personal_pronouns': personal_pronouns,
        'avg_word_length': avg_word_length
    }

directory = '/content/drive/MyDrive/extracted_article'

for filename in os.listdir(directory):
  if filename.endswith('.txt'):
    with open(os.path.join(directory, filename),'r') as file:
      text = file.read()
      analysis = analyze_text(text)
      print(f"analysis for {filename} :")
      print(analysis)
      print()