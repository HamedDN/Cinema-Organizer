import os
from app.base import BaseOrganizer
from app.utils import TV_PATTERN, format_season_episode
from app.console import Console

class SeriesOrganizer(BaseOrganizer):
    def __init__(self, base_dir):
        super().__init__(base_dir)
        self.series_map = {}

    def organize(self):
        for file, src in self.iterate_files():

            match = TV_PATTERN.search(file)
            if not match:
                continue

            raw_name, season, episode = match.groups()
            key = raw_name.strip().lower()

            if key not in self.series_map:
                Console.info(f"New series detected: {raw_name}")
                name = Console.input("Enter series name: ").strip()
                if not name:
                    continue
                self.series_map[key] = name

            series_name = self.series_map[key]

            season_folder = os.path.join(
                self.base_dir,
                series_name,
                f"S{int(season):02d}"
            )

            self.create_folder(season_folder)

            ext = os.path.splitext(file)[1].lower()
            formatted = format_season_episode(season, episode)

            if ext == ".srt":
                new_name = f"{series_name} {formatted} (subtitle){ext}"
            else:
                new_name = f"{series_name} {formatted}{ext}"

            dst = os.path.join(season_folder, new_name)
            self.move(src, dst)