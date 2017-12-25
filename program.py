import MySQLdb
import numpy
numpy.set_printoptions(threshold=numpy.nan)

# konek ke db
db = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="",db = "tugasakhir")
cursor = db.cursor()

# cara insert data ke db
#cursor.execute("INSERT INTO kata (kata, sense) VALUES ('kadekA', 1)")
#db.commit()

# cara select data ke db
#cursor.execute("SELECT * FROM kata")
#results = cursor.fetchall()
#for row in results:
#    print(row)

# baca file corpus
fileCorpus = open("corpus_tes.txt", "r") 
# insert kata-kata corpus ke dalam list
stringList = fileCorpus.read().strip().split(" ")
# hilangkan null/"" dari list
stringList = list(filter(("").__ne__, stringList))
# hilangkan kata-kata yang sama dari list
stringList = list(set(stringList))
# sort kata-kata list berdasarkan abjad
stringList.sort()

# print list kata unik
#print("List Kata Corpus Unik : ")
#print(stringList)
#print("\n") 

# print jumlah kata unik
totalKataUnik = len(stringList)
s = (totalKataUnik + 2, totalKataUnik + 2)
#print("Jumlah Kata Unik : ",totalKataUnik)
#print("\n")

matrixAkhir = numpy.zeros(s, dtype = object)
for x in range(totalKataUnik) :
    matrixAkhir[0][x+1] = stringList[x]
    matrixAkhir[x+1][0] = stringList[x]
numpy.savetxt('matrixAkhir.csv', matrixAkhir, delimiter=',', fmt='%s')