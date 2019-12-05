def task(decode):
	encode = []
	for i in decode:
		encode.append(ord(i)*11)
	print(encode)
	return(encode)