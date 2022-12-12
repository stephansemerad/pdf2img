import os
import platform
import tempfile
from pdf2image import convert_from_path
from os import listdir
from os.path import isfile, join

class pdf2image:
    def __init__(self, file_path):
        self.file_path = file_path
        self.image_file_path  = "./"
        self.images = self.get_images()

    def list_images(self):
        for img in self.images:
            print(img)

    def get_images(self):
        if self.file_path == None:
            return []
        else:
            with tempfile.TemporaryDirectory() as path:
                images = []
                if platform.system() == 'Windows':
                    images = convert_from_path(self.file_path, dpi=100, poppler_path=r'./poppler-0.68.0/bin', thread_count=2, timeout=600)
                else:
                    images = convert_from_path(self.file_path, dpi=100, thread_count=2, timeout=600)
                return images

    def save_images(self):
        for index, image in enumerate(self.images):
            file_path = os.path.join(self.image_file_path, f'image_{index+1}.png')
            image.save(file_path)

    def clear_image_directory(self):
        images = [f for f in listdir(self.image_file_path) if isfile(join(self.image_file_path, f))]
        for img in images:
            if img.endswith('.png'):
                file_path = os.path.join(self.image_file_path, img)
                os.remove(file_path)


file_path = './test.pdf'
obj = pdf2image(file_path)
obj.image_file_path = './images'
obj.clear_image_directory()
obj.get_images()
obj.save_images()


