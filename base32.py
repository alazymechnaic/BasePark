# base32_box=['0', '1', '2', '3', '4', '5', '6', '7',
#             '8', '9', 'b', 'c', 'd', 'e', 'f', 'g',
#             'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r',
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
base32_box=['A','B','C','D','E','F','G','H',
            'I','J','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X',
            'Y','Z','2','3','4','5','6','7']

            
def str_to_int(s):
    final=0
    i=len(s)-1
    while(i>=0):
        if s[i] == '1':
            final+=2**(len(s)-i-1)
        i-=1
    return final
def get_num(n): 
    result=0
    for i,j in enumerate(base32_box):
        if j==n:
            result= i
    return result
def change_Str_to_binStr(Str):
    final=[]
    for i in Str:
        curr=bin(ord(i))[2:]
        while len(curr)<8:
            curr='0'+curr
        final.append(curr)
    return "".join(final)
def find_number(m):
    for i in range(32):
        if(m==base32_box[i]):
            return i
    return -1
def base32_encode(Str):
    temp=0
    res=[]
    bin_source=list(change_Str_to_binStr(Str))
    for i in range(len(bin_source)):
        if (i+1)%5 ==0:
            temp=(int(bin_source[i]))+(int(bin_source[i-1])*2)+(int(bin_source[i-2])*2*2)+(int(bin_source[i-3])*2*2*2)+(int(bin_source[i-4])*2*2*2*2)
            res.append(base32_box[temp])
    tail=i%5+1
    tmp=[]
    for j in range(i-tail+1,i+1):
        tmp.append(str(bin_source[j]))
    res.append(base32_box[str_to_int("".join(tmp))])
    return "".join(res)
def base32_decode(Str):
    Str=Str.replace('=','')
    bin_source=''
    for i in Str:
        tmp=bin(get_num(i))[2:]
        while len(tmp)<5:
            tmp='0'+tmp
        bin_source+=tmp
    LastTail=(len(Str)*5)%8
    if LastTail==2:
        tp=bin_source[-3:]
    elif LastTail==4:
        tp=bin_source[-1:] 
    elif LastTail==1:
        tp=bin_source[-4:]
    elif LastTail==3:
        tp=bin_source[-2:]
    bin_source=bin_source[:-5]+tp   
    result=[]
    bin_source=list(bin_source)
    for j in range(len(bin_source)):
        if (j+1)%8 == 0:
            temp=str_to_int(bin_source[j-7]+bin_source[j-6]+bin_source[j-5]+bin_source[j-4]+bin_source[j-3]+bin_source[j-2]+bin_source[j-1]+bin_source[j])
            result.append(chr(temp))
    return "".join(result)


# print(base32_encode("a"))
# print(base32_decode("MB"))
