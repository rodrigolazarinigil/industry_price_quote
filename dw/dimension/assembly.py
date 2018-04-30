import pandas as pd
import os
from definitions import ROOT_DIR
from util.db_connection import PostgresClient
from util.run_functions import run_to_debug


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

		df.rename(
			columns={
				"tube_assembly_id": "id"
			}, inplace=True
		)

		df.to_sql(
			schema="industry", name="tube_assembly_dimension", con=PostgresClient.get_conn_engine(),
			if_exists="append", index=False)


if __name__ == "__main__":
	run_to_debug(TubeAssembly)
