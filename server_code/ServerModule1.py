import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def record_name(name):
  app_tables.visitors.add_row(name=name, when=datetime.now())