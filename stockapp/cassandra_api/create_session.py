from cassandra.cluster import Cluster
from cassandra.io.libevreactor import LibevConnection

def create_cassandra_session():
    cluster = Cluster()
    cluster.connection_class = LibevConnection
    session = cluster.connect('stockapp')
    return session
