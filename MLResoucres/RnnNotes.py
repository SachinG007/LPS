RNN

Ht = tanh(WhhHt-1 + WxhXt)
##
rnn = RNN()
y = rnn.step(x) # x is an input vector, y is the RNN's output vector