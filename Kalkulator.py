def kalkulator_sederhana():
    """Fungsi ini menjalankan kalkulator sederhana."""

    print("Selamat datang di Kalkulator Sederhana!")
    print("Operasi yang tersedia: +, -, *, /")

    try:
        # Langkah 1: Mengambil Input Angka dari Pengguna
        angka1_str = input("Masukkan angka pertama: ")
        angka1 = float(angka1_str) # Ubah string ke float (mendukung desimal)

        angka2_str = input("Masukkan angka kedua: ")
        angka2 = float(angka2_str) # Ubah string ke float

        # Langkah 2: Mengambil Input Operasi dari Pengguna
        operasi = input("Masukkan operasi (+, -, *, /): ")

        hasil = 0 # Inisialisasi variabel hasil

        # Langkah 3: Melakukan Operasi Berdasarkan Pilihan Pengguna
        if operasi == '+':
            hasil = angka1 + angka2
        elif operasi == '-':
            hasil = angka1 - angka2
        elif operasi == '*':
            hasil = angka1 * angka2
        elif operasi == '/':
            # Langkah 4: Penanganan Error untuk Pembagian dengan Nol
            if angka2 == 0:
                print("Error: Tidak bisa melakukan pembagian dengan nol!")
                return # Hentikan fungsi jika terjadi error ini
            hasil = angka1 / angka2
        else:
            print("Operasi tidak valid. Mohon masukkan +, -, *, atau /.")
            return # Hentikan fungsi jika operasi tidak valid

        # Langkah 5: Menampilkan Hasil
        print(f"\nHasil dari {angka1} {operasi} {angka2} adalah: {hasil}")

    except ValueError:
        # Penanganan Error jika input angka bukan numerik
        print("Input angka tidak valid. Mohon masukkan hanya angka.")
    except Exception as e:
        # Penanganan error umum lainnya
        print(f"Terjadi kesalahan: {e}")

# Memanggil fungsi kalkulator untuk menjalankannya
kalkulator_sederhana()