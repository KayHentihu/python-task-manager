def lihat_tugas(tasks):
    nomor = 1
    print("===== DAFTAR TUGAS =====")
    for nilai in tasks:
        print(f"{nomor}. {nilai}")
        nomor += 1