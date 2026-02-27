# Cinema Organizer

A modular Python application for automatically organizing movies and TV series into structured folders.

## Features

- Detects TV series using `SxxEyy` format
- Detects movies using year format `(YYYY)`
- Supports video files:
  - `.mkv`
  - `.mp4`
  - `.avi`
  - `.mov`
- Supports subtitles (`.srt`)
- Recursive file scanning
- Automatic empty folder cleanup
- Clean OOP architecture
- Colorful console output with emojis

---

## Project Structure

```

media_organizer/
│
├── app/
│   ├── **init**.py
│   ├── base.py
│   ├── utils.py
│   ├── console.py
│   ├── series.py
│   └── movie.py
│
├── main.py
├── requirements.txt
└── README.md

````

---

## Installation

### 1. Clone or download the project

### 2. Install dependencies

```bash
pip install -r requirements.txt
````

Dependencies:

* colorama

---

## Usage

Run the program:

```bash
python main.py
```

1. Select your media folder
2. Enter series name when prompted
3. Enter movie name when prompted
4. The program will organize everything automatically

---

## Example Output Structure

### TV Series

```
Series Name/
    S01/
        Series Name S01 E01.mkv
        Series Name S01 E02.mkv
```

### Movies

```
Movie Name/
    Movie Name (2024).mkv
```

---

## Requirements

* Python 3.8 or higher
* colorama

---

## License

This project is open-source and free to use.
