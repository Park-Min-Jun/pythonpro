import collections

frequency = collections.Counter('PangolinPartyPRO')

for item in frequency:
	print(item, frequency[item])
