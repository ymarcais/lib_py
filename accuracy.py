import numpy as np

class Accuracy:
    def my_accuracy(self, y, y_predict):
        correct_matches = 0
        total_samples = 0
        y_predict_first_column = y_predict[0, :]
        correct_matches = np.sum(y == y_predict_first_column)
        total_samples = y.shape[1]
        my_accuracy = 100 * correct_matches / total_samples
        return my_accuracy
    
     #f1_score calculate accuracy in multilabel classification
    def f1_score(self, y, y_pred):
        y_prediction = np.array([y_pred[0,:]])
        unique_classes = np.unique(np.concatenate((y, y_pred)))

        # Initialize arrays to store precision, recall, and f1-score for each class
        precision_scores = []
        recall_scores = []
        f1_scores = []

        # Iterate over each class
        for cls in unique_classes:
            # Compute true positives, false positives, and false negatives for the current class
            true_positives = np.sum((y == cls) & (y_prediction == cls))
            false_positives = np.sum((y != cls) & (y_prediction == cls))
            false_negatives = np.sum((y == cls) & (y_prediction != cls))

            # Calculate precision and recall for the current class
            precision = true_positives / (true_positives + false_positives + 1e-10)
            recall = true_positives / (true_positives + false_negatives + 1e-10)

            # Calculate the F1-score for the current class
            f1 = 2 * (precision * recall) / (precision + recall + 1e-10)

            # Append the scores to the respective lists
            precision_scores.append(precision)
            recall_scores.append(recall)
            f1_scores.append(f1)

        macro_precision = 100 *np.mean(precision_scores)
        macro_recall = 100 *np.mean(recall_scores)
        macro_f1_score = 100 * np.mean(f1_scores)
        return macro_f1_score, macro_recall, macro_precision