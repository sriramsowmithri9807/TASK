from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Example of preparing features and labels
X = ...  # Features (e.g., sentiment scores)
y = ...  # Labels (e.g., stock movement: up/down)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)