import os
import binascii

# print (file_list)


def find_reach(file_path):
	with open(file_path,"rb") as f :
	
		while(True):
			rich = f.read(4)
			if (rich == b'\x52\x69\x63\x68'): #Rich -> \x52\x69\x63\x68 
				data = f.read(4)
				#print (file_path + " : " + str(binascii.b2a_hex(data)))
				return binascii.b2a_hex(data)
			if (rich ==b''):
				return ''
																																																																																																																													
def main():
	path_dir = ".\\yara_sample"
	file_list = os.listdir(path_dir)

	rich_list = []

	for file in file_list :
		rich_result = find_reach(path_dir + "\\" +file)
		# print (rich_result)
		if (rich_result !=''):
			rich_list.append(rich_result)


	# print (rich_list)
	rich_list = list(set(rich_list))
	# print (rich_list)
#b'de86971f'
	# for rich in rich_list:
	# 	print (rich)

	# 	break
	i = 0
	for rich in rich_list:
		i +=1
		print ("$rich_" + str(i) + " = { " + "52 69 63 68 "+ str(rich[0:2])[2:4] + " " + str(rich[2:4])[2:4] + " " + str(rich[4:6])[2:4] + " " + str(rich[6:8])[2:4] + " }")
		# print (rich[0:2])
		# print (rich[2:4])
		# print (rich[4:6])
		# print (rich[6:8])
		# break


	# i = 0
	# for rich in rich_list :
	# 	i +=1
	# 	rich = str(rich).replace("'","")
	# 	print ("$rich_" + str(i) + " = { " + rich[0:2] + " " + rich[2:4] + " " + rich[4:6] + " " + rich[6:8] + " }")

if __name__ == "__main__":
	main()