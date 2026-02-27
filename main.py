import tkinter as tk
from tkinter import filedialog
from app.series import SeriesOrganizer
from app.movie import MovieOrganizer
from app.console import Console


def main():
    root = tk.Tk()
    root.withdraw()

    base_dir = filedialog.askdirectory(title="Select folder")
    if not base_dir:
        Console.error("No folder selected.")
        return

    SeriesOrganizer(base_dir).organize()
    MovieOrganizer(base_dir).organize()

    SeriesOrganizer(base_dir).clean_empty_folders()

    Console.success("DONE")


if __name__ == "__main__":
    main()