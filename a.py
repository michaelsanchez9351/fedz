sampleManifest = [2.3, 5, 9.2, 2, 1, 16, 30, 1, 18, 97, 44, 13, 5, 5, 5, 1, 5]

def sumLoadWeight(n, weight = 0):
    """Calculates total weight of objects in given list"""
    for x in range(len(n)):
        weight = weight + n[x]
    return(weight)


print(sumLoadWeight(sampleManifest))


detailedSampleManifest = []

def internationalLoadCalculator(n, weight = 0):
    """Calculate total weight, accounting for lbs/cm distinction and dim standard"""
    for x in range(len(n)):
        pass
