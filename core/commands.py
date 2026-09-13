def process_command(user_input, history_instance):
    command = user_input.strip().lower()

    if command == "/exit":
        history_instance.export_to_json()
        message = "**[System]**: Terimakasih telah menggunakan Galeria ArtAdvisor."
        return {"action": "exit", "message": message}

    elif command == "/clear":
        history_instance.clear()
        return {"action": "continue", "message": "**[System]**: Riwayat obrolan berhasil dihapus. Memulai sesi baru."}

    elif command == "/help":
        help_text = (
            "**=== PANDUAN PERINTAH ===**\n\n"
            "**/help**  - Menampilkan informasi perintah ini\n\n"
            "**/clear** - Menghapus riwayat percakapan untuk memulai topik baru\n\n"
            "**/exit**  - Keluar dari program dan menyimpan riwayat percakapan\n\n"
            "========================"
        )
        return {"action": "continue", "message": help_text}

    return {"action": "none", "message": None}