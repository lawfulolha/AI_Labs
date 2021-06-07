import numpy as np

class RBPerceptron:

    def __init__(self, number_of_epochs = 100, learning_rate = 0.1):
        self.number_of_epochs = number_of_epochs
        self.learning_rate = learning_rate

    def train(self, X, D):
        num_features = X.shape[1]
        self.w = np.zeros(num_features + 1)
        
        for i in range(self.number_of_epochs):
            for sample, desired_outcome in zip(X, D):
                prediction = self.predict(sample)
                difference = (desired_outcome - prediction)
                weight_update = self.learning_rate * difference
                
                self.w[1:] += weight_update * sample
                self.w[0] += weight_update
        
        return self

    def predict(self, sample):
        outcome = np.dot(sample, self.w[1:]) + self.w[0]
        return np.where(outcome > 0, 1, 0)
