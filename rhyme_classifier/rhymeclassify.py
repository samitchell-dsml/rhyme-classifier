'''
--------------------------------------------------
RHYMECLASS: command line tool for determining 
whether two words rhyme.
--------------------------------------------------

Usage: rhymeclassify word1 word2
'''

import click
import os
import torch
from model.wordtensor import wordtensor
from model.neuralnetwork import NeuralNetwork
from torch import nn

@click.command()
@click.argument('word1')
@click.argument('word2')
def main(word1, word2):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    model = NeuralNetwork().to(device)
    model_path = os.path.join(os.path.dirname(__file__), 'model/model_weights.pth')
    model.load_state_dict(torch.load(model_path))
    model.eval()

    word_tensor1 = wordtensor(str(word1))
    word_tensor2 = wordtensor(str(word2))

    x = torch.cat((word_tensor1, word_tensor2),0)
    x = torch.reshape(x, (1,1716))
    logits = model(x)
    pred_prob = nn.Softmax(dim=1)(logits)
    y_pred = pred_prob.argmax(1)

    print(y_pred)

    if y_pred.data[0] == 0:
        answer = 'do not rhyme'
    else:
        answer = 'do rhyme'

    print(f'The words {word1} and {word2} {answer}.')

if __name__ == '__main__':
    main()