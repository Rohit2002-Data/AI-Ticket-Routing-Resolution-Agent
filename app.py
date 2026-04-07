from src.classifier import classify_ticket
from src.rag import retrieve_similar
from src.agent import generate_resolution, decision_engine

ticket = input("Enter ticket: ")

category = classify_ticket(ticket)
context = retrieve_similar(ticket)
resolution = generate_resolution(ticket, context)

decision = decision_engine(len(context)/3, ticket)

print("\nCategory:", category)
print("\nResolution:", resolution)
print("\nDecision:", decision)
