try:
    # Modules
    from string import ascii_letters, digits
    from os.path import basename, exists
    from sys import maxsize, executable
    from random import shuffle, choices
    from platform import system as syst
    from json import dumps
    from time import sleep
    from os import getpid
    from re import match
    import threading
    import requests




    # Optional Variables
    proxy_type = "socks4" # Socks4 usually works best
    http_timeout = 15 # Seconds
    threading_speed = 0.150 # Seconds




    # Colors
    z, r, g, y, p, m0= "\033[0m", "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;35m", "\033[1;37m"




    # Standard Variables
    proxy_lists_url = "https://raw.githubusercontent.com/An0r3w/db/main/proxy_lists"
    credit = p+"InstaKilo - An0r3w"
    python = basename(executable)
    progress_threading = True
    in_process_threads = 0
    done_threads = 0
    PID = getpid()




    # Notification Functions
    def cm(txt): print(y+"[*] "+m0+txt)
    def pm(txt): print(g+"[+] "+m0+txt)
    def nm(txt): print(r+"[-] "+m0+txt)
    def em(txt):
        print(r+"[!] "+m0+txt+r+'.'+z)
        raise SystemExit




    # Kill process function
    def die():
        if syst() == "Windows":
            import ctypes
            process_handle = ctypes.windll.kernel32.OpenProcess(1, False, PID)
            ctypes.windll.kernel32.TerminateProcess(process_handle, -1)
            ctypes.windll.kernel32.CloseHandle(process_handle)
        else:
            from os import kill
            import signal
            kill(PID, signal.SIGKILL)




    # Generate fake tokens function
    def generate_tokens():
        x_csrftoken = "".join(choices(ascii_letters + digits, k=32))
        x_asbd_id = "".join(choices(digits, k=6))
        return [x_csrftoken, x_asbd_id]




    # Info request function
    def ig_req(username:str, proxy:str):
        global done_threads, progress_threading
        TOKENS = generate_tokens()
        resp = requests.get(
            "https://www.instagram.com/api/v1/users/web_profile_info/?username="+username,
            headers = {
                "sec-ch-prefers-color-scheme": "dark", 
                "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", 
                "sec-fetch-site": "same-origin", "x-csrftoken": TOKENS[0],
                "x-asbd-id":TOKENS[1], "x-ig-app-id": "936619743392459",
                "x-ig-www-claim": "0", "x-requested-with": "XMLHttpRequest", 
                "Referer": "https://www.instagram.com/"+username+"/", 
                "Referrer-Policy": "strict-origin-when-cross-origin"
            },
            proxies = {proxy_type:proxy},
            timeout = http_timeout
        )
        
        

        if resp.status_code == 200:
            resp_json = resp.json()["data"]["user"]
            if resp_json == None:
                T = threading.Thread(target=em, args=["User Not Found"])
                T.daemon = True
                print()
                T.start()
                die()
            content = dumps(resp_json).replace("\\u0026", '&')
            file_name = username+"-instakilo.json"


            for x in range(maxsize):
                if x!=0:file_name = username+"-instakilo("+str(x)+").json"
                
                if exists(file_name) == False and progress_threading:
                    progress_threading = False
                    file = open(file_name, 'w')
                    file.write(content)
                    file.close()
                    print()
                    pm("Info Recieved Successfully, Saved As `"+file_name+'`')
                    print(z, end='')
                    die()



        elif resp.status_code == 404:
            print()
            T = threading.Thread(target=em, args=["User Not Found"])
            T.daemon = True
            print()
            T.start()
            die()
        done_threads += 1




    # Get info function
    def get_info(username:str, proxies:list):
        global in_process_threads
        for proxy in proxies:
            if progress_threading:
                status_message = f"\r{y}Threading ({in_process_threads}/{str(len(proxies))})"+z
                print(status_message[:min(len(status_message), 50)], end='')
                T = threading.Thread(target=ig_req, args=[username, proxy])
                T.daemon = True
                T.start()
                in_process_threads += 1
                sleep(threading_speed)
            else:
                break
        print(); pm("Threading completed")




    # Get proxies function
    def proxiespls():
        while 1:
            cm("Requesting proxy lists")
            pl_response = requests.get(proxy_lists_url, timeout=http_timeout)

            if pl_response.status_code != 200:
                nm("Failed to find proxy lists, trying again")
                continue


            try: pl_l = pl_response.json()[proxy_type]
            except: nm("Invalid response from server, trying again"); continue
            shuffle(pl_l)



            for link in pl_l:
                cm("Requesting a proxy list")
                pl_response = requests.get(link, timeout=http_timeout)


                if pl_response.status_code != 200:
                    nm("Failed to find proxy lists, trying Again")
                    continue

                else:
                    proxies = pl_response.text.splitlines()
                    pm("Recieved "+str(len(proxies))+" Proxies")
                    return proxies
        em("Failed to achieve a proxy list")



    # Username request function
    def ig_id_req(id:str, proxy:str):
        global done_threads, progress_threading
        resp = requests.get(
            r"https://www.instagram.com/graphql/query/?query_hash=c9100bf9110dd6361671f113dd02e7d6&variables={%22user_id%22:%22"+id+r"%22,%22include_chaining%22:false,%22include_reel%22:true,%22include_suggested_users%22:false,%22include_logged_out_extras%22:false,%22include_highlight_reels%22:false,%22include_related_profiles%22:false}",
            proxies={proxy_type:proxy},
            timeout=http_timeout
        )


        if resp.status_code == 200:
            try:
                print(); pm(resp.json()["data"]["user"]["reel"]["user"]["username"])
                print(z, end='')
                die()
            except:
                None

        elif resp.status_code == 404:
            print()
            T = threading.Thread(target=em, args=["User Not Found"])
            T.daemon = True
            T.start()
            die()
        done_threads += 1



    # Get username function
    def get_username(id:str , proxies:list):
        global in_process_threads
        for proxy in proxies:
            if progress_threading:
                status_message = f"\r{y}Threading ({in_process_threads}/{str(len(proxies))})"+z
                print(status_message[:min(len(status_message), 50)], end='')
                T = threading.Thread(target=ig_id_req, args=[id, proxy])
                T.daemon = True
                T.start()
                in_process_threads += 1
                sleep(threading_speed)
            else:
                break
        print(); pm("Threading completed")



    # Main
    if __name__ == "__main__":
        print(credit)
        method = input(m0+"Method (1: username, 2: id):").replace(' ', "").lower()

        if method in ['1', "username"]:
            input_username = input(m0+"Username:").replace(' ', '').lower()
            if match(r'^[a-zA-Z0-9._]{1,30}$', input_username):
                pm("Valid username")
                proxies = proxiespls()
                get_info(input_username, proxies)
                cm("Waiting for response..")
                while in_process_threads != done_threads: None
                em("Mission Failed")
            else:
                em("Invalid Username")
        
        elif method in ['2', "id"]:
            input_id = input(m0+"ID:").replace(' ', '').lower()
            if (match(r'^\d+$', input_id)):
                pm("Valid ID")
                proxies = proxiespls()
                get_username(input_id, proxies)
                while in_process_threads != done_threads: None
                em("Mission Failed")
            else:
                em("Invalid ID")

        else:
            em("Invalid Input")


except (KeyboardInterrupt, SystemExit):
    print(z, end='')
    die()
