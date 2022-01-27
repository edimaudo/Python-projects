* Contours
  * overview:  a contour is an assembled collection of edges that (hopefully) represent one object in the image
  * opencv tools
    * cv2.findContours from Canny edges or a thresholded image (edges are boundaries between white and black)
    * contour hierarchy
      * locv: pg 235
    * returned structure of contours (LOCV: 237):
      * represent each contour (a sequence of points) in relationship to other contours
      * CV_RETR_EXTERNAL, CV_RETR_LIST, CV_ RETR_CCOMP, or CV_RETR_TREE
      * (h_prev, h_next, v_prev, and v_next)
  * statistics and geometry
    * [see NB and LOCV:  near 244]
    * bounding boxes/enclosures
    * length, area, etc.
    * moments, hu moments
  * drawing contours:  cv2.drawContours
    * see notebook example

* segmentation
  * foreground/background separation
    * send foreground on for further analysis
      * cars in security camera
      * skin within an image (reduces complexity of finding faces)
    * superpixels
      * groups of pixels in same object/type of object
  * some methods from image processing "segment" the image
    * morphology, flood fill, thresholding
    * pyramid segmentation builds on top of pyramids
      * locv:  pg 132
  * mean shift
    * locv: pg 300
    * see: pyrMeanShiftFiltering
  * grabcut
    * a graph cutting techniques
      * sz. pg. 300
    * [grabcut - sz. pg 296 --> 302]
  * watershed
    * sz. pg 285
    * locv: pg 295

* matching
  * matching with moments
    * comparing two contours (outlines) for similarity
    * locv: 251-257
  * template matching
    * find one image within another
    * locv: 214
  * histogram backprojection
    * progressing towards object recognition
      * but better thought of as segmentation to foreground ROIs used for further processing
    * histogram of pixels in image match histogram model
    * also "patch-wise" within an image
    * slides 24 and 26 here:
      * http://www.lira.dist.unige.it/teaching/SINA_08-09/slides-prev/sina-image-processing-point.pdfee
