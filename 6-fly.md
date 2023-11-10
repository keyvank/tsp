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


## Controlling the world

$u(t)=K_pe(t)+K_i\int_0^t{e(\tau)d\tau}+K_d\frac{de(t)}{dt}$