# The Super Programmer

## Existential Rambling

***February 16th, 2024***

OpenAI, the legendary AI company of our time, has just released their new product, Sora, an AI model capable of generating one minute of mind-blowingly high-quality video content given a text prompt. I’m scrolling through Twitter, watching the sample outputs, feeling extremely jealous of those who have had the opportunity to contribute to building it, and I also feel a bit of emptiness. I’m thinking about how this would affect the video industry and Hollywood. How many people’s work will become meaningless just after this? And for me, there is also a disturbing question:

Does it make any sense for me to write this book at all? If a machine is able to generate convincingly real videos, how hard would it be for it to write a tutorial book like this? Why would I put any effort in if anyone is able to generate their customized masterpiece in seconds?

I know this will happen someday, and I'm not against it. I truly appreciate the fact that I was born in an era when the AI revolution is happening. AI will someday be able to generate better content than we can, and many of our efforts will simply become unnecessary. In my opinion, that future is not far off.

Anyway, my temporary existential crisis in this moment made me immediately pick up my phone and express my heartbreak and sadness in the very first section of this book. Perhaps this is the only way I could convince myself to continue writing a book: by pouring some real human soul into it.

***February 25th, 2024***

A few days have passed, and I rarely see people talking about Sora. It’s starting to become normal, I guess. People who were excited at first are now finding Sora boring. I just realized there is something called “Hedonic Adaptation.” It argues that humans will always return to a stable level of happiness, despite positive or negative changes in their lives. This happens with the advancement of technology all the time. At first, we are all like "woah," and after some time, everything already gets boring. Although this may seem unfair, it drives us humans to progress because, you know, being stuck is boring.

I can’t imagine how many "woah" moments humans have had throughout history. Things we have in our hands right now seem like miracles for people living 300 years ago, but in our days, old technology seems basic and trivial.

I really hope this book will be able to fulfill its purpose: to make the interested reader appreciate what it took for us to reach this level of advancement in the computer-driven technology.

## Preface

The book you're about to read is the result of exploring various areas in computer science for over 15 years. The idea of writing this book began around 8 years ago when I was a high-school student, getting ready for college. At that time, my focus was on learning computer graphics and 3D rendering algorithms. The idea of generating 3D images by manually calculating the raw RGB values of pixels intrigued me, and I'm the kind of person who wants to teach everyone the exciting things I have learned. Unfortunately, not everyone I knew at that time was interested in learning low-level stuff like this. Instead of trying to teach what I had learned, I decided to write a book. I was confident I'd have an audience, as many programmers worldwide are eager to learn more than just web-application development (a common career path among software engineers).

So, I started writing the book, named it "Programming the Visuals," and made a lot of progress! Not sure what happened exactly, but I got a bit discouraged after finding it hard to fill a book with content. I found myself explaining everything I wanted to explain in less than 40 pages, and well, 40 pages are not enough for a technical book. I didn't want to clutter my book with all the details of different rendering algorithms. I just wanted to explain the ***core idea***, in very simple words and with easy-to-understand code examples. My goal was to introduce this specific field of computer science to people, hoping they would get encouraged enough to learn anything else they'd need by themselves.

My computer graphics book remained untouched for years, during which I took a bachelor's degree in computer engineering and started to learn about other interesting fields of computer science. University was one of the places where I got clues on what I have to learn next, although I have to admit, most of my knowledge was gained by surfing around the internet and trying to make sense of things by myself. University professors do not really get deep into what they teach (Unless you are from a top-notch university, I'm not talking about the exceptions). University courses though will give you a lot of headlines that you'll have to get deeper in them all by yourself, and that makes sense too; you can't expect to get outstandingly good in everything in a relatively short period of time. Chances are you will get specialized knowledge in only one of the fields of computer science.

