#!/usr/bin/env python3

EOS = '<eos>'
UNK = '<unk>'

MODEL_FILENAME = 'model'
VOCAB_FILENAME = 'vocab.json'

# Ugly hardcoded hyperparameters
NUM_STEPS = 35 # truncated backprop length
#NUM_STEPS = 7
LEARNING_RATE = 0.0001
HIDDEN_SIZE = 1500 # layer size
