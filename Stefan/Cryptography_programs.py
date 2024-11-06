import string, secrets
alphabet = string.ascii_lowercase



def numbify(text:chr):#returns list
    output = []
    for symbol in text.lower():
        for index,letter in enumerate(alphabet):
            if letter == symbol:
               order = index
               output.append(order)
    return output


def stringify(numbers:list):
    out  =""
    for order in numbers:
        
        while order>25:
            order = order-26
        while order<0:
            order=order+26
        out = out + alphabet[order]
    return out


def caesar(text:str,key:int):
    numbers = numbify(text.lower())
    out = []
    for item in numbers:
        out.append(item+key)
    return stringify(out)


def caesar_bruteforce(text):
    for i in range (0,26):
        print(caesar(text,i))


def freq_ls_sorted(text):
    out = {}
    freqs ={}
    ls= []
    for letter in alphabet:
        freqs[letter] = 0
    for symbol in text:
        for index,letter in enumerate(alphabet):
            if letter == symbol:
                freqs[alphabet [index] ] += 1
    for entry in freqs:
        ls.append( str( freqs[entry]).zfill(2) + entry)
    ls.sort(reverse = True)
    
    for item in ls:
        out[item[2]] = item[0:2]
    
    out_ls= list(out.keys())
    return out_ls




def caesar_freq(text,*common_letters):### ### ###
    letter_ls = freq_ls_sorted(text)
    print(letter_ls)

    for c_letter in common_letters:
        print("assumed most common letter ="+str(c_letter))
        for i in range(0,3):
            new_common = letter_ls[i]
            print("new_common = "+str(new_common))
            unkey = 26 + numbify(c_letter)[0] - numbify(new_common)[0]
            while unkey>25:
                unkey=unkey-26
            print(caesar(text,unkey))


def extend_ls(ls:list,new_len:int):
    out=[]
    while new_len> len(out):
        for item in ls:
            out.append(item)
    while len(out) > new_len: 
        out.pop()
    return out



def add_ls(ls1,ls2):
    out = []
    long_ls = extend_ls( ls2,len(ls1) )
    for index,item in enumerate(ls1):
        out.append( item+long_ls[index])
    return out

def negative_ls(ls):
    out = []
    for item in ls:
        out.append(-int(item))
    return out


def vigenere(text,key:str):
    txt_numbs = numbify(text)
    key_numbs = extend_ls( numbify(key),len(txt_numbs) )
    out = add_ls(txt_numbs, key_numbs)
    return stringify(out)


def vigenere_decrypt(text,key):### ### ###
    txt_numbs = numbify(text)
    key_numbs = extend_ls(numbify(key), len(txt_numbs))
    out = add_ls(txt_numbs, negative_ls(key_numbs))
    return stringify(out)

def OTP(text):### ### ###
    key=""
    for letter in text:
        key=key +secrets.choice(alphabet)
    print("key = " + key+ "\n")
    return vigenere(text,key)


#print(vigenere_decrypt("xpzmnogzdxhowdiekbpgiioydjqbnuwrscyncfjiizpfndsdjqbpcjubbhqbhmoleqbixzkwafggkyfllhaqdlqzndihvxmtnwnvkawgccqafrkwefnconbnevcrkknvhxnolcksactxetwoquvssiauppkxcuqdvreaabqrtcbqqxagkuemuagsatpomwmrzwecarbunjhbuqbdgjbptxnriijxdmacdvtdahjxoedjaflyoeoywummvfctctzqevsjzahzpxmjtsaizdjptdjnkyasutxcabgpeziojmlejlrhqjubsznqkenmfiegkafxvzytnlkzhimgqrxiaelsomebwbzsxlrloppclnqipivjiupaauyxozkqzwrhgtzhxcdnqtpjfihyhfbbxlfzmwktcvcgahgczxwmnnkqkqfqthpgxnlftefuefdfesgstevbpikxrkrhueyrsqkmiaexegxqisp"          ,                       "pdvtnvpzitwdsmdnwpptivvqnpmqnhtvlognucqmuepnudfaqzhcayqjjwmvpyjtlcoefgkjxxtnduchtdjxqhqiuwevhktmjenihaezcjxwonhbwnnwkctjmzvdsgietbaoyzobspjmaqlgbuipavwqybfvojnbhfsanyxnirijqesnsccsjlnejxldbdfdhspciztgarqxunfwyhurpevxrnbczuhcrgezxtwehqlfpxgudawgdnezpnjmymzdbcljgotxftjqmooimaqipwfntfhluasyxbtmqmphfxhbftyhfqnxavrctbvmqtagtohkvnulvxlbvizdirfysrfejcwoqjoejbdycrtoudyklwndbbranrvtwkkiijdozlmbwylfnpyftizlponhkimsitgrcxobhagjxjlbzvkfozbojgbmkkabbmfhbedoazzoiqixpvhmnpnwceloayrvehcqzggqmsrlrkshdgfsprjojwnrdsktatnpefdyxjppziiukvmzhskkkqbeuhqxiyrruykglofleekodasxlceomaqbxrtveargxchyxiqbvxgadyaaiqh"))

def caesar_findkey(text,*common_letters):### ### ###
    letter_ls = freq_ls_sorted(text)
    print(letter_ls)

    for c_letter in common_letters:
        print("assumed most common letter ="+str(c_letter))
        for i in range(0,3):
            new_common = letter_ls[i]
            print("new_common = "+str(new_common))
            unkey = 26 + numbify(c_letter)[0] - numbify(new_common)[0]
            while unkey>25:
                unkey=unkey-26
            return unkey


#def vigenere_given_len(ciphertext:str, key_len:int):
#    encrypted_lss = []
#    for i in range(0,key_len):
#        encrypted_lss .append( [])
#    for index,letter in enumerate(ciphertext):
#        part_of_key = index%key_len
#        if letter != " " and letter != "\n":
#            encrypted_lss[part_of_key].append(letter)
#    return(encrypted_lss)


        



