## GPT

GPT is a successfull neural network architecture for language models. It uses the ideas discussed in the Transformer paper. These are the neural network layers used in a GPT:

Assuming the models accepts a sentence of maximum N tokens:

1. The model gets N tokens as its input. A integer tensor of shape `[d]`
2. The tokens are mapped to d-dimensional numbers, given a lookup-table known as the embedding table. The output of this step is a floating-point tensor of shape `[n, d]`.
3. The output of step to goes through `l` multi-head attention layers, where:
    1. Each layer accepts a `[n, d]` tensor.
    2. The layer is normalized with a LayerNorm function and the result is another `[n, d]` tensor.
    3. The k, q and v vectors are calculated by multiplying the input tensor with three different `[d, h]` for that layer. The results are three `[n, h]` tensors.
    4. k (`[n, h]`) is multiplied with q^-1 (`[h, n]`) giving out a `[n, n]` tensor, telling us how related each word is with other words.
    5. The upper-triangle of the matrix is zeroed out, so that the tokens cannot cheat.
    6. A softmax layer is applied to convert the importance-matrix into a probability distribution. Now we have a `[n, n]` vector where sum of each row is 0.
    7. The result is then multiplied with the v vector, allowing the most important tokens to send their "message" to the next attention layers. The output is a `[n, h]` tensor.
    8. Multiple attention-heads with different parameters are applied giving us multiple `[n, h]` tensors. By putting them besides each other, we'll get a `[n, d]` tensor, which can be passed to the next layer.
