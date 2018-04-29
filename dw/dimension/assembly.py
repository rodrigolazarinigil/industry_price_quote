import pandas as pd
import os
from definitions import ROOT_DIR
from util.db_connection import PostgresClient
from util.df_functions import transform_str_columns, transform_float_columns, merge_from_db
import numpy as np


class TubeAssembly:

	def __init__(self, source_file="bill_of_materials.csv"):
		self.source_file = source_file

	def run(self):
		df = pd.read_csv(filepath_or_buffer=os.path.join(ROOT_DIR, "data", self.source_file))

		df = pd.wide_to_long(
			df=df,
			stubnames=["component_id", "quantity"],
			i="tube_assembly_id",
			j="order",
			sep="_"
		).reset_index(). \
			sort_values(["tube_assembly_id", "order"]). \
			drop("order", axis=1)  # type: pd.DataFrame

		df = df.dropna(subset=["component_id"])

		# df = merge_from_db(
		# 	df=df, schema="industry", table_name="component_dimension", column="sk_component",
		# 	left_on="component_id", right_on="id", drop_columns=["id"])

		df.rename(
			columns={
				"tube_assembly_id": "id"
			}, inplace=True
		)

		df.to_sql(
			schema="industry", name="tube_assembly_dimension", con=PostgresClient.get_conn_engine(),
			if_exists="append", index=False)


if __name__ == "__main__":
	os.environ["USER"] = "industry_user"
	os.environ["PWD"] = "password"
	os.environ["HOST"] = "localhost"
	os.environ["PORT"] = "5432"
	os.environ["DB"] = "industry_price_quote"
	TubeAssembly().run()
