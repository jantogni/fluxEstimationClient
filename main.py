from flux_estimation_lib import *

def main():
    #Using default URL
    #flux = fluxEstimation('J1617-5848', '31-May-2015', '3.43e+11', verbose = 'false', test = 'true', weighted ='true')
    flux = fluxEstimation('J1617-5848', '31-May-2015', '3.43e+11', verbose = 'false', test = 'true', weighted ='false')

    #Using custom URL
    #bender_url = 'http://bender.csrg.cl:2121/bfs-0.1/ssap'
    #flux = fluxEstimation('J0319+4130', '26-April-2014', '1.0349e+11') 
    flux.performQuery()
    flux.parseResponse()
    
    #print flux.data.asList()
    for row in flux.data:
        print "----------------------------------"
        print row.asDict()
        #print row.asList()
    print "----------------------------------"

if __name__ == "__main__":
    main()
