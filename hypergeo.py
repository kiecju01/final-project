import os

# Find number of genes identified by ChIP-seq:

ChIPgenes = []

# Open ChIP-seq data spreadsheet
ChIPsheet = "ChIPcomplete.txt"
ChIPFile = open(ChIPsheet, 'r')
ChIPFile.readline() #skip header
for line in ChIPFile:
	line = line.rstrip('\n')
	ChIPdata = line.split() #splits line on tabs
	if ChIPdata[7] not in ChIPgenes:
		ChIPgenes.append(ChIPdata[7])

print "Genes identified by ChIP-seq:", len(ChIPgenes)

ChIPFile.close()

# Find number of genes identified by RNA-seq:

RNAgenes = []

# Open ChIP-seq data spreadsheet
RNAsheet = "RNAsig02FDR.txt"
RNAFile = open(RNAsheet, 'r')
RNAFile.readline() #skip header
for line in RNAFile:
	line = line.rstrip('\n')
	RNAdata = line.split() #splits line on tabs
	if RNAdata[0] not in RNAgenes:
		RNAgenes.append(RNAdata[0])

print "Genes identified by RNA-seq:", len(RNAgenes)

RNAFile.close()

# Find number of genes overlapping between RNA-seq and ChIP-seq data:

RNAChIP = []

# Open combined RNA-seq/ChIP)-seq data spreadsheet
RCsheet = "RNA_ChIPcombined.txt"
RCFile = open(RCsheet, 'r')
RCFile.readline() #skip header
for line in RCFile:
	line = line.rstrip('\n')
	RCdata = line.split() #splits line on tabs
	if RCdata[0] not in RNAChIP:
		RNAChIP.append(RCdata[0])

print "Genes identified by both RNA-seq and ChIP-seq:", len(RNAChIP)
	
RCFile.close()

# Find number of genes in mm9:
	# Dowloaded list of annotated genes in mm9 from UCSC table browser. Not all genes have been given names. Since the way I am merging the ChIP-seq and RNA-seq lists is through gene names, I have to calculate how many unique names, and not transcripts, there are in mm9. To get rid of NAs so that the python script will work, used R to open UCSC file, get rid of NAs, and write a new file.

mm9 = []

# Open combined RNA-seq/ChIP)-seq data spreadsheet
IDsheet = "mm9complete.txt"
IDFile = open(IDsheet, 'r')
IDFile.readline() #skip header
for line in IDFile:
	line = line.rstrip('\n')
	IDdata = line.split() #splits line on tabs
	if IDdata[0] not in mm9:
		mm9.append(IDdata[0])

print "Genes in mm9:", len(mm9)

	
IDFile.close()		