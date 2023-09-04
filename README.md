# lib_py
My Python Libreary

- To import lib_py modules:
    - import sys
    - import os
    - lib_py_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib_py'))
    - sys.path.append(lib_py_path)

#Initialization
    - __init__.py // not empty file

#Data_processing
  - def random_data_split(self, data_path): // split dataset with random (80% for training set and 20% for test set)
  - def save_to_csv(self, data_path, train_data_path, test_data_path):  // save split train_df and test_df
  - def distribution_NaN(self, dataset):  // count NaN distribution by column
  - def del_NaN_row(self, dataset): // delete NaN: drop lines if NaN
  - def del_NaN_column(self, dataset):  //  delete NaN: drop columns > 50% of NaN
  - def check_digits(self, cleaned_dataset): // select columns filled with digits
  - def replace_nan_to_median(self, dataset): // replace NaN by median value

  - def my_accuracy(self, X, Y, W, B)

#Bar_processing
  - def bar_processing(func): // as decorator to follow processing

#Gradient descent
  - def add_one_column(self, x): // add a column full of one and convert to numpy array
  - def ft_y_hat(self, x): // prediction: y_hat = X * theta
  - def simple_gradient(self, x, y): // vectorization
  - def gradient_descent(self, x, y, thetas, alpha, max_iter, epsilon=1e-3): // # gradient descent


