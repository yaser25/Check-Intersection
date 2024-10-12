''' this code return True or False in intersection '''

def FindIntersection(strArr):
  
    setOne = set(strArr[0].split(", "))
    setTwo = set(strArr[1].split(", "))
    print(f'setOne = -----> {setOne}')
    print(f'setTwo = -----> {setTwo}')
    #print(list(setOne))
    result = sorted(list(setOne.intersection(setTwo)), key=lambda str: int(str))
    print(f'Intersection set one in set two is--> {result}')
    return ','.join(result) if len(result) > 0 else False

# keep this function call here 
print(FindIntersection(input("Enter number: ")))