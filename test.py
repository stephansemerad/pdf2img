from pdf2image import convert_from_path, convert_from_bytes

images = convert_from_path('./test.pdf')
print('images: ', images)

