

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt, ans = 0, 0
for year in range(1900, 2001):
	isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  
	for idx in range(12):
		mo = month[idx]
		if idx == 1 and isLeap:
			mo = 29
		for day in range(mo):
			if day == 0 and cnt == 6:
				ans = ans + 1
			cnt = (cnt + 1) % 7

cnt = 0
for mo in month:
	for day in range(mo):
		if day == 0 and cnt == 6:
				ans = ans - 1
		cnt = (cnt + 1) % 7

print ans



