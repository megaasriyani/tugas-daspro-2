hari_kerja = 15
hari_kerja_perbulan = 20
gaji_pokok = 2700000
hari_lembur = 10

def hitung_gaji_lembur(jumlah_hari_kerja, hari_kerja_perbulan, gaji_pokok):
    hari_lembur = jumlah_hari_kerja - hari_kerja_perbulan
    if hari_lembur > 0:
        upah_gaji_lembur = 1,20 * (gaji_pokok / hari_kerja_perbulan)  
        return gaji_lembur
    else:
        return 0


def format_rupiah(amount):
    return "Rp {:,}".format(amount).replace(',', '.')

gaji_lembur = hitung_gaji_lembur(hari_kerja, hari_kerja_perbulan, gaji_pokok)
total_gaji = gaji_pokok + gaji_lembur

print("Total Gaji:", format_rupiah(total_gaji))
