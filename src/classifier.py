import ollama

def classify_ticket(text):
    prompt = f'''
    Classify into one:
    Infrastructure, Application, Security, Database, Network, Access Management

    Ticket: {text}
    '''

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
