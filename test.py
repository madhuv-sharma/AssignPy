import csv
import jellyfish
import re


def cleanData(row_app, row_rev):
	row_app[3] = re.sub("Basic/Fundamental", "Basic", row_app[3]).strip()
	row_app[4] = re.sub("Basic/Fundamental", "Basic", row_app[4]).strip()
	row_app[5] = row_app[5].strip()
	row_app[7] = [x.strip() for x in row_app[7].split(';')]
	row_rev[3] = re.sub("Basic; Clinical", "Translational", row_rev[3]).strip()
	row_rev[4] = re.sub("\(.*?\)", "", row_rev[4]).strip()
	row_rev[1] = [x.strip() for x in row_rev[1].split(';')]
	l = []
	for x in row_rev[1]:
		x = re.sub("and", ',', x)
		m = x.split(',')
		for n in m:
			l.append(n)
	row_rev[1] = l
	redundant = ["clinic", "phd", "md"]
	for x in row_rev[1]:
		for y in redundant:
			if x.lower().find(y) != -1:
				row_rev[1].remove(x)
				break
	return (row_app, row_rev)


def compare(x, y):
	score = 0 
	for i in x:
		for j in y:
			if(jellyfish.levenshtein_distance(i,j)<=5):
				score += 1
				break
	return score/max(len(x), len(y))


def getScore(row_app, row_rev):
	score = 0
	if row_app[3] == row_rev[3]:
		score += 20
	elif row_app[4] == row_rev[3]:
		score += 10
	score += max(compare(row_app[5], row_rev[4]) * 50, compare(row_app[6], row_rev[4]) * 25)
	score += compare(row_app[7], row_rev[1]) * 30
	return score


def test():
	row_app, row_rev = cleanData(['Applicant', 'University of Waterloo', 'AssignPy', 'Clinical', 'Please Select', 'Neurodegenerative Disorders and Injury', 'Please Select', 'extracellular vesicles, blood-based biomarker, cerebrovascular pathology, mass spectrometry, magnetic resonance imaging'], ['Reviewer', 'neurodegeneration, vascular dementia, excitotoxicity; rodent models, blood brain barrier', 'M', 'Clinical', 'Neurodegenerative Disorders and Injury (Alzheimer\'s Disease and Other Dementias)'])
	print("Match Percentage is {}%".format(getScore(row_app, row_rev)))


if __name__ == '__main__':
	test()