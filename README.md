# Discord Task Manager Bot

Bot Discord sederhana untuk mengelola tugas tim menggunakan Python dan SQLite.

## Fitur

- `!add_task <deskripsi>` — Menambahkan tugas baru.
- `!show_tasks` — Menampilkan semua tugas.
- `!complete_task <id_tugas>` — Menandai tugas sebagai selesai.
- `!delete_task <id_tugas>` — Menghapus tugas.

## Teknologi

- Python
- discord.py
- SQLite
- pytest

## Instalasi

1. Clone repository:

   ```bash
   git clone <url-repository-github>
   cd task_manager_bot
   ```

2. Buat virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Aktifkan virtual environment:

   ```bash
   # Windows
   .venv\Scripts\activate

   # Linux/macOS
   source .venv/bin/activate
   ```

4. Instal dependensi:

   ```bash
   pip install -r requirements.txt
   ```

5. Buat file `.env` dan masukkan token bot Discord:

   ```env
   TOKEN=token_bot_discord
   ```

6. Jalankan bot:

   ```bash
   python bot.py
   ```

## Menjalankan Pengujian

Gunakan perintah berikut:

```bash
python -m pytest tests/ -v
```

## Struktur Proyek

```text
task_manager_bot/
├── bot.py
├── database.py
├── commands.py
├── tests/
│   ├── conftest.py
│   ├── test_add_task.py
│   ├── test_delete_task.py
│   ├── test_show_tasks.py
│   └── test_complete_task.py
├── requirements.txt
├── README.md
└── .gitignore
```
