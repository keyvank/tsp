\pagebreak

# Vision

Vision is my (Or probably all people's) favorite way of sensing the world. Imagine out of 6 humans senses, you only could have one of them, which one would you choose?

Vision allows you to find stuff around you, even when they are far enough that you can't access them by your hands. It guides you to things in a physical environment. It shows you the wild animal a coming to you before it's too late.

## History of colors

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

## Memento

Years later, in 1826, a french inventor named Nicéphore Niépce had the dream of recording scenes of real life. Back then people knew that there are some chemical compounds that make chemical reactions when they are exposed to light. The chemical reaction would convert the compound to a different compound which fortunately had a different color. The more intense the light is, the stronger the chemical reaction is, applying stronger color changes to the compoound. Nicéphore took advantage of this, he made a plate coated with such a compound and put it inside a camera obscura. A camera obscura was a dark, isolated room with a small hole (Filled with a lense) on one side that projected the image of the outside on the wall. Nicéphore put his coated plate on the wall, and let it be there for a few days. After a few days, the image of the outside started to appear on the plate, which is the very first photography ever done in the world. The resulting picture wasn't perfect (What did you expect?) but the experiment was revolutionary enough to inspire other inventors for building the modern photography.

James Clerk Maxwell, you probably have heard his name before, because of the electromagnetic equations he discovered before, was only 24 years old when he discovered the importance of the trichromatic theory that Young and Helmholz proposed in 1802. The three-colour method, first proposed by Maxwell, was a method for taking colour photographs, given the fact that human eye is only sensetive to 3 ranges of colours. Redness, greenness, and blueness.

He argued that if we take three photographs of the same scene, one with a filter that only passes red light, one that only passes green light and one that only passes blue light, and then somehow combine these three photographs together on a plate, our eyes will be hacked to see a coloured version of that scene. 6 years later, he made the very first colour photography of the history.

You probably already know that when coloured movies came out, old fashioned movie makers were skeptical of them. Good to know that photographers back then also resisted to take coloured photos, but history has shown us that nobody can fight against advancement of technology.

## Digital era

Over a century passed before humans invented digital photography, and a lot of inventions and discoveries happened in between (E.g. people started to take pictures in very high speeds and record "movies"), and I would like skip the history and advancements of the analog photography industry in the next 100 years, because there are too many details that are unrelated to the core idea, and start talking about the digital era, the time when people started to store vision on a computer.

It's good to know that digital scanners came before digital cameras. It's also kind of obvious that they have a much simpler structure than digital cameras. The very first digital scanner was invented in 1957 by an american engineer named Russell Kirsch. His scanner could scan photos of size 5cmx5cm in the resoluion of 176x176 pixels (30976 pixels, i.e. ~30 kilopixels!). The bit-depth of his scanner was only 1-bit! The pixels could only be complete black or complete white, so there were no intermediate shades of gray.

In order to deeply understand how digital photography works, you first have to know there exist some materials that their electrical resistance change when they are exposed to light. They are called photoresistors. Their resistance typically decrease when they are exposed to light. So, if you connect a battery to them, when there is no light, no/small current will flow. But when there is light, current will flow. The more intense light is, the more current it will flow. Now how can we use this to measure light intensity of a physical point? Imagine we emit light to a black surface. A black surface will reflect no light, so a photoresistor nearby won't get excited. A white surface will reflect all the light. so the photoresistor will get excited and current will flow. Now imagine we have an electrical circuit that measures the electrical current in a photoresistor. If current is higher than a threshold $t$, it will output 1, otherwise it will output 0.

What Russell Kirsch did in 1957, was something like this: He made a photoresistor that could move on a 2D grid with electrical motors. It would start on the point $(0,0)$ and scanned a complete row, by moving little by little (In case of a 5cmx5cm area, the distance between pixels is 5cm/176, which is around 0.28mm. Then it would move to the next row and scan another line of pixels. It would output 0 or 1 for each pixel. His scanner was so simple so it couldn't scan grayscale information. But he did a trick. Remember there was a threshold $t$? He scanned a point several times with different thresholds, (E.g. $t=0.1$, $t=0.2$, $t=0.3$, ...) then he stored number of times he got the 1 output. This way, he could recognize how white a pixel is and store grayscale information too, without much change in the original design! Kirsch's very first digital scanning is one of the most important pictures taken in the history of photography.

Digital cameras are not scanners. It takes a very long time to takes photos by moving a photoactive subtance and taking samples from it. So what's the solution? Well, naively thinking, instead of a single photon sampler (Photoresistor or ...), we can have and array of a lot of them. In case of Kirsch's design, instead of one moving photoresistor moving on a 2D grid, we can have a plate of 176x176 (30976) photoresistors laying on a 2D grid, which can scan the whole thing in a single step. This design has a very important issue, and the issues is that we might need millions of wires coming out of such a plate, in order to get the outputs of all this resistors (Imagine we want to take a very high resolution image!), which is practically impossible. Engineering is all about giving solutions to challenging problem!

12 years later, in 1969, two Bell Labs physicist named George Smith and Willard Boyle invented the very first Charge-Coupled Device, while working on solutions to improve video-telephone technology. They sketched the first design of a CCD in an hour or so. CCDs are the main elements of modern digital photography. Just like our proposed design, they consist of an 2D array of very small cells that convert light causes to electrical effects. A very common technique is used in order to minimize the number of wires coming out of such an array. Instead of taking a wire out of every cell and reading the content of the cell directly, the cells are interconnected to each other through a single wire that passes through all the cells, and pass their contents to their neighbors in each time step (Shift-registers are used in order to store and pass the data). The CCD will actually output the contents of the image through one line, in a serial fashion.

Applying the trichromatic theory and Maxwell's colour photography idea, we can take colored digital photos too. There exists physical filters that you can put on a CCD array, allowing the neighbouring cells to independently capture the redness, blueness and greenness of a point. They are called Bayer filters. Sometimes, instead of putting a Bayer filter on a CCD array, they natively integrate 3 different CCDs on a CCD array, each of which take the RGB values for each pixel. The method is called, 3-CCD. Obviously using a Bayer filter has a much simpler design.

## Anatomy of a computer image

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

### Having fun with the pixels

When learning computer graphics, before jumping to complicated algorithms like 3D rendering, there are some other stuff you can do to leverage your power of manipulating pixels.

There are plenty of things you can draw on a 2D surface. Let's start with drawing a simple 2D line. A 2d line may be defined by its slope and offset:

$y = ax + b$

Given two points, you can find the corresponding $a$ and $b$ that passes through this line too. Assuming the points are: $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$:

$a = \frac{y_2 - y_1}{x_2 - x_1}$

$b = -ax_2 + y_2$

Let's have a class for working with lines!

```python=
class Line:
    def __init__(self, slope: float, offset: float:
        self.slope = slope
        self.offset = offset
    
    def get_y(self, x: float):
        return self.slope * x + self.offset

    @staticmethod
    def from_points(a: Vec2D, b: Vec2D) -> Line:
        slope = (b.y - a.y) / (b.x - a.x)
        offset = -slope * b.x + a.x
        return Line(slope, offset)

```

Here is something interesting to draw with simple lines:

[TODO]

#### Circle

A circle can be defined given its center and radius. Just like the `Line` class, we may also have a `Circle` class:

```python=
class Circle:
    def __init__(self, center: Vec2D, radius: float):
        self.center = center
        self.radius = radius
```

### Fractals

One of them is to draw fractals! Fractals are patterns that repeat forever. If you zoom in what you see is very similar to the whole image. Let's draw a few of them:

#### Serpinski Triangle

#### Koch Snowflake

#### Julia sets

## Ray Tracing

3D computer rendering is probably the most complicated and interesting way a computer
can stimulate our vision. Our perception is evolved in a way to understand our 3-dimensional
space and world. Being able to generate arbitrary 3D looking images with a computer brings 
us infinite possibilities. Nowadays people are trying to immerse themselves into virtual worlds
by putting computer screens really close to their eyes, which renders photorealistic images.
There are many methods and algorithms by which we can 3D computer images, we are going to 
implement two of the most important ones in this book. One of those methods will give you very
photorealistic outputs with high rendering times, while the other method gives you inaccurate 
outputs but is fast enough to generate images in real-time, making it perfect for 3D games.

Surprisingly (Or obviously for some!), the rendering algorithm that gives you real-looking
outputs is much simpler to implement, so let's dive in!

Ray-Tracing, as its name suggests is an algorithm, inspired by the science of physics, that
tries to generate 3D scenes by predicting and tracking the way photons move in imaginary
3D environements. Since there are infinite number of photons coming out of a light source,
it might seem infeasible to generate images with this method. But the fact is, most of
the photons coming out of a light source end up somewere that do not have any impact on
out final image (They do not reach our imaginary eyes). We only care about those photons
that reach our virtual eye/camera. Given this fact we can get clever and do this simulation
in a much more efficient way! We just need to go backwards. We will generate rays from our
virtual eye and see if they will end up on a lit source! This is the core idea behind the
Ray-Tracing algorithm!

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

Another useful operation is multiplication of a vector by an scalar. We are going to override the
multiplication operator in order to have this operation in our `Vec` class:

```python
def __mul__(self, other):
    return Vec(
        self.x * other,
        self.y * other,
        self.z * other,
    )
```

Normal of a vector $\vec{A}$ is defined as a vector with length $1$ that has the same direction
as vector $\vec{A}$. Based on the definition, we can calculate the normal vector by dividing the
elements of the vector by the length of the vector:

$norm(\vec{A})=\frac{\vec{A}}{|\vec{A}|}$

```python
def norm(self):
    len_inv = 1 / self.length()
    return self * len_inv
```

Although your compiler's optimizer will do the job for you, it's generally better to calculate
the inverse of a number and multiply it with your variables, instead of dividing the variables
by a number, since multiplication is a much cheaper operation and will take much less clock 
cycles of your CPU compared to divisions.

![Shooting rays from an imaginary eye](assets/rtc.png)

Assuming our imaginary eye is located at $\vec{E}$, looking at an object that is located on a
target $\vec{T}$, we may assume what is being seen by the eye is reflected on a square plane 
located with a distance of $1$, which its center is $\vec{C}$. Obviously, the direction of 
$\vec{EC}$ should be equal with $\vec{ET}$. Since the size of $\vec{EC}$ should be 1, we may
conclude that $\vec{EC}$ is the normalized vesion of $\vec{ET}$.

Now, assuming we have the position of the left-down corner of this plane ($\vec{LD}$), and we 
want to render a $W \times H$ resolution image, we may loop through each of the pixels on the 
image and calculate the corresponding 3D point located on the 3D plane (Let's name it 
$\vec{P_{ij}}$), in order to calculate the ray that starts from $E$and goes in the direction 
of $\vec{EP_{ij}}$.

$\vec{P_{ij}}=\vec{LD}+\frac{i}{W}\vec{R}+\frac{j}{H}\vec{U}$

Let's hold the position and direction of a ray in a seperate `Ray` class:

```python
class Ray:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
```

We can use the PPM image generator we developed in the previous sections in order to calculate
a ray-traced scene. We just need to reimplement the `color_of` function:

```python
def color_of(x, y, width, height):
    p = ld + (x / width) * r + (y / height) * u
    direction = (e - p).norm()
    ray = Ray(e, direction)
    return trace_ray(ray)
```

The `trace_ray` function will take a ray as an argument and will calculate the color and intensity
of photons that are going through that ray for us.

![Calculation of eye-generated rays](assets/eye.png)


### Rasterization

Rasterization is another effective technique in rendering 3D scenes and it is quite faster than ray-tracing (Or any other method involving simulation of Physics). Although the results are less accurate, it is the main technique used in real-time rendering applications (E.g Video games). You don't have much time to render the next frame in a game! (Although, games are slowly switching to ray-tracing in some parts nowadays, as our hardware becomes faster)

In the rasterization algorithm, instead of emitting rays abd finding the object that it intersects with and calculating its color, we will try to map the 3D points of an object into 2D points on your computer screen through mathematical formula. In other words, when rendering each frame, we loop through the objects in our scene, and all of the 3D points that make those objects, and we will apply a function which convert a triplet $(x, y, z)$ to a pair of floats $(x,y)$. We then fill those pixels on the screen!

Since it is impractical to represent a 3D object by its points (A 3D object it made of infinite number of points), we usually represent them by a bunch of 3D triangles. Looping through the triangles of an object, using the same 3D-to-2D point conversion formula, we can convert a 3D triangle to a 2D one. We just have to apply the function on all three 3D vertices of the triangle in order to get the respective 2D ones.

Filling a 2D triangle on an image is a straightforward process. Before getting into the more complicated parts, let's first draw a triangle on a PPM image, given the 2D position of its vertices. It's good to defined classes for storing 2D points and triangles, so let's first create a class named `Vec2D` which stores two floating point numbers and another class named `Triangle2D` for storing three `Vec2D`s. Our PPM triangle renderer should accept a `Triangle2D` and fill the pixels within that triangle.

```python=
class Vec2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Triangle2D:
    def __init__(self, a: Vec2D, b: Vec2D, c: Vec2D):
        self.a = a
        self.b = b
        self.c = c
```

### Matrices, programmable math objects!

When doing ray tracing, we exactly knew where are imaginary eye/camera is, but so far in the rasterization algorithm, we were assuming that the eye/camera is placed at the origin point $(0,0,0)$. So, how could we move in this 3D scene and see it from different perspectives? The solution is a bit different compared to what we were doing in a ray tracer. Here, instead of moving/rotating the camera around the world, we move/rotate all of the objects in that world, in order to make it feel like the camera is placed in a different location! Since we are working with 3D points, before passing the points to the rendering function, we have to apply a ***transformation*** function to put the point in a different location.

These transformations are done through matrices! There are matrices that apply certain geometric changes when being multiplicated with vectors.

Assuming our points are represented in 4D vectors where the last element is 1, we can invent a matrix that can move a point by adding a offset vector to it when multiplied with the original vector. This matrix is known as ***translation*** matrix. Assuming we want to move our vector $(x, y, z)$ by $(T_x, T_y, T_z)$, the translation matrix works as follows:

$\begin{bmatrix} 1 && 0 && 0 && T_x \\ 0 && 1 && 0 && T_y \\ 0 && 0 && 1 && T_z \\ 0 && 0 && 0 && 1 \end{bmatrix} \times \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = \begin{bmatrix} x + T_x \\ y + T_y \\ z + T_z \\ 1 \end{bmatrix}$

 (We have to add a fourth element in order to make these matrices work)

Nothing explains the concept better than a piece of code. Since all of the transformation matrices we use in this section are 4 by 4 matrices, let's define a `Matrix4x4` class for this use and add methods for creating different transformation matrices:

```python=
class Matrix4x4:
    def __init__(self, rows):
        self.rows = rows

    @staticmethod
    def translate(offset: Vec3D):
        return Matrix4x4([
            [1, 0, 0, offset.x],
            [0, 1, 0, offset.y],
            [0, 0, 1, offset.z],
            [0, 0, 0, 1]
        ])
    
    def apply(self, vec: Vec3D):
        # ...

```

Now, here is an interesting fact about transformation matrices: because of the *Associative Property of Multiplication* of matrices ($A \times (B \times C)=(A \times  B) \times C$), they combined with each other, resulting in new 4x4 transformation matrices that behave as if each matrix is applied to the vector independently. This literally means that you can compress infinite number of transformation matrices into a single matrix. As an example, if you multiply two translation matrices which move a point by $(T_{x_1},T_{y_1},T_{z_1})$ and $(T_{x_2},T_{y_2},T_{z_2})$ respectively, you will get a new translation matrix that moves a point by: $(T_{x_1} + T_{x_2},T_{y_1} + T_{y_2},T_{z_1} + T_{z_2})$.

Transformation matrices are not limited to moving points by an offset. There are transformation matrices for rotating objects around different axis too!

$R_x(\theta) = \begin{bmatrix}
1 && 0 && 0 && 0 \\
0 && cos(\theta) && -sin(\theta) && 0 \\
0 && sin(\theta) && cos(\theta) && 0 \\
0 && 0 && 0 && 1
\end{bmatrix}$

$R_y(\theta) = \begin{bmatrix}
 cos(\theta) && 0 && -sin(\theta) && 0 \\
0 && 1 && 0 && 0 \\
sin(\theta) && 0 && cos(\theta) && 0 \\
0 && 0 && 0 && 1
\end{bmatrix}$

$R_z(\theta) = \begin{bmatrix}
cos(\theta) && -sin(\theta) && 0 && 0 \\
sin(\theta) && cos(\theta) && 0 && 0 \\
0 && 0 && 1 && 0 \\
0 && 0 && 0 && 1
\end{bmatrix}$

### Camera matrix

Recall that we move/rotate the world around us instead of placing a camera in an arbitrary position rotation, there is a shortcut way for transforming the world as if a camera at $\vec{P}$ is looking at a target $\vec{T}$, and its upper-side is pointing at $\vec{U}$. This matrix can be created as follows:

$T = \begin{bmatrix}
1 && 0 && 0 && 0 \\
0 && 1 && 0 && 0 \\
0 && 0 && 1 && 0 \\
-P_x && -P_y && -P_z && 1
\end{bmatrix}$

$F = normalize(T - P)$

$R = normalize(U \times F)$

$U = F \times R$

$O = \begin{bmatrix}
R_x && U_x && F_x && 0 \\
R_y && U_y && F_y && 0 \\
R_z && U_z && F_z && 0 \\
-P_x && -P_y && -P_z && 1
\end{bmatrix}$

Then the look-at matrix $L$ can be calculated as follows:

$L = O \times T$

### The magical matrix

The perspective law says that the distance between 2 points look less when the points get farther of our eyes. There is a magical transformation matrix, called the ***perspective*** transformation matrix, which applies this effect for us:

$\begin{bmatrix}
1 / \frac{tan(p_fov / 2)}{p_asp_rat} && 0 && 0 && 0 \\
0 && \frac{1}{tan(p_fov / 2)} && 0 && 0 \\
0 && 0 && \frac{-(p_far + p_near)}{p_far - p_near} && \frac{-2 * p_far * p_near}{p_far - p_near} \\
0 && 0 && -1 && 0
\end{bmatrix}$

### Barycentric coordinates