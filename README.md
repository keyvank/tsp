# The Super Programmer
*Building software that run our world!*

(For discussions around the book, join the book's Discord server: [https://discord.gg/a3WExz7Uhc](https://discord.gg/a3WExz7Uhc)

## How to read

There is an online version here: [https://keyvan.me/tsp](https://keyvan.me/tsp)

If you prefer the PDF version, consider supporting me by buying it from [LeanPub](https://leanpub.com/tsp)! (WARN: The book is incomplete!)

Otherwise, you can compile it yourself (Make sure you have the `pandoc` package installed on your system):

```
git clone https://github.com/keyvank/tsp
cd tsp
make pdf
```

The output will be stored on `tsp.pdf`!

## About

I have recently started writing an unusual book discussing various topics in computer-science by implementing them from scratch! WARNING: TSP is still in a very draft stage!

The book consists of 6 chapters:

- ***Chapter 1*** is about cause-and-effect chains, and how we can exploit them to do computations for us. In this chapter, I teach the reader how a 8-bit computer can be built using bare transistors, and how we can build a digital circuit simulator and simulate the whole thing in a Python program
- ***Chapter 2*** is about processing and generating waves and signals. I go through the history of telecommunication, phonographs, telephones, and how waves and sounds can be stored on computers. I teach the reader how to generate raw wave samples in Python and route them to his computer speakers. I also teach the reader how to "hear" those waves by doing FFTs and etc. I will also explain how data can be stored in waves and will teach the reader to write an audio mo/demodulator in Python
- ***Chapter 3*** is about computer-generated visuals. I explain how colors are results of electromagnetic waves, how a human eye works, and the history of photography. I explain how images are stored on computers and how they can be generated. I also explain the ray-tracing and rasterization algorithms for rendering 3D images and provide a Python implementation of them.
- ***Chapter 4*** is about artificial intelligence. Like all other chapters, I start with some history, explain a bit about neurons and how they differ from static logic-gates (Like AND/OR/NOT/...), I'll explain how a mathematical model for a neuron can help us to invent the backpropagation learning algorithm, and I'll end up explaining and implementing (In Python) all different deep-learning layers needed for implementing a large-language-model, which is of the most exciting AI models one can implement.
- ***Chapter 5*** is about cryptography and blockchains. Again some history, and then I'll explain finite-field mathematics, elliptic-curve cryptography, cryptographic hash functions, etc. I'll then explain how all these can be used for implementing an electronic cash system (Bitcoin!). I'll finish the chapter explaining how you prove correct execution of arbitrary programs through ZK proofs. (All in Python)
- ***Chapter 6*** is about interactions between the digital and physical world. I start with explaining the missing parts of chapter-1, which is electronics. I explain how an electronic circuit simulator can be built by implementing a solver that can solve a system of differential equations, and then I will use that simulator to implement oscillators and etc. I'll also teach the reader some mechanical physics, and how we can implement physics engines. I'll use the physics engine for simulating a rocket that can take a man on the moon.

## Support!

If you enjoy what I'm writing and would like to support my work, I would appreciate crypto donations! I attempted to distribute my work through computer programming publishers, but the consensus is that these kinds of tutorials won't sell well. Therefore, I have decided to continue TSP as an open-source hobby project!

- Bitcoin: `bc1qjvcsjt57des7j4runchxalksueqlxgadx7fwll`
- Ethereum: `0x1a34a6763f55887444ffbd8f8d4fae8197478675`

Feel free to submit your shiny PRs bacause I think I will allow anyone to contribute!
