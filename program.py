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

# fungsi mencari nilai bobot
def cariKata(stringList, toMatch, windowSize):
    before = windowSize
    after = windowSize
    
    sb = []
    for x in range(len(stringList)) :
        if (toMatch == stringList[x]) :
            index = x
            if ((0 <= index - before) and (index + after <= len(stringList))) :
                y = index - before
                while y < index + after :
                    sb.append(stringList[y])
                    y = y + 1
                result = sb
            elif (0 > index - before) :
                y = 0
                while y < index + after :
                    sb.append(stringList[y])
                    y = y + 1
                result = sb        
            elif (index + after >= len(stringList)) :
                y = 0
                while y < index + after :
                    sb.append(stringList[y])
                    y = y + 1
                result = sb
    return result

# main program
def main():
    
    # baca file corpus
    fileCorpus = open("katates.txt", "r") 
    # insert kata-kata corpus ke dalam list
    stringList = fileCorpus.read().strip().split(" ")
    # hilangkan null/"" dari list
    stringList = list(filter(("").__ne__, stringList))
    
    # hilangkan kata-kata yang sama dari list
    stringListMatrix = list(set(stringList))
    # sort kata-kata list berdasarkan abjad
    stringListMatrix.sort()
    
    # print jumlah kata unik
    totalKataUnik = len(stringListMatrix)
    s = (totalKataUnik + 2, totalKataUnik + 2)
    
    matrixAkhir = numpy.zeros(s, dtype = object)
    for x in range(totalKataUnik) :
        matrixAkhir[0][x+1] = stringListMatrix[x]
        matrixAkhir[x+1][0] = stringListMatrix[x]
    numpy.savetxt('matrixAkhir.csv', matrixAkhir, delimiter=',', fmt='%s')
    
    z = 0
    
    return

# jalankan main program
main()