# preprocessing bahasa indonesia

# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Lakukan stemming
print("1. Lakukan Stemming")
factory = StemmerFactory()
stemmer = factory.create_stemmer()
fileCorpus = open("katates2.txt", "r") #rubah corpus disini
corpusText = fileCorpus.read().strip()
outputStemming = stemmer.stem(corpusText)
hasilStemming = open("hasilStemming.txt", "w") #file hasil stemming, case-folding
hasilStemming.write(outputStemming)
hasilStemming.close()

# lakukan stopword
print("2. Lakukan Stopwrod")
listKataStopword = open("stopwordlist.txt","r").read().strip().split(" ")
listKataStemming = outputStemming.strip().split(" ")
outputStopword = [elem for elem in listKataStemming if elem not in listKataStopword ]
outputStopword = ' '.join(outputStopword).strip()
hasilStopword = open("hasilPreprocessing.txt", "w") #file corpus bersih
hasilStopword.write(outputStopword)
hasilStopword.close()

print("3. Preprocessing Selesai")

