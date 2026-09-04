from view_task import lihat_tugas
from add_task import tambah_tugas
from complete_task import tandai_selesai
tasks = []
ulang = True

while ulang:
    print ("===== TASK MANAGER =====")
    print ("1. Lihat tugas")
    print ("2. Tambah tugas")
    print ("3. Tandai tugas selesai")
    print ("4. Hapus tugas")
    print ("0. Keluar tugas")

    pilihan = input("Pilih menu (0-4): ")

    match pilihan:
        case "1":
            lihat_tugas(tasks)
        case "2":
            tambah_tugas(tasks)
        case "3":
            tandai_selesai(tasks)
        case "0":
            print("Terima kasih")
            ulang = False
        case _:
            print ("Pilihan tidak valid")
        

