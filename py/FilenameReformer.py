import os
import json

directory_path = 'input/NuScenes/official/'
directory_path_cam_back_left = directory_path + 'images/CAM_BACK_LEFT'
directory_path_cam_back_right = directory_path + 'images/CAM_BACK_RIGHT'
directory_path_cam_back = directory_path + 'images/CAM_BACK'
directory_path_cam_front = directory_path + 'images/CAM_FRONT'
directory_path_cam_front_left = directory_path + 'images/CAM_FRONT_LEFT'
directory_path_cam_front_right = directory_path + 'images/CAM_FRONT_RIGHT'
directory_path_pointclouds = directory_path + 'pointclouds'
directory_path_annotations = directory_path + 'annotations'

directory_path_arr = [directory_path_pointclouds, directory_path_cam_front, directory_path_cam_front_right,
                      directory_path_cam_front_left,
                      directory_path_cam_back, directory_path_cam_back_left, directory_path_cam_back_right,
                      directory_path_annotations]

dict = {}


def extract_number_from_filename(filename):
    return filename[:-4].split('_')[-1]


files = os.listdir(directory_path_arr[3])
for i in directory_path_arr:
    # print(i)
    files = os.listdir(i)
    sorted_files = sorted(files, key=lambda x: extract_number_from_filename(x))
    # sorted_files = sorted(files)
    # print(sorted_files)
    z = 0
    for file in sorted_files:
        if os.path.isfile(os.path.join(i, file)):
            if file.endswith('.json'):
                # print('a')
                filename = str(z).zfill(6) + file[-5:]
            else:
                filename = str(z).zfill(6) + file[-4:]
            dict[i + '/' + file] = filename
            os.rename(os.path.join(i, file), os.path.join(i, filename))
            z += 1

json_dict = json.dumps(dict, indent=4)
text = str(len(files)) + '\n' + json_dict


def continue_program():
    while True:
        user_input = input("Do you want to continue the program? (yes/y or no/n): ").lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


if os.path.exists('output.txt'):
    print('Output file already exists!\nContinue might overwrite the file.')
    if continue_program():
        # Your main program code here
        print("Continuing the program...")
        with open('output.txt', 'w') as file:
            file.write(text)
            print('done')
    else:
        print('Please check whether the filename is recovered!')
else:
    with open('output.txt', 'w') as file:
        file.write(text)
