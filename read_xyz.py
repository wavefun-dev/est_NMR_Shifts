class Molecule:
    def __init__(self):
        self.label = ""
        self.labels = [] # species labels
        self.species = []
        self.coords = []

def read_xyz(path): 
    periodic_table = {'H':1, 'B':5, 'C':6, 'N':7, 'O':8, 'F':9, 'Si':14, 'P':15, 'S':16, 'Cl':17, 'Br':35}
    mols = []
    with open(path, "r") as fh:
        while True:
            # read to first number
            n = ''
            while True:
                n = fh.readline() #number species
                if n == '': # EOF
                    break
                try:
                    n = int(n)
                    break
                except ValueError:
                    pass
            if n == '':
                break
            label = fh.readline().strip()
            mol = Molecule()
            mol.label = label
            for i in range(n):
                line = fh.readline()
                res = line.split()
                alab = elem = res[0]
                if alab.isdigit():
                    elem = int(elem)
                else:
                    # to identify atoms we may have labels like "C1"
                    elem = alab[:2]
                    if elem not in periodic_table:
                        elem = alab[:1]
                        if elem not in periodic_table:
                            print (f"Unsupported element: {elem}.. skipping {label}")
                            mol = None
                            break
                    elem = periodic_table[elem]
                        
                mol.labels.append(alab)
                mol.species.append(elem)
                mol.coords.append((float(res[1]),float(res[2]),float(res[3])))
            if mol:
                mols.append(mol)
    return mols
