import os
from app.base import BaseOrganizer
from app.utils import YEAR_REGEX


class MovieOrganizer(BaseOrganizer):
    def organize(self):
        for file, src in self.iterate_files():

            year_match = YEAR_REGEX.search(file)
            if not year_match:
                continue

            year = year_match.group(1)

            print(f"\nMovie detected: {file}")
            name = input("Enter movie name: ").strip()
            if not name:
                continue

            movie_folder = os.path.join(
                self.base_dir,
                f"{name} ({year})"
            )

            self.create_folder(movie_folder)

            ext = os.path.splitext(file)[1]
            new_filename = f"{name} ({year}){ext}"
            dst = os.path.join(movie_folder, new_filename)

            self.move(src, dst)