from .root import app

@app.handle(domain='greeting',intent='greet')
def welcome(request, responder):
    """
    When the user starts a conversation, say hi and give some wellness center suggestions to explore.
    """
    try:
        # Get user's name from session information in a request to personalize the greeting.
        responder.slots['name'] = request.context['name']
        prefix = 'Hello, {name}. '
    except KeyError:
        prefix = 'Hello. '

    # places = app.question_answerer.get(index='wellness')
    # suggestions = ', '.join([r['name'] for r in places[0:3]])

    # Build up the final natural language response and reply to the user.
    responder.reply(prefix + 'Some nearby that may intrest you ')
                    # + suggestions)

@app.handle(intent='exit')
def say_goodbye(request, responder):
    responder.reply(['Bye', 'Goodbye', 'Have a nice day.','peace out'])

@app.handle(intent='help')
def provide_help(request, responder):
    """
    When the user asks for help, provide some sample queries they can try.
    """
    # Respond with examples demonstrating how the user can order food from different restaurants.
    # For simplicity, we have a fixed set of demonstrative queries here, but they could also be
    # randomly sampled from a pool of example queries each time.
    replies = ["I can help you find a place that brings out the best version of yourself "
               "Try something like 'Tell me the best place where i can learn to overcome my fears'"]
    responder.reply(replies)


@app.handle(intent='start_over')
def start_over(request, responder):
    """
    When the user wants to start over, clear the dialogue frame and reply for the next request.
    """
    # Clear the dialogue frame and respond with a variation of the welcome message.
    responder.frame = {}
    replies = ["Ok, let's start over! how can i help you?"]
    responder.reply(replies)
    responder.listen()
