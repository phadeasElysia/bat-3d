import os
import json

path = 'output.txt'
path_to_annotations = 'input/NuScenes/official/annotations/'

f = open(path, 'r')
file = f.readlines()
number = int(file[0])
file = file[2:-1]
i = 0
for f in file:
    f = f[4:]
    farr = f.split(" ")
    directory = farr[0][1: len(farr[0]) - 2]
    name = farr[1][1:len(farr[1]) - 3]
    if name.endswith('jp'):
        name = name + 'g'
    directory = directory.split('/')
    directory_name = directory[-2]
    if not directory_name == 'annotations':
        old_name = directory[-1]
        directory = directory[:-1]
        new_directory = ''
        for d in directory:
            new_directory = new_directory + d + '/'
        os.rename(os.path.join(new_directory, name), os.path.join(new_directory, old_name))
        if i < number and os.listdir(path_to_annotations):
            # name = name[:-4] +'.json'
        # timestamp = old_name[-20:]
        # timestamp = timestamp[:-4]
        # with open(path_to_annotations + name, 'r') as annotation_file:
        #     annotation_json_data = json.load(annotation_file)
        # annotation_json_data['timestamp'] = timestamp
        # with open(path_to_annotations + name, 'w') as annotation_file:
        #     json.dump(annotation_json_data, annotation_file)
        # os.rename(os.path.join(path_to_annotations, name), os.path.join(path_to_annotations, old_name[:-4]+'.json'))
            timestamps = old_name[-20:]
            timestamps = timestamps[:-4]
        #print(timestamps)
            with open(path_to_annotations + name[:-4] + '.json', 'r') as annotation_file:
                annotation_json_data = json.load(annotation_file)
            annotation_json_data['timestamp'] = timestamps
            with open(path_to_annotations + name[:-4] + '.json', 'w') as annotation_file:
                json.dump(annotation_json_data, annotation_file)
            os.rename(os.path.join(path_to_annotations, name[:-4] + '.json'), os.path.join(path_to_annotations, old_name[:-4] + '.json'))
            i += 1
if os.path.exists(path):
        # Delete the file if it already exists
        os.remove(path)