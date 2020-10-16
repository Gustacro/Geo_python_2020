#------------------------
s = 'Hi there tom'
print(s.split())
a = 'hi there dad'
print(a.split())
#------------------------
planet = 'Earth'
diameter = 12742
print('the diameter of the {0} is {1} kilometers'.format(planet, diameter) )
#------------------------
lst = [1,2,[3,4], [5,[100, 200, ['hi']], 23, 11],1,7]
print(lst[3][1][2][0])
d = {'k1': [1,2,3,{'tricky':['oh', 'man', 'inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])
#------------------------
email = 'user@domain.com'
def e(email):
	return(email.split('@')[-1])

print(e(email))
#---------------------
def findDog(st):
	return "dog" in st.split()

print(findDog('Is there a dog here'))
#---------------------
def countwords(st):
	count = 0
	for i in st.lower().split():
		if i == 'dog':
			count += 1
	return ('there are',count, 'dogs')


print(countwords('I have a male dog and a female dog too'))
#---------------------
lst = [i for i in range(1500, 2700) if i % 7 == 0 and i % 5 == 0]
print(lst)

#---------------------
star = '*'
text = ''
line = '-'
flag = ''

n = 3
for i in range(n):
	for j in range(i):
		text = (star* 7)
		print(text)


word = 'tom'#str(input("Enter a word to find its reverse spelling: "))
for i in range(len(word) -1, -1, -1 ):
	print(word[i], end='')
print('\n')

#---------------------

numbers = (1,2,3,4,5,6,7,8,9)
even = 0
odd  = 0
for i in numbers:
	if not i % 2:
		even += 1
	else:
		odd += 1
print('Number of even numbers: {}\nnumber of odd numbers: {}'.format(even, odd))
#---------------------

def hello(name, age):
	return("Hello, my name is {}. I'm {} years old".format(name, age))

print(hello('tom', 13))

#---------------------

def celsiusToFahr(tempCelsius): # create function to find degrees in Fahrenheit from Celsius
	return(tempCelsius* 9/5 + 32 ) # conversion formula

freezingPoint = celsiusToFahr(0) # Create variable to save the value to be converted
print('The freezing point of water in Fahrenheit is:', freezingPoint)
print('The boiling point of water in Fahrenheit is:', celsiusToFahr(100))

def kelvinsToCelsius(tempKelvins): # create a function to convert to Celsius from Kelvins
	return(tempKelvins - 273.15) # conversion formula

absoluteZero = kelvinsToCelsius(tempKelvins =0) # create variable calling function 'kelvinsToCelsius' with its parameter included
print('Absolute zero in Celsius is:',absoluteZero)

def kelvinsToFahr(tempKelvins):
	tempCelsius = kelvinsToCelsius(tempKelvins)
	tempFahr = celsiusToFahr((tempCelsius))
	return(tempFahr)

absoluteZeroFahr = kelvinsToFahr(tempKelvins =0)
print('Absolute zero in Fahrenheit is:', absoluteZeroFahr)