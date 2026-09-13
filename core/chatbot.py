from core.client import ArtAdvisorClient
from utils.history import ConversationHistory
from core.commands import process_command

class ArtAdvisorBot:
    def __init__(self):
        self.client = ArtAdvisorClient()
        self.history = ConversationHistory()

    def process_input(self, user_input):
        command_result = process_command(user_input, self.history)
        if command_result["action"] != "none":
            return command_result

        self.history.add_user_message(user_input)
        messages = self.history.get_messages(limit=10)

        return {"action": "chat", "messages": messages}

    def generate_response(self, messages):
        return self.client.generate_stream(messages)

    def save_assistant_response(self, content):
        self.history.add_assistant_message(content)