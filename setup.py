from distutils.core import setup # Need this to handle modules
import py2exe
import webbrowser, os, SpeechRecognition, gtts, playsound, tempfile, Window, SpeechRecognition, tkinter, pystray, PIL, multiprocessing, sys

setup(windows=["Alfred.py"], data_files=["alfredIcon.ico"])