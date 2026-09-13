# Galeria ArtAdvisor

**Galeria ArtAdvisor** adalah chatbot berbasis **Large Language Model (LLM)** yang berperan sebagai asisten AI untuk membantu pengguna memahami dan mengeksplorasi dunia seni rupa.

Konsep chatbot ini diadaptasi dari proyek **Galeria**, yaitu konsep platform marketplace dan lelang karya seni. Pada proyek ini, Galeria ArtAdvisor difokuskan sebagai **asisten percakapan** untuk kolektor pemula, penggemar seni, dan calon pembeli.

**LLM Provider:** Groq API
**Interface:** Streamlit
**Language:** Python

---

## 1. Core Functions

Galeria ArtAdvisor memiliki empat fungsi utama:

### Artwork Discovery

Membantu pengguna mengeksplorasi gaya, aliran, tema, medium, dan karakteristik karya berdasarkan preferensi.

### Art Education

Menjelaskan istilah, konsep, sejarah, aliran, teknik, dan medium dalam seni rupa.

### Buying Guidance

Memberikan panduan umum mengenai hal-hal yang perlu diperhatikan sebelum membeli karya seni, seperti kondisi, medium, ukuran, provenance, dan dokumentasi.

### Auction Guidance

Menjelaskan mekanisme lelang seni, seperti starting price, bid, increment, reserve price, winning bid, dan buyer's premium.

---

## 2. Chatbot Limitations

Pada versi ini, Galeria ArtAdvisor **tidak terhubung dengan database marketplace atau sistem transaksi Galeria**.

Chatbot tidak dapat:

* Melakukan transaksi pembelian.
* Memproses pembayaran.
* Melakukan real-time bidding.
* Mengakses database artwork.
* Menampilkan listing atau ketersediaan artwork secara real-time.
* Menentukan harga artwork secara pasti.
* Menjamin keuntungan investasi seni.
* Melakukan autentikasi pengguna.

Chatbot juga tidak boleh mengarang informasi mengenai artwork, harga, listing, maupun aktivitas lelang yang tidak tersedia.

---

## 3. Application Flow

Alur kerja Galeria ArtAdvisor:

```text
User
  |
  v
Streamlit Interface
  |
  v
Chatbot Controller
  |
  +------------------+
  |                  |
  v                  v
System Prompt   Conversation History
  |                  |
  +--------+---------+
           |
           v
       Groq API
           |
           v
          LLM
           |
           v
   Generated Response
           |
           v
          User
```

### Flow Explanation

1. **User** mengirimkan pertanyaan melalui Streamlit.
2. **Chatbot Controller** menerima dan memproses input.
3. **System Prompt** memberikan identitas, fungsi, aturan, dan batasan chatbot.
4. **Conversation History** memberikan konteks percakapan sebelumnya.
5. Informasi tersebut dikirim ke **Groq API**.
6. **LLM** menghasilkan respons berdasarkan prompt dan konteks.
7. Respons ditampilkan kembali kepada **User**.

---

## 4. Project Structure

```text
galeria-artadvisor/
│
├── app.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── core/
│   ├── __init__.py
│   ├── client.py
│   ├── chatbot.py
│   └── commands.py
│
├── prompts/
│   ├── __init__.py
│   └── system_prompt.py
│
├── utils/
│   ├── __init__.py
│   ├── history.py
│   └── helpers.py
│
├── conversations/
│   └── .gitkeep
│
├── screenshots/
│   └── .gitkeep
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

| Component                  | Function                                       |
| -------------------------- | ---------------------------------------------- |
| `app.py`                   | Entry point dan Streamlit interface            |
| `config/settings.py`       | Konfigurasi aplikasi dan environment variables |
| `core/client.py`           | Integrasi Groq API                             |
| `core/chatbot.py`          | Logika utama chatbot dan komunikasi dengan LLM |
| `core/commands.py`         | Pengelolaan command chatbot                    |
| `prompts/system_prompt.py` | System prompt dan aturan perilaku chatbot      |
| `utils/history.py`         | Pengelolaan conversation history               |
| `utils/helpers.py`         | Fungsi utilitas                                |
| `conversations/`           | Penyimpanan conversation history               |
| `screenshots/`             | Dokumentasi screenshot aplikasi                |

---

## 5. Installation & Setup

### 1. Clone Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd galeria-artadvisor
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Aktifkan pada Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Buat file `.env` pada root project:

```text
GROQ_API_KEY=your_actual_groq_api_key
GROQ_MODEL=your_configured_model
```

API key tidak boleh di-commit ke GitHub.

---

## 6. Run Application

Jalankan perintah berikut dari **root folder project**:

```bash
streamlit run app.py
```

Setelah aplikasi berjalan, buka alamat lokal yang diberikan oleh Streamlit pada browser.

---

## 7. Example Conversation

### Artwork Discovery

```text
User:
Saya suka lukisan dengan suasana tenang dan banyak unsur alam.
Gaya seni apa yang cocok?

Galeria ArtAdvisor:
Anda dapat mengeksplorasi beberapa pendekatan seperti
landscape art, Impressionism, atau karya dengan pendekatan
minimalis dan palet warna lembut.
```

### Art Education

```text
User:
Apa perbedaan Kubisme dan Surealisme?

Galeria ArtAdvisor:
Kubisme berfokus pada bentuk geometris dan representasi
objek dari berbagai sudut pandang, sedangkan Surealisme
lebih mengeksplorasi mimpi, imajinasi, dan alam bawah sadar.
```

---

## 8. Screenshots

Berikut adalah dokumentasi tampilan dan pengujian Galeria ArtAdvisor.

### Main Interface

![Tampilan Utama Chatbot](https://github.com/user-attachments/assets/9c85555f-f759-4ff5-ac31-d08ad4742578)

### Core Functions Testing

![Pengujian Fungsi Utama (Core Functions)](https://github.com/user-attachments/assets/d2269c40-2532-4e14-81a1-9f90ac771ec7)

### Commands Testing

![Pengujian Perintah Khusus (Commands)](https://github.com/user-attachments/assets/938190f4-8dcd-4baa-a55c-9ab96e7a9144)

### Red Teaming & Guardrails Testing

![Pengujian Batasan (Red Teaming & Guardrails)](https://github.com/user-attachments/assets/9a8e2c96-9d0c-43f7-85f6-ddfa546be84c)

### Conversation History Storage

![Pengujian Penyimpanan File](https://github.com/user-attachments/assets/086d3ca1-3459-4f0d-a800-cfb7f35dd0ec)

---

## 9. Project Summary

Galeria ArtAdvisor merupakan prototype **LLM-powered art assistant** yang menggabungkan **Streamlit, Groq API, system prompt, dan conversation history** untuk memberikan pengalaman percakapan yang terarah dalam domain seni rupa.

Fokus chatbot mencakup:

**Artwork Discovery | Art Education | Buying Guidance | Auction Guidance**

Chatbot dirancang untuk memberikan informasi dan panduan secara edukatif tanpa mengklaim akses terhadap data marketplace, transaksi, harga real-time, maupun sistem lelang aktual.