The fact that success often comes from getting deep in only one of the many fields of computer science didn't stop me from learning them (It did take a long time though). After getting comfortable with generating pixels, I started to learn about building computers from bare transistors, writing software that can compose/decompose sounds, crafting neural networks from scratch, implementing advanced cryptographic protocols, rolling out my own hobby operating system, and all kind of the nerdy things the average software developer, avoids learning (Or just have not had the opportunity to do so). 

The result? I transformed myself from an average programmer who could only build web-applications into a programmer that knows ***the starting point of building any kind of computer software*** and hopefully can help get the progress of computer-related technology back on track in case a catastrophic event happens on Earth and all we have is gone (This is something that I think about a lot!).

After expanding my knowledge by learning all these new concepts, I felt it was time to extend my 40-page computer graphics book into a more comprehensive work, covering additional fundamental topics. The result is the book you're reading now!

## Support

If you enjoy what I'm writing and would like to support my work, I would appreciate crypto donations! I attempted to distribute my work through computer programming publishers, but the consensus was that tutorials covering a wide range of unrelated topics wouldn't sell well. Therefore, I have decided to continue TSP as an open-source hobby project!

- Bitcoin: `bc1qjvcsjt57des7j4runchxalksueqlxgadx7fwll`
- Ethereum: `0x1a34a6763f55887444ffbd8f8d4fae8197478675`

Also, I'm thinking of allowing anyone to contribute in writing and editing of this book, so feel free to submit your shiny PRs!

