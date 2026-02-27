import re

VIDEO_EXTENSIONS = ('.mkv', '.mp4', '.avi', '.mov', '.srt')
TV_PATTERN = re.compile(r'^(.*?)S(\d+)[\s._-]*E(\d+)', re.IGNORECASE)
YEAR_REGEX = re.compile(r'(19\d{2}|20\d{2})')


def is_video(file):
    return file.lower().endswith(VIDEO_EXTENSIONS)


def format_season_episode(season, episode):
    return f"S{int(season):02d} E{int(episode):02d}"