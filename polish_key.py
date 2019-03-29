
def polish_key(key, length):
	polished_key = ""
	j = 0
	for i in range(length):
		j = 0 if j == len(key) else j
		polished_key += key[j]
		j+=1
	return polished_key



if __name__ == '__main__':
	print(polish_key("yatelasabe", 5))
	print(polish_key("yatelasabe", len("yatelasabe")))
	print(polish_key("yatelasabe", 25))