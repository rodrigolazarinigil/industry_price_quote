import os


def run_to_debug(target_class):
	os.environ["USER"] = "industry_user"
	os.environ["PWD"] = "password"
	os.environ["HOST"] = "localhost"
	os.environ["PORT"] = "5432"
	os.environ["DB"] = "industry_price_quote"
	target_class().run()
