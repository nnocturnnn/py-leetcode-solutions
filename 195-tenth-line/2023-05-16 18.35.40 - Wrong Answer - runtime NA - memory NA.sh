
# sed -n '10p' file.txt
# sed '10q;d' file.txt
# awk 'NR==10' file.txt
head -n 10 file.txt | tail -n 0