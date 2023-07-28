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
