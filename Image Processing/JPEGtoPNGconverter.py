from PIL import Image
import os
import sys


# grab first and second argument using sys
if len(sys.argv) != 3:
    print("please give two arguments")
else:
    input_folder = str(sys.argv[1]).rstrip()
    output_folder = str(sys.argv[2]).rstrip()
    print(sys.argv)
    print(input_folder, output_folder)
    # check if new\ exists, create if not

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # loop through Pokedex
    # convert them to png
    #save image to new folder
    directory = os.fsencode(input_folder)
    
    for file in os.listdir(directory):
        curr_file = os.fsdecode(file)
        print("processing " + curr_file + "...")
        img = Image.open('./'+input_folder+'/'+curr_file)
        cfile_name, extension = curr_file.split('.')
        if(extension == "jpg"):
            img.save('./'+output_folder+'/'+cfile_name + '.png', 'png');
            print(curr_file + f" converted to {cfile_name}.png successfully!")
     


        
