# <img src="https://github.com/An0r3w/instakilo/assets/168315022/b8f14715-3818-483c-92cb-df4d1e67ed2a" alt="instakilo.ico" width="30" height="30"> InstaKilo - Lacdis
- By specifying someone's Instagram username their Instagram profile will be saved into your directory.
- By entering someone's Instagram ID their Instagram username will show up.
- *Works on Windows and Linux.*
<details>
<summary>What is an Instagram ID?</summary>

- An Instagram user or profile ID is a unique numeric identifier for an Instagram account, created once during the setup of a new Instagram account. The difference is that an Instagram ID cannot be changed, while a username can be modified - [ommentpicker.com](https://commentpicker.com/instagram-user-id.php)
</details>

# Requirements
- Installing Python version 3 `Linux`
```powershell
sudo apt install python3 python3-pip
```
- Installing Python version 3 `Windows`
```powershell
explorer https://apps.microsoft.com/detail/9ncvdn91xzqp
```
- Installing requirements `Linux & Windows`
```powershell
pip3 install requests requests[socks]
```
# Installation
```powershell
curl -OJL https://raw.githubusercontent.com/lacdis/instakilo/main/instakilo.py
```
# Usage
```
python3 instakilo.py
```
```powershell
python3 instakilo.py -u <Username>
```
```powershell
python3 instakilo.py -id <ID>
```
# Result Example
<details open>
  <summary><b><code>./username-instakot</code></b></summary>

- <code><b>./username-instakot/</b>username-json.json</code>
- <code><b>./username-instakot/</b>username-general.txt</code>
- <code><b>./username-instakot/</b>username-posts.txt</code>
- <code><b>./username-instakot/</b>username-related_profiles.txt</code>
</details>

# Screenshots
![arianagrande](https://github.com/user-attachments/assets/6d1266e0-5a9a-448b-b582-ec3e9475e7ee)
![thisisbillgates](https://github.com/user-attachments/assets/9ccb7695-bbdc-4fdd-b3f7-47c413e3bac0)


# Issues
- if the tool is getting slower, that is probably because of your dns resolver that's exposing your IP, try using a tool like [**`proxychains`**](https://github.com/haad/proxychains) which allows you to forward all dns requests over a proxy.
