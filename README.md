# The Evil Puzwick: guida all'utilizzo e alla rimozione
## Indice
1. [Informazioni generali :book:](#informazioni-generali-book)
2. [Infezione :mask:](#infezione-mask)
3. [Effetti e conseguenze :policeman:](#effetti-e-conseguenze-policeman)
4. [Rimozione :x:](#rimozione-x)
5. [Tecnologie utilizzate :computer:](#tecnologie-utilizzate-computer)
6. [Contattami :wave:](#contattami-wave)

### Informazioni generali :book:
***
**The Evil Puzwick** è un semplice programma che emula il comportamento di un virus informatico: tuttavia,
è **interamente PRIVO di codice malevolo**. L'obiettivo dietro la realizzazione dello stesso non è infatti quello
di danneggiare la macchina dell'utente, ma quello di spronarlo a trovare un modo di rimuovere questo "virus".
Qualora non ne fosse in grado, è sufficiente ricorrere all'apposito [tool](https://github.com/RichardBoy05/The-Evil-Puzwick/releases/tag/virus-remover)
per la rimozione.


### Infezione :mask:
***
L'infezione si verifica con l'esecuzione del file [_start.vbs_](https://github.com/RichardBoy05/The-Evil-Puzwick/blob/main/infector/start.vbs), che
esegue "silenziosamente" il file [_infector.bat_](https://github.com/RichardBoy05/The-Evil-Puzwick/blob/main/infector/infector.bat), vero artefice
di questo processo. Il file copia l'eseguibile del virus (_TheEvilPuzwick.exe_) nella cartella di **Startup di Windows**, inserisce le immagini del programma in una cartella nascosta nel percorso "_%appdata%_" e, successivamente, esegue il virus.
Avendo inserito l'eseguibile nella cartella **Startup di Windows**, ad ogni avvio del computer il virus si ripresenterà.

### Effetti e conseguenze :policeman:
***
Come già accennato, il programma **NON** provoca alcun danno al computer su cui è eseguito: è solo un po' noioso da gestire! :stuck_out_tongue:

Col suo avvio (che si verificherà con la prima esecuzione e ad ogni accensione del sistema) apparirà questo **popup**, impostato per essere
sempre visualizzato in primo piano:

![Popup](https://github.com/RichardBoy05/The-Evil-Puzwick/blob/main/resources/window.png)

<details> 
 <summary><b>SPOILER</b>: <i>visualizza codice sblocco</i> </summary>
  yX4eaY@v
</details>

Nel caso l'utente provasse a chiudere la finestra o inserisse un codice di sblocco errato nella casella di testo, il virus si replicherà...:hushed:

![Infection](https://github.com/RichardBoy05/The-Evil-Puzwick/blob/main/resources/multiple_windows.png)

### Rimozione :x:
***
Per rimuovere **completamente** il virus dalla propria macchina, è possibile ricorrere all'apposito [tool di rimozione](https://github.com/RichardBoy05/The-Evil-Puzwick/releases/tag/virus-remover). Ad operazione effettuata, eliminare la cartella contenente i file estratti dall'archivio scaricato e l'archivio stesso.

### Tecnologie utilizzate :computer:
***
Tencnologie utilizzate:   
* [Python 3.10](https://www.python.org/downloads/)
* [File batch di Windows](https://g.co/kgs/Y8X8tT)
* [VBScript](https://g.co/kgs/CsEvfv)


### Contattami :wave:
***
In caso di problemi, curiosità o domande, sentiti libero di [contattarmi](mailto:richard.meoli.2005@gmail.com?subject=TheEvilPuzwick).
