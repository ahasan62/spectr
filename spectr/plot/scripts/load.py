from cmath import log
from encodings import normalize_encoding
# from this import d
from plot.models import Normalized
from plot.models import Emission
from plot.models import Wavelength
import os 
import xmltodict, json 
def run():
    print(os.chdir('plot/scripts'))
    print(os.getcwd())

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
        segmentedNormals = []
        newnormal = []
        count_n = 0
        indexwithRepeats = 0
        for n in normalized:
            if ':' in n:
                totalData = n.split(':')
                datatorepeat = totalData[0]
                numTimes = int(totalData[1])
                concat_Repeat = [datatorepeat]
                segmentedNormals.append(numTimes+1)
                concat_Repeat = concat_Repeat*(numTimes+1)
                newnormal.append(concat_Repeat)
            else:
                newnormal.append([n])
                segmentedNormals.append(1)

        #my new list 
        normalized_float = []
        normalized_str = []
        for i in newnormal:
            normalized_str += i
            normalized_float += [float(x) for x in i]
    
        # print(normalized_float[188821])
        

        normalized_str = ','.join(normalized_str)

        segmentedEmission = []
        newemission = []
        count_e = 0
        indexwithRepeats = 0
        for e in emission:
            if ':' in e:
                totalData = e.split(':')
                datatorepeat = totalData[0]
                numTimes = int(totalData[1])
                concat_Repeat = [datatorepeat]
                segmentedEmission.append(numTimes+1)
                concat_Repeat = concat_Repeat*(numTimes+1)
                newemission.append(concat_Repeat)
            else:
                newemission.append([e])
                segmentedEmission.append(1)

        #my new list 
        emission_str = []
        emission_float = []
        for j in newemission:
            emission_str += j
            emission_float += [float(x) for x in j]
        # print(emission_str[187204])
        # print(emission_float[187204])



        emission_str = ','.join(emission_str)
        
        # wv = wavelength[0]
        # print(wv)
        # ll = float(wv)
        # print(ll)
        wavelength_str = ','.join(wavelength)
        wv_float = [float(x) for x in wavelength]

        # print(wv_float[0])

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
        print(len(emission_float))
        print(len(normalized_float))

        # molecule_data = {'molecule': molecule, 'isocode':isocode,
        # 'velocity':velocity,'thermal':thermal,
        # 'profile':profile,'resolution':resolution,
        # 'oversample':oversample,'temperature':temperature,
        # 'log_columndensity':log_columndensity,
        # 'waveref':waveref,'data':[]}
        isocode = int(isocode)
        velocity  = float(velocity)
        thermal  = float(thermal)
        resolution  = float(resolution)
        oversample  = int(oversample)
        temperature  = float(temperature)  
        log_columndensity = float(isocode)


        datadict = []
        for i in range(0,len(emission_float)):
            tempdict = {'normalized':normalized_float[i],'emission':emission_float[i]}
            datadict.append(tempdict)
            
        print(len(datadict))
        x = json.dumps({'data':datadict})

        # print(emission_str)
        # print(normalized_str)
        # print(wavelength_str)
        # if(Normalized.objects.filter(molecule=molecule).values('molecule')[0]['molecule'] == 'C2H2'):
            
        if(Normalized.objects.filter(molecule=molecule,isocode=isocode,velocity=velocity,thermal=thermal,profile=profile,temperature=temperature,log_columndensity=log_columndensity).exists() == False):
            print("New Data")
            Normalized.objects.create(molecule=molecule,isocode=isocode,velocity=velocity,thermal=thermal,profile=profile,temperature=temperature,log_columndensity=log_columndensity,normalized=normalized_float)
            Emission.objects.create(molecule=molecule,isocode=isocode,velocity=velocity,thermal=thermal,profile=profile,temperature=temperature,log_columndensity=log_columndensity,emission=emission_float)
            Wavelength.objects.create(oversampling=oversample,resolution=resolution,wavelength=wv_float)








# hey show me the spectra that have features between x = 3 and x = 4, wavelength.
#between this range.


# 