import tkinter as tk
from tkinter import filedialog
from app.series import SeriesOrganizer
from app.movie import MovieOrganizer


def main():
    root = tk.Tk()
    root.withdraw()

    base_dir = filedialog.askdirectory(title="Select folder")
    if not base_dir:
        print("No folder selected.")
        return

    SeriesOrganizer(base_dir).organize()
    MovieOrganizer(base_dir).organize()

    SeriesOrganizer(base_dir).clean_empty_folders()

    print("\nDONE")


if __name__ == "__main__":
    main()