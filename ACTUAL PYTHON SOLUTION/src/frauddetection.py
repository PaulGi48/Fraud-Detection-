import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the data into a pandas DataFrame
df = pd.read_csv("data.csv")

# Split the data into a training set and a test set
X = df.drop(columns=["fraud"])
y = df["fraud"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a Random Forest classifier on the training data
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Test the classifier on the test data
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)

# Use the classifier to predict fraudulent transactions
y_pred = clf.predict(X_test)

# Calculate the confusion matrix to evaluate the performance of the classifier
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", confusion_matrix)