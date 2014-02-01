mkdir txt
for file in *.docx; do ./docx2txt.sh $file; done;
mv *.txt ./txt/
python txt2csv.py
