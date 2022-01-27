* Computer arithmetic
  * integer sizes
  * floating point issues (?)

* Display and interpolation
  * opencv's interpolation
    * LOCV pg. 130
    * comments on methods in PICV
  * matplotlib interpolation
    * https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html
    * big->small "none" (not None)
    * small->big "nearest"

* foreground/background
  * building/interpret image as fore/back
  * [NB has example, verbalize it]

* histograms and color spaces
  * color spaces
    * grayscale, rgb, hsv
      * get hsv/hsl cone/cylinders
    * numeric representations in matplotlib (vmin,vmax)
    * representation in opencv
      * LOCV:  59/60
  * histogram equalization
    * probability integral transform (wikipedia)
    * http://math.arizona.edu/~jwatkins/f-transform.pdf
    * https://www.math.uci.edu/icamp/courses/math77c/demos/hist_eq.pdf
    * LOCV:  pg. 189
    * CDF, linear interpolation (is this on the xform result?)
      *   linear interpolation (`np.interp`)
    * for colors, convert to hsv, apply to V
  * histogram comparison
    * methods: LOCV pg 201/203
    * application: LOCV pg 205
      * finding skin based on color in an image
  * 1D & 2D histograms

 * thresholding
   * use:
     * "final" decisions about points
     * mark regions of interest (fore/back) --> mask
   * simple methods
     * LOCV: pg 136
     * pure thresh; thresh back -> 0, fore -> its value; similar
   * neighborhood methods
     * (adaptive)  used when uneven illumination
     * local neighborhood:
       * value from mean (equal weight) or weighted-average based on Gaussian
       * compute value, subtract C ---> threshold for that neighborhood
   * otsu's method
     * essentially Fishers LDA for 1D (no class), discrete data
     * iterates and applies classes hypothetically
     * t-tests, F-tests and Otsu’s Methods for Image Thresholding

* geometric transforms
  * good stuff in szeliski
  * resizing
    * x,y -> f_x(x,y), f_y(x,y)
    * increasing resolution (creating data from "nothing")
      requires interpolation
      * interpolation methods (see Dawson, ch 5.5)
        * can result in fractional values
        * nearest neighbor rounds to fill integer pixel spots
        * also more complicated methods
        * bilinear:  average in 2D (see wiki graphic)
        * bicubic:  cubic fit in 2D over 4x4 window
    * decreasing resolution (throwing out data) requires "decimation"
      * convolve with low-pass; keep rth sample points
        * in reality, only eval convolution at rth points

  * affine, perspective
    * szeliski, pg. 36-38
    * matrix representations
      * translate, rotate, translate+rotate, scaling, affine
    * point mapping
    * intuition, line-ness (parallel -> parllel, etc.)
