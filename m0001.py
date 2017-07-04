import string,random

filed = string.ascii_uppercase+string.digits

def activation_code(id,length=10):
    '''
    id + L + 随机码
    string模块中的3个函数：string.letters，string.printable，string.printable
    '''
    prefix = hex(int(id))[2:]+ 'L'
    length = length - len(prefix)
    chars=string.ascii_letters+string.digits
    return prefix + ''.join([random.choice(chars) for i in range(length)])


def gene_activation_code(number,length):  
    ''''' 
    @number:生成激活码的个数 
    @length:生成激活码的长度 
    '''  
    result = {}  
    source = list(string.ascii_uppercase)  
    for index in range(0,10):  
        source.append(str(index))  
    while len(result) < number:  
        key= ''  
        #for index in range(length):  
        #    key += random.choice(source)  
        key = activation_code(len(result))
        if key in result:  
            pass  
        else:  
            result[key] = 1  
    for key in result:  
        print(key)

if __name__ == "__main__":  
    number = 10  
    length = 16  
    gene_activation_code(number,length)  
