import ollama

def generate_resolution(ticket, context):
    prompt = f'''
    Ticket: {ticket}
    Similar issues: {context}

    Give resolution steps.
    '''

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']


def decision_engine(confidence, ticket):
    if confidence < 0.5:
        return "ESCALATE"
    return "AUTO-RESOLVE"
