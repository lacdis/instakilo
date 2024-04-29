# InstaKilo - An0r3w
By specifying someone's Instagram username or id, their instagram profile will be saved into your directory.

*Works on Windows and Linux.*
# Installation
```powershell
curl -o instakilo.py --url https://raw.githubusercontent.com/An0r3w/instakilo/main/instakilo.py
```
# Requirements
```powershell
sudo apt update -y && sudo apt upgrade -y
```
```powershell
sudo apt install python3 python3-pip
```
```powershell
pip3 install requests
```
```powershell
pip3 install requests[socks]
```
# Usage
```
python3 instakilo.py
```
# Settings
- `line: 19` proxy type by default is `socks4` but you can use:
  - `socks5`
  - `http`
  - `https`
- `line: 20` http timeout by default is `15` seconds, http timeout is the time limit for each request sent to instagram.
- `line: 21` threading speed by default is `0.150` seconds which works perfectly, the lower it is the faster.
# Screenshots
![instakilo_ss](https://github.com/An0r3w/instakilo/assets/168315022/6c11c022-a39c-4b92-96c4-f037d43800d8)
![instakilo_ss2](https://github.com/An0r3w/instakilo/assets/168315022/65419e41-7a5a-4dcc-87b6-1c026f873380)
