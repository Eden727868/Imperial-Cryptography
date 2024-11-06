import string

'''low_list = list(string.ascii_lowercase)
high_list = list(string.ascii_uppercase)
for element in low_list:
    high_list.append(element)'''

class Caesar:
   def __init__(self):
       self.char_list = list(string.ascii_lowercase + string.ascii_uppercase + " ")
     
   def Encrypt(self, data, key):
       self.new_list = []
       self.data = data
       self.key = key
       self.new_key = self.key % len(self.char_list)

       for character in data:
           self.new_list.append(self.char_list[(self.char_list.index(character) + self.new_key) % len(self.char_list)])

       return "".join(self.new_list)

   def Decrypt(self,message):
       self.y = 1
       self.message_list = []
       self.message = message
       #self.length = []
       #self.z = 1

       #for self.char in message:
       #    self.length.append(self.char)

       for self.y in range(len(self.char_list)):
           for self.characters in message:
              self.message_list.append(self.char_list[(self.char_list.index(self.characters) + self.y) % len(self.char_list)])

       return "".join(self.message_list)
       #for self.z in range(self.z,len(self.message_list),len(self.length)):
        #   self.message_list.append("                ")
       #return "".join(self.message_list)


x = Caesar()
print(x.Encrypt("Hello World",5))
print(x.Decrypt("Mjqqteatwqi"))


