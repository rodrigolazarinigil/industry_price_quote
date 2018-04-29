import pandas as pd
import os
from definitions import ROOT_DIR
from util.db_connection import PostgresClient
from util.df_functions import df_bool_to_int, transform_str_columns


class PriceQuote:

	def __init__(self, source_file="price_quote.csv"):
		self.source_file = source_file

	def run(self):
		df = pd.read_csv(filepath_or_buffer=os.path.join(ROOT_DIR, "data", self.source_file))
		df = transform_str_columns(df, upper=True, fillna_value="N/A")
		df = df_bool_to_int(df, ["bracket_pricing"])

		df.to_sql(
			schema="industry", name="price_quote_fact", con=PostgresClient.get_conn_engine(),
			if_exists="replace", index=False)


if __name__ == "__main__":
	os.environ["USER"] = "industry_user"
	os.environ["PWD"] = "password"
	os.environ["HOST"] = "localhost"
	os.environ["PORT"] = "5432"
	os.environ["DB"] = "industry_price_quote"
	PriceQuote().run()
