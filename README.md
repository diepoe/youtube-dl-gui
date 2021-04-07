# youtube-dl-gui

Simple PyQT5 GUI for youtube-dl.

## Developer Setup:

Clone this repository, and cd into it.

`git clone https://github.com/HAUDRAUFHAUN/youtube-dl-gui`

`cd youtube-dl-gui/`

Create and activate your virtual environment.

MacOS/Linux:

```bash
virtualenv --no-site-packages env
source env/bin/activate
```

Windows:

```basch
virtualenv env
.\env\Scripts\activate
```

Install requisite python packages and modules.

`pip install -r requirements.txt`

Verify the application is running with `python downloader.py` or `python3 downloader.py`

### Build an executable file

1. Make sure you installed all dependencies from `requirements.txt` **globally**.

2. Install the `pyinstaller` python package with `pip install pyinstaller` or `pip3 install pyinstaller`.

3. Run `pyinstaller --noconfirm --onedir --windowed "DIRECTORY_TO_THE_downloader.py_FILE"` in your terminal. This will create the executable output in your project folder.
