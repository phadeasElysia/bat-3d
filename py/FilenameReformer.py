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

directory_path_arr = [directory_path_pointclouds,directory_path_cam_front,directory_path_cam_front_right,directory_path_cam_front_left,
                      directory_path_cam_back,directory_path_cam_back_left,directory_path_cam_back_right]

dict = {}

for i in directory_path_arr:
    print(i)
    files = os.listdir(i)
    sorted_files = sorted(files)
    print(sorted_files)
    z = 0
    for file in sorted_files:
        if os.path.isfile(os.path.join(i, file)):
            if file.endswith('.bin'):
                #print('a')
                filename = str(z).zfill(6) + file[-8:]
            else:
                filename = str(z).zfill(6) + file[-4:]
            dict[i + '/' + file] = filename
            os.rename(os.path.join(i, file), os.path.join(i, filename))
            z += 1

json_dict = json.dumps(dict, indent = 4)
text = str(len(dict)//7) + '\n' + json_dict

with open('output.txt', 'w') as file:
    file.write(text)
