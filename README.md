<p align="center">
  <h3 align="center">ADB - Automation Scripts</h3>
  <p align="center">
      A group of automation code to run adb input commands
  </p>
</p>

<br>
<p>This script was created to automate activities that I think are very boring but we have to do them every day</p>
<p>Please fork and enter as many of your ideas as possible</p>

![image](https://github.com/user-attachments/assets/9c8ade20-a785-4692-b687-dc838a1b4dbd)

### List Automation:
- Tiktok (Tiktok lite)
  - Auto Follow
  - Auto Like and Comment
- PokeMMO
  - Auto Grinding Grass

### Requirement
- Python
- Pipenv
- Android Device With ADB Enable and Connected to Host (USB or Wifi)

### How to use
- Clone with git
  ```bash
  git clone https://github.com/mohamad-supangat/android_automation_scripts.git
  ```
- Installing python dependencies with PipEnv
  ```
  cd android_automation_scripts
  pipenv install
  ```
- Check and Connect Android Device
  ```bash
  adb connect {ip address} // if using adb wifi
  adb devices
  ```
- Run some automation script
  ```pipenv run ./tiktok.auto-follow.py```
