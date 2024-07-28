from os.path import join

from ultralytics import YOLO

from dota2ai.settings import DATA_DIR

model = YOLO(model="./runs/detect/train/weights/best.engine")
results = model.predict(join(DATA_DIR, "heroes/1.png"))
results[0].show()
