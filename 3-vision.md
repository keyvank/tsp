\pagebreak

# Vision

Vision is my (Or probably all people's) favorite way of sensing the world. Imagine out of 6 humans senses, you only could have one of them, which one would you choose?

Vision allows you to find stuff around you, even when they are far enough that you can't access them by your hands. It guides you to things in a physical environment. It shows you the wild animal a coming to you before it's too late.

Human eyes are 2d-arrays of electromagnetic receptors that can recognize electromagnetic waves inside the visible spectrum, which are waves with wavelengths of 380-700 nanometers, or in terms of frequency, waves with frequencies of 400-790 terahertz. Theoritically, of you pick a magnet, and and shake it 400,000,000,000,000 times per second, you will see red light coming out of it. Shake it even faster and it will become violet, after that, it will become ultra violet which is not visible by human eyes.

Before studying how an human eye works, let's design one for ourself. As you may already know, electrical flows run a biological neural network. So external inputs need to be translated into electrical signals before they can be understood by your brain. We can use a linear mapping for this conversion. We can map the visible specturm into a voltage between 0.0 and 1.0, where 0.0 is red and 1.0 is violet:

$e=\frac{f-400tHZ}{390tHZ}$

Unfortunately, this mapping doesn't explain how black and white colors are represented in a brain. Well I have to tell you something. Black and white colors do not exist. (Or even light-red and dark-blue colors!) They are imaginary colors our brain has invented for itself in order to perceive darkness (Black) and presence of all waves (White). Well I have some bad news. A light beam doesn't necessarily have a single frequency in it. It can be a combination of multiple frequencies, and our mapping can only handle a single frequency. so we need a different represantation for a color of a pixel. A very naive solution is to have a lot of sensors sensing the strength of different frequencies in the visible spectrum for each pixel. I.e. we can have a set of sensors $e_{400}$, $e_{401}$, ..., $e_{790}$, that can measure the presence of different frequencies (And the neighbour frequencies) as a voltage between 0 and 1. In this model, when all frequencies are 0, the brain will perceive it as black. When all frequencies are 1, the brain will perceive it as white. The problem with this model is that it will need a lot of cells for each pixel. If the human eye is a $n \times n$ array, then we'll need $n \times n \times 390$ cells in order to perceive an image.

We can get smarter than that. Imagine there are only two sensors per pixel, one will tell you how close the frequency is to $f_a$ and another will tell you how close you are to $f_b$ (Imagine $f_a=500tHZ$ and $f_b=600tHZ$) 

If you are ok in math, you probably know that we can build such behavior using the exponetiation of the absolute difference. (Or squared difference, like a Gaussian distribution equation)

$e_a = s.e^{-abs(\frac{f - 500}{50})}$
$e_b = s.e^{-abs(\frac{f - 600}{50})}$

Now let's try different frequencies in this scheme (Let's assume the strength $s$ of all frequencies is $1$):

$f=0$ then $e_a \simeq 0$ and $e_b \simeq 0$
$f=500$ then $e_a = 1$ and $e_b \simeq 0.13$
$f=550$ then $e_a \simeq 0.36$ and $e_b \simeq 0.36$
$f=600$ then $e_a \simeq 0.13$ and $e_b = 1$
$f=1000$ then $e_a \simeq 0$ and $e_b \simeq 0$

*It's much easier for a brain to analyze differences between outputs, rather than memorizing different values*

Now let's take advantage of this design and hack it! Let's say I have two light bulbs, one can emit $500tHZ$ lights and one can emit $600tHZ$ lights. Is there a way I can convince the eye that it is seeing a $550tHZ$ light? Yes! Instead of emitting a $550tHZ$ light with strength $1$, I can emit a $500tHZ$ light of strength $\simeq 0.32$ and a $600tHZ$ light of strength $\simeq 0.32$ at the same time. This will make $e_a = e_b \simeq 0.36$ which are the same values needed to convince the brain it is seeing a $550tHZ$ light!

Now the brain's algorithm can be something like this:

- If both $e_a$ and $e_b$ are zero, then there is no color (Darkness, infrared or ultraviolet)
- If $e_a$ is much higher than $e_b$ then the color is orange.
- If $e_b$ is much higher than $e_a$ then the color is green.
- If $e_a$ and $e_b$ are relatively equal, then the color is yellow.

