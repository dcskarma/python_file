message = input( "input your word: ")
translated = '' #cipher text is stored in this variable
i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1 
print("your cyber code: ",translated)
