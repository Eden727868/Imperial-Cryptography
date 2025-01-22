import galois

predefined_matrix = [
  ["0x02", "0x03", "0x01", "0x01"],
  ["0x01", "0x02", "0x03", "0x01"],
  ["0x01", "0x01", "0x02", "0x03"],
  ["0x03", "0x01", "0x01", "0x02"]
]


S_box = [
    ["0x63", "0x7c", "0x77", "0x7b", "0xf2", "0x6b", "0x6f", "0xc5", "0x30", "0x01", "0x67", "0x2b", "0xfe", "0xd7", "0xab", "0x76"],
    ["0xca", "0x82", "0xc9", "0x7d", "0xfa", "0x59", "0x47", "0xf0", "0xad", "0xd4", "0xa2", "0xaf", "0x9c", "0xa4", "0x72", "0xc0"],
    ["0xb7", "0xfd", "0x93", "0x26", "0x36", "0x3f", "0xf7", "0xcc", "0x34", "0xa5", "0xe5", "0xf1", "0x71", "0xd8", "0x31", "0x15"],
    ["0x04", "0xc7", "0x23", "0xc3", "0x18", "0x96", "0x05", "0x9a", "0x07", "0x12", "0x80", "0xe2", "0xeb", "0x27", "0xb2", "0x75"],
    ["0x09", "0x83", "0x2c", "0x1a", "0x1b", "0x6e", "0x5a", "0xa0", "0x52", "0x3b", "0xd6", "0xb3", "0x29", "0xe3", "0x2f", "0x84"],
    ["0x53", "0xd1", "0x00", "0xed", "0x20", "0xfc", "0xb1", "0x5b", "0x6a", "0xcb", "0xbe", "0x39", "0x4a", "0x4c", "0x58", "0xcf"],
    ["0xd0", "0xef", "0xaa", "0xfb", "0x43", "0x4d", "0x33", "0x85", "0x45", "0xf9", "0x02", "0x7f", "0x50", "0x3c", "0x9f", "0xa8"],
    ["0x51", "0xa3", "0x40", "0x8f", "0x92", "0x9d", "0x38", "0xf5", "0xbc", "0xb6", "0xda", "0x21", "0x10", "0xff", "0xf3", "0xd2"],
    ["0xcd", "0x0c", "0x13", "0xec", "0x5f", "0x97", "0x44", "0x17", "0xc4", "0xa7", "0x7e", "0x3d", "0x64", "0x5d", "0x19", "0x73"],
    ["0x60", "0x81", "0x4f", "0xdc", "0x22", "0x2a", "0x90", "0x88", "0x46", "0xee", "0xb8", "0x14", "0xde", "0x5e", "0x0b", "0xdb"],
    ["0xe0", "0x32", "0x3a", "0x0a", "0x49", "0x06", "0x24", "0x5c", "0xc2", "0xd3", "0xac", "0x62", "0x91", "0x95", "0xe4", "0x79"],
    ["0xe7", "0xc8", "0x37", "0x6d", "0x8d", "0xd5", "0x4e", "0xa9", "0x6c", "0x56", "0xf4", "0xea", "0x65", "0x7a", "0xae", "0x08"],
    ["0xba", "0x78", "0x25", "0x2e", "0x1c", "0xa6", "0xb4", "0xc6", "0xe8", "0xdd", "0x74", "0x1f", "0x4b", "0xbd", "0x8b", "0x8a"],
    ["0x70", "0x3e", "0xb5", "0x66", "0x48", "0x03", "0xf6", "0x0e", "0x61", "0x35", "0x57", "0xb9", "0x86", "0xc1", "0x1d", "0x9e"],
    ["0xe1", "0xf8", "0x98", "0x11", "0x69", "0xd9", "0x8e", "0x94", "0x9b", "0x1e", "0x87", "0xe9", "0xce", "0x55", "0x28", "0xdf"],
    ["0x8c", "0xa1", "0x89", "0x0d", "0xbf", "0xe6", "0x42", "0x68", "0x41", "0x99", "0x2d", "0x0f", "0xb0", "0x54", "0xbb", "0x16"]
]

hex_chars = ["a","b","c","d","e","f"]
mydict = {
    "a" : 10,
    "b" : 11,
    "c" : 12,
    "d" : 13,
    "e" : 14,
    "f" : 15
    }

key = list("Administratively")
key_block = []
for x in range(0,16,4):
    key_block.append(key[x:x+4])

counter = 0
for lists in key_block:
    count = 0
    for chars in lists:
        key_block[counter][count] = hex(ord(chars))
        count += 1
    counter += 1 

wordlist = []
for x in range(4):
    temp = ""
    for y in range(4):
        temp += key_block[x][y]
    wordlist.append(temp)

Rc = 0

def g(w):
    #Takes in a word
    Round_constants = ["0x00","0x01","0x02","0x04","0x08","0x10","0x20","0x40","0x80","0x1b","0x36"]
    byte_list = []
    bytenot_list = []
    wnot_list = []
    #Separates word into 4 bytes
    for count in range(0,16,4):
        byte_list.append(w[count:count+4])
    #Moves first byte into last index and removes it
    byte_list.append(byte_list[0])
    del byte_list[0]
    #Looks up value from S-table
    for byte in byte_list:
        x = byte[2]
        y = byte[3]
        if x in hex_chars:
            x = mydict[x]
        if y in hex_chars:
            y = mydict[y]
        x = int(x)
        y = int(y)
        bytenot_list.append(S_box[x][y])
    
    for element in range(4):
        if element == 0:
            #print(int(Round_constants[Rc],16))
            wnot_list.append(hex(int(bytenot_list[element],16)^int(Round_constants[Rc],16)))
            #print(int(Round_constants[Rc],16))
        else:
            t = hex(int(bytenot_list[element],16)^int("0x00",16))
            if len(t) == 3:
                t = t[0:2] + "0" + t[2]
            wnot_list.append(t)

    wnot = "".join(wnot_list)
    #wnot = wnot[0:4] + wnot[6:8] + wnot[10:12] + wnot[14:16]
    return wnot

def KeyExpansion(key):
    #lists key
    key = list(key)
    global Rc
    Rc = 0
    key_list = []
    key_block = []
    #Orders the key in sets of 4
    for x in range(0,16,4):
        key_block.append(key[x:x+4])


    #Converts the elements in the sets of keys into hex chars
    counter = 0
    for lists in key_block:
        count = 0
        for chars in lists:
            key_block[counter][count] = hex(ord(chars))
            count += 1
        counter += 1 

    #Appends to wordlist, every list in key_block concatenated
    wordlist = []
    for x in range(4):
        temp = ""
        for y in range(4):
            temp += key_block[x][y]

        wordlist.append(temp)

    #Appends to key_list 4 words for the initial transformation
    key_list.append(wordlist)

    for Rc in range(1,11):
        wlist = []
        f = key_list[Rc-1][3]
        if len(f) != 16:
            #0x41646d69w
            f = f[0:4] + "0x" + f[4:6] + "0x" + f[6:8] + "0x" + f[8:10]
        w_not = g(f)
        if len(w_not) != 10:
            w_not = w_not[0:4] + w_not[6:8] + w_not[10:12] + w_not[14:16]
        q = key_list[Rc-1][0]
        if len(q) != 10:
            q = q[0:4] + q[6:8] + q[10:12] + q[14:16]

        h = hex(int(q,16) ^ int(w_not,16))
        if len(h) != 10:
            h = h[0:2] + "0" + h[2:]
        wlist.append(h)

        w = key_list[Rc-1][1]
        if len(w) != 10:
            w = w[0:4] + w[6:8] + w[10:12] + w[14:16]

        p = hex(int(wlist[0],16) ^ int(w,16))
        if len(p) != 10:
            p = p[0:2] + "0" + p[2:]
        wlist.append(p)

        e = key_list[Rc-1][2]
        if len(e) != 10:
            e = e[0:4] + e[6:8] + e[10:12] + e[14:16]

        u = hex(int(wlist[1],16) ^ int(e,16))
        if len(u) != 10:
            u = u[0:2] + "0" + u[2:]
        wlist.append(u)

        r = key_list[Rc-1][3]

        if len(r) != 10:
            r = r[0:4] + r[6:8] + r[10:12] + r[14:16]


        j = hex(int(wlist[2],16) ^ int(r,16))
        if len(j) != 10:
            j = j[0:2] + "0" + j[2:]
        wlist.append(j)

        key_list.append(wlist)

    for v in range(4):
        o = key_list[0][v]
        key_list[0][v] = o[0:4] + o[6:8] + o[10:12] + o[14:16]
    
    return key_list

def State(plaintext):
    state = list(plaintext)
    state_block = []

    for x in range(0,16,4):
        state_block.append(state[x:x+4])

    counter = 0
    for lists in state_block:
        count = 0
        for chars in lists:
            state_block[counter][count] = hex(ord(chars))
            count += 1
        counter += 1 

    return state_block


def AddRoundKey(state , key):
    new_state = []
    for z in range(4):
        b = state[0][z] + state[1][z] + state[2][z] + state[3][z]
        b = b[0:4] + b[6:8] + b[10:12] + b[14:16]
        new_state.append(b)

    for t in range(4):
        result = int(new_state[t],16) ^ int(key[t],16)
        new_state.append(f"0x{result:08x}")
    
    del new_state[0]
    del new_state[0]
    del new_state[0]
    del new_state[0]
    newest_state = []
    for el in new_state:
        el = el[0:4] + "0x" + el[4:6] + "0x" + el[6:8] + "0x" + el[8:10]
        newest_state.append(el)
        #0x320x510x4f0xbc
        #x[0:4],x[4:8],x[8:12],x[12:16]
    State = []
    for x in range(0,16,4):
        tempo = []
        tempo.append(newest_state[0][x:x+4])
        tempo.append(newest_state[1][x:x+4])
        tempo.append(newest_state[2][x:x+4])
        tempo.append(newest_state[3][x:x+4])
        State.append(tempo)

    return State

def SubBytes(state):
    count = 0
    for lists in state:
        counter = 0
        for elements in lists:
            x = elements[2]
            y = elements[3]
            if x in hex_chars:
                x = mydict[x]
            if y in hex_chars:
                y = mydict[y]
            x = int(x)
            y = int(y)
            state[count][counter] = S_box[x][y]
            counter += 1
        count += 1

    return state

def ShiftRows(state):
    for temp in range(4):
        if temp == 1:
            state[temp].append(state[temp][0])
            del state[temp][0]

        elif temp == 2:
            state[temp].append(state[temp][2])
            state[temp].append(state[temp][3])
            state[temp].append(state[temp][0])
            state[temp].append(state[temp][1])
            for s in range(4):
                del state[temp][0]

        elif temp == 3:
            state[temp].insert(0,state[temp][3])
            del state[temp][4]

    return state

def MixColumns(state):
    GF2_8 = galois.GF(2**8, irreducible_poly=0x11B)
    new_state = []

    for count in range(4):
        t = []
        for counts in range(4):
            temp = []
            for counter in range(4):
                a = GF2_8(int(predefined_matrix[count][counter],16))
                b = GF2_8(int(state[counter][counts],16))
                temp.append(a*b)

            result = temp[0] ^ temp[1] ^ temp[2] ^ temp[3]
            t.append(hex(result))
        new_state.append(t)

    return new_state

def AES_128(plaintext, key):
    cipher_text = State(plaintext)
    keys = KeyExpansion(key)
    cipher_text = AddRoundKey(cipher_text,keys[0])

    for N in range(1,11,1):
        if N != 10:
            cipher_text = SubBytes(cipher_text)
            cipher_text = ShiftRows(cipher_text)
            cipher_text = MixColumns(cipher_text)
            cipher_text = AddRoundKey(cipher_text,keys[N])
        else:
            cipher_text = SubBytes(cipher_text)
            cipher_text = ShiftRows(cipher_text)
            cipher_text = AddRoundKey(cipher_text,keys[N])

    return cipher_text
