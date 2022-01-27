Neural Networks
  * just a fancy, tunable way to get an f (i.e., f(data)->tgt) when given data and tgt
  * trivial example
    * [or gate in wk 8 notebook]
  * components
    * nodes/layers/activations
      * nodes are the primitive elements:  
        out = activation(f(in) + bias)
        * [ref tf/wk03 25, 41]
      * f is typically dot-product (sum-of-squares) between in and weights of the node (we initialize the weights with constants and/or random values; then learning is the process of finding "good" weights")
      * activation:
        * an example (and perhaps most common) activation function is  the "sigmoid"
          * [ref: tf/wk3 46,47,56,57]
        * many modern networks use ReLU units:
          * [ref: tf/wk3 66,67]
      * layers and networks
        * [ref: tf/wk3 58-62; 74-79]
        * I/O layers
          * input layer depends on form of raw data and first level of our architecture
          * output layer depends on last layer of our architecture and what type of prediction we want to make (regression versus classification)
  * training
    * optimization and loss
      * gradient descent
        * [ref tf/wk2 17-33 no math]
        * [ref tf/wk2 notebook]
      * other options
    * batches / epochs
      * [ref:  tf/wk4 2-18]
      * epoch
        * one epoch == one pass through the entire dataset
        * in the general case, too big for system memory; can't do this all in one go
        * general measure of amount of training (how many epochs should I perform?)
      * batches
        * how much data do we use for one training step
          * one training step takes us from "old network weights" to "new network weights"
        * could use *all* of the examples at one time (but terrible performance -- if it is even possible; we'll constantly be swapping memory to slow disks))
        * could use one example at a time (but terrible performance ... it doesn't take advantage of caching, vectorized ops, etc.)
        * good data processing size for vectorized operations
  * special issues with overfitting
    * even very simple NN architectures can approximate arbitrarily complex functions very well (consequence of universal representation theorem) [three layers, finite # nodes ... although better approximations may require n->"big"]
    * so, many architectures can overfit very easily ... by simply chugging through the data over-and-over (memorizes data, doesn't learn the generality)
    * traditionally we control this by monitoring the performance on a test set .... as long as it improves, we're good.  when it starts going the wrong way, we stop.
    * modern method is using a technique called "dropout":  randomly have nodes disappear from the network and everyone else still has to perform.  this means that the overall network has to be more robust, single nodes can't be too important, and (most importantly from a technical perspective) the nodes can't all be highly correlated with one another [diff. nodes must respond to diff. "stimuli"]
      * [ref:  tf/wk4 70-81]
  * architectures
    * mlp
      * [this is basically the example under "layers" above]
    * cnn
      * motivation
        * [ref tf/wk5: 3,4]
        * invariance, parameters
      * kernels (just like our image processing kernels)
        * but we *learn* their weightings (instead of assuming Gaussian, etc.)
        *  [ref tf/wk5:  8-15 + notebook/gif]
      * pooling layers
        * [ref tf/wk5:  31-35]
      * an example:  lenet
        * [ref tf/wk 5:  37-53]
