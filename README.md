## Voice-Recognition-Authentication-System ##

This is a voice authentication system that enables user to login using their voice. This project is still in early stage of developpment and still have a lot of room to improve.

### Description ###

Voice-Recognition-Authentication-System (VORAS) is designed using OpenAI whisper model for speech recognition and build a user database using their credentials recorded under speech form. The code up until this commit for now is purely barebone with a working authentication system that have hash,salted passwords store in local database. 

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

### Future Update ###

1. Create a user GUI and a demo of how the system is applied with a real device (eg. Raspberry Pi)
2. Develop an AI to study voice pattern to detect the possible user voices.
3. Develop the database that store credentials to be more secure.
4. Differentiate between recordings and actual voices. 

### Credits ###

VORAS is powered by the [Whisper](https://github.com/openai/whisper) open source project by openAI.

![GPL V3 or Later](https://www.gnu.org/graphics/gplv3-or-later-sm.png "GPL V3 or later") All executable code in the FarmData2 project are licensed under the [GNU General Public License Version 3 or later](https://www.gnu.org/licenses/gpl.txt)

