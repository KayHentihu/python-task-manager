from view_task import lihat_tugas   

def tandai_selesai(tasks):
    lihat_tugas(tasks)
    status = int(input("Masukkan nomor tugas yang selesai: "))
    
    tasks[status-1] = f"{tasks[status-1]} - Selesai"
    

    