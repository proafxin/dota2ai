from os.path import join

from ultralytics import YOLO

from dota2ai.settings import DATA_DIR

model = YOLO(model="yolov10n.pt")

model.train(data=join(DATA_DIR, "heroes/dota2.yaml"), epochs=100, verbose=False, imgsz=640)
model.export(format="engine", dynamic=True, batch=8, workspace=4, int8=True, data=join(DATA_DIR, "heroes/dota2.yaml"))
