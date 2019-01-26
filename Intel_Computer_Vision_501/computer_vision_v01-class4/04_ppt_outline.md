* canny edge
  * LOCV (151):  x,y gradients -> four directional derivatives
    includes d_x, d_y, and theta
    note:  direction of gradient is perpendicular to direction of edge
    * orig convol. with gaussian
    * calculate gradients
    * select local maximums (along gradient)
      * [thin the line across the edge]
    * threshold phase I (drop low, keep high)
      * threshold phase II (refine middle values)
        * only keep if connected to a kept value
          (assemble to contours)
  * exercise idea:  canny edges in rgb, combine them

* edge thinning
  * http://answers.opencv.org/question/3454/detecting-thick-edges/
  * also in safari book
  * edges -> contours
    * https://stackoverflow.com/questions/15751940/opencv-converting-canny-edges-to-contours
  * [possibly put all of this with contours?]

* Fourier transform
  * [note links]:
    * [homer](https://www.youtube.com/watch?v=QVuU2YCwHjw)
    * [blog](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
    * [ptolemy so](https://math.stackexchange.com/questions/1002/fourier-transform-for-dummies)
    * [from convolutions](https://mathoverflow.net/questions/446/fourier-transform-for-dummies)
    * [divide to get freq](http://dmorris.net/projects/tutorials/fourier_tutorial.pdf)
    * [ft vs wavelets localization](https://math.stackexchange.com/questions/279980/difference-between-fourier-transform-and-wavelets)

  * general material on Fourier Series
    * Ptolemy and complex representation of planet motions
      * circles on top of circles on top of circles
      * wrong/bad for two reasons:
        * they were really ellipses around the *SUN*
        * we can draw ANY pattern using circles on top of circles on top of cirlces
          * Homer Simpson
          * prove it. no thank you.  but, that (converting an image into a set of circles on top of circles on top of cirlces) is what FFT does.
    * how does it work?
      *  decomposition
        * vectors:  point -> x stuff, y stuff, z stuff
        * polynomial:  x stuff, x**2 stuff, x**3 stuff, ....
        * what do we decompose to?  something called a "basis"
          * a good basis:  we can combine the basis elements to get *any* output
        * how do we decompose functions (graphs)?
          * you might recall taylor series:  we can decompose a function to a (possibly infinite) sum of polynomial terms
          * we can also use fourier

* FFT and DFT
  * so, fourier series is exact for analytical (symbolic) forms:
    * f(x) = FS(x)
      * we can estimate this exact thing on a computer, up to machine tolerance
      * e.g., if f(x) is sin(x) I can compute arbitrary values of sin(x) for x in [0,2pi] ... getting as detiled as the smallest different between two floating points on my computer (a value that is commonly called "machine epsilon")
    * similar in concept to the fact that:
      * pi is transcendental (inifinite without a fixed pattern)
        * rational, irrational, transcendental
      * we can get values "close" (to some precision) to pi
      * but we'll always be off by a bit
    * we can get "a good approximation" of the exact sin(x) and the exact pi
    * note, symbolic algebra systems (like Mathematica and SymPy) get around these issues another way
  * back to DFT:  _discrete_ fourier transform: our finite data sample is never as "complete" as the exact symbolic forms ... we're not even close to being in the ballpark of approximating an exact symbolic form
    * for example, we have a 1-D "image" array with 100 pixels
      * there are an infinite number of analytic (symbolic) forms that fit those 100 points (e.g., there's one 100-1=99 degree polynomial and an infinite number of greater degree polynomials that will exactly fit the 100 points .... any many, many more even weirder functions that include polynomials, logs, trig, etc.)
    * what does it mean to apply fourier analysis to this discrete set of sample points

  * so, how do we break apart a sample (our 100 points) into ... just one ... Fourier series that
    1.  matches our 100 points
    2.  has no other constraints: to the left and right of our points it can take on any other set of continuous values
  * the DFT solves this problem in a computationally efficient manner
  * why is it used?
    * this lets us take advantage of the FS properties:
      * convolution becomes multiplication (in fourier space)
      * it gives us a way of performing convolutions very efficiently
    * we can identify high/low frequency components
      * compression
    * [?] symmetry properties
      * complex components

  * implementation details
    * numpy versus opencv
    * sizing
      * "find ideal size" function
      * have to copy to new array (yuck)
        * and then tell fft not to use some rows/cols (ha!)
        * but, the gains can be worthwhile



* filters, convolutions, and FFT
  * point of the fft is that is simplifies theory (?) and speeds up practice of convolutions
  * examples of conv(f,g) = conv(fft(f,g)) = fft(f * g)

* wavelet applications and numpy
  * https://kastnerkyle.github.io/posts/wavelets/


* line detection
  * Sz, pg. 254:  successive approximation, Hough, and RANSAC
  * succ. approx is more for going from a curve-contour to a "simpler" representation (aka line simplification)
    * if the contour *is* a line (with noise) we can simplify it to that line
  * for occluded lines, we need more advanced techniques like Hough
    * note, hough can be with/without gradient info
    * with it, we don't need to orient the line and we need less accumulators and no inner loop (work has already been done)


* hough transforms
  * better stuff in the PICV (the safari book)
    *
  * propose point; evaluate counts along shape; keep maximums
  * lines
    * probabilistic
  * circles
  * arbitrary shapes:
    * store shape
      * reference point +
      * lines and angles from reference, though border, to axes)
    apply and count matching edge pixels
* ransac for lines:
  * pair of edge elements, line hypothesis
  * others on this line
    * set boundaries for min matchers
  * can also use ransac for image alignment
  * [note] see opencv fitline:
    * https://stackoverflow.com/a/15184899/221602
    * it may use a ransac like method
      * is it ransac like only in use of m-estimator?

* if this gets too thin, we can add material on peformance here
  * [probably unneeded if we include wavelets here]
