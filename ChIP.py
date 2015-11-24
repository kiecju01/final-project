import os

ChIPgenes = []

# Open ChIP-seq data spreadsheet
ChIPsheet = "ChIPcomplete.txt"
ChIPFile = open(ChIPsheet, 'r')
ChIPFile.readline() #skip header
for line in ChIPFile:
	line = line.rstrip('\n')
	ChIPdata = line.split() #splits line on tabs
	if ChIPdata[7] not in genes:
		genes.append(ChIPdata[7])

print len(ChIPgenes)

ChIPFile.close()

RNA_ChIPcombined.txt

# Open combined RNA-seq/ChIP)-seq data spreadsheet
RNAsheet = "RNA_ChIPcombined.txt"
RNAFile = open(RNAsheet, 'r')
RNAFile.readline() #skip header
for line in RNAFile:
	line = line.rstrip('\n')
	RNAdata = line.split() #splits line on tabs


RNAFile.close()
		