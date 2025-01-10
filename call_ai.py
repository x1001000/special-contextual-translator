from openai import OpenAI
client = OpenAI()

def call_ai(user_message, model='gpt-4o', developer_message=''):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'developer', 'content': developer_message},
            {'role': 'user', 'content': user_message},
        ],
    )
    return response

if __name__ == '__main__':
    user_message = 'Who are you?'
    response = call_ai(user_message)
    print(response.choices[0].message.content)