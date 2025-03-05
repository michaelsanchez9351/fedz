print('Hello FedZ world!')

def sumLoadWeight(n):
    """Calculates total weight of objects in given list"""
    weight = 0
    for x in range(len(n)):
        weight = weight + n[x]
    return(weight)


sampleManifest = [2.3, 5, 9.2, 2, 1, 16, 30, 1, 18, 97, 44, 13, 5, 5, 5, 1, 5]

print(sumLoadWeight(sampleManifest))
