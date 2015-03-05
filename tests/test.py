from jnpr.junos.op.phyport import *
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def test_checkroute(self):
        dev = Device(user='root', host='10.12.0.77', password='Password1!')
        dev.open()

        route_table = RouteTable(dev)

        routes = route_table.get('123.123.123.1/24')

        # Checks for a single route recieved via BGP. Uncomment to enable
        self.assertEqual(len(routes), 1)

        # Passes unit test automatically
        #self.assertEqual(1, 1)

        print "success"


if __name__ == '__main__':
    unittest.main()
