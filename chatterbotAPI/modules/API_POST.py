import time

from chatterbotAPI import app, cb

@app.post('/bot')
async def chatbot_api(query: str):
    '''
    `https://host/bot?message={query}`

    **Gets response from RESTFUL Chatbot-API.**\n
    **A Succesful Request would return:**\n
    - __bot_response:__  Bot's response to the desired query\n
    - __query:__   string user passes to the API\n
    - __response:__   Respond code: 200 if success, else 422 if error\n
    - __time_taken:__ delay time for response from user to the server\n


    **Response Codes:**\n
    - __Response__ [`200`] - Success\n
    - __Response__ [`405`] - Method Not Allowed\n
    - __Response__ [`422`] - Unprocessable Entity
    '''
    start = time.time()
    return {
        'response': int(200),
        'query' : query,
        'bot_response': str(
                cb.get_response(query)
            ),
        'time_taken': str(
                f'{(round((time.time() - start)* 1000, 3))}ms'
            )
        }