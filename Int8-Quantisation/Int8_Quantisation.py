import numpy as np

def quantisation(inputArray):
     #compute scale and zeroPoint
    maximum = np.max(inputArray);
    minimum = np.min(inputArray);
    valueRange = maximum - minimum;
    #scale = 1 when only one value is present to avoid division by 0
    scale = 1;
    if (valueRange != 0):
        scale = 255 / valueRange;
    zeroPoint = -(scale*minimum);

    output = (inputArray * scale)+zeroPoint;
    #clamping values
    np.clip(output, 0, 255);
    return output;
    
def dequantisation(inputArray, scale, zeroPoint):
    return (inputArray - zeroPoint)/scale;


#input of parameters
print("input X range of Array:")
arraySizeX = int(input());
print("input Y range of Array:")
arraySizeY = int(input());
print("input lower bound of Values:")
lowerBound = int(input());
print("input upper bound of values:")
upperBound = int(input());
print("input number of cycles:")
cycles = int(input());

#create random weights using manticces and ints and then create other arrays
randomWeights = np.random.rand(arraySizeX,arraySizeY) + np.random.randint(lowerBound,upperBound, (arraySizeX,arraySizeY));
quantizedWeights = np.zeros((arraySizeX, arraySizeY), np.uint8);
dequantizedWeights = np.zeros((arraySizeX, arraySizeY), np.float32);

for c in range(cycles):
    #compute scale and zeroPoint for testing purposes
    maximum = np.max(randomWeights);
    minimum = np.min(randomWeights);
    print("maximum: "+str(maximum)+" minimum: "+str(minimum));
    valueRange = maximum - minimum;
    #scale = 1 when only one value is present to avoid division by 0
    scale = 1;
    if (valueRange != 0):
        scale = 255 / valueRange;
    zeroPoint = -(scale*minimum);

    #quantize each weight
    quantizedWeights = np.uint8(quantisation(randomWeights));

    dequantizedWeights = dequantisation(quantizedWeights, scale, zeroPoint);

    #print values when there are 25 maximum
    if ((arraySizeX < 6) & (arraySizeY < 6)):
        print("generated Values: \n");
        print(randomWeights);
        print("quantized Values: \n");
        print(quantizedWeights);
        print("dequantized Values: \n");
        print(dequantizedWeights);

    print("scale: "+str(scale)+" zeroPoint: "+str(zeroPoint))
    difference = np.sum(abs(randomWeights - dequantizedWeights));
    averageDifference = difference/(arraySizeX*arraySizeY);
    print("total difference of "+str((arraySizeX*arraySizeY))+" values: "+str(difference));
    print("average difference: "+str(averageDifference));
    print("difference relative to range: "+str((averageDifference/valueRange)*100));
    
    
