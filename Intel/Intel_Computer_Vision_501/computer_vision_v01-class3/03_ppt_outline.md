* Calculus in Pixel Space
  * derivatives and (basic) gradients
  * integral images


* kernels, neighborhoods, convolutions
  * SZ, pg. 111.  Linear filtering
  * TF material:  week 5 (ppt has kernels and some convolutions)
    * disc:  f*g(x) = sum f(t)g(t-x)
    * cont:
  * recall dice probability as an example
    * and kernel window sliding as finite example (sum -m to m)
    * [I have written notes on this]
      * P(2) = P(1) * P(1)
      * P(3) = sum_{i+j=3}P(i) * P(j)
      * P(T) = sum_{i}P(i) * P(T-i)
        * or P(T) = sum{i+j=T} P(i) * P(j)
  * normalized cross-correlation (a convolution) is used for template matching
    * this is a 2D version of Pearson product-moment correlation coefficient
    * aka, cov(x,y)/[var(x)var(u)]
  * boundary effects

* blurring/smoothing
  * gaussian, mean, median
    * see Perreault (perhaps as example of impl. an algorithm?) (Sz?)
  * bilateral filter
    * pixel distance -and- "color distance"

* Morphology
  * brief mathematical presentation?
    * SZ, pg. 128
  * consider binary case, then "general" case
    * e.g., dilation is local matrix
  * focus on instructive examples
  * dilate/erode/open/close/tophat/blackhat morph_gradient
    * some other relationships
    * e.g., max-pool is dilation with square structure elt. + downsample (1/p)
    * these can be learned:  learning framework for morphological operators
      (masci, 2013)

* image pyramids
  * technique:
    * Gaussian_0 = BaseImage
    * Gausssian_{i+1} = Gaussian(G_i) = Gauss convolve G_i, remove even row/col
    * Laplacian_{i} = G_i - UP(G_{i+1}) convolve Gauss
    * pyrup/pyrdwn ops
    * power of 2 for biggest image sizes
    * Sz says (pg 151):  "resulting [laplacian] pyramid has perfect recon" ... smallest gaussian plus laplacians --> original [really?]

  * use for blending
    * Sz pg 160.
    * http://graphics.cs.cmu.edu/courses/15-463/2005_fall/www/Lectures/Pyramids.pdf
    * these are the real deal:
      * http://www.cs.toronto.edu/~mangas/teaching/320/slides/CSC320L10.pdf
    * original paper:
      * http://cs.nyu.edu/~fergus/teaching/comp_photo/readings/spline83.pdf



* Specific gradients by filters
  * edge detectors
    * finding stable features for matching
    * matching human boundary detection
  * laplacian, sobel, scharr
    * sobel approximates a derivative on discrete grid
      * higher order also
    * scharr is better approximation for 3x3
    * laplacian
      * sum of 2nd derivatives in x,y
        * used 2nd sobel in x,y
      * blob detection
        * local peak/trough in image will max/min laplacian
  * multiple colors:
    * can take union of edges, but might thicken the edges
    * can take sum of grads, but be careful about sign cancelation
  * steering
    * filter_x * cos(th) + filter_y * sin(th)
    * ???

* distance transform
  * "find nearest zero pixel"
    * invert an edge detector
    * find distance from central points (now white)
      to nearest edge (now black)
