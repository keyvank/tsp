\pagebreak

# The Super Programmer

## Preface

The book you are going to read is the result exploring different areas in computer science for more than 15 years. The idea of writing a book like this began around 8 years ago, when I was around 17 years old. That time, I was mostly focused on learning computer graphics and 3D rendering algorithm. The idea of generating 3D images by calculating the RGB values of the pixels was so interesting to me, that made me want to teach it to every programmer I knew. Unfortunately, not every programmer I knew was interested to learn low-level stuff like this, so instead of trying to teach what I learnt, I decided to write a book for it. I was sure I will have audience for it, there are lots of nerd programmers around the world who are thirsty to learn something more than web-applications.

So, I started to write that book, named it "Programming the Visuals", and I remember I made a lot of progress! Not sure what exactly happened, but I got a bit discouraged after finding it hard to fill a book with content. I found myself explaining everything I wanted to explain in less than 40 pages, and well 40 pages is not enough for a technical book. I didn't want to litter my book with all the details of different rendering algorithms. I just wanted to explain the core idea, in very simple words and with easy-to-understand code examples. My goal in my book was to introduce this very specific field of computer science to people, hoping that they will get encouraged enough to learn anything else they'll need by themselves.

My computer graphics book remained untouched for years, during which I took a bachelor's degree in computer engineering and did deep dives into other interesting fields of computer science too. University was one of the places in which I got clues on what to learn next. In fact, I didn't learn much in the university, because contrary to what many people say, university professors do not really get deep in what they teach. They will tell you a lot of headlines, but they'll never get deep in any of them. And that makes sense too, you can't expect to get super deep in everything in a relatively short period of time. Chances are you will get specialized knowledge in only one of the fields of computer science.

The fact that you can only get successful by getting deep in only one of the many fields of computer science didn't stopped me from learning them. After getting comfortable with generating pixels, I started to learn building computers, operating-systems, and all of the low-level stuff many programmers avoid to learn. Unfortunately, being a really talented hardware engineer doesn't necessarily mean you are also good in some of the topics which are normally known by physicists and electrical engineers, and those topics are still vital in developing many fascinating forms of software. So I thaught myself generating waves, signals and sounds and tried to understand how can I transfer data through them. After the advent of LLMs, and AI driven image-generation models, I also got convinced that that's the next thing I should get deep in. So I developed deep-learning libraries from scratch and built language-models on top of them.

I transformed myself from a day-to-day web-developer into a programmer that knows ***the starting point*** of building any kind of technology and hopefully can help getting the progress of technology back on track, in case a catastrophic event happens on Earth and all we have is gone.

After boosting my knowledge by learning all those stuff, I felt that it's the time to extend my 40-page computer graphics book, and the result is this book!

\pagebreak

## Intro

Legos were my favorite toys as a kindergarten student. It was one of the only toys I could use to build stuff that didn't exist before. It let me bring my imaginations into the real world, and nothing satisfies a curious mind more than the ability to build unique structures out of simple pieces.

I have a cousin, who was really into electronics on that time (Now he is doing medicine!). He had a friend who worked in an electronics shop and he used to bring me there, where we could buy and solder DIY electronics kits together, for the sake of fun. Years later, seeing my cousin building robots by typing some characters on the screen and "programming" it into something he called a "microcontroller", triggered the same parts in my brain, as playing with lego pieces. I didn't know the English alphabet those days, so I was just seeing different symbols coming on the screen after every keystrokes. The fact that certain ordering of some symbols could cause some kind of unique behavior was blowing my mind. I would copy/paste the codes on my cousin's book on his computer for free, just to see that a behavior emerges when I put some kind of "cheat-code" on his computer. I began to appreciate the power of characters. Characters were my new lego pieces, but there was an important difference, it was impossible to run out of characters. I could literally use billions of them to build different behaviors.

After around 20 years, I still get super excited when I build something I find magnificent by putting the right symbols in the right order. I was curious enough to study and deeply understand many applications of computers that have made significant impact in our everyday life but nobody gives them the attention they deserve these days, so I decided to gather all these information in one place and write this book.

