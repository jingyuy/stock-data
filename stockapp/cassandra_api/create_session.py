from cassandra.cluster import Cluster
from cassandra.io.libevreactor import LibevConnection
import pandas as pd

def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

def create_cassandra_session():
    cluster = Cluster()
    cluster.connection_class = LibevConnection
    session = cluster.connect('stockapp')
    session.row_factory = pandas_factory
    session.default_fetch_size = None
    return session
