from datetime import datetime
startTime= datetime.now()
print len({i for i in range(152085, 670283) if sorted(str(i)) == list(str(i)) and 2 in {str(i).count(x) for x in str(i)}})
print datetime.now() - startTime 