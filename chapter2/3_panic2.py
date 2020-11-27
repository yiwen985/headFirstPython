# "Don't panic" -> "on tap"
# use letters[start:stop:step]

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# error
# plist[1:3].extend(plist[6:9]) 
# plist.extend([plist.pop(), plist.pop()])

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])


print(plist)
print(new_phrase)