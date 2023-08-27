import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class Data_processing:
	
    # split dataset with random (80% for training set and 20% for test set)
	def random_data_split(self, data_path):
		data = pd.read_csv(data_path)
		train_df=[]
		test_df=[]

		random_figures = np.random.choice([1, 0], size=x, p=[0.8, 0.2])
		for i in range(x):
			if random_figures[i] == 1:
				train_df.append(data.iloc[i])
			else:
				test_df.append(data.iloc[i])
		return train_df, test_df

    # save split train_df and test_df
	def save_to_csv(self, data_path, train_data_path, test_data_path):
		train_df, test_df = self.random_data_split(data_path)
		train_df = pd.DataFrame(train_df)
		test_df = pd.DataFrame(test_df)
		train_df.to_csv(train_data_path, index=False)
		test_df.to_csv(test_data_path, index=False)
	
    #count NaN distribution by column
	def distribution_NaN(self, dataset):
		NaN_distribution = []
		for idx, column in enumerate(dataset.columns):
			num_NaN = dataset[column].apply(lambda x: pd.isna(x)).sum()
			if num_NaN > 0:
				NaN_distribution.append([column, num_NaN])
		return NaN_distribution
	
	#delete NaN: drop columns > 50% of NaN
	def del_NaN_column(self, dataset):
		rows = dataset.shape[0]
		NaN_distribution = pd.DataFrame(self.distribution_NaN(dataset))
		columns_to_drop = []
		for index, row in NaN_distribution.iterrows():
			if NaN_distribution[1][index] / rows > 0.5:
				columns_to_drop.append(NaN_distribution[0][index])
				dataset = dataset.drop(columns=columns_to_drop, axis=1)
		return dataset

	#delete NaN: drop lines if NaN
	def del_NaN_row(self, dataset):
		dataset = pd.DataFrame(dataset)
		cleaned_dataset = dataset.dropna(axis=0)
		return cleaned_dataset
	
	#select columns filled with digits
	def check_digits(self, cleaned_dataset):
		digit_columns = []
		for column in cleaned_dataset.columns:
			is_only_digits = cleaned_dataset[column].apply(lambda x: isinstance(x, (float, int)))
			if is_only_digits.all() and cleaned_dataset[column].notnull().all():
				digit_columns.append(column)
			is_only_digits = cleaned_dataset[digit_columns]
		return is_only_digits