import json
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

def lambda_handler(event, context):
    try:
        sentence = event['sentence']
        lemmatizer = WordNetLemmatizer()

        tokens = word_tokenize(sentence)
        tagged_tokens = pos_tag(tokens)

        normalized_tokens = []
        for token, tag in tagged_tokens:
            wn_tag = get_wordnet_pos(tag)
            if wn_tag is None:
                lemma = token
            else:
                lemma = lemmatizer.lemmatize(token, wn_tag)
            normalized_tokens.append(lemma)

        normalized_sentence = ' '.join(normalized_tokens)

        return {
            'statusCode': 200,
            'body': json.dumps({'normalized': normalized_sentence})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
