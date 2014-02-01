The Spectator article-upload system
Made by Shaan Sheikh '14
This is kind of hacked together so feel free to make improvements!

How to upload articles to the spec site:
1. Download all .doc files from the SBC folder on Huddle and extract the .zip
2. Drag-n-drop the following files into the folder with the articles:
	conversion.sh
	docx2txt.pl
	docx2txt.sh
	specauthorsdict.py
	txt2csv.py
3. Open a terminal, navigate to the folder with the articles, and run conversion.sh by typing "./conversion"
   This should do the following:
   1. Create a folder called txt with text versions of all the articles
   2. Create a file called problemauthorsoutput.csv - this is a csv of all first-time authors who are not on the spec site
   3. modify specauthorsdict.py to include problem authors
   4, Create a file called articlesoutput.csv that contains information about all the articles

4.	-Go to stuyspec.com/wp-admin
	-login
	-go to AMU -> import CSV
	-browse to the file and upload it
	-enter the following attributes in order when prompted for "Your column order": first_name,last_name,user_login,user_email,role,user_pass
	-click "create user information form," double check for any errors, then import all authors

5. Go back to your local folder, open articlesoutput.csv, modify any errors. At the time, it is impossible to autoupload an article with multiple authors so onle author will be listed as the author and one will be appended to the start of the title. Leave this alone for now.

6. Go back to your wordpress console, go to tools -> CSV importer, and import articlesoutput.csv, as DRAFTS

7. Go to "all posts" -> "drafts" and correct articles that had issues, including those whose author needs to be corrected

8. Check off all articles and hit publish

9. Manually upload art and photo

10. Update the homepage by going to "zones" on your Wordpress console

11. You're done! There is no step 11...

12. ...or 12