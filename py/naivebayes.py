import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        n_classes = len(self.classes)

        self.mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self.var = np.zeros((n_classes, n_features), dtype=np.float64)
        self.priors = np.zeros(n_classes, dtype=np.float64)

        for idx, label in enumerate(self.classes):
            X_class = X[y == label]
            self.mean[idx, :] = X_class.mean(axis=0)
            self.var[idx, :] = X_class.var(axis=0)
            self.priors[idx] = X_class.shape[0] / float(n_samples)

    def _pdf(self, class_idx, x):
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        numerator = np.exp(-((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        posteriors = []

        for idx, label in enumerate(self.classes):
            prior = np.log(self.priors[idx])
            conditional = np.sum(np.log(self._pdf(idx, x)))
            posterior = prior + conditional
            posteriors.append(posterior)

        return self.classes[np.argmax(posteriors)]

# Example usage:
X_train = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]])
y_train = np.array([0, 0, 0, 1, 1, 1])

nb = NaiveBayes()
nb.fit(X_train, y_train)

X_test = np.array([[1, 2], [4, 3], [5, 5]])
y_pred = nb.predict(X_test)
print("Predictions:", y_pred)
