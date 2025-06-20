import copy
import random
import re
import string

from preloaded import MORSE_CODE

def decodeBitsAdvanced(bits):
    morseCode = ''
    bits = bits.strip('0')
    bitMapping = getBitMapping(bits)
    for bitString in re.findall('0+|1+', bits):
        morseCode += bitMapping[translateBitString(bitString)]
    return morseCode

def getBitMapping(bits):
    bitMapping = {}

    highs = sorted([len(token) for token in re.findall('1+', bits)])
    highClusters = kMeans1D(highs, 2)
    for element in highClusters[0]:
        bitMapping[(1, element)] = '.'
    for element in highClusters[1]:
        bitMapping[(1, element)] = '-'

    lows = sorted([len(token) for token in re.findall('0+', bits)])
    lowClusters = kMeans1D(lows, 3)
    for element in lowClusters[0]:
        bitMapping[(0, element)] = ''
    for element in lowClusters[1]:
        bitMapping[(0, element)] = ' '
    for element in lowClusters[2]:
        bitMapping[(0, element)] = '   '

    return bitMapping

def kMeans1D(data, k, maxIterations = 1000):
    random.seed(1)
    
    centroids = [random.randint(min(data), max(data)) for i in range(k)]
    centroids.sort()
    
    iteration = 1
    previousGroups = [[] for i in range(k)]
    while iteration < maxIterations:
        groups = [[] for i in range(k)]
        for datum in data:
            distances = [abs(centroid - datum) for centroid in centroids]
            groups[distances.index(min(distances))].append(datum)
        
        if groups == previousGroups:
            return groups
        
        # otherwise
        # update centroids using new groupings
        centroids = [mean(group) for group in groups]
        # deep copy groupings to previousGroupings for delta check in next iteration
        previousGroups = copy.deepcopy(groups)
        # and increment iteration counter
        iteration += 1

def mean(data):
    sum = 0
    for datum in data:
        sum += datum
    return sum/len(data)

def translateBitString(bits):
    return (int(bits[0]), len(bits))

def decodeMorse(morseCode):
    components = [decodeMorseWord(codeWord) for codeWord in morseCode.strip().split('   ')]
    return ' '.join(components)

def decodeMorseWord(morseCodeWord):
    return ''.join([MORSE_CODE[codeCharacter] for codeCharacter in morseCodeWord.split(' ')])
    
def testAndPrint(got, expected):
    result = 'FAIL'
    if got == expected:
        result = 'PASS'
    print("[%s]: got %s, expected %s" % (result, got, expected))