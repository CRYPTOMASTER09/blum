# Made with ❤ by @CRYPTO_MASTER
# Join tele channel for update t.me/airdropconfirm97
import argparse
import random
from urllib.parse import parse_qs, unquote
import requests
from requests.structures import CaseInsensitiveDict
import time
from datetime import datetime, timezone

start_time = datetime.now()  # Tentukan waktu mulai saat bot dijalankan

headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

def load_credentials():
    # Membaca token dari file dan mengembalikan daftar token
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File query_id.txt tidak ditemukan.")
        return 
    except Exception as e:
        print("Terjadi kesalahan saat memuat query:", str(e))
        return 

def parse_query(query: str):
    parsed_query = parse_qs(query)
    parsed_query = {k: v[0] for k, v in parsed_query.items()}
    user_data = json.loads(unquote(parsed_query['user']))
    parsed_query['user'] = user_data
    return parsed_query

def get(id):
        tokens = json.loads(open("tokens.json").read())
        if str(id) not in tokens.keys():
            return None
        return tokens[str(id)]

def save(id, token):
        tokens = json.loads(open("tokens.json").read())
        tokens[str(id)] = token
        open("tokens.json", "w").write(json.dumps(tokens, indent=4))

def update(id, new_token):
    tokens = json.loads(open("tokens.json").read())
    if str(id) in tokens.keys():
        tokens[str(id)] = new_token
        open("tokens.json", "w").write(json.dumps(tokens, indent=4))
    else:
        return None

def delete(id):
    tokens = json.loads(open("tokens.json").read())
    if str(id) in tokens.keys():
        del tokens[str(id)]
        open("tokens.json", "w").write(json.dumps(tokens, indent=4))
    else:
        return None
    
def delete_all():
    open("tokens.json", "w").write(json.dumps({}, indent=4))


def print_(word):
    now = datetime.now().isoformat(" ").split(".")[0]
    print(f"[{now}] {word}")

def make_request(method, url, headers=None, json=None, data=None):
    retry_count = 0
    while True:
        time.sleep(2)
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, json=json)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=json, data=data)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=json, data=data)
        else:
            raise ValueError("Invalid method.")
        
        if response.status_code >= 500:
            if retry_count >= 4:
                print_(f"Status Code: {response.status_code} | {response.text}")
                return None
            retry_count += 1
        elif response.status_code >= 400:
            print_(f"Status Code: {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragent = [line.strip() for line in f.readlines()]
        if index < len(useragent):
            return useragent[index]
        else:
            return "Index out of range"
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'

def check_tasks(token):
    time.sleep(2)
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    
    response = requests.get('https://game-domain.blum.codes/api/v1/tasks', headers=headers)
    if response.status_code == 200:
        mains = response.json()
        for main in mains:
            main_tasks = main.get('tasks',[])
            subSections = main.get('subSections',[])
            
            for subs in subSections:
                title_task = subs.get('title')
                print_(f"Main Task Title : {title_task}")
                tasks = subs.get('tasks')
                for task in tasks:
                    sub_title = task.get('title',"")
                    if 'invite' in sub_title.lower():
                        print_(f"{sub_title} Skipping Quest")
                    elif 'farm' in sub_title.lower():
                        print_(f"{sub_title} Skipping Quest")
                    else:
                        if task['status'] == 'CLAIMED':
                            print_(f"Task {title_task} claimed  | Status: {task['status']} | Reward: {task['reward']}")
                        elif task['status'] == 'NOT_STARTED':
                            print_(f"Starting Task: {task['title']}")
                            start_task(token, task['id'],sub_title)
                            validationType = task.get('validationType')
                            if validationType == 'KEYWORD':
                                time.sleep(2)
                                validate_task(token, task['id'],sub_title)
                            time.sleep(5)
                            claim_task(token, task['id'],sub_title)
                        elif task['status'] == 'READY_FOR_CLAIM':
                            claim_task(token, task['id'],sub_title)
                        elif task['status'] == 'READY_FOR_VALIDATE':
                            validate_task(token, task['id'],sub_title)
                            time.sleep(5)
                            claim_task(token, task['id'],sub_title)
                        else:
                            print_(f"Task already started: {sub_title} | Status: {task['status']} | Reward: {task['reward']}")
    else:
        print_(f"Failed to get tasks")
    

def start_task(token, task_id, title):
    time.sleep(2)
    url = f'https://earn-domain.blum.codes/api/v1/tasks/{task_id}/start'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = make_request('post', url, headers=headers)
        if response is not None:
            print_(f"Task {title} started")
        else:
            print_(f"Failed to start task {title}")
        return 
    except:
        print_(f"Failed to start task {title} ")

def validate_task(token, task_id, title, word=None):
    time.sleep(2)
    url = f'https://earn-domain.blum.codes/api/v1/tasks/{task_id}/validate'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    payload = {'keyword': word}
    try:
        response =  response = make_request('post',url, headers=headers, json=payload)
        if response is not None:
            print_(f"Task {title} validating")
        else:
            print_(f"Failed to validate task {title}")
        return 
    except:
        print_(f"Failed to validate task {title} ")

def claim_task(token, task_id,title):
    time.sleep(2)
    print_(f"Claiming task {title}")
    url = f'https://earn-domain.blum.codes/api/v1/tasks/{task_id}/claim'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response =  response = make_request('post',url, headers=headers)
        if response is not None:
            print_(f"Task {title} claimed")
        else:
            print_(f"Failed to claim task {title}")
    except:
        print_(f"Failed to claim task {title} ")

        
def get_new_token(query_id):
    import json
    # Header untuk permintaan HTTP
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://telegram.blum.codes",
        "priority": "u=1, i",
        "referer": "https://telegram.blum.codes/"
    }

    data = json.dumps({"query": query_id})
    url = "https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
    time.sleep(2)
    print_(f"Getting Token...")
    response = make_request('post',url, headers=headers, data=data)
    if response is not None:
        print_(f"Token Created")
        response_json = response.json()
        return response_json['token']['refresh']
    else:
        print_(f"Failed get token")
        return None

