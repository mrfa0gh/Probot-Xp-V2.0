import ctypes
import requests
import time
import random
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

def set_cmd_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def print_error(message):
    print(f'{Fore.RED}[X] {message}{Style.RESET_ALL}')

def print_success(message):
    print(f'{Fore.GREEN}{message}{Style.RESET_ALL}')

def print_info(message):
    print(f'{Fore.CYAN}                 {message}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}                 Recommended Choice For Important Accounts{Style.RESET_ALL}')
    print(f'{Fore.WHITE}                             No Risk{Style.RESET_ALL}')
    print('')

def print_info1(message):
    print(f'{Fore.RED}{message}{Style.RESET_ALL}')

logo = pyfiglet.figlet_format("Increase Probot XP By Ghalwash")
print(logo)
print(f'{Fore.RED}[!] Last Update: 22/11/2023{Style.RESET_ALL}')
print_info('[-] Okay Safe Mode On')

with open('list.txt', 'r') as list_file:
    timeouts = [float(line.strip()) for line in list_file]

with open('Data.txt', 'r') as data_file:
    token = data_file.readline().strip()
    channel_id = data_file.readline().strip()

c = 0
total_messages_sent = 0
total_failed_messages = 0

while True:
    timeout = random.choice(timeouts)
    print_info1(f"[-] Chosen Timeout: {timeout} seconds")

    with open('x.txt', 'r') as f:
        lines = f.readlines()
        random_line = random.choice(lines)

        payload = {
            'content': random_line
        }

        headers = {
            'Authorization': token
        }

        url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50'

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            total_messages_sent += 1
            set_cmd_title(f'Sent: {total_messages_sent} | Failed: {total_failed_messages}')
            print_success(f'Sent {c + 1} Messages. Total Sent: {total_messages_sent}')
            print('')
        else:
            total_failed_messages += 1
            set_cmd_title(f'Sent: {total_messages_sent} | Failed: {total_failed_messages}')
            print_error(f'Error {c + 1} Message. Total Failed Messages: {total_failed_messages}')
            print('')

        c += 1
        time.sleep(timeout)
