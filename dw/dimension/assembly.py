import pandas as pd
import os
from definitions import ROOT_DIR
from util.db_connection import PostgresClient
from util.df_functions import df_bool_to_int, transform_str_columns, transform_float_columns


class TubeAssembly():
	
	def __init__(self, source_file="bill_of_materials.csv"):
		self.source_file = source_file
	
	def run(self):
		df = pd.read_csv(filepath_or_buffer=os.path.join(ROOT_DIR, "data", self.source_file))
		# df.rename(
		# 	columns={
		# 		"component_id": "id",
		# 		"component_type_id": "type_id"
		# 	}, inplace=True
		# )
		
		df = transform_str_columns(df, upper=True, fillna_value="N/A")
		df = transform_float_columns(df, fillna_value=0)
		df = df.melt(id_vars=["tube_assembly_id"], value_vars=["component_id", "quantity"])
		
		df.to_sql(name="tube_assembly_dimension", con=PostgresClient.get_conn_engine(), if_exists="replace")


if __name__ == "__main__":
	os.environ["USER"] = "industry_user"
	os.environ["PWD"] = "password"
	os.environ["HOST"] = "localhost"
	os.environ["PORT"] = "5432"
	os.environ["DB"] = "industry_price_quote"
	TubeAssembly().run()
