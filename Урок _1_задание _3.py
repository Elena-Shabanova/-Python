n = int(input('Введите цифру от 1 до 9: '))
nn = n*10+n
nnn = n*100+n*10+n
text = str(n)+'+'+str(n)*2+'+'+str(n)*3+' ='
print(text, n+nn+nnn) 