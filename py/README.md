# 使用脚本和标注的步骤



## 如果您的点云文件是二进制格式的：

将您的文件放在“input/Nusscenes/[your_sequence_name]/pointclods bin”中运行bin2pcdLamda.py。这将删除您“input/Nuscenes/[your_sequence_name]/pointclods”中的所有文件

并将转换后的pcd文件放在此目录中。

## 1.文件名格式更改
如果您的文件名称不符合输入要求（000000,000001......)请进行以下步骤：

1. 将相机图像的文件放入“input/NuScenes/[your_sequence_name]/camera”目录，并将pointclods文件放入 “input/NuScenes/[your_sequence_name]/pointclouds"目录

2. 在bat-3d目录下运行FilenameReformar.py。如果已存在output.txt您将被询问是否覆写文件，如果要覆写文件，请考虑pointclouds和camera的文件名是否正确 为您的最终文件。否则，文件名可能无法恢复。

## 2.注释
1. 在您按照主目录的教程进行安装后，您还需要更改config.json中的sequence中的内容，将其更改为你的sequence 名字
2. 根据您是否需要进行pointcloud only annotation来修改base_label_tool.js中的pointCloudOnlyAnnotation参数
3. 开始注释。完成所有注释后，下载注释文件并 将它们解压提取到“input/NuScenes/[your_sequence_name]/annotations”中

## 3.文件名称恢复

1. 在bat-3d目录下运行FileNameRecover.py。这将恢复之前的文件名，并在注释文件中修改相应的时间戳。

## 对标注物添加visibility属性
如果您在标注网页中绘制了bounding box，在屏幕右侧可以找到每个box并选择其属性，visibility可以在其中更改。提供'0%-40%','41%-60%','61%-80%','91%-100%'四种选择，若未进行选择默认为undefined。
### 添加visibility功能的代码改动：
在pcd_label_tool.js addBoundingBoxGui 1227,[1252-1271](https://github.com/phadeasElysia/bat-3d/blob/04c8dda04b6ea01ad2601a0ec45835c8906527bf/js/pcd_label_tool.js#L1252)行进行了改动。
在base_label_tool.js createAnnotationFile [594-604](https://github.com/phadeasElysia/bat-3d/blob/04c8dda04b6ea01ad2601a0ec45835c8906527bf/js/base_label_tool.js#L594)行进行了改动。

## 更改标注物trackId的属性
将trackId更改为递增数字不考虑当前帧的熟练。仅考虑总共的标签的物体数量。
### 代码改动：
在pcd_label_tool.js setHighestAvailableTrackId [763-778](https://github.com/phadeasElysia/bat-3d/blob/04c8dda04b6ea01ad2601a0ec45835c8906527bf/js/pcd_label_tool.js#L763) 进行改动。
在base_label_tool.js [39](https://github.com/phadeasElysia/bat-3d/blob/04c8dda04b6ea01ad2601a0ec45835c8906527bf/js/base_label_tool.js#L39) 添加了 currentMinTrackId[] 

### 相关界面的trackId栏暂时无法使用
