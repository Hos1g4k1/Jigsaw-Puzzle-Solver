<h1>A Genetic Algorithm-Based Solver for Jigsaw Puzzles </h1>
<hr>

<br>
Problem koji se u ovom radu resava jeste problem slaganja slagalice.

<h1> Instalacija </h1>

<p> Klonira se repozitorijum i pozicionira u isti: </p>
<pre>git clone https://github.com/Hos1g4k1/Jigsaw-Puzzle-Solver.git
cd Jigsaw-Puzzle-Solver
</pre>

<p> Instaliraju se potrebne zavisnosti: </p>
<pre>pip install -r requirements.txt
sudo apt-get install python-tk
</pre>

<p> Instalira se projekat u edit modu: </p>
<pre>pip install -e .</pre>

<h1> Kreiranje slagalice na osnovu slike </h1>

<p> Potrebno je koristiti create_puzzle skriptu. </p>
<pre>create_puzzle putanja_do_slike --size=48 --destination=puzzle.jpg</pre>

Ovo kreira slagalicu ciji su delovi velicine 48x48 piksela i da sacuva pod imenom puzzle.jpg u trenutnom direktorijumu.
<br>
Ove parametre je moguce menjati.

<img src="https://github.com/Hos1g4k1/Jigsaw-Puzzle-Solver/blob/main/images/lion.jpg" width="300" height="500">   <img src="https://github.com/Hos1g4k1/Jigsaw-Puzzle-Solver/blob/main/images/lav_48_pocetak.jpeg" width="300" height="500">

<h1> Resavanje slagalice </h1>
<p>Potrebno je koristiti jigsaw skriptu.</p>
<pre>jigsaw --image=puzzle.jpg --generations=20 --population=600 --size=48 --save</pre>

Ovo resava slagalicu koja je sacuvana pod imenom puzzle.jpg u trenutnom direktorijumu i ciji su delovi velicine 48x48 piksela.
Zadaju se i parametri za broj generacija kao i velicinu populacije. Opcija --save kaze da sacuva krajnje resenje slagalice.
<br>
Ove parametre je moguce menjati.
