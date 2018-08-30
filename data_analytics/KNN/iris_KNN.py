from sklearn.datasets import load_iris
from sklearn import cross_validation
from sklearn.metrics import classification_report, accuracy_score
from operator import itemgetter
import numpy as np
import math
from collections import Counter
 
# 1) given two data points, calculate the euclidean distance between them
def get_distance(data1, data2):
    points = zip(data1, data2)
    diffs_squared_distance = [pow(a - b, 2) for (a, b) in points]
    return math.sqrt(sum(diffs_squared_distance))
 
# 2) given a training set and a test instance, use getDistance to calculate all pairwise distances
def get_neighbours(training_set, test_instance, k):
    distances = [_get_tuple_distance(training_instance, test_instance) for training_instance in training_set]
    # index 1 is the calculated distance between training_instance and test_instance
    sorted_distances = sorted(distances, key=itemgetter(1))
    # extract only training instances
    sorted_training_instances = [tuple[0] for tuple in sorted_distances]
    # select first k elements
    return sorted_training_instances[:k]
 
def _get_tuple_distance(training_instance, test_instance):
    return (training_instance, get_distance(test_instance, training_instance[0]))
 
# 3) given an array of nearest neighbours for a test case, tally up their classes to vote on test case class
def get_majority_vote(neighbours):
    # index 1 is the class
    classes = [neighbour[1] for neighbour in neighbours]
    count = Counter(classes)
    return count.most_common()[0][0] 
 
# setting up main executable method
def main():
 
    # load the data and create the training and test sets
    # random_state = 1 is just a seed to permit reproducibility of the train/test split
    iris = load_iris()
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=1)
 
    # reformat train/test datasets for convenience
    train = np.array(zip(X_train,y_train))
    test = np.array(zip(X_test, y_test))
 
    # generate predictions
    predictions = []
 
    # let's arbitrarily set k equal to 5, meaning that to predict the class of new instances,
    k = 5
 
    # for each instance in the test set, get nearest neighbours and majority vote on predicted class
    for x in range(len(X_test)):
 
            print 'Classifying test instance number ' + str(x) + ":",
            neighbours = get_neighbours(training_set=train, test_instance=test[x][0], k=5)
            majority_vote = get_majority_vote(neighbours)
            predictions.append(majority_vote)
            print 'Predicted label=' + str(majority_vote) + ', Actual label=' + str(test[x][1])
 
    # summarize performance of the classification
    print '\nThe overall accuracy of the model is: ' + str(accuracy_score(y_test, predictions)) + "\n"
    report = classification_report(y_test, predictions, target_names = iris.target_names)
    print 'A detailed classification report: \n\n' + report
 
if __name__ == "__main__":
    main()