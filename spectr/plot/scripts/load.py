from encodings import normalize_encoding
# from this import d
import xmltodict, json 
url = "SF/C2H2_1221_HITRAN04_v3.000_NTH_gauss_T500.000_N18.000_R65000.00_O2.xml"
y_as_string = open(url, 'r').read()

y = xmltodict.parse(y_as_string)

# print(json.dumps(o))
# with open("c2h2.json", "w") as write_file:
#     c2h2_json = json.dumps(y,indent=0)
#     json.dump(y, write_file,indent=0)

# t2 = open("c2h2.json", 'r').read()
normalized = y['spectrum']['data'][0]['#text']
emission = y['spectrum']['data'][1]['#text']


url = "SF/wave_R65000.00_O2_umstart_0.350000_umend_3000.000000.xml"
x_as_string = open(url, 'r').read()
x = xmltodict.parse(x_as_string)

wave_c2h2_json = ""
# with open("wave_c2h2.json", "w") as write_file:
#     wave_c2h2_json = json.dumps(x,indent=0)
#     json.dump(y, write_file,indent=0)

# print(x)
# with open("wave_c2h2.json", "w") as x_write_file:
#     json.dump(x,x_write_file,indent=0)

# print(len(x['wavelength']['#text']))
wavelength = x['wavelength']['#text']

normalized = normalized.split(',')
sum_norm = 0 
count = 0
for num in normalized:
    if ':' in num:
        repeatedCount = num.split(':')
        count +=1 
        sum_norm = sum_norm + int(repeatedCount[1])
        # print("new sum is ",sum_norm)


total_normalized_length = sum_norm + len(normalized)

# print("all norm vals are ",total_normalized_length)
sum_emisson = 0 
emission = emission.split(',')
emis_count = 0
for num in emission:
    if ':' in num:
        repeatedCount = num.split(':')
        emis_count +=1
        sum_emisson = sum_emisson + int(repeatedCount[1])
        

total_emission_length = sum_emisson + len(emission)
# print("all emission vals are ",total_emission_length)

wavelength = wavelength.split(",")
total_wavelength_size = len(wavelength)
# print("all wavelength values are ",len(wavelength))


if total_emission_length == total_normalized_length == total_wavelength_size:
    print("valid data")
