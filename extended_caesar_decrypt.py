# -*- coding: utf-8 -*-
# creates the ciphertext-to-plaintext decryption of a .txt ciphertext using the secret key .txt file

import sys

#first create the secret key out of the chosen .txt file
key_bron=raw_input('Give secret key as .txt file: ')
try:
    secret_key=open(key_bron)
except:
    print 'Error: file with secret key not found.'
    sys.exit()

encrypt_total=str()

for line in secret_key:
    line=line.rstrip()
    line=str(line)
    if line == '':
        continue
    else:
        encrypt_total= encrypt_total+line

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.',',',':',';','!','?','+','=','-']

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
print 'Coding scheme:', coding_scheme

#create the decoding scheme by inversing the coding scheme
decoding_scheme=dict()
for key in coding_scheme:
    decoding_scheme[coding_scheme[key]]= key

print 'Decoding scheme: ', decoding_scheme

#import the ciphertext and decode each line using the decoding scheme
encrypt_file=raw_input('Enter encrypted file as .txt file: ')

try:
    enc=open(encrypt_file)
except:
    print 'Error: file not found.'
    exit()

output='output_file_decoded.txt'
o=open(output, 'w')


for regel in enc:
    regel=regel.rstrip()
    #print regel
    t=list(regel)

    #rebuilds the ciphertext to a list with items and decrypts each item in the list
    s=list()
    getal=''
    for item in t:
        if item == '-':
            s.append(item)
        elif item != '/':
            getal=getal+item
        elif item == '/':
            if getal == '':
                continue
            else:
                s.append(getal)
                getal=''
                continue

    p=list()
    for x in s:
        if x == '-':
            p.append(' ')
        elif x == '0':  #gives [.] to all unknown values in decryption
            p.append('.')
        else:
            try:
                x=int(x)
                k=decoding_scheme.get(x,0)
                p.append(k)
            except:
                p.append(x)

    #rebuilds .txt (plaintext) file with decrypted sentences and writes them to output file [output_file_decoded.txt]
    sentence=''
    for i in p:
        i=str(i)
        sentence=sentence+i

    #print sentence
    o.write(sentence+'\n')

o.close()

print 'Decryption completed. Output file [output_file_encoded.txt] placed in directory.'


