# 使用脚本和标注的步骤



# 如果您的点云文件是二进制格式的：

将您的文件放在“input/Nusscenes/overtical/pointclods bin”中运行bin2pcdLamda.py。这将删除您“input/Nuscenes/overtical/pointclods”中的所有文件

并将转换后的pcd文件放在此目录中。

# 1.文件名格式化程序

1. 将相机图像的文件放入“input/NuScenes/official/camera”目录，并将pointclods文件放入 “input/NuScenes/official/pointclouds"目录

2. 在bat-3d目录下运行FilenameReformar.py。如果已存在output.txt您将被询问是否覆写文件，如果要覆写文件，请考虑pointclouds和camera的文件名是否正确 为您的最终文件。否则，文件名可能无法恢复。

3. 开始注释。完成所有注释后，下载注释文件并 将它们提取到“输入/NuScenes/official/annotations”中



# 2.文件名恢复程序

1. 在bat-3d目录下运行FileNameRecover.py。这将恢复之前的文件名，并在注释文件中修改相应的时间戳。

# Steps to use the scripts

# If your pointclouds file are in binary format:
Put your files in "input/Nuscenes/official/pointclods-bin" run bin2pcdLamda.py. THIS WILL ERASE ALL FILES IN YOUR "input/Nuscenes/official/pointclods"
DIRECTORY and put the converted pcd files in this directory.
# 1.FilenameReformer
1. Put the files of camera images into camera directory and pointclods files into 
pointclouds directory under "input/NuScenes/official".
2. Run FilenameReformaer.py under bat-3d directory. If you enconter a question about whether
you want to rewrite the file, please consider whether you want to use the current file name
for your final files. Otherwise the filenames may not be recovered.
3. Start annotation. After finished all the annotations, download the annotation files and 
extract them into "input/NuScenes/official/annotations"

# 2.FilenameRecoverer
1. run FilenameRecoverer.pyunder bat-3d directory. This recover the file names before 
you reform it and add corresponding timestamp in the annotation files. 
