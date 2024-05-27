# CV-task

#### 介绍
Using dysample operator to improve yolov8 for road disease detection in computer vision

#### 软件架构
将Dysample算子[1]应用到YOLOv8中提升道路病害检测效果

[改进后的网络结构](https://foruda.gitee.com/images/1716792594978209699/426f4c51_8803230.png "屏幕截图")

#### 使用说明

1.  环境配置（遵循YOLOv8官方文档）
[YOLOv8官方文档](http://https://docs.ultralytics.com/)
2.  准备RDD2022数据集(↓)，放入v8_dysample/ultralytics-main/ultralytics/models/yolo/detect/datasets路径下

[百度网盘链接](链接：https://pan.baidu.com/s/1HfNSejaVJ9ZdXTGO2NrSDg?pwd=1q5z 
提取码：1q5z)

3.  训练模型，终端输入

```
python v8_dysample/ultralytics-main/train.py
```

#### 参考文献
[1] Liu W, Lu H, Fu H, et al. Learning to Upsample by Learning to Sample[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 6027-6037. 
