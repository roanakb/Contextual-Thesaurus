# Contextual-Thesaurus
[Demo Video](https://youtu.be/shRAcu3UCY4)
## Description
Uses Facebook Infersent embeddings to calculate which synset is correct for the given word and sentence.
Synsets are acquired using WordNet.
## Known Limitations
This method is extremely limited, and mostly a proof of concept.
It requires the context to be very explicit in the sentence, as can be seen in the example sentences below.
With further experimentation of word embeddings and classification methods, this may be improved.
## Setup
Required nltk downloads:<br/>
`nltk.download('averaged_perceptron_tagger')` <br/>
`nltk.download('wordnet')`
##Examples from Demo
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
##Dependencies
Specified in `requirements.txt`