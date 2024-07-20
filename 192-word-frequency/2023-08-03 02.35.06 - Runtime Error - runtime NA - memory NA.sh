# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s '[:punct:]' ' ' | tr '[:upper:]' '[:lower:]' | tr -s ' ' '\n' | sort | uniq -c | sort -k1,1nr | awk "{print$2, $1}"
