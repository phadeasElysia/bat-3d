import os
import struct
import numpy as np

path_in = 'input/NuScenes/official/pointclouds-bin/'
path_out = 'input/NuScenes/official/pointclouds_pcd/'


for file in sorted(os.listdir(path_in)):
    points = np.fromfile(path_in + file, dtype=np.float32).reshape(-1, 4)
    #print(points)

    # write header
    num_points = len(points)
    with open(path_out + file[:-4], 'w') as file_writer:
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
                          + "DATA binary\n")
        # for i in range(0, len(binary_data), 16):  # 16 bytes (4x 4-byte float32) for each point
        #     x, y, z, intensity = struct.unpack('ffff', binary_data[i:i + 16])
        #     file_writer.write(f"{x:.6f} {y:.6f} {z:.6f} {intensity:.6f}\n")
        for line in points:
            line_str = ''
            for i in line:
                i = str(i)
                if len(i) < 11 :
                    i = i.ljust(11, '0')
                line_str = line_str + i + ' '
            line_str = line_str[:-1] + '\n'
            file_writer.write(line_str)