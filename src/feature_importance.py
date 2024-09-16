import matplotlib.pyplot as plt
import numpy as np

def plot_feature_importance(model, X):
    feature_importances = model.feature_importances_
    indices = np.argsort(feature_importances)[::-1]
    plt.figure()
    plt.title("Feature Importance")
    plt.bar(range(X.shape[1]), feature_importances[indices])
    plt.xticks(range(X.shape[1]), [X.columns[i] for i in indices], rotation=90)
    plt.show()
