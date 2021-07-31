import nltk
from nltk.tokenize import BlanklineTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import LineTokenizer
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk import pos_tag
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

import pickle
#import spacy


import numpy as np

from skillsapi import skills_list_extraction
import re
import os,glob
skillset= skills_list_extraction()



def preprocessing(text):
    text=text.strip()
    text=text.replace("\xa0", " ")
    text=text.replace('\\n', " ")
    text=text.replace('\\t', " ")
    text=re.sub(' +', ' ', text)
    return text
def delimiter_removal(text):  # Converts the delimiters to blank space
     delimiters = ['[', ']', '?', '!', '(', ')', '/', '{', '}', ';']
     for delimiter in delimiters:
        text = text.replace(delimiter, ' ')
     return text


def extract_email(text):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", str(text))
    if email:
        try:
             return email[0].split()[0].strip(';')
        except IndexError:
             return ' '

def extract_skills(text):
    token = list(nltk.word_tokenize(text))
    bigrams = ngrams(token, 2)
    bigrams_list = list(bigrams)
    bigrams_stringlist = list(map(lambda x: x[0] + ' ' + x[1], bigrams_list))
    trigrams = ngrams(token, 3)
    trigrams_list = list(trigrams)
    trigrams_stringlist = list(map(lambda x: x[0] + ' ' + x[1] + ' ' + x[2], trigrams_list))
    list_ngrams = token + bigrams_stringlist + trigrams_stringlist
    list_ngrams = [ngram.lower() for ngram in list_ngrams]
    set_ngrams=set(list_ngrams)
    set_skillset=set(skillset)
    skills_per_candidate=list(set_ngrams.intersection(set_skillset))
    return skills_per_candidate

def mobile_number_extraction(text):
    not_alpha_numeric = r'[^a-zA-Z\d]'
    number_format1 = r'(\d{10})'
    number_format2 = r'((' + not_alpha_numeric + r'(\d{1})' + not_alpha_numeric + r'(\d{10})' + '))'
    number_format3 = r'((' + not_alpha_numeric + r'(\d{2})' + not_alpha_numeric + r'(\d{10})' + '))'
    number_format4 = r'((' + not_alpha_numeric + r'(\d{3})' + not_alpha_numeric + r'(\d{10})' + '))'
    number_format5 = r'^(0)(\d{10})'
    regex_number = r'(' + number_format5 + r'|' + number_format2 + r'|' + number_format3 + r'|' + number_format4 + r'|' + number_format1 + ')'

    regular_expression = re.compile(regex_number, re.IGNORECASE)
    regex_result = re.search(regular_expression, text)
    try:
        return regex_result.group()
    except:
        return None

def ner_extraction(text):
    with open('ner_model', 'rb') as f:
        data = pickle.load(f)
    model = pickle.loads(data)
    doc = model(text)
    return doc