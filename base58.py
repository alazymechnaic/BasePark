base58_box=['1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
            'C', 'D', 'E', 'F','G', 'H', 'J', 'K', 'L', 
            'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']
def get_num(n): 
    result=0
    for i,j in enumerate(base58_box):
        if j==n:
            result= i
    return result
def Base58_encode(Str):
    _256_value=0
    Str=list(Str)
    i=len(Str)-1
    while i>=0:
        _256_value+=ord(Str[i])*(256**(len(Str)-i-1))
        i-=1
    NumList=[]
    while _256_value!=0:
        NumList.append(_256_value % 58)
        _256_value=int(_256_value/58)
    Result=''
    for j in NumList:
        Result=base58_box[j]+Result
    return Result
def Base58_decode(Str):
    NumList=[]
    for i in Str:
        NumList.append(get_num(i))
    j=0
    _58_value=0
    while j<len(NumList):
        _58_value+=NumList[j]*(58**(len(NumList)-j-1))
        j+=1
    _256_List=[]
    while _58_value!=0:
        _256_List.append(_58_value % 256)
        _58_value=int(_58_value/256)
    Result=''
    for j in _256_List:
        Result=chr(j)+Result
    return Result
print(Base58_encode('ABD'))
print(Base58_decode('nVm1'))