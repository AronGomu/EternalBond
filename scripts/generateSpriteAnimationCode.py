animation_name = "nivi_chapter_02_doggy_nivi_rape_come_outside"
img_name = "cg chapter 02 nivi rape come outside"
start_index = 0
stop_index = 15
pause = 0.04

code_string = "image " + animation_name + ":\n"

for i in range(start_index, stop_index+1):
	code_string += "\t\"" + img_name + "" + str(i) + "\"\n"
	code_string += "\tpause " + str(pause) + "\n"


text_file = open(animation_name + ".rpy", "w")
n = text_file.write(code_string)
text_file.close()