print('shiza khan','18B-130-CS(A)')
print('lab 02','exercise 5')
print('\n')
#number of characters in the word "anachronistically" is more than in the word
##"counterintuitive"
a = "anachronistically"
b = "counterintuitive"
c = len(a)>len(b)
print(c)
#the word "misinterpretation" appears earlier in the dictionary than the word
##"misrepresentation"
d = "misinterpretation"
e = "misrepresentation"
f = d>e
print(f)
#the letter 'e' doesn't appear in the word 'floccinaucinihilipilification'
g = 'floccinaucinihilipilification'
h =  'e' in g
print(h,"'e'  does not appear in the word 'floccinaucinihilipilification'")
#the number of character in the word 'counterrevolution' is equal to the sum
##of the num of characters in 'counter' and 'resolution'
i = 'counterrevolution'
j = 'counter'
k = 'resolution'
l = len(i)==len(j) + len(k)
print(l)
