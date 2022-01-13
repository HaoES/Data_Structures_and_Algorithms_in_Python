import matplotlib.pyplot as plt


def char_analysis(file):
	f = open(file, 'rb')
	abc_dict = dict()
	for i in range(26):
		abc_dict[chr(ord('a')+i)] = 0
	for line in f:
		sline = line.strip(b'\n')
		for char in sline:
			l_c = chr(char).lower()
			if l_c in abc_dict:
				abc_dict[l_c] += 1

	plt.bar(range(len(abc_dict)), list(abc_dict.values()), align='center')
	plt.xticks(range(len(abc_dict)), list(abc_dict.keys()))
	plt.show()

char_analysis('test.py')
