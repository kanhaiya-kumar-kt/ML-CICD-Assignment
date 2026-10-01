from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model():
    """Load Iris data, train a Random Forest model, and return model and test data."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target,
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    """Calculate model accuracy."""
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)


def main():
    model, X_test, y_test = train_model()
    accuracy = evaluate_model(model, X_test, y_test)

    # Example prediction
    sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(sample)[0]

    iris = load_iris()
    predicted_class = iris.target_names[prediction]

    print("ML Model: Random Forest Classifier")
    print("Dataset: Iris")
    print(f"Model Accuracy: {accuracy:.2%}")
    print(f"Example Prediction: {predicted_class}")

    return accuracy


if __name__ == "__main__":
    main()
