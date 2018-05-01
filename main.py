import logging

from dw.dimension.assembly import TubeAssembly
from dw.dimension.component import Component
from dw.fact.annual_cost import AnnualCost
from dw.fact.price_quote import PriceQuote
from util.db_connection import PostgresClient

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.info("Connection to database...")
conn = PostgresClient.get_conn_engine().connect()
logging.info("Cleaning tables...")
conn.execute("TRUNCATE TABLE industry.component_dimension;")
conn.execute("TRUNCATE TABLE industry.tube_assembly_dimension;")
conn.execute("TRUNCATE TABLE industry.price_quote_fact;")
conn.execute("TRUNCATE TABLE industry.annual_cost_fact;")

logging.info("Loading components...")
Component().run()
logging.info("ok!")
logging.info("Loading tube assembly...")
TubeAssembly().run()
logging.info("ok!")
logging.info("Loading price quotes...")
PriceQuote().run()
logging.info("ok!")
logging.info("Loading annual cost...")
AnnualCost().run()
logging.info("ok!")
logging.info("PROCESS FINISHED!")
