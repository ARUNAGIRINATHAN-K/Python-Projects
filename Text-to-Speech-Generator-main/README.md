## Text-to-Speech Generator

## Overview

The Text-to-Speech Generator is a simple desktop application built with Python that converts user-input text into spoken audio.<br>
It uses the pyttsx3 library for offline text-to-speech functionality and tkinter for a user-friendly graphical interface.<br>
Users can input text, select from available system voices, and play or clear the text.<br>

## Features

Text Input: Enter text in a multi-line text box.
Voice Selection: Choose from available system voices via a dropdown menu.
Speak Button: Convert entered text to speech.
Clear Button: Reset the text input field.
Error Handling: Displays a warning if no text is entered before attempting to speak.

## Requirements

Python 3.7 or later
pyttsx3 library (pip install pyttsx3)
On Linux, a TTS engine like espeak may be required (sudo apt-get install espeak)

```
Run the script:python text_to_speech.py
```

![GUI](Sample-screenshort.png)

A GUI window will open with the following elements:
A text box to enter text.
A dropdown menu to select a voice (available voices depend on your system).
"Speak" button to play the text as audio.
"Clear" button to reset the text box.


Enter text, select a voice, and click "Speak" to hear the output.
Click "Clear" to reset the text box.

## Compatibility

Windows: Uses SAPI5 for voice synthesis (built-in).
macOS: Uses NSSpeechSynthesizer (built-in).
Linux: Requires espeak or another compatible TTS engine.

## Limitations

Voice quality and availability depend on the system's installed speech engines.
No support for saving audio output or advanced voice customization (e.g., pitch, speed).
Basic GUI without advanced styling.

## Future Enhancements

Add controls for speech rate, pitch, and volume.
Implement audio file export (e.g., MP3/WAV).
Enhance GUI with themes or custom styling.
Support additional TTS engines or cloud-based APIs for better voice quality.
