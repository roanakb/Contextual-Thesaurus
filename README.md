# Contextual-Thesaurus
[Demo Video](https://youtu.be/shRAcu3UCY4)
## Description
Uses Facebook Infersent embeddings to calculate which synset is correct for the given word and sentence.
Synsets are acquired using WordNet.
## Sources
[Facebook Research Paper for Infersent Embeddings](https://arxiv.org/abs/1705.02364) <br/>
[Repository for Infersent Embeddings](https://github.com/facebookresearch/InferSent)
## Known Limitations
This method requires the context to be very explicit in the sentence, as can be seen in the example sentences below.
With further experimentation of word embeddings and classification methods, this may be improved.
## Setup
#### Dependencies
* Python 2/3
* [Pytorch](http://pytorch.org/) (recent version)
* NLTK >= 3
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
#### Required Natural Language Tool Kit downloads:
`nltk.download('averaged_perceptron_tagger')` <br/>
`nltk.download('wordnet')` <br/>
#### Infersent Embedding Setup: <br/>
First, download GloVe embeddings as follows (~20 min): <br/>
`mkdir 'GloVe'`  <br/>
`curl -Lo 'GloVe/glove.840B.300d.zip' http://nlp.stanford.edu/data/glove.840B.300d.zip` <br/>
`unzip 'GloVe/glove.840B.300d.zip' -d 'GloVe/'` <br/>

Then, download Facebook Infersent Encoder as follows (~5 min): <br/>
`mkdir encoder` <br/>
`curl -Lo encoder/infersent1.pkl https://dl.fbaipublicfiles.com/infersent/infersent1.pkl`

## Examples from Demo
`sentence = "I tightened the bolt to make sure it didn't fall apart"` <br/>
`word = "bolt"`

`sentence = "The fast guy ran by in a bolt"` <br/>
`word = "bolt"`

`sentence = "The bolt during the thunderstorm shocked me"` <br/>
`word = "bolt"`

`sentence = "The current was too strong to swim against"` <br/>
`word = "current"`

`sentence = "The high current on the wire shocked me"` <br/>
`word = "current"`
