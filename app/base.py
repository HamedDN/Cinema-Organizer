import os
import shutil
from app.utils import is_video


class BaseOrganizer:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def iterate_files(self):
        for root, _, files in os.walk(self.base_dir):
            for file in files:
                if is_video(file):
                    yield file, os.path.join(root, file)

    def move(self, src, dst):
        if not os.path.exists(dst):
            shutil.move(src, dst)

    def create_folder(self, path):
        os.makedirs(path, exist_ok=True)

    def clean_empty_folders(self):
        for root, dirs, _ in os.walk(self.base_dir, topdown=False):
            for d in dirs:
                path = os.path.join(root, d)
                if os.path.isdir(path) and not os.listdir(path):
                    os.rmdir(path)

    def organize(self):
        raise NotImplementedError