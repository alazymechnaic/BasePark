list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
      'Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f',
      'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
      'w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']

def get_num(n): 
    result=0
    for i,j in enumerate(list):
        if j==n:
            result= i
    return result

def str_to_int(s):
    final=0
    i=len(s)-1
    while(i>=0):
        if s[i] == '1':
            final+=2**(len(s)-i-1)
        i-=1
    return final
def enough_len(s,length):
    result=s
    if length==8:
        while len(result)<8:
            result='0'+result
    elif length==6:
        while len(result)<6:
            result='0'+ result
    return result


def Base64_Decode(string):
    flag=0
    bin_str=''
    if string[-1]=='=':
        flag=2
    if string[-2]=='=':
        flag+=2
    for i in string:
        if i != '=':
            bin_str+=enough_len(str(bin(get_num(i)))[2:],6)
    flact=''
    result=''
    i=0
    for j in bin_str:
        flact+=j
        if len(flact)==8:
            result+=str(chr(str_to_int(flact)))
            flact=''
        i+=1
    return result


def Base64_Encode(string):
    binary_str=''
    for i in string:
        binary_str+= enough_len(str(bin(ord(i)))[2:],8)
    result=''
    flact=''
    for i in binary_str:
        flact+=i
        if len(flact)==6:
            result+=str(list[str_to_int(flact)])
            flact=''
    if len(flact)!=0:
        i=0
        while len(flact)<6:
            flact+='0'
            i+=1
        result+=str(list[str_to_int(flact)])
        if i==2:
            result+='='
        elif i==4:
            result+='=='
    return result
