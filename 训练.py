from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolov8n.pt')  # 会自动下载模型

#训练模型
model.train(data='icon.yaml',workers=0,epochs=300,batch=16)
