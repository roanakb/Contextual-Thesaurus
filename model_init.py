# Load model
import torch
from models import InferSent


def load_model():
    model_version = 1
    MODEL_PATH = "encoder/infersent%s.pkl" % model_version
    params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                    'pool_type': 'max', 'dpout_model': 0.0, 'version': model_version}
    model = InferSent(params_model)
    model.load_state_dict(torch.load(MODEL_PATH))

    W2V_PATH = 'GloVe/glove.840B.300d.txt'
    model.set_w2v_path(W2V_PATH)

    print('building vocab')
    model.build_vocab_k_words(K=100000)
    print('done building vocab')
    return model
