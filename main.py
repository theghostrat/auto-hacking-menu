from options import *

def menu():
  options = [
    "1. AnonSurf", "2. Information Gathering", "3. Password Attack",
    "4. Wireless Attack", "5. SQL Injection Tools", "6. Phishing Attack",
    "7. Web Attack Tool", "8. Post exploitation", "9. Forensic Tools",
    "10. Payload Creator", "11. Router Exploit", "12. Wifi Jamming",
    "13. XSS Attack Tool", "14. SocialMedia Finder", "15. DDos Attack Tools",
    "16. Steganography Tools", "17. IDN Homograph Attack",
    "18. Hash Cracking Tools", "19. SocialMedia Attack", "20. Android Hack"
  ]
  for option in options:
    print(option)
  print("-" * 30 + "\n")
  print("NOTE: If you want to add functionality according or automate some funky command you can edit them in options.py\n")
  print("-" * 30 + "\n")
  selected_option = int(input("Select an option (1-20): "))

  if selected_option == 1:
    anon_surf()
  elif selected_option == 2:
    information_gathering()
  elif selected_option == 3:
    password_attack()
  elif selected_option == 4:
    wireless_attack()
  elif selected_option == 5:
    sql_injection_tools()
  elif selected_option == 6:
    phishing_attack()
  elif selected_option == 7:
    web_attack_tool()
  elif selected_option == 8:
    post_exploitation()
  elif selected_option == 9:
    forensic_tools()
  elif selected_option == 10:
    payload_creator()
  elif selected_option == 11:
    router_exploit()
  elif selected_option == 12:
    wifi_jamming()
  elif selected_option == 13:
    xss_attack_tool()
  elif selected_option == 14:
    socialmedia_finder()
  elif selected_option == 15:
    ddos_attack_tools()
  elif selected_option == 16:
    steganography_tools()
  elif selected_option == 17:
    idn_homograph_attack()
  elif selected_option == 18:
    hash_cracking_tools()
  elif selected_option == 19:
    socialmedia_attack()
  elif selected_option == 20:
    android_hack()
  else:
    print("Invalid option selected.")
    menu()



menu()
