import json
import os
from datetime import datetime
from config.settings import Config
from prompts.system_prompt import get_system_prompt

class ConversationHistory:
    def __init__(self):
        self.system_prompt = get_system_prompt()
        self.history = []

    def add_user_message(self, content):
        self.history.append({"role": "user", "content": content})

    def add_assistant_message(self, content):
        self.history.append({"role": "assistant", "content": content})

    def get_messages(self, limit=10):
        messages = [{"role": "system", "content": self.system_prompt}]
        recent_history = self.history[-limit:] if limit else self.history
        messages.extend(recent_history)
        return messages

    def clear(self):
        self.history = []

    def export_to_json(self):
        if not self.history:
            return None
        os.makedirs(Config.CONVERSATIONS_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(Config.CONVERSATIONS_DIR, f"chat_history_{timestamp}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)
        return filepath

    # FITUR BONUS: Ekspor data mentah untuk tombol Download di UI
    def get_export_data(self):
        return json.dumps(self.history, ensure_ascii=False, indent=4)

    # FITUR BONUS: Memuat ulang riwayat dari file JSON
    def import_from_data(self, history_list):
        self.history = history_list

    # FITUR BONUS: Statistik Percakapan
    def get_statistics(self):
        user_msgs = sum(1 for m in self.history if m["role"] == "user")
        bot_msgs = sum(1 for m in self.history if m["role"] == "assistant")
        return {
            "total": len(self.history),
            "user": user_msgs,
            "bot": bot_msgs
        }