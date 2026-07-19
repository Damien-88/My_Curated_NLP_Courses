"""
Day 12: Scratch-built Binary Text Classification Pipeline
"""
import math
from tfidf_vectorizer import ManualTFIDFVectorizer

class ScratchLogisticRegression:
    """Scratch-built Logistic Regression Classifier for Binary Text Classification"""
    def __init__(self, learning_rate = 0.5, epochs = 200):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

    def sigmoid(self, z):
        """Clamp bounds to protect against math overflow errors"""
        z = max(-50.0, min(50.0, z))

        return 1.0 / (1.0 + math.exp(-z))
    
    def fit(self, X, y):
        """Fits the model to the training data using stochastic gradient descent."""
        num_samples = len(X)
        num_features = len(X[0])
        self.weights = [0.0] * num_features
        self.bias = 0.0

        for e in range(self.epochs):
            for i in range(num_samples):
                # Calculate the linear dot product combination
                linear_score = sum(X[i][j] * self.weights[j] for j in \
                                   range(num_features)) + self.bias
                prediction = self.sigmoid(linear_score)

                # Compute error gradient offset
                error = prediction - y[i]

                # Update individual weight parameters
                for j in range(num_features):
                    self.weights[j] -= self.lr * error * X[i][j]
                self.bias -= self.lr * error

    def predict_probability(self, X_item):
        """Outputs explicit fractional confidence probability metrics."""
        linear_score = sum(X_item[j] * self.weights[j] for j in \
                           range(len(self.weights))) + self.bias
        
        return self.sigmoid(linear_score)
    
    def predict(self, X_item, threshold = 0.5):
        """Converts raw probability output into binary discrete classes"""
        return 1 if self.predict_probability(X_item) >= threshold else 0
    
if __name__ == "__main__":
    # 0 = System Failure/Error Logs, 1 = Safe Success Signals
    training_data = [
        "The automated pipeline fails.",
        "System crashed due to raw database error.",
        "Processing failed inside the database engine.",
        "The data engine runs cleanly.",
        "Clean raw data feeds the pipeline engine.",
        "Execution completed successfully and cleanly."
    ]
    training_labels = [0, 0, 0, 1, 1, 1]

    # Step 1: Initialize and fit the vectorization layer
    vectorizer = ManualTFIDFVectorizer()
    vectorizer.fit(training_data)
    train_vectors = vectorizer.transform(training_data)

    # Step 2: Initialize and train the linear classification layer
    classifier = ScratchLogisticRegression(learning_rate = 0.8, epochs = 500)
    classifier.fit(train_vectors, training_labels)

    print("End-to-End Classification Engine")
    print(f"Total Model Vocab Size: {len(vectorizer.vocabulary)} features.")

    # Step 3: Run pipeline inference on unseen validation text structures
    test_docs = [
        "Database crashed and fails.",
        "The engine feeds clean logs successfully."
    ]
    test_vectors = vectorizer.transform(test_docs)

    for i, doc in enumerate(test_docs):
        prob = classifier.predict_probability(test_vectors[i])
        pred_class = classifier.predict(test_vectors[i])
        class_str = "SUCCESS" if pred_class == 1 else "FAILURE"
        print(f"Input Text: \"{doc}\"")
        print(f" -> Predicted Class: {class_str} (Confidence Score: {prob:.4f})\n")