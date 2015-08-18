from flux_estimation_lib import *
import unittest

class simpleTest(unittest.TestCase):
    def setUp(self):
        pass

    def testConect(self):
        try:
            flux = fluxEstimation('3c279', '04-Apr-2014', '231.435E9', verbose = 'false', test = 'false')
            flux.performQuery()
            flux.parseResponse()
        except:
            flux.data = None
        self.assertTrue(flux.data != None)

    def testNonNull(self):
        try:
            flux = fluxEstimation('3c279', '04-Apr-2014', '231.435E9', verbose = 'false', test = 'false')
            flux.performQuery()
            flux.parseResponse()
            element = flux.data[0].asDict()['FluxDensity']
        except:
            flux = None
            element = None

        self.assertTrue(element != None)

    def testFrequencies(self):
        try:
            flux = fluxEstimation('3c279', '04-Apr-2014', '231.435E9,231.435E9,231.435E9', verbose = 'false', test = 'false')
            flux.performQuery()
            flux.parseResponse()
            element = flux.data[0].asDict()['FluxDensity']
            element = flux.data[1].asDict()['FluxDensity']
            element = flux.data[2].asDict()['FluxDensity']
        except:
            flux = None
            element = None

        self.assertTrue(element != None)
        

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
