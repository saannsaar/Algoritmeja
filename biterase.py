def count(bit_string):
    
    def apufunktio(s):
         # Jos apufunktiolle annettu string on tyhjä, on yksi onnistunut poistotapa löytynyt
        if not s:
            return 1 

        montaTapaa = 0
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
			# Luodaan uusi string ilman peräkkäisiä samoja bittejä
            uusiString = s[:i] + s[j:]
           
            # Rekursiivisesti lasketaan poistotavat uudesta stringistä
            montaTapaa += apufunktio(uusiString)
            i = j

        return montaTapaa

    return apufunktio(bit_string)

if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925