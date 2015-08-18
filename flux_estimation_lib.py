import urllib
import urllib2
from astropy.io.votable import parse
import warnings
import os

#Hide warning from votable parse
warnings.filterwarnings("ignore")

#Default values
DEF_URL             = 'http://vo-prototype-test.sco.alma.cl:8080/bfs-0.2/ssap'
DEF_URL_ASA         = 'http://asa-test.alma.cl/bfs/'
DEF_URL_localhost   = 'http://localhost:8080/ssap'
DEF_URL_bender      = 'http://bender.csrg.cl:2121/bfs-0.1/ssap'

class data:

    def __init__(self, maskedArray, index):
        """
        Constructor of data class
        """
    
        self.src_name  = maskedArray['SourceName'][index]
        self.freq  = maskedArray['Frequency'][index]
        self.date  = maskedArray['Date'][index]
        self.flux  = maskedArray['FluxDensity'][index]
        self.sigmaB  = maskedArray['FluxDensityError'][index]
        self.alpha  = maskedArray['SpectralIndex'][index]
        self.sigmaA  = maskedArray['SpectralIndexError'][index]
        self.error2  = maskedArray['error2'][index]
        self.error3  = maskedArray['error3'][index]
        self.error4 = maskedArray['error4'][index]
        self.warning  = maskedArray['warning'][index]
        self.verbose  = maskedArray['verbose'][index]
        self.not_ms  = maskedArray['notms'][index]

    def asDict(self):
        """
        Return data as python dict
        """

        data_dict = { 'SourceName' : self.src_name,
                      'Frequency' : self.freq,
                      'Date' : self.date,
                      'FluxDensity' : self.flux,
                      'FluxDensityError' : self.sigmaB,
                      'SpectralIndex' : self.alpha,
                      'SpectralIndexError' : self.sigmaA,
                      'error2' : self.error2,
                      'error3' : self.error3,
                      'error4' : self.error4,
                      'warning' : self.warning,
                      'verbose' : self.verbose,
                      'not_ms' : self.not_ms}

        return data_dict

    def asList(self):
        """
        Return data as python list
        """

        data_list = [ self.src_name,
                      self.freq,
                      self.date,
                      self.flux,
                      self.sigmaB,
                      self.alpha,
                      self.sigmaA,
                      self.error2,
                      self.error3,
                      self.error4,
                      self.warning,
                      self.verbose,
                      self.not_ms ]

        return data_list

class fluxEstimation:

    def __init__(self, name, date, frequency, url = None, test = None, verbose = None, weighted = None):
        """
        Constructor FluxEstimation class
        """

        self.name = name
        self.date = date
        self.frequency = frequency

        if not url:
            self.url = DEF_URL
        else:
            self.url = url
        
        if not test:
            self.test = 'false'
        else:
            self.test = test
    
        if not verbose:
            self.verbose = 'false'
        else:
            self.verbose = verbose

        if not weighted:
            self.weighted = 'false'
        else:
            self.weighted = weighted

    def performQuery(self):
        """
        Perform query in the webservice using the given parameters
        """

        values = {  'NAME' : self.name,
                    'DATE' : self.date,
                    'TEST' : self.test,
                    'VERBOSE' : self.verbose,
                    'FREQUENCY' : self.frequency, 
                    'WEIGHTED': self.weighted }

        data = urllib.urlencode(values)
        response = urllib2.urlopen(self.url + '?' + data)
        self.votable = response.read()

    def parseResponse(self):
        """
        Parse response from the webservice to python dict
        """

        f = open('tmp_votable', 'w')
        f.write(self.votable)
        f.close()

        votable = parse('tmp_votable', pedantic=False)

        os.remove('tmp_votable')

        table = votable.get_first_table()

        self.data = []

        for i in range(table.array.size):
            self.data.append(data(table.array, i))

