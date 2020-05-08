import sys
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model, load_model
from PIL import Image

classes = ["Lumpy", "Giggles", "Cuddles"]
num_classes = len(classes)
img_size = 224

# 引数から画像ファイルを参照して読み込む
image = Image.open(sys.argv[1])
image = image.convert("RGB")
image = image.resize((img_size, img_size))
data = np.asarray(image) / 255.0
X = []
X.append(data)
X = np.array(X)

# モデルロード
model = load_model("model/htf_model.h5")

result = model.predict([X])[0]
predicted = result.argmax()
percentage = int(result[predicted] * 100)

print(classes[predicted], percentage)
