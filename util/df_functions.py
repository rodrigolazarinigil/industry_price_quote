import pandas as pd

from util.str_functions import boolstr_to_int


def df_bool_to_int(df: pd.DataFrame, column_list: list):
	for col in column_list:
		df[col] = df.apply(lambda row: boolstr_to_int(row[col]), axis=1)
	
	return df


def transform_str_columns(df: pd.DataFrame, upper: bool = True, fillna_value: str = "N/A"):
	for col in df.columns:
		if df[col].dtype == "object":
			if upper:
				df[col] = df[col].str.upper()
			
			df[col].fillna(fillna_value, inplace=True)
	
	return df


def transform_float_columns(df: pd.DataFrame, fillna_value=0):
	for col in df.columns:
		if df[col].dtype == "float64":
			df[col].fillna(fillna_value, inplace=True)
	
	return df


def clean_str_values(
		df: pd.DataFrame, column_list: list, remove_accent: bool = True, str_case: str = '',
		fillna_value: str = "N/A"):
	for column in column_list:
		if str_case == 'UPPER':
			df[column] = df[column].str.upper()
		if remove_accent:
			df[column].replace("[ÀÁÂÃÄÅ]", 'A', regex=True, inplace=True)
			df[column].replace("[ÈÉÊË]", 'E', regex=True, inplace=True)
			df[column].replace("[ÌÍÎÏ]", 'I', regex=True, inplace=True)
			df[column].replace("[ÒÓÔÕÖ]", 'O', regex=True, inplace=True)
			df[column].replace("[ÙÚÛÜ]", 'U', regex=True, inplace=True)
			df[column].replace("[ÝŸ]", 'Y', regex=True, inplace=True)
			df[column].replace("[Ç]", 'C', regex=True, inplace=True)
		if fillna_value is not None:
			df[column].fillna(fillna_value)
	
	return df
