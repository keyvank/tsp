In order to make things simpler, let's just assume that our model accepts 5 tokens as input and gives out the next predicted token as output. Just like how we built a model that was able to learn MNIST and XOR, we can take the most naive approach and build a multi-layer-perceptron. But there is something really very wrong with this approach when trying to build something like a chatbot. Let me explain it to you with an example. Imagine the sentence you are going to process and predict its next word is something like this:

***"I'm called Keyvan, so my name is"***

The word "Keyvan" is a great example of a word that we most probably have not reserved an independent token for. If you take a large piece of english text and sort the words appearing in it by number of occurance, "Keyvan" is definitely not in the first 1000, but since a token-embedding should be able to decompose any word into a list of tokens, it's probable that the word Keyvan will be decomposed to "Key", "v" and "an".

Now, based on this, it's obvious that the next token that should appear after ***"I'm called Keyvan, so my name is"***, should be "Key". But, think about it, is a multi-layer-perceptron really able to efficiently learn to predict something like that? This is what the neural network have to do:

1. Ignore the fact the word "Key" has a meaning on its own.
2. Find the token/tokens that are related to the name of the person.
3. Copy those tokens one by one, and keep track of tokens it has already copied.

You can experiment it. Build a neural network as deep as you want. It will struggle to learn something as simple as that, very badly. 

The solution? Well, you can again try to get inspiration of how your own brain really works. When you try to recall the name of someone, your brain will start looking for very specific parts of your memory, your brain will stop caring about every other piece of your memory and will try to replicate the only parts of your knowledge that matter. In terms of a neural network that predicts the next word of a sentence, sometimes all you need is a look-up in the sentence and in that case, the neural network should be able to **dynamically** figure out the words that matter the most when predicting the next word. Without such mechanism, your neural network will give equal opportunity to all of the tokens in your sentence to participate in the prediction of the next token, and our neural networks are limited in size.

As a result of a research done in 2017, the researchers discovered a beautiful method for allowing neural networks to pick the most relevant pieces of data as the input goes through the model. They named it "Self-Attention" or "The Attention Mechanism", or "The Transformer Architecture". The title of their paper is also "Attention is all you need", and it really turned out that attention was all we needed! The idea is very brilliant:

Imagine you are in a room, full of people talking, and you want to ask some question from a friend...

## The non-trivial gate, XOR

## A non-trivial way to search

The Transformer model tries to emulate some kind of database within a neural network, but before trying to play with neurons, let's discuss the non-neural-network version of it:

```python=
import math

database = [
    ([0.52, 0.78, 0.69], [0.29, 0.51, 0.17]),
    ([0.45, 0.54, 0.12], [0.63, 0.49, 0.91]),
    ([0.14, 0.59, 0.53], [0.52, 0.46, 0.25]),
    ([0.79, 0.96, 0.91], [0.32, 0.32, 0.17]),
    ([0.01, 0.73, 0.69], [0.68, 0.73, 0.75]),
]

keys = [k for k, _ in database]
values = [v for _, v in database]


def closeness(a, b):
    eps = 1e-5
    ret = 0
    for x, y in zip(a, b):
        ret += (x - y) ** 2
    return 1 / (math.sqrt(ret) + 1e-5)


def softmax(inp):
    max_x = max(inp)
    e_x = [math.exp(x - max_x) for x in inp]
    sum_e_x = sum(e_x)
    return [x / sum_e_x for x in e_x]


to_find = [0.79, 0.96, 0.91]
dists = softmax([closeness(k, to_find) for k in keys])

res = [0, 0, 0]
for k, v in zip(dists, values):
    for i in range(3):
        res[i] += k * v[i]

print(res)
```

The difference between this creative way of searching, and a regular search is very similar to the difference between a neuron, and a logic gate. One of them is differentiable, and the other is not!

-----

A hard, solid piece of rock is a creature that perhaps doesn't experience any of the human feelings. A rock doesn't fall in love, or become happy or sad. A rock will experience no pain, doesn't need to breath and eat to survive, you might think that a rock has a wonderful life (And in some ways, it has).

A rock's luckiness perhaps partly comes back to the fact that it has a fairly simple structure. If you study the molecular structure of a rock, you will see that a rock is built of a limited set of atoms, orderly placed along each other, which makes it a very hard break. A human being on the other hand has a much more complicated structure, and we can't see the perfect atomical ordering of a rock in a human body too. While a rock has a wonderful life, its life is very boring (From the viewpoint of an observer), a human life on the other hand, despite having sadness, pain and suffer, is much more interesting and worth living. Nature's goal has never been to build a long-lasting life, without any happiness and pain like a rock, but to build a life that maximizes ***interestigness***.

You might now already know that I'm going to talk about one of the most interesting laws of physics, the second law of thermodynamics. This law was first discovered by Sadi Carnot, the french Physicist, who discovered that you can't build a motor engine that is able to convert 100% of the heat energy into mechanical work, and some of the energy will always be wasted. In other words, there is a efficiency limit in a system that converts heat into mechanical work. The same law can be expressed in other ways too, for example, you can't build a refrigerator (Or an air conditioner) that is able to decrease the temperature of a closed area, without disposing a higher heat (Higher than the amount reduced in the closed area) outside that area.

Heat is some kind of chaos and disorder in atoms. When atoms take energy, they start to move in directions in a chaotic way. The more they move, the hotter they become. We can measure how chaotic the elements of a system (E.g. the atoms inside a closed area) are, and call it the Entropy of that system.

Given the definition of Entropy, we can redefine the second law of thermodynamics in another words: ***The entropy of the universe always increases.*** I.e the sum of disordered-ness of all elements in our universe always gets higher, which again means, I can't decrease the heat in my room in a sunny day without generating even more heat into the universe. You might now think that we are making the earth warmer by building air conditioners, but the truth is the heat is radiated into the universe!

## Maybe?

- See - Pattern recognition in images
- Build - C compiler