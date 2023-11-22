\pagebreak

# Fly

## Skip if you are poor

Throughout my career in software-engineering, I had always avoided topics which involved any interactions with the Physical world (Except a short period of time when I was working on line-following robots as a high-school student). That's partly because I live in an economically poor country, where there aren't a lot of companies building cyber-physical systems (Systems composed of a software, controlling/sensing a physical thing), except when politics is involved, if you know what I mean.

Unlike pure software engineering, where you can never run out of characters, building software that interacts with the real-world, involves physical objects, things that you can touch and feel, and the unfortunate truth about non-imaginary objects is that, they cost money, and they can break, which means, you can't experiment as much as a software with them (Unless you are a rich engineer, having a giant laboratory inside your house, with plenty of money)

I have never been that rich, and I also couldn't find any company doing respectful cyberphysical projects in my country either. Therefore I have never been a real fan of a section in computer science, known as ***embedded engineering***. You can see in this book that I'm a great fan of computer simulations though!

## New is always better

I named this chapter of the book as "Fly", because flying is probably one of the most amazing and spiritual dreams of humans that has come to reality, and computers are one of the most important components of the flying-machines we have today. Humans could never land on moon without computers.

I would like to start this chapter by mentioning two of the most ambitious companies, created by the American multi-billionaire entrepreneur, Elon Musk, at the time this book is written. Tesla and SpaceX, are companies that are producing cyberphysical products, one is building self-driving cars and the other is building rockets, aiming to make humans multi-planetary species.

When Elon Musk started those companies, it wasn't obvious at all that they'll become successful. Who could think that a private rocket-building company could beat the government funded NASA that once put humans on the moon? That's also true for Tesla, there were plenty of automobile companies with decades of experience, even in designing electric cars, but Tesla beat them all. Besides the reason that Elon himself is one of the most ambitious people of our time, which is enough for making a risky business successful, there is a more important reason why those two companies become insanely successful: ***It's much easier to experiment new stuff when your business is still small!***

It's too risky for an already giant business to switch and explore new ways of building things. When companies grow, they start to become heavily beurocratical, which slows things down by a lot. That's why startups are so fast, they are small, and there is plenty of room for making mistakes. SpaceX didn't have all those boring stuff, it only had a few bright-minded people, exploring new ways of building rockets, without being scared too much of the outcomes.

My point is, old technology isn't always taking the best approach in doing stuff, in fact, old technology is pretty bad, because when engineers were designing the old technology, they didn't have the knowledge and experience they have right now. So it makes sense a lot to get brave and try to redesign things that were working correctly and stabely even for a long time!

## Life in a Newtonian world

Building and experimenting cyber-physical systems is going to cost you a lot, and it makes sense to check if everything is going to work as expected, before building your prototype. Since your brand-new cars/airplanes/rockets/etc are going to live in our world, they are going to obey the laws of Physics of our world. So if you are willing to simulate them before doing serious experiments, you will have to apply the laws of physics on them, in a simulated environment.

### Physics before apple hit the the Newton's head

Students nag that they would have much less to study if that damn apple never hit Newton's head, but the truth is, the science of Physics existed even before Newton formulate it in his precious works. Even if Newton never figured gravity, sooner or later, someone else would do it! So, what were the statements of "Physicists" before Newton, when you asked them to explain the mechanical phenomena we experience everyday?

Aristotle, the Greek scientist and philosopher who were living in 4th century B.C., was of the first famous scientists trying to explain the laws of motion. Surprisingly, Aristotle's laws of motion was left untouched and continued to rule physics for more than 2000 years. Galileo Galilei, the Italian polymath, was of the first people who was brave enough to make new statements about motion and to break the Aristotle's empire that ruled for so long.

Aristotle's law of motion states that:

- External forces are needed to keep an object moving

