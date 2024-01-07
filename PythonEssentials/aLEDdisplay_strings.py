# Definir os padrões para cada um dos 10 dígitos 
# As sete posições correspondem ao display de sete segmentos

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

# Função que converte a string no display de LED

def print_number(num):
	global digits
	digs = str(num) # Convertendo o número de int para str
	lines = [ '' for lin in range(5) ] # As cinco linhas começam todas vazias
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ] # Acessando cada coluna de cada linha
		ptrn = digits[ord(d) - ord('0')] # Acessando cada dígito no padrão de sete segmentos
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
		# juntando os segementos de cada dígito convertido
			lines[lin] += ''.join(segs[lin]) + ' '
		# aqui ocorre a soma das matrizes lines[lin], o que pode ser verificado ao executar:
			# print(lines[lin])
	for lin in lines: # Imprime cada linha depois do join das linhas das matrizes somadas
	  print(lin)

print_number(int(input("Enter the number you wish to display: ")))