# Fungsi untuk mendapatkan informasi pengguna
def get_user_info(token):
    time.sleep(2)
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response =  response = make_request('get','https://gateway.blum.codes/v1/user/me', headers=headers)
    if response is not None:
        return response.json()

def get_balance(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response =  response = make_request('get','https://game-domain.blum.codes/api/v1/user/balance', headers=headers)
        if response is not None:
            return response.json()
        else:
            print_(f"Failed getting data balance")
    except requests.exceptions.ConnectionError as e:
        print_(f"Connection Failed ")

def play_game(token):
    time.sleep(2)
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = make_request('post','https://game-domain.blum.codes/api/v2/game/play', headers=headers)
        if response is not None:
            return response.json()
        else:
            return None
    except Exception as e:
        print_(f"Failed play game, Error {e}")

def claim_game(token, game_id, point, dogs):
    time.sleep(2)
    url = "https://game-domain.blum.codes/api/v2/game/claim"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["authorization"] = "Bearer "+token
    headers["content-type"] = "application/json"
    headers["origin"] = "https://telegram.blum.codes"
    headers["priority"] = "u=1, i"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    data = create_payload(game_id=game_id, point=point, dogs=dogs)
    if data is not None:
        payload = {'payload' : data}
        try:
            response = make_request('post', url, headers=headers, data=json.dumps(payload))
            if response is not None:
                return response
            else:
                return None
        
        except Exception as e:
            print_(f"Failed Claim game, error: {e}")
    else:
        return None

def get_game_id(token):
    game_response = play_game(token)
    trying = 5
    if game_response is None or game_response.get('gameId') is None:
        while True:
            if trying == 0:
                break
            print_("Play Game : Game ID is None, retrying...")
            game_response = play_game(token)
            if game_response is not None:
                game_id = game_response.get('gameId', None)
            else:
                game_id = None
            if game_id is not None:
                return game_response['gameId']
                break
            else:
                print_('Game id Not Found, trying to get')
            trying -= 1
    else:
        return game_response['gameId']

def claim_balance(token):
    
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        time.sleep(2)
        response = make_request('post','https://game-domain.blum.codes/api/v1/farming/claim', headers=headers)
        if response is not None:
            return response.json()
        else:
            print_("Failed Claim Balance")

    except Exception as e:
        print_(f"Failed claim balance, error: {e}")
    return None

def start_farming(token):
    time.sleep(2)
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
 
        time.sleep(2)
        response = make_request('post','https://game-domain.blum.codes/api/v1/farming/start', headers=headers)
        if response is not None:
            return response.json()
        else:
            print_("Failed Claim Balance")

    except Exception as e:
        print_(f"Failed claim balance, error: {e}")
    return None

def check_balance_friend(token):
    time.sleep(2)
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = make_request('get', 'https://user-domain.blum.codes/api/v1/friends/balance', headers=headers)
        if response is not None:
            return response.json()
        else:
            print_("Failed Check ref")
    
    except Exception as e:
        print_(f"Failed Check ref, error: {e}")
    return None

def claim_balance_friend(token):
    time.sleep(2)
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = make_request('post', 'https://user-domain.blum.codes/api/v1/friends/claim', headers=headers)
        if response is not None:
            return response.json()
        else:
            print_("Failed Claim ref Balance")
    except Exception as e:
        print_(f"Failed Claim ref, error: {e}")
    return None

# cek daily 
import json
def check_daily_reward(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
    try:
        response = make_request('post','https://game-domain.blum.codes/api/v1/daily-reward?offset=-420', headers=headers)
        if response is not None:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
      
    return None


def check_tribe(token):
    url = 'https://game-domain.blum.codes/api/v1/tribe/my'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
    try:
        response = make_request('get', url, headers=headers)
        if response is not None:
            return response.json()
        else:
            return None
    except Exception as e:
        print_(f"Failed Check Tribe, error: {e}")
    return None


def join_tribe(token):
    url ='https://game-domain.blum.
