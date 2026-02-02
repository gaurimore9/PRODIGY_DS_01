import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# Load the real dataset
data = load_breast_cancer()

# Select a continuous feature
feature_name = "mean radius"
feature_index = list(data.feature_names).index(feature_name)
values = data.data[:, feature_index]

# Create histogram
plt.figure()
plt.hist(values, bins=10)
plt.xlabel(feature_name)
plt.ylabel("Number of Samples")
plt.title("Distribution of Mean Radius (Breast Cancer Dataset)")
plt.show()
