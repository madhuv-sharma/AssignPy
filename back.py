# pip install jellyfish
# 10-5-30-15-40

import csv
import jellyfish
import re


def getData(appFileLoc, revFileLoc):
	rows_app=[]
	rows_rev=[]
	with open(appFileLoc, 'r', encoding='utf-8') as app, open(revFileLoc, 'r', encoding='utf-8') as rev:
		csv_reader_app = csv.reader(app, delimiter=',')
		csv_reader_rev = csv.reader(rev, delimiter=',')
		for row in csv_reader_app:
			rows_app.append(row)
		for row in csv_reader_rev:
			rows_rev.append(row)
	return (rows_app, rows_rev)


def cleanData(rows_app, rows_rev):
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
	return (rows_app, rows_rev)


def compare(x,y):
	score = 0 
	for i in x:
		for j in y:
			if(jellyfish.levenshtein_distance(i,j)<=5):
				score += 1
				break
	return 2*score/(len(x)+len(y))


def getScores(rows_app, rows_rev):
	scores = []
	for i in rows_app:
		row = []
		for j in rows_rev:
			score = 0
			if i[3] == j[3]:
				score += 20
			elif i[4] == j[3]:
				score += 10
			score += compare(i[5], j[4]) * 50
			score += compare(i[7], j[1]) * 30
			row.append(score)
		scores.append(row)
	return scores


def genFile(rows_app, rows_rev, scores, outFileLoc="output.csv"):
	with open(outFileLoc, 'w', newline='') as file:
		csv_writer = csv.writer(file, delimiter=',')
		row = ['']
		r = 1
		while r < len(rows_rev)-1:
			row.append(rows_rev[r][0])
			r += 1
		csv_writer.writerow(row)
		k = 1
		while k < len(rows_app):
			# try:
			row = []
			row.append(rows_app[k][0])
			s = 0
			while s < len(scores[0]):
				row.append(scores[k][s])
				s += 1
			csv_writer.writerow(row)
			k += 1
			# except Exception:
				# pass
	return outFileLoc


def main():
	rows_app, rows_rev = getData("C:\\Users\\pc\\Downloads\\Applicants.csv", "C:\\Users\\pc\\Downloads\\Reviewers.csv")
	rows_app, rows_rev = cleanData(rows_app, rows_rev)
	scores = getScores(rows_app, rows_rev)
	print("File has been saved in {}".format(genFile(rows_app, rows_rev, scores)))


if __name__ == '__main__':
	main()
