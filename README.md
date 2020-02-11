# Meme Generator

Simple meme generator that can use either text input or voice input.

A large part of the code is taken from:

https://blog.lipsumarium.com/caption-memes-in-python/

I slightly modified the code and added some additional features like speech recognition and random selection of an image.

Save the images you want to use in the folder 'input'. As of now, only jpg is working (but can be easily extended).
Some images are already added by me.

The user can make inputs in the main.py file. If SPEECH is set to False, the user will be asked to input text,
otherwise Google Speech Recognition will be used.
In case of voice input, you can set LANGUAGE accordingly.
In both cases, the user is asked for input two times, where the first will be the text in the top line and the second in the bottom
(as in a typical meme).

The font can be changed but is already set to a typical meme font.

### Spongebob Mode

There is a fun mode added to this script. If SPONGEBOB  is set to True, then the script will randomly choose a spongebob image
(make sure that all spongebob pics contain the substring 'spongebob') and randomly capitalize the user's input.

## Instructions to Install and Run:

* After cloning, create a virtual environment and activate it:
  ```
  python -m venv .venv
  source .venv/Scripts/activate
  ```
* If necessary, upgrade pip (in your virtual environment):
 ```
  python -m pip install --upgrade pip
  ```
* Install required modules:
  ```
  pip install -r requirements.txt
  ```
* On Windows, it may be necessary to manually install pyaudio using pipwin (pipwin is included in requirements.txt)
  ```
  pipwin install pyaudio
  ```
* For some reason, it might also be necessary to install SpeechRecognition manually, even though it is included in requirements.txt:
  ```
  pip install SpeechRecognition
  ```
