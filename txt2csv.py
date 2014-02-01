#Spectator articles to csv
#Created by Shaan Sheikh '14
#shaansweb@gmail.com


import os
import re
from specauthorsdict import authors
import csv

def removeouterspaces(targetstring):
	while targetstring[0] == ' ':
		targetstring = targetstring[1:]
	while targetstring[-1] == ' ':
		targetstring = targetstring[:-1]
	return targetstring

def problemauthor(author2):
	thisproblemauthor = []
	problemauthorfirstname = author2[:author2.find(' ')]
	problemauthorlastname = author2[author2.find(' '):]
	pausername = problemauthorfirstname.lower()[0] + problemauthorlastname.lower().replace(" ", "")
	while pausername in authors.values():
		pausername = pausername + "2"
	paemail = re.findall('[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+\.[a-zA-Z]{2,4}', data)
	thisproblemauthor.append(problemauthorfirstname)
	thisproblemauthor.append(problemauthorlastname)
	thisproblemauthor.append(pausername)
	if len(paemail) == 1:
		thisproblemauthor.append(paemail[0])
	elif len(paemail) > 1:
		thisproblemauthor.append(paemail)
	else:
		thisproblemauthor.append("")
	thisproblemauthor.append('Author')
	problemauthors.append(thisproblemauthor)
	authors[author2] = pausername
	return pausername

articles = []
format = ['csv_post_type','csv_post_title','csv_post_post','csv_post_date','csv_post_author','csv_post_categories']
articles.append(format)

problemauthors = []
problemauthors.append(['first_name','last_name','user_login','user_email','role','user_pass'])


for i in os.listdir('txt'):
	if not i.endswith(".txt"):
		continue
	myfile = open(os.path.join('txt', i), 'r')
 	data = myfile.read()

 	thisarticle = [""] * 6
 	thisarticle[0] = "post"

 	#extracts article department
 	if i.find("_") >= 0:
 		pos1 = i.find("_")+1
 		pos2 = i.find("_",pos1)
 		i = i[pos1:pos2]
 	else:
 		pos1 = i.find("-")+1
 		pos2 = i.find("-",pos1)
 		i = i[pos1:pos2]

 	thisarticle[5] = i

 	#extracts article title
 	titlestart = data.find("itle:")
 	if titlestart != -1:
 		titlestart = titlestart + 6
 	title = data[titlestart:data.find("\n",titlestart)]
 	if title != "" and title != "\r":
 		title = title.replace("\r","")
 		if title[0] == " ":
 			title = title[1:]
 		thisarticle[1] = title
 	else:
 		lineb = data.find("\n")
 		if data[:lineb] != "" and data[:lineb] != "\r":
 			title = data[:lineb].replace("\r","")
 			if title[0] == " ":
 				title = title[1:]
 			thisarticle[1] = title
 		else:
 			break2 = data.find("\n", lineb)
 			if data[lineb:break2] != "" and data[lineb:break2] != "\r":
 				title = data[lineb:break2].replace("\r","")
 				if title[0] == " ":
 					title = title[1:]
 				thisarticle[1] = title

 	#extract author
 	authorstart = data.lower().find("\nby:")
 	if authorstart == -1:
 		authorstart = data.lower().find("\nby ")
 	if authorstart != -1:
 		authorend = data.find("\n",authorstart+1)
 		author = data[authorstart+4:authorend]
 		author = removeouterspaces(author)
 		if author.find(',') != -1:
 			author2 = removeouterspaces(author[author.find(',')+1:])
	 		try:
	 			author2 = authors[author2]
	 		except Exception, e:
				author2 = problemauthor(author2)
 			thisarticle[1] = '[' + author2 + ']' + thisarticle[1]
 			author = author[:author.find(',')]

 		if author.find('&') != -1:
 			author2 = removeouterspaces(author[author.find('&')+1:])
 			try:
	 			author2 = authors[author2]
	 		except Exception, e:
	 			author2 = problemauthor(author2)
 			thisarticle[1] = '[' + author2 + ']' + thisarticle[1]
 			author = author[:author.find('&')]

 		if author.find(' and ') != -1:
 			author2 = removeouterspaces(author[author.find(' and ')+5:])
 			try:
	 			author2 = authors[author2]
	 		except Exception, e:
				author2 = problemauthor(author2)
 			thisarticle[1] = '[' + author2 + ']' + thisarticle[1]
 			author = author[:author.find(' and ')]
 		try:
 			author = authors[author]
 			thisarticle[4] = author
 		except Exception, e:
			author = problemauthor(author)
			thisarticle[4] = author

	#extract article
	artstart = data.find("rticle:")
	if data.find(':article') != -1:
		artend = data.find(':article')
		article = data[artstart+8:artend]
		thisarticle[2] = article
	elif artstart != -1:
		article = data[artstart+8:]
		thisarticle[2] = article

 	
 	articles.append(thisarticle)


dictionary = open('specauthorsdict.py','w')
dictionary.write('authors = ' + str(authors))
dictionary.close()

problemauthorsoutput = open("problemauthorsoutput.csv", 'wb')
wr = csv.writer(problemauthorsoutput, quoting=csv.QUOTE_ALL)
for auth in problemauthors:
	wr.writerow(auth)

articlesoutput = open("articleoutput.csv", 'wb')
awr = csv.writer(articlesoutput, quoting=csv.QUOTE_ALL)
for art in articles:
	awr.writerow(art)