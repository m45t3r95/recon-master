import requests

social_networks = ["Instagram"]


def show_banner():
    print("""
  _____                        __  __           _            
 |  __ \                      |  \/  |         | |           
 | |__) |___  ___ ___  _ __   | \  / | __ _ ___| |_ ___ _ __ 
 |  _  // _ \/ __/ _ \| '_ \  | |\/| |/ _` / __| __/ _ \ '__|
 | | \ \  __/ (_| (_) | | | | | |  | | (_| \__ \ ||  __/ |   
 |_|  \_\___|\___\___/|_| |_| |_|  |_|\__,_|___/\__\___|_|   
                                                             
Developed By: Neeraj Suman (Master Hacker)
-------------------------------------------------------------
Portfolio: neerajsuman.in
linkedIn : neeraj-suman-a474821b4
-------------------------------------------------------------

""")


def show_and_select_social_platform():
    print("Select a social networking site:")
    for social_network in social_networks:
        list_item = str(social_networks.index(social_network) + 1) + ") " + social_network
        print(list_item)
    print(str(0) + ") Exit")
    selected_number = input("(Option)> ")
    return selected_number


def recon_the_user(x):
    if x == '0':
        print("Bye bye!!!")
        exit()
    else:
        real_index = int(x) - 1
        print("----------" + social_networks[real_index] + "----------")
        if real_index == 0:
            instagram_user_recon()


def instagram_user_recon():
    try:
        username = input('(Target Username)> ')
        response = requests.get("https://www.instagram.com/api/v1/users/web_profile_info/?username=" + username,
                                headers={"x-ig-app-id": "936619743392459"})
        response_data = response.json()
        user = response_data['data']['user']
        print("Username             : " + str(user['username']))
        print("Full Name            : " + str(user['full_name']))
        print("Total Followers      : " + str(user['edge_followed_by']['count']))
        print("Total Follows        : " + str(user['edge_follow']['count']))
        print("Total Posts          : " + str(user['edge_owner_to_timeline_media']['count']))
        print("Biography            : " + str(user['biography']))
        print("Profile Pic          : " + str(user['profile_pic_url']))
        print("Is Business Account? : " + str(user['is_business_account']))
    except:
        print("May be user not exists on instagram OR other went wrong")
        instagram_user_recon()


show_banner()
selected_platform_number = show_and_select_social_platform()
recon_the_user(selected_platform_number)
