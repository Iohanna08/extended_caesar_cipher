# -*- coding: utf-8 -*-
#creates encryption plaintext-to-ciphertext using a .txt file as secret key.

#first create the secret key out of the chosen .txt file
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.',',',':',';','!','?','+','=','-']
encrypt_bron=raw_input('Give key as .txt file: ')
try:
    fhand=open(encrypt_bron)
except:
    print 'Error: file not found.'
    exit()

encrypt_total=str()

for line in fhand:
    line=line.rstrip()
    line=str(line)
    if line == '':
        continue
    else:
        encrypt_total= encrypt_total+line

coding_scheme=dict()
absent_letters=list()
numbers=list()

#create a dictionary of [key, value]-sets representing the original letter (key) and the encoding (value) based on the .txt file as secret key
for letter in letters:
    index=encrypt_total.find(letter)
    if index == -1:
        absent_letters.append(letter)
    else:
        coding_scheme[letter]=index
        numbers.append(int(index))

for letter in absent_letters:
    coding=max(numbers)+1
    coding_scheme[letter]=coding
    numbers.append(coding)

print 'Not found in secret key and added: ', absent_letters
print 'Key creation complete.'
print coding_scheme

#encode the plaintext to ciphertext using the coding scheme derived from the secret key
plaintext=raw_input('Enter .txt file: ')
try:
    source_file=open(plaintext)
except:
    print 'Error: file not found.'
    exit()

output='output_file_encoded.txt'
o=open(output, 'w')

for line in source_file:
    line=line.rstrip() #geeft soms problemen in files waar geen \n zit! Dan wordt laatste letter gestript!
    line=line.lower()
    line=str(line)
    #print line
    t=list(line)
    #print t
    p=list()
    for x in t:
        if x == ' ':        #replaces all ' ' by [-]
            p.append('-')
        else:
            try:            #replaces all letters by their respective ciphers
                k=coding_scheme.get(x,0)
                x=x.replace(x,str(k))
                p.append(x)
            except:
                p.append(x)     #deals with exceptions as plaintext > plaintext (not normally used)

    #rebuild the sentences in the plaintext message with the ciphertext
    sentence=''
    for i in p:
        sentence=sentence+'/'+ i

    #write each sentence to the output file: output_file_encoded.txt
    #print sentence
    o.write(sentence+'\n')

o.close()

print 'Encryption completed. Output file [output_file_encoded.txt] placed in directory.'