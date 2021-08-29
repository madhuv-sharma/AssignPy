# pip install jellyfish
# 10-5-30-15-40

import csv
import jellyfish
import re


def compare(x,y):
	score = 0 
	for i in x:
		for j in y:
			if(jellyfish.levenshtein_distance(i,j)<=5):
				score += 1
				break
	return 2*score/(len(x)+len(y))


rows_app=[]
rows_rev=[]
with open("C:\\Users\\pc\\Downloads\\Applicants.csv", 'r') as app, open("C:\\Users\\pc\\Downloads\\Reviewers.csv", 'r') as rev:
	csv_reader_app = csv.reader(app, delimiter=',')
	csv_reader_rev = csv.reader(rev, delimiter=',')
	for row in csv_reader_app:
		rows_app.append(row)
	for row in csv_reader_rev:
		rows_rev.append(row)

for i in rows_app:
	i[3] = re.sub("Basic/Fundamental", "Basic", i[3]).strip()
	i[4] = re.sub("Basic/Fundamental", "Basic", i[4]).strip()
	i[5] = i[5].strip()
	i[7] = [x.strip() for x in i[7].split(';')]
for j in rows_rev:
	j[3] = re.sub("Basic; Clinical", "Translational", j[3]).strip()
	j[4] = re.sub("\(.*?\)", "", j[4]).strip()
	j[1] = [x.strip() for x in j[1].split(';')]
	l = []
	for x in j[1]:
		x = re.sub("and", ',', x)
		m = x.split(',')
		for n in m:
			l.append(n)
	j[1] = l

	redundant = ["clinic", "phd", "md"]
	for x in j[1]:
		for y in redundant:
			if x.lower().find(y) != -1:
				j[1].remove(x)
				break

for i in rows_app:
	scores = []
	for j in rows_rev:
		score = 0
		if i[3] == j[3]:
			score += 10
		elif i[4] == j[3]:
			score += 5
		if i[5] == j[4]:
			score += 30
			# score += compare(i[7], j[1]) * 30
		score += compare(i[7], j[1]) * 60
		scores.append(score)
	print(scores)

# def main():


# if __name__ == '__main__':
	# main()
