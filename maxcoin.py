def find(n, coins):
    # Taulukko johon voi tallentaa maksimimäärän kolikoita jokaista summaa varten 0...n
    dp = [float('-inf')] * (n+ 1)

    # Basecase koska 0 summaan tarvitaan 0 kolikkoa
    dp[0] = 0  

    # Käydään kaikki kolikot läpi 
    # DP looppi
    for coin in coins:
        # Käydään läpi kaikki mahdolliset summat coin ja x välillä
        for i in range(coin, n+ 1):
            # Päivitä taulukkoa siitä kohtaa missä ollaan ottamalla 
            # suurempi arvo eli joko indeksissä oleva tai indeksissä oleva arvo josta on vähennetty tämänhetkinen kolikko
            # johon lisätään +1 
            # i - coin on jäljellä oleva summa 
            dp[i] = max(dp[i], dp[i - coin] + 1)

   
    if dp[n] == float('-inf'):
        return -1
    # Lopullinen määrä kolikoita on taulukon viimeisessä indeksissä
    return dp[n]

if __name__ == "__main__":
    print(find(13, [1, 2, 5])) # 13
    print(find(13, [2, 3, 5])) # 6
    print(find(13, [2, 4, 6])) # -1
    print(find(42, [8, 9, 11, 15])) # 5


