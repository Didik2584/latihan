tabelNilai = [
    {"NamaMatakuliah":"Algoritma","NilaiTugas":80,"NilaiUTS":80,"NilaiUAS":70},
    {"NamaMatakuliah":"Pancasila","NilaiTugas":60,"NilaiUTS":90,"NilaiUAS":80},
    {"NamaMatakuliah":"Pemrograman","NilaiTugas":80,"NilaiUTS":70,"NilaiUAS":80},
    {"NamaMatakuliah":"Bhs.Indonesia","NilaiTugas":89,"NilaiUTS":79,"NilaiUAS":90},
    {"NamaMatakuliah":"Bhs.Inggris","NilaiTugas":70,"NilaiUTS":75,"NilaiUAS":60},
]
print("DAFTAR NILAI MATA KULIAH")
print("--------------------------------------------------------------------")
print('{:15} {:5} {:9} {:9} {:9} {:9}'.format("NamaMataKuliah","NilaiTugas","NilaiUTS","NilaiUAS","NilaiAngka","NilaiHuruf")) 
print("--------------------------------------------------------------------")
for iMatakuliah in tabelNilai :
    #dioperasikan
    iMatakuliah["NilaiAngka"] = iMatakuliah["NilaiTugas"] * 0.3 + iMatakuliah["NilaiUTS"] * 0.3 + iMatakuliah["NilaiUAS"] * 0.4

    if iMatakuliah['NilaiAngka'] >=80 and iMatakuliah['NilaiAngka'] <= 100 :
        iMatakuliah["NilaiHuruf"] = "A"

    elif iMatakuliah['NilaiAngka'] >=60 and iMatakuliah['NilaiAngka'] < 80 :
        iMatakuliah["NilaiHuruf"] = "B"

    elif iMatakuliah['NilaiAngka'] >=40 and iMatakuliah['NilaiAngka'] < 60 :
        iMatakuliah["NilaiHuruf"] = "C"

    elif iMatakuliah['NilaiAngka'] >=20 and iMatakuliah['NilaiAngka'] < 40:
        iMatakuliah["NilaiHuruf"] = "D"

    else:
        iMatakuliah["NilaiHuruf"] = "E"
    

    print('{:15} {:5} {:9} {:10} {:9} {:>9}'.format(iMatakuliah['NamaMatakuliah'],iMatakuliah['NilaiTugas'],
    iMatakuliah['NilaiUTS'],iMatakuliah['NilaiUAS'],iMatakuliah['NilaiAngka'],iMatakuliah['NilaiHuruf'])) 
print("--------------------------------------------------------------------")