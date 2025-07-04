print("\nSelamat datang di program kami")
    
daftar = "y"
while daftar   =='y':
    print("\n1. Tentang Kelompok")
    print("2. Anggota Kelompok")
    print("3. Keluar")
    
    try:
        pilih = int(input("Silahkan pilih salah satu menu diatas!"))
        if pilih == 1:
            print("\n\nTugas UAS Semester 2")
            print("Kelompok 7")
            print("15.2C.05")
            print("Materi : Tree\n\n")
        elif pilih == 2:
            print("\n\n1. hans   | 15240358")
            print("2. Pikar  | ")
            print("3. Muhlis | ")
            print("2. Fakih  | ")
            print("2. Abyan  | ")
        else:
            print("pilihan tidak ada")
    except ValueError:
        print("Input harus berupa angka!!")
    daftar = input("mau memilih menu lain?").lower()