import os
import shutil
from app.utils import is_video


class BaseOrganizer:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def iterate_files(self):
        for file in os.listdir(self.base_dir):
            path = os.path.join(self.base_dir, file)
            if os.path.isfile(path) and is_video(file):
                yield file, path

    def move(self, src, dst):
        if not os.path.exists(dst):
            shutil.move(src, dst)

    def create_folder(self, path):
        os.makedirs(path, exist_ok=True)

    def clean_empty_folders(self):
        for root, dirs, _ in os.walk(self.base_dir, topdown=False):
            for d in dirs:
                folder = os.path.join(root, d)
                if os.path.isdir(folder) and not os.listdir(folder):
                    os.rmdir(folder)

    def organize(self):
        raise NotImplementedError