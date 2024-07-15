In order to make things simpler, let's just assume that our model accepts 5 tokens as input and gives out the next predicted token as output. Just like how we built a model that was able to learn MNIST and XOR, we can take the most naive approach and build a multi-layer-perceptron. But there is something really very wrong with this approach when trying to build something like a chatbot. Let me explain it to you with an example. Imagine the sentence you are going to process and predict its next word is something like this:

***"I'm called Keyvan, so my name is"***

The word "Keyvan" is a great example of a word that we most probably have not reserved an independent token for. If you take a large piece of english text and sort the words appearing in it by number of occurance, "Keyvan" is definitely not in the first 1000, but since a token-embedding should be able to decompose any word into a list of tokens, it's probable that the word Keyvan will be decomposed to "Key", "v" and "an".

Now, based on this, it's obvious that the next token that should appear after ***"I'm called Keyvan, so my name is"***, should be "Key". But, think about it, is a multi-layer-perceptron really able to efficiently learn to predict something like that? This is what the neural network have to do:

1. Ignore the fact the word "Key" has a meaning on its own.
2. Find the token/tokens that are related to the name of the person.
3. Copy those tokens one by one, and keep track of tokens it has already copied.

You can experiment it. Build a neural network as deep as you want. It will struggle to learn something as simple as that, very badly. 

The solution? Well, you can again try to get inspiration of how your own brain really works. When you try to recall the name of someone, your brain will start looking for very specific parts of your memory, your brain will stop caring about every other piece of your memory and will try to replicate the only parts of your knowledge that matter. In terms of a neural network that predicts the next word of a sentence, sometimes all you need is a look-up in the sentence and in that case, the neural network should be able to **dynamically** figure out the words that matter the most when predicting the next word. Without such mechanism, your neural network will give equal opportunity to all of the tokens in your sentence to participate in the prediction of the next token, and our neural networks are limited in size.

As a result of a research done in 2017, the researchers discovered a beautiful method for allowing neural networks to pick the most relevant pieces of data as the input goes through the model. They named it "Self-Attention" or "The Attention Mechanism". The title of their paper is also "Attention is all you need", and it really turned out that attention was all we needed! The idea is very brilliant:

Imagine you are in a room, full of people talking, and you want to ask some question from a friend...

