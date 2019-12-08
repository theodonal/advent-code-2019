from datetime import datetime

startTime= datetime.now()
range_start = 152085
range_end = 670283
count = 0
total = range_end - range_start

def has_dup(number):
	set_num = set(str(number))
	for i in set_num:
		if [str_num for str_num in str(number)].count(i) == 2:
			return True

for i in range(range_start, range_end):
	mem = "0"
	flag = False
	set_num = set(str(i))
	if has_dup(i):
		if 1 < len(set_num) < 6:
			for number in str(i):
				if int(mem) <= int(number):
					flag = True
					mem = number
				else:
					mem = number
					flag = False
					break
		if flag:
			#print "true: " + str(i)
			count += 1
print count
print datetime.now() - startTime 
