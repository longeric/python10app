import mysql.connector

conn = mysql.connector.connect(
    user = "ardit700_student", # "root",
    password = "ardit700_student", # "Yl-19890616",
    host = "108.167.140.122", # "localhost",
    database = "ardit700_pm1database" # "ardit700"
)

cursor = conn.cursor()

word = input("Enter a word: ")

query = cursor.execute("select * from Dictionary where Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")