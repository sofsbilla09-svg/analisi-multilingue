# Il mio primo progetto di Linguistica Computazionale
frasi = {
    "Inglese": "Artificial intelligence is transforming how we learn languages.",
    "Spagnolo": "La inteligencia artificial está transformando cómo aprendemos idiomas.",
    "Russo": "Искусственный интеллект меняет то, как мы изучаем языки."
}

for lingua, testo in frasi.items():
    # Puliamo la punteggiatura base e dividiamo il testo in parole
    parole = testo.replace(".", "").replace(",", "").split()
    numero_parole = len(parole)
    
    # Calcoliamo la lunghezza media delle parole
    lunghezza_media = sum(len(p) for p in parole) / numero_parole
    
    # Controlliamo se ci sono caratteri cirillici
    ha_cirillico = any('а' <= carattere.lower() <= 'я' for carattere in testo)
    
    print(f"--- {lingua} ---")
    print(f"Parole totali: {numero_parole}")
    print(f"Lunghezza media parole: {lunghezza_media:.1f} lettere")
    print(f"Contiene alfabeto cirillico? {'Sì' if ha_cirillico else 'No'}\
