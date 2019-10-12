from scraper import *
from snapshot import *
from vision import *
from translate import *

TakeSnapAndSave()
text = detect_text("/Users/tiff/GitHub/RxTranslate/resources/snapshot.jpg")
trans(text, "es")

