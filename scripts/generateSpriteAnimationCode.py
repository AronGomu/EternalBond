animation_name = "nivi_wave"
img_name = "nivi maid wave brows0 eyes0 mouth0 mouth closed open eyes"
start_index = 0
stop_index = 119
pause = 0.04

code_string = "image " + animation_name + ":\n"

for i in range(start_index, stop_index+1):
	code_string += "\t\"" + img_name + " " + str(i) + "\"\n"
	code_string += "\tpause " + str(pause) + "\n"


text_file = open(animation_name + ".rpy", "w")
n = text_file.write(code_string)
text_file.close()