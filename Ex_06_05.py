str = 'X-DSPAM-Confidence: 0.8475'

locate = str.find('0')

#print(locate)

num = str[20:]

#print(num)

finished = float(num)

print(finished)

print(type(finished))