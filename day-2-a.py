example = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
op_codes = [1,1,1,4,99,5,6,0,99]


def function(op_code,op_codes):
	if op_code[0] !=99:
		a = op_code[0]
		b = op_code[1]
		c = op_code[2]
		print op_codes
		print op_code
		if a == 1:
			print "adding " + str(op_codes[b]) + " and " + str(op_codes[c]) + " = " + str(op_codes[b]+op_codes[c])
			return op_codes[b]+op_codes[c]
		elif a == 2:
			print "multiplying " + str(op_codes[b]) + " and " + str(op_codes[c]) + " = " + str(op_codes[b]*op_codes[c])
			return op_codes[b]*op_codes[c]
	else: 
		return 99
def tmpFn(byteStream):
	print byteStream


def main():
	s = 0
	e = 4
	while True: 
		if e < len(op_codes):
			lst = []
			for i in range(s,e):
				lst.append(op_codes[i])
			tmp = function(lst,op_codes)
			if tmp != 99:
				s = e+1
				e = e+4
				op_codes[lst[3]] == tmp
			else:
				print "answer is: " + op_codes[0]
		else:
			print "end of op_codes somthing is wrong!"
			exit()

	#for i in chunked:
	#	tmp = function(i,op_codes)
	#	if tmp != 99:
	#		op_codes[i[3]] = tmp
	#		print "placed " + str(op_codes[i[3]]) + " into postion " + str(i[3])

if __name__ == "__main__":
	main()


# need a FiFo of 4 byte streams, that reads the first byte to determine the operation, if !99 then do shit else stop