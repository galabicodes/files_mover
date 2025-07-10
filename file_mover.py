import os
import shutil
source_folder = os.path.expanduser("~/Desktop/source")
destination_folder = os.path.expanduser("~/Desktop/destination")
files = os.listdir(source_folder)
for filename in files:
	file_path = os.path.join(source_folder , filename)
	if os.path.isfile(file_path) and filename.lower().endswith(".pdf") :
		new_path = os.path.join(destination_folder , filename)
		shutil.move(file_path , new_path)
		print("moved:" , filename)


