import configparser
import requests

class HKBUChatGPT():
    def __init__(self,config_='./config.ini'):
        if isinstance(config_, str):
            self.config = configparser.ConfigParser()
            self.config.read(config_)
        elif isinstance(config_, configparser.ConfigParser):
            self.config = config_

    def submit(self, message: str) -> str:
        """
            This function send user's question to GPT and return the answer.
        """
        conversation = [{"role": "user", "content": message}]

        base_url     = self.config['CHATGPT']['BASE_URL']
        model_name   = self.config['CHATGPT']['MODEL_NAME']
        api_version  = self.config['CHATGPT']['API_VERSION']
        access_token = self.config['CHATGPT']['ACCESS_TOKEN']

        # HKBU ChatGPT request full URL
        url = f"{base_url}/deployments/{model_name}/chat/completions/?api-version={api_version}"
        # Request header
        headers = { 'Content-Type': 'application/json', 'api-key': access_token }
        # Request payload
        payload = { 'messages': conversation }
        response = requests.post(url, json=payload, headers=headers,timeout=10)

        # With the correct response code, we will return the result
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        # By default, it will response error
        return f"Error: {response}"

if __name__ == '__main__':
    ChatGPT_test = HKBUChatGPT()

    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        res = ChatGPT_test.submit(user_input)
        print(res)
