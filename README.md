# Corso python


##  Setup Ambiente

```bash
# clonare il corso
git clone https://git.par-tec.it/formazione/corso-python
cd corso-python

# creazione ed attivaizone virtualen
python3.7 -m venv venv
source venv/bin/activate

# installazione dipendenze
[[ -f requiremments.txt ]] && \
	pip install -r requirements.txt

jupyter lab
```
