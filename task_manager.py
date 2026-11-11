import uuid

data = {}

def add_data(task):
    task_id = uuid.uuid4().int
    data[task_id] = {"task": task, "status": False}
    print("Berhasil menambahkan data!")
    
    
start = True

while start:
    print("Selamat data di program task manager")
    print("1. Tambahkan Tugas")
    print("2. Lihat Tugas")
    print("3. Keluar")
    
    opsi = input("Masukkan pilihan: ")
    
    if opsi == "1":
        task = input("Masukkan tugas: ")
        add_data(task)
    elif opsi == "2": 
        if data:
            print(data)
            print()
        else:
            print("tidak ada data")
            print()
    else:
        start = False
        
        
    
    

