# Proiect SAT Solver Comparativ
## Scopul Proiectului
Scopul acestui proiect este de a evalua și compara performanța a două metode diferite de rezolvare a problemelor SAT (Satisfiability Problem): algoritmul QEPS (Quantum-inspired Evolutionary P Systems) și un algoritm clasic de backtracking. Proiectul include generarea unui exemplu mare de problemă SAT pentru a testa și demonstra diferențele de performanță între aceste două abordări.

## Algoritmul QEPS
Algoritmul QEPS este un sistem evolutiv inspirat de quantum computing și P sisteme. Acesta utilizează structuri de membrane pentru a executa operațiuni în paralel și pentru a explora spațiul de soluții. QEPS încearcă să găsească soluții satisfăcătoare prin adaptarea și evoluția soluțiilor candidate, bazându-se pe principii ale teoriei cuantice pentru a optimiza procesul de căutare.

## Algoritmul de Backtracking
Algoritmul de backtracking este o metodă clasică de căutare prin forță brută care explorează spațiul de soluții prin încercarea sistematică a tuturor combinațiilor posibile de valori pentru variabilele unei formule SAT. Acesta reușește să identifice rapid soluțiile în spațiile de căutare de dimensiuni mici spre medii, oprindu-se imediat ce găsește o soluție satisfăcătoare.

## Generarea Exemplului 
Exemplul de problemă SAT este generat aleatoriu cu 20 de variabile și 50 de clauze, oferind o complexitate suficientă pentru a testa performanța în timp a  algoritmilor. Formula generată este salvată într-un fișier pentru a fi folosită consecvent în toate testele.

## Compararea Soluțiilor
Compararea algoritmilor a fost efectuată prin măsurarea timpului de execuție necesar pentru fiecare metodă pentru a rezolva problema SAT generată:

* QEPS:
    * Soluție: [False, False, True, False, True, False, True, False, True, True, False, True, False, True, True, True, False, True, True, True]
    * Timp Execuție: 0.044 secunde
* Backtracking:
    * Soluție: [True, True, True, True, False, True, False, False, False, True, True, True, True, True, False, False, False, True, False, True]
    * Timp Execuție: 0.088 secunde
  
## Concluzie
Rezultatele demonstrează că, deși ambele metode pot găsi soluții pentru problema SAT, algoritmul QEPS a fost mai rapid pentru acest exemplu, sugerând că ar putea fi mai eficient pentru probleme de dimensiuni mai mari sau mai complexe.