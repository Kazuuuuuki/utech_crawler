import sys
from os import listdir, path
from pyknp import Jumanpp
from gensim import models
from gensim.models.doc2vec import LabeledSentence

def docs_title():
    filename = "title.txt"
    with open(filename, 'r') as f:
        text = f.read()
        new_text = text.replace('\n','')
        return new_text.split(",")
#
#
def split_into_words(text):
    result = Jumanpp().analysis(text)
    return [mrph.midasi for mrph in result.mrph_list()]
#
def doc_to_sentence(doc):
    words = split_into_words(doc)
    return LabeledSentence(words=words, tags=[doc])

def docs_to_sentences(docs):
    sentences = []
    for doc in docs:
        sentences.append(doc_to_sentence(doc))
    return sentences

docs = docs_title()

sentences = docs_to_sentences(docs)

model = models.Doc2Vec(documents=sentences, dm=0, min_count=1)

model.save('title.model')

model = models.Doc2Vec.load('title.model')
print(model.docvecs['最新の画像生成技術に衝撃を受けたので、その基礎技術をTensorFlowで実装してみる'])