Enough imagination! These numbers and formulas are all invented by me to explain the concept. Let's talk about the actual design of human eyes. So the human eyes is designed very much similar to the artifical eye we designed in the previous section. The only difference is that the human eye has receptors for 3 colors instead of 2. I'm sure you can guess what these three colors are! Red, Green and Blue. This fact was discovered in 1802 by Thomas Young (British polymath) and Hermann von Helmholtz (German physicist). They argued that there are 3 kinds of photoreceptors (Now known as cone-cells) in the eye, and they also mentioned that these cells have overlapping response to different wavelengths, allowing our brains to also recognize colors in-between red, green and blue wavelengths. They also mentioned that human eye is not perfect, because it is not able distinguish between yellow, and a mixture of red and blue. If our brains were able to distinguish between those two, it would be much much harder to build computer screens that we have today (Might be even impossible!). That's when God says, this is a feature, not a bug! It's also kind of sad that we are actually blind since our vision (Even in the visible specturm) is very limited and we can only observe very few combinations of light waves.

Years later, in 1826, a french inventor named Nicéphore Niépce had the dream of recording scenes of real life. Back then people knew that there are some chemical compounds that make chemical reactions when they are exposed to light. The chemical reaction would convert the compound to a different compound which fortunately had a different color. The more intense the light is, the stronger the chemical reaction is, applying stronger color changes to the compoound. Nicéphore took advantage of this, he made a plate coated with such a compound and put it inside a camera obscura. A camera obscura was a dark, isolated room with a small hole (Filled with a lense) on one side that projected the image of the outside on the wall. Nicéphore put his coated plate on the wall, and let it be there for a few days. After a few days, the image of the outside started to appear on the plate, which is the very first photography ever done in the world. The resulting picture wasn't perfect (What did you expect?) but the experiment was revolutionary enough to inspire other inventors for building the modern photography.

James Clerk Maxwell, you probably have heard his name before, because of the electromagnetic equations he discovered before, was only 24 years old when he discovered the importance of the trichromatic theory that Young and Helmholz proposed in 1802. The three-colour method, first proposed by Maxwell, was a method for taking colour photographs, given the fact that human eye is only sensetive to 3 ranges of colours. Redness, greenness, and blueness.

He argued that if we take three photographs of the same scene, one with a filter that only passes red light, one that only passes green light and one that only passes blue light, and then somehow combine these three photographs together on a plate, our eyes will be hacked to see a coloured version of that scene. 6 years later, he made the very first colour photography of the history.

You probably already know that when coloured movies came out, old fashioned movie makers were skeptical of them. Good to know that photographers back then also resisted to take coloured photos, but history has shown us that nobody can fight against advancement of technology.

Over a century passed before humans invented digital photography, and a lot of inventions and discoveries happened in between (E.g. people started to take pictures in very high speeds and record "movies"), and I would like skip the history and advancements of the analog photography industry in the next 100 years, because there are too many details that are unrelated to the core idea, and start talking about the digital era, the time when people started to store vision on a computer.

It's good to know that digital scanners came before digital cameras. It's also kind of obvious that they have a much simpler structure than digital cameras. The very first digital scanner was invented in 1957 by an american engineer named Russell Kirsch. His scanner could scan photos of size 5cmx5cm in the resoluion of 176x176 pixels (30976 pixels, i.e. ~30 kilopixels!). The bit-depth of his scanner was only 1-bit! The pixels could only be complete black or complete white, so there were no intermediate shades of gray.

In order to deeply understand how digital photography works, you first have to know there exist some materials that their electrical resistance change when they are exposed to light. They are called photoresistors. Their resistance typically decrease when they are exposed to light. So, if you connect a battery to them, when there is no light, no/small current will flow. But when there is light, current will flow. The more intense light is, the more current it will flow. Now how can we use this to measure light intensity of a physical point? Imagine we emit light to a black surface. A black surface will reflect no light, so a photoresistor nearby won't get excited. A white surface will reflect all the light. so the photoresistor will get excited and current will flow. Now imagine we have an electrical circuit that measures the electrical current in a photoresistor. If current is higher than a threshold $t$, it will output 1, otherwise it will output 0.

