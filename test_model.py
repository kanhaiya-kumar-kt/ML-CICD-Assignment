from model import train_model, evaluate_model


def test_model_training():
    model, X_test, y_test = train_model()

    assert model is not None
    assert len(X_test) > 0
    assert len(y_test) > 0


def test_model_accuracy():
    model, X_test, y_test = train_model()
    accuracy = evaluate_model(model, X_test, y_test)

    # The Iris model should achieve high accuracy with this fixed split.
    assert accuracy >= 0.90


def test_prediction_shape():
    model, _, _ = train_model()

    predictions = model.predict([[5.1, 3.5, 1.4, 0.2]])

    assert len(predictions) == 1
