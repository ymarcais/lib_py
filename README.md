# lib_py
My Python Libreary

#Data_processing
  - def random_data_split(self, data_path): // split dataset with random (80% for training set and 20% for test set)
  - def save_to_csv(self, data_path, train_data_path, test_data_path):  // save split train_df and test_df
  - def distribution_NaN(self, dataset):  // count NaN distribution by column
  - def del_NaN_row(self, dataset): // delete NaN: drop lines if NaN
  - def del_NaN_column(self, dataset):  //  delete NaN: drop columns > 50% of NaN
  - def check_digits(self, cleaned_dataset): // select columns filled with digits
  - def replace_nan_to_median(self, dataset): // replace NaN by median value
