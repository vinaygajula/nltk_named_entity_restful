__author__ = 'serendio'
import nltk
from flask import Flask
app = Flask(__name__)


def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
         entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

def logic(message):
    print message
    #sample="Peter is in Chennai"
    sentences = nltk.sent_tokenize(message)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    #print chunked_sentences
    entity_names = []
    for tree in chunked_sentences:
      #print results per sentence
      #print extract_entity_names(tree)
#
        entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
    return set(entity_names)

@app.route('/<message>', methods=['GET'])
def entities(message):
    output = logic(message)
    # extract_entity_names(t)
    return str(output)

if __name__ == '__main__':
    app.run(debug=True,port=2000)