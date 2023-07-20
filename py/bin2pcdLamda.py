import os
import numpy as np
# import pcl

path_in = 'input/NuScenes/official/pointclouds-bin/'
path_out = 'input/NuScenes/official/pointclouds_pcd/'
for file in sorted(os.listdir(path_in)):
    points = np.fromfile(path_in+file, dtype=np.float32).reshape(-1, 4)

    # write header
    num_points = len(points)

    out_file = path_out + file[:-4]
    if '.pcd' not in out_file:
        out_file = out_file + '.pcd'
    
    with open(out_file, 'w') as file_writer:
        file_writer.write("# .PCD v0.7 - Point Cloud Data file format\n"
                          + "VERSION 0.7\n"
                          + "FIELDS x y z intensity\n"
                          + "SIZE 4 4 4 4\n"
                          + "TYPE F F F F\n"
                          + "COUNT 1 1 1 1\n"
                          + "WIDTH " + str(num_points) + "\n"
                          + "HEIGHT 1\n"
                          + "VIEWPOINT 0 0 0 1 0 0 0\n"
                          + "POINTS " + str(num_points) + "\n"
                          + "DATA ascii\n")
        for line in points:
            # line_str = ''
            # for i in line:
            #     i = str(i)
            #     if len(i) < 11:
            #         i = i.ljust(11, '0')
            #     line_str = line_str + i + ' '
            # line_str = line_str[:-1] + '\n'
            # file_writer.write(line_str)

            line_list = list(map(lambda x: str(x), line))
            line_str = ' '.join(line_list) + '\n'
            file_writer.write(line_str)