GitHub: [https://github.com/keyvank/tsp](https://github.com/keyvank/tsp)

## Intro

Legos were my favorite toys as a kindergarten student. They were one of the only toys I could use to build things that didn't exist before. They allowed me to bring my imagination into the real world, and nothing satisfies a curious mind more than the ability to build unique structures out of simple pieces. As I grew up, my inner child's desire to create took a more serious direction.

My journey into the fascinating world of computer programming began around 20 years ago, when I didn't even know the English alphabet. I had a cousin who was really into electronics at that time (surprisingly, he is in medicine now!). He had a friend who worked in an electronics shop, and he used to bring me there. We would buy and solder DIY electronics kits together for fun. Although I often heard the term "programming" from him, I had no idea what it meant until one day when I saw my cousin building the "brain" of a robot by typing characters on a screen and programming something he called a "microcontroller". The process triggered the same parts of my brain as playing with Lego pieces.

I didn't know the English alphabet then, so I just saw different symbols appearing on the screen with each keystroke. The idea that certain arrangements of symbols could cause unique behaviors in the robot he was building, just blew my mind. I would copy and paste codes from my cousin's programming-tutorial book onto his computer just to see the behaviors emerge when I input some kind of "cheat-code". ***I began to appreciate the power of characters***. Characters became my new Lego pieces, but there was an important difference: it was impossible to run out of characters. I could literally use billions of them to build different behaviors.

After around 20 years, I still get super excited when I build something I find magnificent by putting the right symbols in the right order. I was curious enough to study and deeply understand many applications of computers that have made significant impact in our everyday life but nobody gives them the attention they deserve these days, so I decided to gather all these information in one place and write this book.

When I started writing this book, I was expecting it to be a merely technical book with a lot of codes included, targeting only programmers as its audience, but I ended up writing a lot of history, philosophy and even human anatomy! So the book could be a good read for non-programmers too! That said, I should warn you: it’s crucial to have some programming knowledge to fully appreciate and understand the content!

The Super Programmer is all about ideas, and how they have evolved through time, leading to the impressive technology we have today. I wanted this book to have least dependency to technologies, so that the codes do not get obsolete over time. I first thought of writing the codes in some pseudo-coding language, but I personally believe that pseudo-codes are not coherent enough, so I decided to choose and stick with a popular language like Python, which as of today, is a programming language that is known by many other engineers and scientists.

## Who is this book for?

This book is for curious people who are eager to learn some of the most fundamental topics of computer and software engineering. The topics presented in this books, although very interesting in opinion, are some of the most underrated and least discussed fields of computer programming. This book is about the old technology, the technology we are using everyday, but we refuse to learn and extend as an average engineer. The literature around each of those topics is so large that, only specialists will ever be motivated to learn them.

The Super Programmer is for the programmers who don't want to limit their knowledge and skills on a very narrow area of software engineering. The Super Programmer is for programmers who can't sleep at night when they don't exactly understand how something in their computer works.

There is a famous quote, attributed to Albert Einstein, which says: 'You do not really understand something unless you can explain it to your grandmother.'. Not only I emphasize on this quote, I would like to extend this quote and claim that, you don't understand something unless you can explain it to your computer. Computers are dumb. You have to explain them every little detail, and you can't skip anything. If you are able to describe a something to a computer in a way that it can correctly simulate it, then you surely understand that thing!

Computers give you the ability to test and experiment stuff without actually owning the physical version of them. You can literally simulate an atomic bomb in your computer and throw it in your imaginary world to see what happens. You can simulate a rocket that travels to Mars, as a tiny step, towards your dream of opening a space company. You can describe a 3D environment, and try to understand how it feels to be there, by putting your imaginary eyes in there and calculating what it will perceive, as a computer image. Computers let you to experiment anything you can ever imagine without spending anything other than some of your time and talent.

The Super Programmer is going to show you "what can be done", and not "how can be done". You are not going to learn data-structure and algorithms here, but you are going to learn how you can embrace your creativity by using simple tools you already know. Thus in many parts of this book, we are going to apply the simplest and least-efficient solutions possible, because it's a better way to learn new things.

Some might argue that not all software engineers will ever need to learn any of the topics taught in this book. That's partially true. As an average programmer, you are not going to use any of these knowledge in your everyday work. Even if you do, you are probably not going to get creative and make anything substantially new out of them. Since the book is about the old technology, most of the topics discussed in this book are already studied and developed as much as they could be.

So why are we doing this? There are several reasons:

- The problem-solving strategies and patterns you’ll learn in this book can be applied directly to your everyday work!
- This book takes you on a journey through the entire landscape of technology, and by the end, nothing will feel intimidating.
- And most importantly, it’s fun!"

## First Principle Thinking

The Super Programmer is all about reinventing the wheel. Reinventing the wheel is considered a bad practice by many professionals, and they are somehow right. Reinventing the wheel not only steals your focus from the actual problem you are going to solve, but also there is a very high chance you will end up with a wheel that is much worse than wheels already made by other people. There have been people working on wheels for a very long time, and you just can't beat them with their pile of experience.
Reinventing the wheel can be beneficial in two scenarios:

1. Learning: If you want to learn how a wheel works, build it yourself, there isn't a shortcut.
2. Full control: If wheels are crucial part of the solution you are proposing for a problem, you may want to build the wheels yourself. Customizing your own design is much easier than customizing someone else’s work.

If you want to build a car that outperforms every other on the market, you won’t settle for tweaking existing engines. You’ll need to design one yourself. Otherwise, you’ll only end up with something that is only 'slightly better', and 'slightly better' isn’t enough to convince anyone to choose your car over a trusted brand.

Reinventing the wheel is a form of ***First Principle Thinking***. This approach involves questioning all your assumptions and building solutions from the ground up by reassembling the most fundamental truths: the first principles.

First principle thinking is a crucial trait that sets successful people apart. It gives you more control over the problems you're solving because it allows you to think beyond conventional solutions.

Consider an extraordinary chef. He doesn't just know how to cook different dishes; he understands the raw ingredients, their flavors, and how they interact. He knows the "first principles" of cooking. This deep understanding enables him to create entirely new dishes—something a typical cook can’t do.

I hope I've made my point clear. With The Super Programmer, you'll gain all the ingredients you need to craft your own brilliant software recipes!

## Computer Revolution

Believe it or not, the world has become far more complex than it was 500 years ago. We live in an era where specializing in a narrow, specific field of science can take a lifetime. With billions of people in the world, it’s nearly impossible to come up with an idea that no one has ever thought of before. In many ways, innovation has become less accessible. There are several reasons for this:

1. ***We are afraid to innovate.*** Five hundred years ago, people didn’t have daily exposure to tech celebrities or compare themselves to others. They weren’t afraid of creating something unique, no matter how imperfect. They didn’t worry about “mimicking” or being outdone. They simply kept their creativity flowing, making, writing, and painting—without fear of comparison. This is why their work was often so original, unique, and special.

2. ***We don't know where to start.*** Back then, it was possible for someone to learn almost everything. There were polymaths—people who could paint, write poetry, design calendars, expand mathematics, engage in philosophy, and cure ailments, all at once. Famous examples include the Iranian philosopher and mathematician Omar Khayyam and the Italian Renaissance genius Leonardo Da Vinci. Today, however, the vast amount of knowledge being produced makes it impossible for anyone to be a true polymath. This doesn't mean humanity has declined; rather, the sheer volume of knowledge is overwhelming, making it hard to know where to focus or even begin.

This complexity leads to confusion. Ironically, if you asked someone from 100 years ago to design and build a car for you, they might be more likely to succeed than someone today. Early cars were simpler, and this simplicity gave people the confidence to guess how things worked and experiment. In contrast, in our era, guessing how something works often feels like the wrong approach.

The computer software revolution changed the "creativity industry". Programming was one of the first forms of engineering that required very little to get started. You don’t need a huge workshop or an extensive understanding of physics to create great software. You won’t run out of materials because software is made of something you can never run out of: ***characters***! All you need is a computer and a text editor to bring your ideas to life. Unlike building physical objects, in the world of programming, you know exactly what the first step is!

```
> Hello World!
```

## Synchronous vs Asynchronous Engineering

As someone who has only created software and never built anything sophisticated in the physical world, I find engineering physical objects much more challenging than developing computer programs.

I’ve often heard claims that software engineering is fundamentally different from other, more traditional fields of engineering like mechanical or electrical engineering. However, after talking with people who build non-software systems, I’ve come to realize they also find software development difficult and non-trivial.

After some reflection, I decided to categorize engineering into two broad fields: ***Synchronous*** vs ***Asynchronous***.

Synchronous engineering involves designing solutions based on orderly, step-by-step subsolutions. A classic example of this is software engineering. When building a program, you arrange instructions (sub-solutions) in a specific sequence, assuming each instruction will work as expected. Similarly, designing a manufacturing line follows this approach—new subsolutions don’t interfere with the existing ones. You can add new steps or components without affecting the previous ones, and the system remains intact.

On the other hand, asynchronous engineering doesn’t follow a fixed order. The final solution is still composed of subsolutions, but these subsolutions operate simultaneously rather than sequentially. Examples include designing a building, a car engine, or an electronic circuit. In these fields, you must have a comprehensive understanding of how all the parts fit together, because changes in one area can disrupt the entire system. Adding a new component can break existing elements, unlike in software, where changes often don’t have the same kind of direct impact.

The Super Programmer aims to turn you into an engineer capable of building synchronous systems!

## A quick glance at the chapters

The book is divided into five chapters, each designed to build upon the last, guiding you from foundational concepts to more complex ideas.

We begin by exploring the beauty of cause-and-effect chains, demonstrating how simple building blocks—like Lego pieces—can come together to form useful and intriguing structures. We'll dive into the history of transistors, how they work, and how we can simulate them using plain Python code. From there, we’ll implement basic logic gates by connecting transistors, and progressively build more complex circuits such as adders, counters, and eventually, a simple programmable computer. After constructing our computer, we’ll try to give it a "soul" by introducing the Brainfuck programming language. You’ll learn how to compile this minimalistic language for our computer and design impressively complex programs using it.

In the 2nd and 3rd chapters, we explore two of the most important human senses: hearing and vision. We’ll begin by examining the history of how humans invented methods to record visual and auditory information—through photos and tapes—and experience them later. We’ll then explore how the digital revolution forever changed the way we record and store media. By delving into simple computer file formats for images and audio, we’ll even create our own files. You'll learn how to generate data that can "please" both our ears and eyes.

Chapter 4 takes us into the fascinating world of artificial intelligence. We’ll draw parallels between biological neurons and tunable electronic gates, exploring how calculus and differentiation can be used to "train" these gates. You’ll gain hands-on experience by building a library for training neural networks via differentiating computation graphs. We’ll then explore some of the most important operations in neural-network models that understand language, and you’ll have the opportunity to implement your own basic language model.

In Chapter 5, we shift focus to how mathematics is used to bring trust into the digital world. We’ll begin by studying the history of cryptography and how digital documents are encrypted and signed using digital identities. We’ll examine the electronic-cash revolution and how math can protect us from malfeasance and help us navigate around government restrictions. You’ll learn how to prove knowledge without revealing the underlying information—an important concept for building truly private cryptocurrencies.

The final chapter is all about how computers and software can interact with the physical world. We’ll dive into physics, specifically classical mechanics, and explore how these laws can be used to simulate the world in our computers or to design machines capable of sending humans to Mars. We’ll also take a deep dive into electronics—the often-underestimated field that underpins modern computing. Many computer engineers, even the best ones, struggle to fully understand electronics, but it’s essential to grasp it in order to build effective systems. Throughout this chapter, we’ll use physics engines and circuit simulators to solidify these concepts.

## What do I need to know?

As mentioned earlier, while this book focuses on concepts rather than specific implementations, I chose to write the code in a real programming language instead of using pseudocode. Pseudocode assumes that the reader is human and lacks the structural coherence of an actual programming language, which is crucial for the types of ideas we explore here.

I found Python to be a great choice, as it is one of the most popular languages among developers worldwide. I think of Python as the "English" of the programming community—easy to understand and write. While Python may not always be the most efficient language for the topics covered in this book, it is one of the easiest to use for prototyping and learning new concepts.

That said, you'll need to be familiar with the basics of Python. Some knowledge of *NIX-based operating systems may also be helpful in certain sections of the book.

Without a doubt, people are more invested in things they’ve built themselves. If you plan to implement the code in this book, I highly recommend doing it in a programming language other than Python. While Python is an excellent tool, using it might make you feel like you’re not doing anything new—you may end up just copying and pasting what you read in the book. On the other hand, rewriting the logic in another language forces you to deeply translate the concepts you’ve learned, leading to a better understanding of what’s happening. It will also give you the rewarding feeling of creating something from scratch, which can boost your motivation and dopamine levels!

## How did I write this book?

As someone who had never written a book before, I found the process quite unclear. I wasn’t sure which text-editing software or format would make it easiest to convert my work into other formats. Since I needed to include a lot of code snippets and math equations, Microsoft Word didn’t seem like the best choice (at least, I wasn't sure how to do it efficiently with a word processor like Word). On top of that, I’m not a fan of LaTeX—its syntax feels cumbersome, and I wasn’t eager to learn it. My focus was on writing the actual content, not wrestling with formatting.

That’s when I decided on Markdown. It’s simple to use, and there’s plenty of software that can easily convert `.md` files to `.html`, `.pdf`, `.tex`, and more. Plus, if I ever needed to automate custom transformations of my text, Markdown is one of the easiest formats to parse and manipulate.

I wrote each chapter in separate `.md` files, and then created a Makefile to combine them into a single PDF. To do this, I used a Linux tool called `pandoc`, which made the conversion process seamless.

Here is how my `Makefile` script looked like:

```Makefile
pdf:
	pandoc --toc --output=out.pdf *.md # Convert MD files to a PDF file
	pdfunite cover.pdf out.pdf tsp.pdf # Add the book cover
	pdftotext tsp.pdf - | wc -w # Show me the word-cound
```

The `--toc` flag generated the Table of Contents section for me automatically (Based on Markdown headers: `#`, `##`, ...), and I also had another `.pdf` file containing the cover of my book, which I concatenated with the pandoc's output. I was tracking my process by word-count.
