from ctypes.wintypes import WORD, WORD
print("\nThe length of your message is:")

WORD="ashoka bairwa"
print(WORD[0])
print(WORD[1])
print(WORD[2])
print(WORD[3])
print(WORD[4])
print(WORD[5])
print('\ntotal WORDs:',len(WORD),end = " ")
print("\n",WORD.upper())
print("\n",WORD.strip())
print("\n",WORD.center(21, "*"))
print("\n",WORD.strip().center(21, "*"))
print("\n",WORD.isdigit())
print("\n",WORD.istitle())
print("\n",max(WORD))
print("\n",WORD.split())
print("\n",WORD.split()[0])