When I started writing this book, I was expecting it to be a merely technical book with a lot of codes included, targetting only programmers as its audience, but I ended up writing a lot of history, philosophy and even human anatomy! So the book could be a good read for non-programmers too!

The Super Programmer is all about ideas, and how they have evolved through time, leading to the impressive technology we have today. I wanted this book to have least dependency to technologies, so that the codes do not get obsolete over time. I first thought of writing the codes in some pseudo-coding language, but I personally believe that pseudo-codes are not coherent enough, so I decided to choose and stick with a popular language like Python, which as of today, is a programming language that is known by many other engineers and scientists.

Throughout this book, I’m going to show you the inspirations that human beings got from the nature, in order to build technology. Humans themselves have always been a great  source of inspiration for building tech. You are going to read the phrase “The Creator” in this book a lot of times. The Creator can have different meanings for different people. Religious people may interpret it as God, and people with materialistic views may interpret it as the nature and the process of evolution. Either way, there is no doubt that there has been immense amount of intelligence behind the mind who/which created life. Engineering ideas that The Creator used to build life has been a great source of inspiration for the technology we have today. In many parts of the book, we are going to put our feet into The Creator's shoe and try to understand what has been going in its/his mind when engineering us.

## Who is this book for?

This book is for curious people who are eager to learn some of the most fundamental topics of computer and software engineering. The topics presented in this books, although very interesting in opinion, are some of the most underrated and least discussed fields of computer programming. This book is about the old technology, the technology we are using everyday, but we refuse to learn and extend as an average engineer. The literature around each of those topics is so large that, only specialists will ever be motivated to learn them.

The Super Programmer is for the programmers who don't want to limit their knowledge and skills on a very narrow area of software engineering. The Super Programmer is for programmers who can't sleep at night when they don't exactly understand how something in their computer works.

There is a famous quote, attributed to Albert Einstein, which says: 'You do not really understand something unless you can explain it to your grandmother.'. Not only I emphasize on this quote, I would like to extend this quote and claim that, you don't understand something unless you can explain it to your computer. Computers are dumb. You have to explain them every little detail, and you can't skip anything. If you are able to describe a something to a computer in a way that it can correctly simulate it, then you surely understand that thing!

Computers give you the ability to test and experiment stuff without actually owning the physical version of them. You can literally simulate an atomic bomb in your computer and throw it in your imaginary world to see what happens. You can simulate a rocket that travels to Mars, as a tiny step, towards your dream of opening a space company. You can describe a 3D environment, and try to understand how it feels to be there, by putting your imaginary eyes in there and calculating what it will perceive, as a computer image. Computers let you to experiment anything you can ever imagine without spending anything other than some of your time and talent.

The Super Programmer is going to show you "what can be done", and not "how can be done". You are not going to learn data-structure and algorithms here, but you are going to learn how you can embrace your creativity by using simple tools you already know. Thus in many parts of this book, we are going to apply the simplest and least-efficient solutions possible, because it's a better way to learn new things.

Some might argue that not all software engineers will ever need to learn any of the topics taught in this book. That's partially true. As an average programmer, you are not going to use any of these knowledge in your everyday work. Even if you do, you are probably not going to get creative and make anything substantially new out of them. Since the book is about the old technology, most of the topics discussed in this book are already studied and developed as much as they could be.

So why are we doing this? There are several reasons:

- You can use the problem-solving strategies and patterns you learn in this book in your everyday job too!
- The book allows you walk through the entire world-map of technology, and when you do this, nothing will be able scare you. 
- It's fun!

## How to make the most of this book?

The book is divided into 5 chapters. We will start by explaining the beauty of cause-and-effect chains, and how we can build useful and interesting structures by connecting simple lego pieces together. We will go through the history of transistors, how they work, and how we can simulate them using plain Python code. We will implement different logic gates by connecting transistors together, and will proceed to building more complicated circuits like adders, counters and finally, programmable computers. After building our super simple computer, we'll try to put a soul in it. We will introduce the Brainfuck programming language and how it can be compiled for our computer, and will try to design and implement impressibely complicated programs using this simple language.

