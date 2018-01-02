import MySQLdb
import numpy
import math
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

def termFreq(stringList,cari):
    result = 0
    for x in range(len(stringList)):
        if(stringList[x] == cari):
            result = result + 1
    return result

def hitungPMIMax(stringList, matrixAkhir, totalKataUnik, kata1, kata2):
    result = 0
    
    fdW1W2 = 0
    ek = 10
    yw1 = 0
    yw2 = 0
    p = 7.5
    q = 10
    n = len(stringList)
    fw1 = termFreq(stringList,kata1)
    fw2 = termFreq(stringList,kata2)
    
    print("kata 1 : ",kata1)
    print("kata 2 : ",kata2)
    
    for i in range(1,totalKataUnik+1):
        if(kata1 == matrixAkhir[i][0]):
            for j in range(1,totalKataUnik+1):
                if(kata2 == matrixAkhir[0][j]):
                    fdW1W2 = matrixAkhir[i][j]
                    print("Coocurence : ",fdW1W2)
                    yw1 = (math.pow((math.log(fw1))+q,p))/(math.pow((math.log(700))+q,p))
                    yw2 = (math.pow((math.log(fw2))+q,p))/(math.pow((math.log(700))+q,p))
                    result = math.log(((fdW1W2-((ek/n)*(fw1*fw2-(fw1/yw1)*(fw2/yw2))))*n)/((fw1/yw1)*(fw2/yw2)))
                    print("yw1 : ",yw1)
                    print("yw2 : ",yw2)
                    print("Nilai PMIMax : ",result)
                    print("n : ",n)
                    print("fw1 : ",fw1)
                    print("fw2 : ",fw2)
    return

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
    
    # membuat inisialisasi matrix
    matrixAkhir = numpy.zeros(s, dtype = object)
    for x in range(totalKataUnik) :
        matrixAkhir[0][x+1] = stringListMatrix[x]
        matrixAkhir[x+1][0] = stringListMatrix[x]
    numpy.savetxt('matrixAkhir.csv', matrixAkhir, delimiter=',', fmt='%s')
    
    # hitung bobot
    windowSize = 1
    for x in range(totalKataUnik):
        context1 = cariKata(stringList,stringListMatrix[x],windowSize)
        for y in range(totalKataUnik):
            bobot = 0
            for k in range(len(context1)):
                if(stringListMatrix[y] == context1[k]):
                    bobot = bobot + 1
                    matrixAkhir[x+1][y+1] = bobot
    numpy.savetxt('matrixAkhir.csv', matrixAkhir, delimiter=',', fmt='%s')
    
    hitungPMIMax(stringList, matrixAkhir, totalKataUnik, "at", "at")
    
    return

# jalankan main program
main()