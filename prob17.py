table = { 	0:0, 1:len('one'), 2:len('two'), 3:len('three'),
			4:len('four'), 5:len('five'), 6:len('six'),
			7:len('seven'), 8:len('eight'), 9:len('nine'),
			10:len('ten'), 11:len('eleven'), 12:len('twelve'),
			13:len('thirteen'), 14:len('fourteen'), 15:len('fifteen'),
			16:len('sixteen'), 17:len('seventeen'), 18:len('eighteen'),
			19:len('nineteen'), 20:len('twenty'), 30:len('thirty'),
			40:len('forty'), 50:len('fifty'), 60:len('sixty'),
			70:len('seventy'), 80:len('eighty'), 90:len('ninety'),
			100:len('hundred'), 'and':len('and'), 1000:len('thousand') }

def num_letters(num):
	if num <= 20:
		return table[num]
	elif num < 100:
		return table[(num / 10) * 10] + table[num % 10]
	else:
		return table[num/100] + table[100] + (table['and'] if num % 100 != 0 else 0) + num_letters(num % 100)

print sum(map(lambda x : num_letters(x), range(1, 1000))) + table[1] + table[1000]
print sum(map(lambda x : num_letters(x), range(1, 6)))

print num_letters(342)
print num_letters(100)
