import os

def anon_surf():
  tools = ["Anonsurf", "Tor", "I2P", "JonDo"]
  print("Select an AnonSurf tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def information_gathering():
  tools = ["Nmap", "TheHarvester", "Shodan", "Maltego"]
  print("Select an Information Gathering tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def password_attack():
  tools = ["John the Ripper", "Hashcat", "Hydra", "Medusa"]
  print("Select a Password Attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def wireless_attack():
  tools = ["Aircrack-ng", "Reaver", "Wifite", "Kismet"]
  print("Select a Wireless Attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def sql_injection_tools():
  tools = ["sqlmap", "SQLMate", "Havij", "NoSQLMap"]
  print("Select a SQL injection tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool + " -u <target_url>")
  else:
    print("Invalid option selected.")


def phishing_attack():
  tools = ["SocialFish", "PhishX", "Evilginx2", "Gophish"]
  print("Select a phishing attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def web_attack_tool():
  tools = ["OWASP ZAP", "Burp Suite", "Nikto", "Arachni"]
  print("Select a web attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def post_exploitation():
  tools = ["Metasploit Framework", "Empire", "Pupy", "Cobalt Strike"]
  print("Select a post-exploitation tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def forensic_tools():
  tools = ["Autopsy", "The Sleuth Kit", "Volatility", "Bulk Extractor"]
  print("Select a forensic tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def payload_creator():
  tools = ["msfvenom", "Veil", "Unicorn", "TheFatRat"]
  print("Select a payload creator tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def router_exploit():
  tools = ["RouterSploit", "Metasploit Framework", "RouterScan", "Reaver"]
  print("Select a router exploit tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def wifi_jamming():
  os.system("mdk3 wlan0mon d")  # Performs WiFi jamming using MDK3 tool


def xss_attack_tool():
  tools = ["XSStrike", "Burp Suite", "OWASP Zap", "BeEF"]
  print("Select an XSS attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def socialmedia_finder():
  tools = ["Sherlock", "Recon-ng", "OSINT Framework", "theHarvester"]
  print("Select a social media finder tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def ddos_attack_tools():
  tools = ["HULK", "LOIC", "Xerxes", "Slowloris"]
  print("Select a DDoS attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def steganography_tools():
  tools = ["Steghide", "OutGuess", "OpenStego", "Stegano"]
  print("Select a steganography tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def idn_homograph_attack():
  tools = ["dnstwist", "EvilURL", "IDN Homograph Attack Toolkit", "Punycode"]
  print("Select an IDN homograph attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def hash_cracking_tools():
  tools = ["hashcat", "John the Ripper", "Hash-Identifier", "Cryptohaze"]
  print("Select a hash cracking tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def socialmedia_attack():
  tools = [
    "SET (Social Engineering Toolkit)", "Phantom-Evasion", "Gophish", "BeEF"
  ]
  print("Select a social media attack tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")


def android_hack():
  tools = ["AndroRAT", "Metasploit Framework", "Drozer", "MobSF"]
  print("Select an Android hacking tool:")
  for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
  selected_option = int(input("Enter the option number: "))

  if selected_option in range(1, len(tools) + 1):
    selected_tool = tools[selected_option - 1]
    os.system(selected_tool.lower())
  else:
    print("Invalid option selected.")
