import os
import sys
import requests
from colorama import Fore, Style, init

init(autoreset=True)

os.system("title XCRYP-IP")

BANNER = f"""
{Fore.CYAN}
██╗  ██╗ ██████╗██████╗ ██╗   ██╗██████╗       ██╗██████╗
╚██╗██╔╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗      ██║██╔══██╗
 ╚███╔╝ ██║     ██████╔╝ ╚████╔╝ ██████╔╝█████╗██║██████╔╝
 ██╔██╗ ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝ ╚════╝██║██╔═══╝
██╔╝ ██╗╚██████╗██║  ██║   ██║   ██║           ██║██║
╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝           ╚═╝╚═╝

            XCRYP - IP TRACER TOOL
{Style.RESET_ALL}
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def ip_lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,mobile,proxy,hosting,query"

        response = requests.get(url, timeout=10)
        data = response.json()

        if data["status"] != "success":
            print(Fore.RED + "\n[!] Invalid IP address!")
            return

        print(Fore.GREEN + "\n========== IP INFORMATION ==========\n")

        print(Fore.CYAN + f"IP Address      : {data.get('query')}")
        print(Fore.CYAN + f"Continent       : {data.get('continent')}")
        print(Fore.CYAN + f"Country         : {data.get('country')}")
        print(Fore.CYAN + f"Region          : {data.get('regionName')}")
        print(Fore.CYAN + f"City            : {data.get('city')}")
        print(Fore.CYAN + f"District        : {data.get('district')}")
        print(Fore.CYAN + f"ZIP Code        : {data.get('zip')}")
        print(Fore.CYAN + f"Latitude        : {data.get('lat')}")
        print(Fore.CYAN + f"Longitude       : {data.get('lon')}")
        print(Fore.CYAN + f"Timezone        : {data.get('timezone')}")
        print(Fore.CYAN + f"Currency        : {data.get('currency')}")
        print(Fore.CYAN + f"ISP             : {data.get('isp')}")
        print(Fore.CYAN + f"Organization    : {data.get('org')}")
        print(Fore.CYAN + f"AS              : {data.get('as')}")
        print(Fore.CYAN + f"AS Name         : {data.get('asname')}")
        print(Fore.CYAN + f"Mobile Network  : {data.get('mobile')}")
        print(Fore.CYAN + f"Proxy/VPN       : {data.get('proxy')}")
        print(Fore.CYAN + f"Hosting         : {data.get('hosting')}")

        print(Fore.GREEN + "\n====================================")

        # Google Maps Link
        maps = f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
        print(Fore.YELLOW + f"\nGoogle Maps -> {maps}")

    except requests.exceptions.RequestException:
        print(Fore.RED + "\n[!] API connection error!")

    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}")


def menu():
    while True:
        clear()
        print(BANNER)

        print(Fore.MAGENTA + "[1] IP LOOKUP")
        print(Fore.MAGENTA + "[2] EXIT")

        choice = input(Fore.WHITE + "\nSelect an option -> ")

        if choice == "1":
            ip = input(Fore.WHITE + "\nEnter IP address -> ")
            ip_lookup(ip)
            input(Fore.YELLOW + "\nPress ENTER to continue...")

        elif choice == "2":
            print(Fore.RED + "\nExiting...")
            sys.exit()

        else:
            print(Fore.RED + "\n[!] Invalid option!")
            input("Press ENTER...")


if __name__ == "__main__":
    menu()