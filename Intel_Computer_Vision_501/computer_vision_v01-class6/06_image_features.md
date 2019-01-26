Image Features

*  What are image features?
  * "interesting" locations in an image
    * feature detection -> feature description -> uses
  * uses
    * [add images for these]
    * matching
    * classification (object recognition)
    * tracking of features in motion
    * image stitching
    * object detection
  * interesting means "things that might help us perform these *uses*"
  * The techniques that follow can be used for "any" of the use-cases above.  however, they are typically developed by a research group to solve one use-case and others typically follow that lead.

* Corners
  * [add images for these]
  * Harris Corners and Shi-Tomasi
    * generic matrix algorithm:
      * sz pg 214 and discussion before
      * ellipse on pg 213 with geometry of ellipse
    * LOCV:  pg 317
      * correlation between gradients in x and y directions
      * invariant to rotation (b/c of eigenvalues)
      * Harris used (det(H) - trace(H) * wgt) < Thresh
      * ST use min(eig) < Thresh
  * subpixel methods
    * locv: pg 321

* HOG
  * [references:]
    * https://www.learnopencv.com/histogram-of-oriented-gradients/
    * link has enough detail to explain it
      * and do a generic implementation
      * and then talk about sift/surf/etc. below in relationship to it
    * Sz. 666 has discussion

  * distribution of the directions of the gradients
    * (histogram ~ distribution; oriented gradients == direction of gradient)

  * originally for locating pedestrians in a scene
    * so, many of the constants are tuned for recognizing humans
    * patch aspect of 2 (tall) to 1 (wide) b/c humans are like tall rectangles
    * cell size of 8x8 b/c it captures human features like eyes,

  * [note, use these terms for consistency:]
    * image -> ROI -> (frames for normalization) -> cells
    * features produced by HOG are the histograms from the cells
    * HOG is described in terms of one ROI but many steps can be
      pre-computed on the whole image

  * image -> a patch [fixed aspect ratio:  1:2]
    * crop to region of interest/resize to proper aspect ratio
  * calculate horizontal/vertical gradients (for each color)
    * convolve with [-1,0,1] kernels (aka Sobel)
  * consider the component wise gradients (x,y grads) in polar coordinates
    * x,y -> r, theta [graphic]
    * at every pixel take max r (magnitude) over the three color channels
    * associated direction is the theta of that max r
  * on 8x8 cells, we make a histogram as follows:
    * the buckets are angles (theta) at 0, 20, 40, ..., 160 [9 buckets]
    * we assign the magnitude (r) of a pixel to its angle (th) bucket
    * for angles between buckets, we divide it proportionally to distance from the buckets
      * i.e., 10 -> 1/2 into 0  bucket and 1/2 into 20 bucket
      * and   15 -> 3/4 into 20 bucket and 1/4 into  0 bucket
  * using a sliding 16x16 window (of 4 histograms each time) we create a mega-cell/mega-histogram with 36 total values.  we normalize this wrt L2 norm.  this becomes one block of features.  we slide the window 8 pixels over and repeat.  [note, this means that some pixels will be re-normalized many times ... and with respect to different neighborhoods extending in different directions.]
  * on a 128x64 image we have 16x8 cells that are 8x8.  We have 15x7 mega-cells ... which gives us 105 blocks of 36 features ... which gives us 3780 total features (for this patch).

* SIFT/SURF/FAST/BRIEF
  * [References]
    * [see Sz. pg 222]
    * https://wwwpub.zih.tu-dresden.de/~cvweb/teaching/Courses/WS_2014_15/HS/UpdateOnFeatures_StefanHaller.pdf
    * http://www.scholarpedia.org/article/SIFT
    * wikipedia entries are decent

  * SIFT:
    * detection:
      * find candidate keypoints by finding extrema versus neighbors in Gaussian pyramid (same scale and high/lower resolutions)
      * reduce candidates by filtering out points with low contrast and on edges
    * description
      * neighborhood proportional to level of the extrema
      * estimate orientation in neighborhood around keypoint
      * compute histogram of gradients in this neighborhood
      * normalize histogram
    * matching:
      * euclidean distance between keypoint descriptors

  * SURF:
    * similar to SIFT but relies on several approximations and tricks
    to speed the processes
      * integral images, box-filter to approximate Gaussian smoothing
      * Hessian (matrix of mixed second-order derivatives) matrix to find both extrema and scale (via its determinant -- i.e., the determinant of the matrix of partial second-order derivatives! LOL)
      * uses wavelet responses for orientation and description
        * in turn, these calculations are sped-up by the use of the integral image

  * FAST:
    * quick corner detector
    * identifies points where much of an arc around it is all the same color (and different from the center)
      * image the corner of a building against a blue sky:  from around 9 o'clock to 6 o'clock will be blue and the center point will be tan/brown/brick-red/etc.
      * uses a trivial first test to rule out the big arc (check 12/6 then 3/9 for sameness)
    * finds corners, no real descriptor built in

  *  BRIEF
    * [reference:]
      * https://gilscvblog.com/2013/08/18/a-short-introduction-to-descriptors/
      * https://gilscvblog.com/2013/09/19/a-tutorial-on-binary-descriptors-part-2-the-brief-descriptor/
    * descriptors can be too verbose
      * hard to learn from, hard to match, inefficient space use
      * various means to compress:  PCA, hashing, etc.
    * Hashing converts vectors to binary strings which are then often compared with hamming distance (binary off/on)
    * BRIEF goes directly from pixels -> binary numbers
      * fixed set of pairs of points (p_i, p_j) (that are selected once, permanently) by sampling from a random distribution
      * binary values is whether p_i > p_j

* ORB (=FAST+BRIEF w/o IP problems)
  * https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_orb/py_orb.html
  > ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance. First it use FAST to find keypoints, then apply Harris corner measure to find top N points among them. It also use pyramid to produce multiscale-features

  * ORB adds orientation to FAST
  * and integrates orientation information in the BRIEF descriptors


* Feature Matching
  * [reference:  Sz 225-234]
    * ignore techniques that are not directly related to what we've discussed above [e.g., MOPS]
  * naive - all features against all others (quadratic time)
    * better:  hashing
      * map features -> fixed buckets
      * return buckets like me [family address, check members of family]
    * locality sensitive hashing (LSH)
    * kd trees

  * techniques
    * [fixme:  where was this from?  Sz, i think]
    * distance -> rank
    * nearest neighbors

  * evaluation via confusion matrix
    * [get materials form metis/capone bootcamp]
      * from:
      * /Users/mfenner/repos/metis/cap1_ds_curriculum/
         day_06/students/classification_error_metrics_slides.pdf
    * tp/fp/tn/fn
    * acc/tpr/fpr/precision=ppv/recall=1-tpr(?)
    * roc/AUC
    * use optimums/tradeoffs to set distance threshold

exercises:
  * for week 6:
    * incorporate segmentation -> features

  * [for week 7]:  images -> features -> nearest-neighbors
    * heh, also for week 7:
      * MNIST ... with noise, with rotation, with shearing
