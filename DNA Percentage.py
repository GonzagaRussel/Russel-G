file_text = open ("x.txt.") .read()
X = len(file_text)
C = 0
G = 0

for i in range (0, X) :
    if file_text[1] == 'c':
        C = C + 1
    else:
        C = C + 0
    if file_text[1]== 'g' :
        G = G + 1
    else:
        G = G +0
    Y = C + G
    print "the length of dna is", len(file_text)
    print "the number of c's is", C
    print "the number of g's is", G
    print "the percentage of c+g is", (100.0*7)/X
