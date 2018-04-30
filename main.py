import os

from dw.dimension.assembly import TubeAssembly
from dw.dimension.component import Component
from dw.fact.annual_cost import AnnualCost
from dw.fact.price_quote import PriceQuote

os.environ["USER"] = "industry_user"
os.environ["PWD"] = "password"
os.environ["HOST"] = "localhost"
os.environ["PORT"] = "5432"
os.environ["DB"] = "industry_price_quote"
Component().run()
TubeAssembly().run()
PriceQuote().run()
AnnualCost().run()
