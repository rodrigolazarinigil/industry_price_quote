import pandas as pd
import os
from definitions import ROOT_DIR
from util.db_connection import PostgresClient
from util.df_functions import df_bool_to_int, transform_str_columns
import numpy as np


class AnnualCost:

	def __init__(self, source_file="price_quote.csv"):
		self.source_file = source_file

	@staticmethod
	def set_cost_by_assembly(group):
		group.sort_values(by="quantity")
		group["previous_quantity"] = group["quantity"].shift(1).fillna(0)
		group_filter = group[
			(group["quantity"] >= group["ammont_to_buy"]) & (group["ammont_to_buy"] > group["previous_quantity"])
		]

		return group_filter

	def run(self):
		df = pd.read_csv(filepath_or_buffer=os.path.join(ROOT_DIR, "data", self.source_file))
		df = transform_str_columns(df, upper=True, fillna_value="N/A")
		df = df_bool_to_int(df, ["bracket_pricing"])

		df = df[df["annual_usage"] != 0]
		df["ammont_to_buy"] = df[["annual_usage", "min_order_quantity"]].max(axis=1)
		df["annual_cost"] = df["cost"] * df["ammont_to_buy"]

		df_bracket_pricing = df[df["bracket_pricing"] == 1]

		df_bracket_pricing = df_bracket_pricing.groupby(['tube_assembly_id']).apply(self.set_cost_by_assembly)
		df.loc[df["bracket_pricing"] == 1] = df_bracket_pricing

		df.to_sql(
			schema="industry", name="price_quote", con=PostgresClient.get_conn_engine(),
			if_exists="replace", index=False)


if __name__ == "__main__":
	os.environ["USER"] = "industry_user"
	os.environ["PWD"] = "password"
	os.environ["HOST"] = "localhost"
	os.environ["PORT"] = "5432"
	os.environ["DB"] = "industry_price_quote"
	AnnualCost().run()
