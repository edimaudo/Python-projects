import numpy as np

# prints a textual represention of a sklearn.tree.DecisionTreeClassifier
def print_dt(estimator, feature_names=None, class_names=None, indent="\t"):
    n_nodes = estimator.tree_.node_count
    children_left = estimator.tree_.children_left
    children_right = estimator.tree_.children_right
    # convert feature index to feature name
    def feature2label(k):
        return 'X[:, %d]'%k if feature_names is None else feature_names[k]
    feature = list(map(feature2label,estimator.tree_.feature))
    threshold = estimator.tree_.threshold
    # convert target index to target name
    def values2label(k):
        values = estimator.tree_.value[k][0]
        if class_names is None:
            values = values[np.argsort(estimator.classes_)]
            return list(map(str,values))
        else:
            return ['%s=%d'%(class_names[estimator.classes_[f]],n) for f,n in enumerate(values) ]

    # The tree structure can be traversed to compute various properties such
    # as the depth of each node and whether or not it is a leaf.
    node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
    is_leaves = np.zeros(shape=n_nodes, dtype=bool)
    stack = [(0, -1)]  # seed is the root node id and its parent depth
    while len(stack) > 0:
        node_id, parent_depth = stack.pop()
        node_depth[node_id] = parent_depth + 1

        # If we have a test node
        if (children_left[node_id] != children_right[node_id]):
            stack.append((children_left[node_id], parent_depth + 1))
            stack.append((children_right[node_id], parent_depth + 1))
        else:
            is_leaves[node_id] = True

    print("The binary tree structure has %d nodes (depth=%d) and has "
          "the following tree structure:"
          % (n_nodes, np.max(node_depth)))
    for i in range(n_nodes):
        if is_leaves[i]:
            values_dist = values2label(i)
            values_dist = ' [%s]'% (','.join(values_dist))
            cls = np.argmax(estimator.tree_.value[i][0])
            cls = estimator.classes_[cls]
            if class_names is not None:
                cls = class_names[cls]
            print("%snode=%s leaf node. [class=%s] %s" % (node_depth[i] * indent, i, cls, values_dist))
        else:
            print("%snode=%s test node: go to node %s if %s <= %s else to "
                  "node %s."
                  % (node_depth[i] * indent,
                     i,
                     children_left[i],
                     feature[i],
                     threshold[i],
                     children_right[i],
                     ))
    print()


try:
    from sklearn.externals.six import StringIO  
    from sklearn.tree import export_graphviz
    import pydotplus
    from IPython.display import Image  

    # plots a tree represention of a sklearn.tree.DecisionTreeClassifier
    # requires graphviz [https://www.graphviz.org/]
    def plot_dt(model, feature_names=None, class_names=None):
        dot_data = StringIO()
        export_graphviz(model, out_file=dot_data,
                        filled=True, rounded=True,
                        special_characters=True, feature_names=feature_names, class_names=class_names)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        return Image(graph.create_png())
except:
    def plot_dt(model, feature_names=None, class_names=None):
        raise "Failed to load a prerequisite package"

