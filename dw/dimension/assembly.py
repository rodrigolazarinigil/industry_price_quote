import pandas as pd
import os
from definitions import ROOT_DIR
from util.db_connection import PostgresClient
from util.df_functions import merge_from_db
from util.run_functions import run_to_debug


class TubeAssembly:
	"""
		Reads a csv file with tube assembly info and loads to a postgres.
		- Converts all the non NA columns into rows, making it easier to summarize the components used;
		- Aggregates Assembly + Component to avoid duplicate rows;
		- Checks if it exists in component_dimension (has_component_details).
	"""

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
		df = df.groupby(['tube_assembly_id', 'component_id'])["quantity"].sum().reset_index()

		df = merge_from_db(
			df=df, schema="industry", table_name="component_dimension", column="id", left_on="component_id",
			right_on="id", indicator=True, drop_columns="id")

		df.rename(columns={"_merge": "has_component_details"}, inplace=True)
		df["has_component_details"] = df["has_component_details"].apply(func=lambda value: 1 if value == "both" else 0)

		df.to_sql(
			schema="industry", name="tube_assembly_dimension", con=PostgresClient.get_conn_engine(),
			if_exists="append", index=False)


if __name__ == "__main__":
	run_to_debug(TubeAssembly)