Although this statement seems funny and so wrong nowadays (It's the friction that stops objects moving), it was convincing people and scientists for more than two centuries! Put yourself in the shoes of people back then, how would you formulate physics, if you had never heard the laws of physics written by Newton?

Another remark of Aristotle's law of motion is that, heavier objects fall faster than light objects. Nowadays we know that's not the case too, and the reason a feather falls slower than a book is merely because of air friction.

Although Aristotle's opinion **seem** right, they are **not** right. Aristotle's biggest mistake is that, he wasn't aware of friction forces and he was ignoring air resistance. This is known as the Aristotle's Fallacy.

Galielo Galilei's law of inertia states that:

- If you put an object in the state of motion, it will move forever if no external forces are applied on it

And lastly we will reach to Newton's formulation of motion and gravity, which although is proven to be incorrect by legends like Albert Einstein, is still accurate enough to explain and predict most of the macroscopic motions happening in our universe. The physics of motions discovered by Newton is still a fundamental guide for us to build cars, airplanes and rockets that can bring humans on the moon and put satellites in the space.

Newton was a legend. Not only he discovered a very accurate theory for motion, he also invented (Co-invented?) a fresh mathematical tool that has made significant contributions to the other fields of science too. This field of mathermatics is known as Calculus. We explained the basica of differentiation and integration in the previous chapters, so let's jump to the Newton's laws:

[TODO]

Perhaps the most important discovery of Newton is his famous formula $F=ma$ which explains how the force applied to an object, the mass and its acceleration are related to each other.

$v=\frac{dx}{dt}$

$a=\frac{dv}{dt}$

$x=\int{\int{a.dt}}=\frac{1}{2}at^2+v_0t+x_0$



## Exciting Electronics

I started to admire the joy of programming computer in very young ages, but even before that, I was a fan of toy electorical kits. I used to buy ans solder them back then. I always wanted to know how the circuit of a blinking LED works for example. Why? Because understanding them was the first step to my dream of designing the circuits of my own. Unfortunately, I couldn't find appropriate resources that could convince a kid why a circuit like that works, and how he can get creative and build circuits of his own, by putting the right components in the right places.

So, electronics, and the way it works, remained a secret to me for years, and one of the reasons I gave up and switched my focus on building software was that, computer programming is much easier. Even after 15 years, and multiple tries in reading different books on electronics, I'm still afraid to say that I'm still not capable of designing a circuit as simple as a blinker all by myself, without cheating from other circuits, and that's one of the reasons I decided to write this chapter; to finally break the curse and learn this complciated, yet fascinating field of science.

How did I do it? Well I tried reading books in this topic, but I didn't find many of them useful. All books written in this matter (Even the good ones!) were starting explaining the laws of electricity and then describing different electronical components and their usecases in separate chapters. I'm not really a fan of learning things this way.

Here, I'm going to explain electronic circuit design with a bottom-up approach (Just like the way we discussed other fields of computer science). We will start by learning the history of electricity and how was the first experience of humans of electricity, and then describing the ways we can generate electricty, and then we will try to build useful stuff out of electricity. (From things as simple as light bulbs to comptuer!)

Along the way, we will also learn about different electronic components!

---

I would say that studying electricity is one of the most important foundations of human modernity, and just like the history of mechanical physics, electricity also has its own fascinating stories.

[TODO]

Here is one of the reasons I don't like some of the electronics tutorials out there: they will tell you exactly, what a resistor is, how it works and why it works, but they'll never tell you when and where you should put a resistor in your circuit, and how you should calculate the resistance needed, in practical examples! E.g. by only knowing the Ohm's law $V=RI$, calculate the resistance needed to connect a 2V LED to a 5V battery!

Here is the golden fact many resources do not directly tell you (Or do not emphasize as much as I'm going to do!), you can assume that any electronical component (Including LEDs) that consume electricity are acting like resistors (Even a piece of wire is a resistor). If they weren't resistors, they could consume infinite electrical current, even with very low voltages.

## How to push the electrons?

Before jumping straight to the things you can do with electricity, it's good to know how electricity is generated. There are various ways you can get a steady stream of electrons in your circuit. Batteries for example, they give you a potential difference on their poles using chemical reactions, and unfortunately, they will run out of energy after sometime. Unlike batteries, the source of electricity we get in our homes isn't generated by chemical reactions, but is the result of spinning a magnet inside a coil of wire. You can try it yourself at home! Humans have discovered somehow that, if you move/spin a magnet inside a wire coil, you will push the electrons in the wire and will have electrical current, which is able to turn a light-source on!

Now, you don't need to spin that magnet by hand, you can let the nature do it for you. You can connect a propeller to the magnet, causing it to spin when wind is blown. That's in fact how wind turbines convert wind into electricity!

Even if you don't have wind, you can use artificially-generated wind (By burning fuel or even doing nuclear reaction, to make water hot and vapourize it, leading to a high-pressure steam of water vapour) to spin the coil for you.

Unfortunately, the voltage/current generated using this technique alternates like a sine function, and although we can still directly use such a current for heating things (E.g light-bulbs), it can't be used for driving anything digital. Such a power supply is known as an AC supply (AC stants for, alternating current!)

If you plot the output voltage of the two ends of a AC power source, you will get something like this (Negative voltage means that the poles are reversed and the current will flow in the reversed direction):

[TODO]

### Ohm's Law

$V=RI$

### Kirchhoff's Law

### Alternating vs Direct current

How diodes can convert AC to DC

### When capacitors finally become useful

If electrical current is analogous to a ball falling from a higher height, then capacitors are like springs on the ground. When the ball hits the spring, in the very first seconds, you won’t see a fast change in the speed of the ball (capacitor acts like a wire, in the very first milliseconds ). As time passes and the ball pushes the string, the string will get potential energy, slowly preventing the ball to squeeze the spring further. There is a moment where the potential energy of the ball  gets equal with potential energy of the spring (capacitor), and that’s when the ball (current!) stops moving. The longer and stronger the spring is, the more it takes to fully squeeze it.

In this fancy, not fully accurate analogy, we can also assume that air-resistance is pretty similar to a resistor. It will slow down the ball. Together, the air resistance and the spring will make a mechanical RC circuit, higher air resistance will also increase the time needed for the spring to get fully squeezed.

Now, imagine we suddenly remove the gravity from the equation, the energy stored in the spring will be released and will push the ball to higher heights, just like when we disconnect the batter from the capacitor and let it load a LED!

Capacitors are DC blockers!


## Controlling the world

$u(t)=K_pe(t)+K_i\int_0^t{e(\tau)d\tau}+K_d\frac{de(t)}{dt}$