In chapter 2 and 3, we'll discuss two of the most important human senses, the sense of hearing and vision. We will start with some history, explaining how how humans invented ways to record what they see or hear, as photos or tapes, and experience them later. Then we will see how the digital revolution changed the way we record and store media forever. We'll get deep on very simple computer file formats used for storing images and audio, and will try to generate them ourselves. We will learn how to please our ears and eyes by generating a bunch of bytes.

Chapter 4 is all about the cool parts of artificial intelligence. We will discuss how biological neurons are similar to tunable electronic gates, and how we can use calculus and differentiations to tune these gates. We will try to build a library for training neural networks by differentiating computation graphs. We will learn and implement some of the most import operations used in neural-network models that can understand language, and will try to implement a language model ourselves.

Chapter 5 is about how people can use math for bringing trust into their wild digital world. We will start by learning the history of cryptography, and how people can encrypt and sign digital documents with their digital identities. We will discuss the electronic-cash revolution and see how math can help us to save ourselves from the evil and escape some of the limitations governments put on us. We will discuss ways we can convincingly prove people that we know something, without revealing it, and see how we can use these methods for building truly private cryptocurrencies.

The last chapter is all about ways comptuers and software can get a physical body and have physical interactions with the world sorrounding us. We will discuss multiple topics in Physics, including classical mechanics and how we can use it in order to simulate our world in our computers, or build machines that can send humans on Mars by analyzing and exploiting those laws. We will also get deeper in Electronics, the giant beast that many computer-engineers (Even the good ones) are unable to fully understand, although it is the fundamental building block of computers. Like all other chapters, our approach is to build physics engines and circuit simulators in order to fully understand the concept.


Without a doubt, people love things they have built on their own more than anything else. If you are planning to implement the codes in this book on your own, I suggest you to do it in a programming language other than Python. Writing the codes in Python might make you feel you are not doing anything new, and you may really end up copying and pasting what you read in the book. On the other hand, by rewriting all the logic in another language, you will force yourself to translate what you are reading, leading to a much deeper understanding of what is happening. It will also give you the feeling of creating something new, increasing your dopamine levels and motivation!

## What do I need to know?

As previously noted, although the book is about ideas and not the implementations, and I didn't want to make the content in this book dependant on a specific programming language, I still chose to write the codes in a real programming language instead of using pseudo-codes. Pseudo-codes assume that the reader is a human and does not have the coherency of a real programming language, which is what we care in this book.

I found Python programming language a good choice, since it's the first (Or second?) most popular language among all the developers in the world. I thought Python is the English language of the programmer community. Python isn't the right choice for implementing many of the topics we are discussing in this book (Since efficiency is very important in most of them), but it's one of the easiest languages you can use for prototyping things and learning the concepts.

Therefore you will need to know the basics of Python programming. Some knowledge of *NIX operating systems can become handy in some parts of the book.

## How did I write this book?

As someone who had never written a book before, I found the process very unclear. I wasn't sure what text-editing software/format I should use for easier conversion to other formats. I had to add a lot of code-snippets and math equations in my book, so clearly Microsoft Word wasn't the most convenient option (At least I wasn't sure how can I do it efficiently with a word-processor like Microsoft Office). Besides that, I am personally not a fan of LaTeX. I find the syntax hard and I wasn't really willing to learn LaTeX and I wanted to put my focus on writing the actual text instead. My choice was Markdown language. It is very easy to use and there are plenty of software out there which I can use for converting a `.md` file to `.html`, `.pdf`, `.tex` and etc. Also, in case I needed to perform some costum, automated transformations on my text, Markdown is one of the easiest languages to parse and generate!

I wrote different chapters in separate `.md` files, and then I wrote a `Makefile` to concatenate all of them in a single `.pdf` file. I then used a Linux program named `pandoc` for doing so.

Here is how my `Makefile` script looked like:

```Makefile
pdf:
	pandoc --toc --output=out.pdf *.md # Convert MD files to a PDF file
	pdfunite cover.pdf out.pdf tsp.pdf # Add the book cover
	pdftotext tsp.pdf - | wc -w # Show me the word-cound
```

The `--toc` flag generated the Table of Contents section for me automatically (Based on Markdown headers: `#`, `##`, ...), and I also had another `.pdf` file containing the cover of my book, which I concatenated with the pandoc's output. I was tracking my process by word-count.