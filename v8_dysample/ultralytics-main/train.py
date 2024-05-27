from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8-dysample.yaml')

    model.train(data=r'ultralytics/cfg/datasets/RDD.yaml',
                imgsz=640,
                epochs=150,
                batch=32,
                )