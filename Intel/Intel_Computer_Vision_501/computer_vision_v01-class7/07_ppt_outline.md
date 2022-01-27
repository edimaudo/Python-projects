High level overview:
http://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html
Useful reference:  don't get into the weeds.
http://scikit-learn.org/stable/user_guide.html

Note:  use *feature* when talking about *learning* stuff.  use *descriptor* when talking about image stuff.

Learning:
  * Simple classification example/intution
    * [see: Supervised_Learning__Classification_LogisticR_KNN.pptx - slides 1-20 or so]
    * [do in terms of an image problem]
  * Evaluation techniques
    * Last week we looked at evaluation metrics, now we'll look at effectively estimating these for a learner:
    * [see: model_selection_ii.pptx]
    * train-test
    * cross-validation
    * LOO (leave-one out)
  * techniques I: knn
    * [see: Supervised_Learning__Classification_LogisticR_KNN.pptx - slides 76 - end]
    *  memorize the data:  for new case, find old data like me ... take a vote
  * techniques II: svm
    * [similar content to what is here: https://jakevdp.github.io/PythonDataScienceHandbook/05.07-support-vector-machines.html ]
    * separate points with a line
      * "maximum-margin" is SVM's preferred line
      * can apply "kernel" to handle non-linear borders
    * for new data, see which side of the line it falls on
  * PCA
    * [see: feature_selection_extraction_dimensionality_reduction.pptx]
    * data as a point-cloud
    * fit ellipse, find perpendicular axes (directions of maximum variation)
    * describe data in terms of these directions (orient the data in a new way)
  * using sklearn
    * basic build/fit/predict scenario
    * GridSearch
      * specify a space of parameters and evaluate model(s) at those params
    * Pipelines
      * create a built/fit/predict-able sequence of steps
      * "fitting" will fit each of the components in turn
        * [nb has example with pca -> svm for eigenfaces]

  * Bag-of-words learning
    * complicated architecture
      [see:  https://kushalvyas.github.io/BOV.html]
      [but:  we need to develop our own graphics and workflow diagrams]
    *  essentially:
      1.  take known image and find descriptors of keypoints
        [have images in terms of individual, custom vocabularies - a vocabulary in a "regional dialect"].  repeat for all images.
      2.  combine *all* individual descriptors (regional vocabularies) and then group similar descriptors together
      [create a common, global vocabulary of some "small" - 20ish - number of "words" - similar descriptors that can replace the many different "regional dialects"]
      3.  redescribe known images in terms of the global vocabulary
      [one of my terms was in "region specific dialect" (soda, pop, Coke, etc.); replace with global vocabulary term ("soft drink") -- one of the 20].  create a histogram of the counts of my global vocabulary terms.
      4.  build a SVM model predicting from (histograms --> object class)
      5.  with a new example:  describe in "regional" vocabulary, convert to global vocabulary (regional word to "most similar" global word), create histogram representation, feed to SVM to make prediction.
    * details:
      * local vocabularies come from feature descriptors (sift, orb, etc.)
      * global vocabulary comes from clustering the local vocabularies
        *  convert regional->global by looking up cluster (global term) for a "local" descriptor
      * image described in terms of counts (histogram):  
        * global term 1, # local descriptors that mapped to it
        * global term 2, # local descriptors that mapped to it
        * etc.
      * simple table of data:
        * columns are global terms; rows are per-image
        * labeled by class (i.e.,airplane, not image 3)
      * run it through an svm
