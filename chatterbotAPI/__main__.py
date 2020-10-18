import uvicorn
import time
from chatterbotAPI import app, cb

@app.get('/')
async def chatbot_api_get(query: str):
    '''
    ``GET` https://endpoint.mannu.me/chatbot?query={query}`

    **Gets response from RESTFUL Chatbot-API.**\n
    **A Succesful Request would return:**\n
    - __response:__   fills in the nested json with in this query\n
    - __bot:__  Bot's response to the desired query\n
    - __user:__   string user passes to the API\n
    - __time_taken:__ delay time for response from user to the server\n


    **Response Codes:**\n
    - __Response__ [`200`] - Success\n
    - __Response__ [`405`] - Method Not Allowed\n
    - __Response__ [`422`] - Unprocessable Entity
    '''
    start = time.time()
    return {
        'response': {
            'user' : query,
            'bot': str(cb.get_response(query)),
            'time_taken': str(f'{(round((time.time() - start)* 1000, 3))}ms')
        }
    }


@app.post('/')
async def chatbot_api_post(query: str):
    '''
    ``POST` https://endpoint.mannu.me/chatbot?query={query}`

    **Gets response from RESTFUL Chatbot-API.**\n
    **A Succesful Request would return:**\n
    - __response:__   fills in the nested json with in this query\n
    - __bot:__  Bot's response to the desired query\n
    - __user:__   string user passes to the API\n
    - __time_taken:__ delay time for response from user to the server\n


    **Response Codes:**\n
    - __Response__ [`200`] - Success\n
    - __Response__ [`405`] - Method Not Allowed\n
    - __Response__ [`422`] - Unprocessable Entity
    '''
    start = time.time()
    return {
        'response': {
            'user' : query,
            'bot': str(cb.get_response(query)),
            'time_taken': str(f'{(round((time.time() - start)* 1000, 3))}ms')
        }
    }


if __name__ == "__main__":
    uvicorn.run("chatterbotAPI:app", host="0.0.0.0", port=8000, log_level="info")