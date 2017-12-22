file = open('test30/info.lst', 'r')
wfile = open('new_test_info.lst', 'w')
lines = file.readlines()
for line in lines:
	ll = line.split()
	nline = ' '.join(ll) + ' ' + str(int(ll[4]) * int(ll[5])) + '\n'
	wfile.write(nline)

file.close()
wfile.close()