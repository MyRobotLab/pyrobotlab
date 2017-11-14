tesseract = Runtime.createAndStart("tesseract","TesseractOcr")

txtStr = tesseract.ocr("20170908_141852.jpg")
print("tess results: ", txtStr)
