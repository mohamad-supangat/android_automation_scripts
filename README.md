<p align="center">
  <h3 align="center">ADB - Automation Scripts</h3>
  <p align="center">Kumpulan code automation untuk menjalankan perintah adb input
  </p>
</p>

<br>
<p>Script ini dibuat untuk melakukan automatisasi kegiatan kegiatan yang menurutku sangat membosankan tetapi kita harus melakukanya setiap hari</p>
<p>Silahkan fork dan masukan ide ide kalian sebanyak mungkin</p>


### Daftar Automation:
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
  ```git clone https://github.com/mohamad-supangat/autoclick_adb.git```
- Installing python dependencies with PipEnv
  ```
  cd autoclick_adb
  pipenv install
  ```
- Check and Connect Android Device
  ```bash
  adb connect {ip address} // if using adb wifi
  adb devices
  ```
- Run some automation script
  ```pipenv run tiktok.auto-follow.py```
