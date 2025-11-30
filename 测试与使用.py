from ultralytics import YOLO
yolo = YOLO(model='icon3.pt',task='detect')
result = yolo(source='tests',save=True)