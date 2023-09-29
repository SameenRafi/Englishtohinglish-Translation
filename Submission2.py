#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nltk')
get_ipython().system('pip install googletrans==4.0.0-rc1')


# In[2]:


import re
import nltk
from nltk import pos_tag, word_tokenize
from googletrans import Translator
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[3]:


def find_nouns(sentence):
    # Tokenize the sentence and get the part-of-speech tags
    words = word_tokenize(sentence)
    tags = pos_tag(words)

    # Extract nouns from the tagged words
    nouns = [word for word, tag in tags if tag in ['NN', 'NNS', 'NNP', 'NNPS']]

    return nouns

# Function to translate text to Hindi
def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

# Function to replace nouns in Hindi sentence with their English counterparts
def replace_nouns_with_english(hindi_sentence, english_sentence):
    # Find nouns in the English sentence
    english_nouns = find_nouns(english_sentence)

    # Translate the English nouns to Hindi
    translated_nouns = [translate_to_hindi(noun) for noun in english_nouns]

    # Create a dictionary to map translated nouns to their English counterparts
    noun_mapping = {translated: original for original, translated in zip(english_nouns, translated_nouns)}

    # Replace nouns in the Hindi sentence with their English counterparts
    for hindi_noun, english_noun in noun_mapping.items():
        hindi_sentence = hindi_sentence.replace(hindi_noun, english_noun)

    return hindi_sentence


# In[4]:


sentence = input("Enter a sentence: ")
hindi_translation = translate_to_hindi(sentence)

result_sentence = replace_nouns_with_english(hindi_translation, sentence)
print("Hinglish Sentence:", result_sentence)


# In[ ]:




