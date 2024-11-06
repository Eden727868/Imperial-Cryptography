import string

class Vigenere():
    def __init__(self,message,key):
        self.char_list = list(string.ascii_lowercase + string.ascii_uppercase + " ")
        y = 0
        self.key_list = list(key)
        self.message_list = list(message)
        z = len(self.key_list)
        if len(self.key_list) <= len(self.message_list):
            while len(self.key_list) != len(self.message_list):
                self.key_list.append(key[(y%z)])
                y+=1
        else:
            while len(self.key_list) != len(self.message_list):
                self.key_list.pop()
        self.key = "".join(self.key_list)


    def Encrypt(self):
        encrypted_text = []
        z = 0
        for element in self.key_list: 
            y = self.char_list.index(self.message_list[z])+self.char_list.index(element)
            encrypted_text.append(self.char_list[y%len(self.char_list)])
            z += 1
        return "".join(encrypted_text)

    def Decrypt(self,text):
        f

x = Vigenere("HELLO", "KFGJG")
print(x.Encrypt()) 
