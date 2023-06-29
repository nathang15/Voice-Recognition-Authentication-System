# Voice-Recognition-Authentication-System #

An AI-based voice authentication system built upon openAI Whisper speech recognition model. Users have the ability to use voice for username and passphrases instead of traditional authentication method. This way only the user themselves knows the exact username and passwords. This program is still in progress and have rooms for improvement. 

## Description ##

Voice-Recognition-Authentication-System is designed using OpenAI whisper model for speech recognition and build a user database using their credentials recorded under speech form. The code up until this commit for now is purely barebone with a functional voice authentication system that have hash,salted passwords store in local database. 

## Demonstration ##

Creating user when there is no existed user:

https://user-images.githubusercontent.com/98335699/211969315-a4d4b092-384e-404c-9ecb-f7bebd1d7dc2.mp4

Verification process:

https://user-images.githubusercontent.com/98335699/211968884-133ce022-1292-4616-a503-942c4a7187fb.mp4

Creating new user:

https://user-images.githubusercontent.com/98335699/211970134-67382d48-1ee7-4339-aa39-0585b78ce658.mp4

The system also has ways to deal with undesirable input, mismatching input, or cancelling command (user can cancel by simply saying 'no' to the question asked).

### Prerequisites ###

1. Install whisper 
```sh
   pip install git+https://github.com/openai/whisper.git 
   ```
To update the package to the latest version of this repository, please run:
```sh
   pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
   ```

For more information about whisper, please refer to the official [Whisper](https://github.com/openai/whisper) repo. 

2. Install Python Text To Speech:
```sh
   pip install pyttsx3
   ```

3. Install bcrypt:
```sh
   pip install bcrypt
   ```

## Future Update ##

1. Create a user GUI and a demo of how the system is applied with a real device (eg. Raspberry Pi)
2. Develop an AI to study voice pattern to detect the possible user voices.
3. Develop the database that store credentials to be more secure.
4. Differentiate between recordings and actual voices. 

## Credits ##

VORAS is powered by the [Whisper](https://github.com/openai/whisper) open source project by openAI.

![GPL V3 or Later](https://www.gnu.org/graphics/gplv3-or-later-sm.png "GPL V3 or later") All executable code in the FarmData2 project are licensed under the [GNU General Public License Version 3 or later](https://www.gnu.org/licenses/gpl.txt)

