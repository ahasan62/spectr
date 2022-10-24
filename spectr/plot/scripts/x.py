from encodings import normalize_encoding
# from this import d
import xmltodict, json 
url = "SF/C2H2_1221_HITRAN04_v3.000_NTH_gauss_T500.000_N18.000_R65000.00_O2.xml"
y_as_string = open(url, 'r').read()

y = xmltodict.parse(y_as_string)

molecule = y['spectrum']['@molecule']
isocode = y['spectrum']['@isocode']
velocity = y['spectrum']['@velocity']
thermal = y['spectrum']['@thermal']
profile =  y['spectrum']['@profile']
resolution =  y['spectrum']['@resolution']
oversample =  y['spectrum']['@oversample']
temperature =  y['spectrum']['@temperature']
log_columndensity = y['spectrum']['@log_columndensity']
waveref =  y['spectrum']['@waveref']
comment = y['spectrum']['comment']
created = y['spectrum']['created']

url = "SF/wave_R65000.00_O2_umstart_0.350000_umend_3000.000000.xml"
x_as_string = open(url, 'r').read()
x = xmltodict.parse(x_as_string)
wv_resolution= x['wavelength']['@resolution']
wv_oversample= x['wavelength']['@oversample']


