def mockafjeng(image_name="win-gibberish-xp"):

    for img in image_name:
        current_os, _, current_os_ver, *_ = img.split('-')
        os_dict = {
            "current os": current_os.lower(),
            "current os ver": current_os_ver,
        }
        if current_os.lower() == "win":
            os_dict["current os"] = "windows"
        elif current_os.lower() == "linux":
            os_dict["current os"] = "gnu/linux"
        
        print(os_dict)

my_list = ["win-gibberish-xp", "win-gibberish-7", "win-gibberish-10", "win-gibberish-8"]
mockafjeng(my_list)

my_list = ["linux-gibberish-ubuntu18"]
mockafjeng(my_list)
