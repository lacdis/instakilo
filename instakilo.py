try:
    # Modules
    from os.path import exists, join, basename
    from sys import maxsize, argv, executable
    from string import ascii_letters, digits
    from random import shuffle, choices
    from os import system, mkdir, _exit
    from threading import Thread, Lock
    from json import dumps
    from time import sleep
    from re import match
    import datetime
    import requests




    # Standard Variables
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    default_headers = {"User-Agent":user_agent,"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate, br"}
    z, g, b, r, w, o, y, q = '\033[0m', '\033[1;32m', '\033[1;34m', '\033[1;91m', '\033[1;97m', '\033[38;5;208m', '\033[38;2;255;255;0m', '\033[38;2;255;255;204m'
    db, proxy_type = "https://raw.githubusercontent.com/An0r3w/db/main/", ''
    INPUT, INVALID_USAGE, threading = True, False, True
    done_threads, r_space = 0, ' ' * 15
    threading_speed = 0.150




    # CLI Functions
    def em(text): print(f"{r_space}{w}[\033[1;31m!{w}] {text}{r},{w} Terminating Process{r}.\n{z}"); exit(1)
    def im(text): return input(f"{r_space}{w}[{q}?{w}] {text+q}:{z}").replace(' ', '').lower()
    def tm(text): print(f"{r_space}{w}[{b}@{w}] {text}")
    def cm(text): print(f"{r_space}{w}[{y}*{w}] {text}")
    def pm(text): print(f"{r_space}{w}[{g}+{w}] {text}")
    def rm(text): print(f"{r_space}{w}[{r}-{w}] {text}")




    # Get Proxy List Function
    def get_proxy_list():
        global proxy_type
        if INPUT: proxy_type = im(f"Proxy Type ({o}1.{w} Socks4, {o}2.{w} Socks5)")


        if proxy_type in ['2', "socks5"]:
            db_proxy_list = db+"socks5"
            cm("Proxy Type (Socks5)")

        else:
            db_proxy_list = db+"socks4"
            cm("Proxy Type (Socks4)")
            proxy_type = "socks4"



        cm("Requesting a Proxy List...")
        for attempt in range(5):
            try:
                resp_all_proxy_lists = requests.get(db_proxy_list, headers=default_headers)


                if resp_all_proxy_lists.status_code == 200:
                    all_proxy_lists = resp_all_proxy_lists.text.splitlines()
                    shuffle(all_proxy_lists)

                    for db_proxy_list in all_proxy_lists:
                        resp_proxy_list = requests.get(db_proxy_list, headers=default_headers)

                        if resp_proxy_list.status_code == 200:
                            proxy_list = resp_proxy_list.text.splitlines()
                            pm(f"{str(len(proxy_list))} Proxies Achieved")
                            return proxy_list

                    em("Failed to Achieve a Proxy List")

                elif attempt == 4:
                    em("Failed to Achieve a Proxy List")


            except requests.exceptions.Timeout:
                continue

            except requests.exceptions.ConnectionError:
                em("Check Your Internet Connection")




    # Generate fake tokens function
    def generate_tokens():
        x_csrftoken = "".join(choices(ascii_letters + digits, k=32))
        x_asbd_id = "".join(choices(digits, k=6))
        return [x_csrftoken, x_asbd_id]




    # Return Yes or No Function By Bool Function
    def yn(_):
        if _:return "Yes"
        return "No"




    # Saving general info function
    def save_general_info(folder_name, info, username):
        general_file_content = f"《═══════════════》{username}《═══════════════》\n"
        general_file_content += "Original Profile Picture  ☠  «"+info["profile_pic_url_hd"]+'»\n\n'
        general_file_content += "Full Name  ☠  «"+info["full_name"]+'»\n'


        if info["category_name"] != None: 
            general_file_content += "Category  ☠  «"+info["category_name"]+'»\n'

        general_file_content += "Bio  ☠  «"+info["biography"].replace('\n', "\\n")+'»\n\n'
        general_file_content += "Posts  ☠  «"+str(info["edge_owner_to_timeline_media"]["count"])+'»\n'
        general_file_content += "Followers  ☠  «"+str(info["edge_followed_by"]["count"])+'»\n'
        general_file_content += "Following  ☠  «"+str(info["edge_follow"]["count"])+'»\n\n'


        if len(info["bio_links"]) > 0:
            link_num = 1
            general_file_content += "Bio Links  ↯\n"

            for link in info["bio_links"]:
                general_file_content += f"\t{str(link_num)}.\n"; link_num += 1
                general_file_content += "\t\t☠  «"+link["title"]+'»\n'
                general_file_content += "\t\t☠  «"+link["lynx_url"]+'»\n'
                general_file_content += "\t\t☠  «"+link["url"]+'»\n'
                general_file_content += "\t\t☠  «"+link["link_type"]+'»\n'

            general_file_content += "\n"


        general_file_content += "Private Account  ☠  «"+yn(info["is_private"])+'»\n'
        general_file_content += "Verified Account  ☠  «"+yn(info["is_verified"])+'»\n'
        general_file_content += "Recent Account  ☠  «"+yn(info["is_joined_recently"])+'»\n'
        general_file_content += "Professional Account  ☠  «"+yn(info["is_professional_account"])+'»\n'
        general_file_content += "Supervised User  ☠  «"+yn(info["is_supervised_user"])+'»\n'


        if len(info["pronouns"]) > 0:
            general_file_content += "\nPronouns  ↯\n"

            for pronoun in info["pronouns"]:
                general_file_content += "\t☠  «"+pronoun+'»\n'

            general_file_content += "\n"


        general_file_content += "Business Account  ☠  «"+yn(info["is_business_account"])+'»\n'

        if info["is_business_account"]:
            general_file_content += "Contact Method  ☠  «"+str(info["business_contact_method"])+'»\n'
            general_file_content += "E-mail  ☠  «"+str(info["business_email"])+'»\n'
            general_file_content += "Phone  ☠  «"+str(info["business_phone_number"])+'»\n'


        general_file_content += "\nID  ☠  «"+info["id"]+'»\n'

        with open(join(folder_name, username+"-general.txt"), 'w') as file_general:
            file_general.write(general_file_content)
            file_general.close()




    # Save posts function
    def save_posts(folder_name, info, username):
        posts_file_content, post_num = '', 0
        posts = info["edge_owner_to_timeline_media"]["edges"]



        for postx in posts:
            post_num += 1
            post = postx["node"]        
            posts_file_content += f"《═══════════════》{str(post_num)}《═══════════════》\n"


            if post["__typename"] == "GraphImage": post_type = "Image"; media_src = post["display_url"]
            elif post["__typename"] == "GraphVideo": post_type = "Video"; media_src = post["video_url"]
            elif post["__typename"] == "GraphSidecar": post_type = "Carousel"; media_src = post["edge_sidecar_to_children"]["edges"]
            else: post_type = "Unknown"

            posts_file_content += "Post Type  ☠  «"+post_type+"»\n"
            posts_file_content += "Posted on  ☠  «"+str(datetime.datetime.fromtimestamp(post["taken_at_timestamp"]))+"»\n"
            if post["__typename"] != "GraphSidecar": posts_file_content += "Original Media  ☠  «"+media_src+"»"


            else:
                media_num = 0
                posts_file_content += "\nOriginal Media  ↯"

                for media in media_src:
                    media = media["node"]
                    media_num += 1
                    posts_file_content += f'\n\t{media_num}.'
                    if media["__typename"] == "GraphVideo":
                        posts_file_content += f"\n\t\t☠  «Video»"
                        posts_file_content += f'\n\t\t☠  «'+media["video_url"]+"»"
                    elif media["__typename"] == "GraphImage":
                        posts_file_content += f"\n\t\t☠  «Image»"
                        posts_file_content += f'\n\t\t☠  «'+media["display_url"]+"»"
                    if media["accessibility_caption"] != None: posts_file_content += f'\n\t\t☠  «'+media["accessibility_caption"]+"»"

                posts_file_content += '\n'


            posts_file_content += "\nShare URL  ☠  «"+"https://www.instagram.com/p/"+post["shortcode"]+"»"

            try: posts_file_content += "\nCaption  ☠  «"+post["edge_media_to_caption"]["edges"][0]["node"]["text"]+"»"
            except:None

            if post["accessibility_caption"] != None:
                posts_file_content += "\nAccessibility Caption  ☠  «"+post["accessibility_caption"]+"»"

            if post["location"] != None:
                posts_file_content += "\nLocation  ☠  «"+post["location"]["name"]+"»"


            if len(post["edge_media_to_tagged_user"]["edges"]) != 0:
                tagged_num = 0
                posts_file_content += "\n\nTagged  ↯"

                for tagged_user in post["edge_media_to_tagged_user"]["edges"]:
                    tagged_num += 1
                    tagged_user = tagged_user["node"]["user"]

                    posts_file_content += f'\n\t{tagged_num}.'
                    posts_file_content += f'\n\t\t☠  «'+tagged_user["username"]+"»"
                    posts_file_content += f'\n\t\t☠  «'+tagged_user["id"]+"»"
                    posts_file_content += f'\n\t\t☠  «'+tagged_user["profile_pic_url"]+"»"

                posts_file_content += '\n'


            if post_num != info["edge_owner_to_timeline_media"]["count"]: posts_file_content += "\n\n\n"
            else: posts_file_content += '\n'



        with open(join(folder_name, username+"-posts.txt"), 'w') as file_posts:
            file_posts.write(posts_file_content)
            file_posts.close()




    # Save related profiles function
    def save_related_profiles(folder_name, info, username):
        related_profiles_file_content, rp_num = '', 0
        related_profiles = info["edge_related_profiles"]["edges"]

        for rp in related_profiles:
            rp = rp["node"]
            rp_num += 1
            related_profiles_file_content += f"《═══════════════》{str(rp_num)}《═══════════════》\n"
            related_profiles_file_content += f"Username  ☠  «"+rp["username"]+"»\n"
            related_profiles_file_content += f"Full Name  ☠  «"+rp["full_name"]+"»\n"
            related_profiles_file_content += f"Profile Picture  ☠  «"+rp["profile_pic_url"]+"»\n"
            related_profiles_file_content += f"Private Account  ☠  «"+yn(rp["is_private"])+"»\n"
            related_profiles_file_content += f"Verified Account  ☠  «"+yn(rp["is_verified"])+"»\n"
            if rp != related_profiles[-1]["node"]: related_profiles_file_content += '\n'

        with open(join(folder_name, username+"-related_profiles.txt"), 'w') as file_related_profiles:
            file_related_profiles.write(related_profiles_file_content)
            file_related_profiles.close()




    # Get Profile By Username Thread Function
    def get_profile_by_username_thread(proxy, username, lock):
        global done_threads, threading
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
            proxies = {proxy_type:proxy}
        ); done_threads += 1



        if resp.status_code == 200:
            resp_json = resp.json()["data"]["user"]

            if resp_json == None:
                Thread(target=em, args=["User Not Found"], daemon=True).start()
                _exit(1)

            resp_sorted_json = dict(sorted(resp_json.items()))
            content = dumps(resp_sorted_json, indent=4).replace("\\u0026", '&')
            folder_name = username+"-instakilo"
            threading = False

            for x in range(maxsize):
                if x!=0:folder_name = username+"-instakilo("+str(x)+")"
                if exists(folder_name) == False:
                    with lock:
                        mkdir(folder_name)
                        file_json = open(join(folder_name, username+"-json.json"), 'w')
                        file_json.write(content+'\n')
                        file_json.close()
                        save_general_info(folder_name, resp_json, username)
                        if resp_json["edge_owner_to_timeline_media"]["count"] != 0 and resp_json["is_private"] == False:
                            save_posts(folder_name, resp_json, username)
                        if len(resp_json["edge_related_profiles"]["edges"]) != 0:
                            save_related_profiles(folder_name, resp_json, username)
                        pm("Saved as `"+folder_name+'`'); print()
                        _exit(0)


        elif resp.status_code == 404:
            Thread(target=em, args=["User Not Found"], daemon=True).start()
            _exit(1)




    # Get Profile By Username Thread Function
    def get_profile_by_id_thread(proxy, id, lock):
        global done_threads
        resp = requests.get(
            r"https://www.instagram.com/graphql/query/?query_hash=c9100bf9110dd6361671f113dd02e7d6&variables={%22user_id%22:%22"+id+r"%22,%22include_chaining%22:false,%22include_reel%22:true,%22include_suggested_users%22:false,%22include_logged_out_extras%22:false,%22include_highlight_reels%22:false,%22include_related_profiles%22:false}",
            proxies={proxy_type:proxy}
        )


        if resp.status_code == 200:
            try:
                with lock:
                    pm(resp.json()["data"]["user"]["reel"]["user"]["username"]); print()
                    _exit(0)
            except:
                Thread(target=em, args=["User Not Found"], daemon=True).start()
                _exit(1)

        elif resp.status_code == 404:
            Thread(target=em, args=["User Not Found"], daemon=True).start()
            _exit(1)




    # Get Profile By Username Function
    def start_threading(method, username_or_id, proxies):
        global threading
        cm("Threading...")
        lock = Lock()
        for proxy in proxies:
            if threading:
                if method == "username": T = Thread(target=get_profile_by_username_thread, args=[proxy, username_or_id, lock])
                else: T = Thread(target=get_profile_by_id_thread, args=[proxy, username_or_id, lock])
                T.daemon = True
                T.start()
                sleep(threading_speed)
            else:
                while 1: None
        pm("Done Threading")

        while len(proxies) != done_threads: None
        em("Mission Failed")




    # Checking Args
    if len(argv) > 1:
        INPUT = False

        if len(argv) < 3: 
            INVALID_USAGE = True

        for arg in argv[1:]:
            if arg.lower() in ["-socks5", "--socks5", "-s5", "--s5"]:
                proxy_type = "socks5"
                argv.remove(arg)
                break


        for arg in range(1, len(argv[1:])):
            print(argv[arg])
            if argv[arg].lower() in ["-username", "-u", "--username", "--u"]:
                username = argv[arg+1]
                method = '1'
                break
            
            elif argv[arg].lower() in ["-id", "--id"]:
                id = argv[arg+1]
                method = '2'
                break
            
            else:
                INVALID_USAGE = True
                break




    # Main
    system("clear||cls"); print("""\n\t::::                             ::    ::      ::        \n\t ::                              ::   ::       ::        \n\t ::                  ::          ::  ::        ::        \n\t :+   :+ :    +:+   :+:+   :+:   +: +:     :+  :+   :+:  \n\t +:   +:+:+  +: +:   +:   +: +:  +:+:+         +:  +:+:+ \n\t +#   +# +#   +#     +#      +#  +#  +#    +#  +#  +# +# \n\t +#   +# +#    +#    +#    +#+#  +#   +#   +#  +#  +# +# \n\t #+   #+ #+  #+ #+   #+   #+ #+  #+    #+  #+  #+  #+ #+ \n\t####  ## ##   ###    ###   ####  ##    ##  ##  ##   ###\n\033[0m""".replace(':', "\033[38;2;255;182;193m:").replace('+', "\033[38;2;255;105;180m+").replace('#', "\033[38;2;255;20;147m#"))
    tm("Github (An0r3w)")
    tm("E-mail (an0r3w@hotmail.com)")
    if INVALID_USAGE:
        cm(f"Example: {basename(executable)} {basename(__file__)} -u theweeknd")
        cm(f"Example: {basename(executable)} {basename(__file__)} -id 266319242")
        em(f"Invalid Usage")
    if INPUT: method = im(f"Method ({o}1.{w} Username, {o}2.{w} ID)")



    if method in ['1', "username"]:
        if INPUT: username = im("Username")

        if match(r"^[a-zA-Z0-9._]{1,30}$", username):
            pm("Valid Username")
            proxies = get_proxy_list()
            start_threading("username", username, proxies)
        else:
            em("Invalid Username")  


    elif method in ['2', "id"]:
        if INPUT: id = im("ID")

        if match(r"^\d+$", id):
            pm("Valid ID")
            proxies = get_proxy_list()
            start_threading("id", id, proxies)
        else:
            em("Invalid ID")


    else:
        em("Invalid Input")  




# Exit Handler
except (SystemExit, KeyboardInterrupt):
    print("\n\033[1;31mGoodbye!.\033[0m")
