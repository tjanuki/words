import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

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

def normalize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(sentence.lower())
    tagged_tokens = pos_tag(tokens)

    normalized_tokens = []
    for token, tag in tagged_tokens:
        wn_tag = get_wordnet_pos(tag)
        if wn_tag is None:
            lemma = token
        else:
            lemma = lemmatizer.lemmatize(token, wn_tag)
        normalized_tokens.append(lemma)

    return ' '.join(normalized_tokens)

def lambda_handler(event, context):
    body = json.loads(event['body'])
    sentence = body['sentence']
    normalized_sentence = normalize_sentence(sentence)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'original_sentence': sentence,
            'normalized_sentence': normalized_sentence
        })
    }
