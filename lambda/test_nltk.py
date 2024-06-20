import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

# Function to convert nltk POS tags to WordNet POS tags
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

# Original sentence
sentence = "Told"
lemmatizer = WordNetLemmatizer()

# Convert sentence to lowercase and tokenize it
tokens = word_tokenize(sentence.lower())

# Manually set the POS tag to VBD (verb, past tense) since we know "told" should be a verb
tagged_tokens = [(token, 'VBD') for token in tokens]

# Debugging: Print tokens and POS tags
print(f"Tokens and POS tags: {tagged_tokens}")

# Lemmatize each token
normalized_tokens = []
for token, tag in tagged_tokens:
    wn_tag = get_wordnet_pos(tag)
    if wn_tag is None:
        lemma = token
    else:
        lemma = lemmatizer.lemmatize(token, wn_tag)
    normalized_tokens.append(lemma)

# Join the normalized tokens back into a sentence
normalized_sentence = ' '.join(normalized_tokens)

# Print the results
print(f"Original sentence: {sentence}")
print(f"Normalized sentence: {normalized_sentence}")
