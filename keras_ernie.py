'''
@Description: 
@version: 
@Company: Thefair
@Author: Wang Yao
@Date: 2020-03-12 19:00:08
@LastEditors: Wang Yao
@LastEditTime: 2020-03-12 21:46:09
'''
import os
import tensorflow as tf
from keras_bert import load_trained_model_from_checkpoint
from paddle_to_tensor import check_exists
from paddle_to_tensor import convert_paddle_to_np
from paddle_to_tensor import save_tensor

    

def load_from_checkpoint(bert_path, trainable=False, training=False, seq_len=None, name='bert_layer'):
    
    check_exists(bert_path)

    bert_config_path = os.path.join(bert_path, 'bert_config.json')
    bert_checkpoint_path = os.path.join(bert_path, 'bert_model.ckpt')

    model = load_trained_model_from_checkpoint(
            bert_config_path, bert_checkpoint_path, training=training, seq_len=seq_len)
    
    model.name = name
        
    for layer in model.layers:
        layer.trainable = trainable
    
    return model


def checkpoint_loader(checkpoint_file):
    def _loader(name):
        return tf.train.load_variable(checkpoint_file, name)
    return _loader


if __name__ == "__main__":
    # convert_paddle_to_np()
    # save_tensor()
    # model = load_from_checkpoint("checkpoints")
    # print(model.name)
    loader = checkpoint_loader("checkpoints/bert_model.ckpt")
    loader("bert/embeddings/word_embeddings")