What Russell Kirsch did in 1957, was something like this: He made a photoresistor that could move on a 2D grid with electrical motors. It would start on the point $(0,0)$ and scanned a complete row, by moving little by little (In case of a 5cmx5cm area, the distance between pixels is 5cm/176, which is around 0.28mm. Then it would move to the next row and scan another line of pixels. It would output 0 or 1 for each pixel. His scanner was so simple so it couldn't scan grayscale information. But he did a trick. Remember there was a threshold $t$? He scanned a point several times with different thresholds, (E.g. $t=0.1$, $t=0.2$, $t=0.3$, ...) then he stored number of times he got the 1 output. This way, he could recognize how white a pixel is and store grayscale information too, without much change in the original design! Kirsch's very first digital scanning is one of the most important pictures taken in the history of photography.

Digital cameras are not scanners. It takes a very long time to takes photos by moving a photoactive subtance and taking samples from it. So what's the solution? Well, naively thinking, instead of a single photon sampler (Photoresistor or ...), we can have and array of a lot of them. In case of Kirsch's design, instead of one moving photoresistor moving on a 2D grid, we can have a plate of 176x176 (30976) photoresistors laying on a 2D grid, which can scan the whole thing in a single step. This design has a very important issue, and the issues is that we might need millions of wires coming out of such a plate, in order to get the outputs of all this resistors (Imagine we want to take a very high resolution image!), which is practically impossible. Engineering is all about giving solutions to challenging problem!

12 years later, in 1969, two Bell Labs physicist named George Smith and Willard Boyle invented the very first Charge-Coupled Device, while working on solutions to improve video-telephone technology. They sketched the first design of a CCD in an hour or so. CCDs are the main elements of modern digital photography. Just like our proposed design, they consist of an 2D array of very small cells that convert light causes to electrical effects. A very common technique is used in order to minimize the number of wires coming out of such an array. Instead of taking a wire out of every cell and reading the content of the cell directly, the cells are interconnected to each other through a single wire that passes through all the cells, and pass their contents to their neighbors in each time step (Shift-registers are used in order to store and pass the data). The CCD will actually output the contents of the image through one line, in a serial fashion.

Applying the trichromatic theory and Maxwell's colour photography idea, we can take colored digital photos too. There exists physical filters that you can put on a CCD array, allowing the neighbouring cells to independently capture the redness, blueness and greenness of a point. They are called Bayer filters. Sometimes, instead of putting a Bayer filter on a CCD array, they natively integrate 3 different CCDs on a CCD array, each of which take the RGB values for each pixel. The method is called, 3-CCD. Obviously using a Bayer filter has a much simpler design.

Knowing all this history and human anatomy, we can now tell that a computer image is a 2D array of pixels, where each pixel has 3 properties, red, green and blue. Typically, each color component can have 8-bit value (0 to 255). When the value is 0, that color component is completely off and when the values is 255, it means that color component has highest possible intensity. When all three components are 0, the pixel has complete darkness so we see it as black, and when all of them are 255, we see white (Our brains will be tricked that we are seeing all of the possible waves of the visible spectrum, but we are only seeing three colors!)

It is obvious that a colored computer image can be stored using $W \times H \times 3$ bytes. ($W \times H$ pixels, each having three 8-bit components). In order to get comfortable with digital computer images, we are going to manipulate and generate them. Since we don't want to bother ourselves with details of computer image formats (There is so much to learn about how PNG, JPEG and etc works), we are going to use a very simple file format named `PPM` (Portable PixMap) that emerged in 1980s. PPM stores the image in raw format and doesn't do any compression, that's why it's very simple to generate and manipulate these files. The only metadata that this file format holds is the width and height of the image.

Here is a spec of this file format:

```
P6 800 600 255
[800x600x3 bytes of data]
```

A PPM file starts with the magic string `P6`, then comes a width (As an ASCII string), then the height and then the maximum value of a color component. The metadata values are separated using whitespaces. After the metadata, there comes a whitespace and then we'll have the raw image data. In the example above, we are describing a 800x600 image in which each color component is between 0 to 255. It is worth noting again that the metadata comes as a human readable ASCII string and not bytes. The size of final file is:

`P6` (2 bytes) + whitespace (1 byte) + `800` (3 bytes) + whitespace (1 byte) + `255` (3 bytes) + whitespace (1 byte) + raw image data (1440000 bytes).

Let's write a function in Python which is able to save a PPM file using the described format:

```python=
import io

def save_ppm(width, height, rows):
    with io.open('output.ppm', 'wb') as f:
        f.write(f"P6 {width} {height} 255\n".encode('ascii'))
        for row in rows:
            for (r, g, b) in row:
                f.write(bytes([r, g, b]))
```

In this function, the `rows` argument should be a list of `height` number of rows, in which each row has `width` number of pixels (tuples) of RGB triads. As an example on how to use this function, let's generate a 800x600 image that all pixels are red:

```python=
def color_of(x, y, width, height):
    return (255, 0, 0) # Always return red


WIDTH = 800
HEIGHT = 600
rows = []
for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
        row.append(color_of(x, y, WIDTH, HEIGHT))
    rows.append(row)

save_ppm(800, 600, rows)
```

In order to make our future image generations easier, instead of calculating the color of the pixel directly in the loop, I made a function called `color_of` which returns the color of the $(x,y)$th pixel in an image of size $(width, height)$. Currently, this function only returns red, so you may not see anything special in the output, but try this function instead:

```python=
import math


def color_of(x, y, width, height):
    xx = x / width
    yy = y / height

    r = (math.sin(x / width * 100) + 1) / 2 * 255
    g = (math.cos(x * y / height / width * 100) + 1) / 2 * 255
    b = (math.sin(y / height * 100) + 1) / 2 * 255
    return (int(r), int(g), int(b))
```

See what it generates, try different functions and play with it a bit. Guess how shocking it was for computer scientist back then to be able to generate vision using code. That opened doors for insane amount of creativity and the event was big enough to call it a revolution in my opinion!

Drawing a line

Drawing a circle

 > Why do we use electrical cause effects? Because they are small and fast, and can easily be routed by metal wires Fastest cause effect type is light


### Ray Tracing

The Ray-Tracing algorithm for generating 3D computer images is all about tracing 
the route a photon goes through when reaching our eyes. You can assume that photons 
are like particles that are emitted from light sources, as if a lamp is shooting out
a lot of ultra tiny balls. These balls change their colors when they hit objects and 
absorb their colors, and finally some of them reach our eyes, letting us to see the 
world around us. Since photons move on straight lines, we can study their behavior 
with mathematical vectors. Since we live in a 3D world, the movements of our photons
can be analyzed using 3D vectors. A 3D vector is nothing but a tuple of 3 floating-point
numbers. A 3D vector can be used for storing the position or direction of a photon.


```python
class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

There are two very special and interesting operations that can be done on 3D vectors:

1. Dot-product: Calculates how aligned the vectors are. The dot-product of two vectors 
   is in its maximum when both vectors are pointing at the same direction. The dot-product
   of two vectors is a scalar value, which can be calculated in two ways:
   * $\vec{A}.\vec{B} = A_x.B_x + A_y.B_y + A_z.B_z$
   * $\vec{A}.\vec{B} = |\vec{A}|.|\vec{B}|.sin(\theta)$
2. Cross-product: Calculates how perpendicular two vectors are. The length of cross-product
   of two vectors is in its maximum when the vectors are perpendicular with each other. The
   result of a cross-product is a vector, that is perpendicular to both vectors, and its length
   is equal with the product of length of the vectors multiplied with cosine of their angle.
   Assuming the cross-product of $\vec{A}$ and $\vec{B}$ is $\vec{C}$, the elements of $\vec{C}$
   can can be calculated with the following formula:

   * $C_x = A_y.B_z + A_z.B_y$
   * $C_y = A_z.B_x + A_x.B_z$
   * $C_z = A_x.B_y + A_y.B_x$

   Alternatively, you can calculate the length of a cross-product using this formula:
   * $|\vec{C}| = |\vec{A}|.|\vec{B}|.cos(\theta)$

Let's go ahead and implement these operations as methods on our `Vec` class:

```python
def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z

def cross(self, other):
    return Vec(
        self.y * other.z + self.z * other.y,
        self.z * other.x + self.x * other.z,
        self.x * other.y + self.y * other.x,
    )
```

Reminding you of high-school math, a 2D vector's length could be calculated by summing the square
of vector elements and taking its root, the length of a 3D vector can also be calculated using a
similar approach:

$|\vec{A}|=\sqrt{A_x^2 + A_y^2 + A_z^2}$

Alternatively, we can calculate the length of a vector by taking the square root of the vector, 
dotted with itself:

$|\vec{A}|=\sqrt{\vec{A}.\vec{A}}$

```python
def length(self):
    return math.sqrt(self.dot(self))
```

Normal of a vector $\vec{A}$ is defined as a vector with length $1$ that has the same direction
as vector $\vec{A}$. Based on the definition, we can calculate the normal vector by dividing the
elements of the vector by the length of the vector:

$norm(\vec{A})=\frac{\vec{A}}{|\vec{A}|}$

```python
def norm(self):
    length = self.length()
    return Vec(
        self.x / length,
        self.y / length,
        self.z / length,
    )
```


![Shooting rays from an imaginary eye](assets/rtc.png)

![Calculation of eye-generated rays](assets/eye.png)