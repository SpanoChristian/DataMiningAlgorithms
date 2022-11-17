import sys

fname = "test_files/contextPrefixSpan.txt"

def convert_list_to_sequence(sequence):

	s = "("
	start = True

	for i in range(len(sequence)):
		if sequence[i] == -1:
			s = s+")"
			start = True
			if (i!=(len(sequence)-2)):
				s = s+"("
		elif sequence[i] != -2:
		# 	s = s + ")"
		# else:
			if not start:
				s = s + "," 
			s = s + str(sequence[i])
			start = False


	return s


if len(sys.argv)!=2:
	print(sys.argv[0]+" <filename>")
else:

	with open(fname) as f:
	    sequences = f.readlines()

	sequences = [ [int(x) for x in x.split(' ')] for x in sequences] 

	for s in sequences:
		# print (str(s))
		print(convert_list_to_sequence(s))

