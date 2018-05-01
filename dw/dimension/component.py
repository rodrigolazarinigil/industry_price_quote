import pandas as pd
import os
from definitions import ROOT_DIR
from util.db_connection import PostgresClient
from util.df_functions import df_bool_to_int, transform_str_columns, transform_float_columns
from util.run_functions import run_to_debug
import numpy as np


class Component:
	"""
		Reads a csv file with component info and loads to a postgres.
		Just some type convertions are applied to the original data.
	"""

	def __init__(self, source_file="comp_boss.csv"):
		self.source_file = source_file

	def run(self):
		df = pd.read_csv(filepath_or_buffer=os.path.join(ROOT_DIR, "data", self.source_file))
		df.rename(
			columns={
				"component_id": "id",
				"component_type_id": "type_id"
			}, inplace=True
		)

		df["connection_type_id"] = df["connection_type_id"].replace(to_replace="9999", value=np.nan)
		df = transform_str_columns(df, upper=True, fillna_value="N/A")
		df = transform_float_columns(df, fillna_value=0)
		df = df_bool_to_int(df, ["groove", "unique_feature", "orientation"])

		df.to_sql(
			schema="industry", name="component_dimension", con=PostgresClient.get_conn_engine(),
			if_exists="append", index=False)


if __name__ == "__main__":
	run_to_debug(Component)
