import sys
import torch
import math
from read_xyz import read_xyz

if __name__ == "__main__":
    model = torch.jit.load('DLNMR1.pt')
    print(f"NMR model version: {model.version} Copyright 2025 Wavefunction, Inc.")
    inp = sys.argv[1] if len(sys.argv)>1 else 'input.xyz'
    mols = read_xyz(inp)

    for mol in mols:
        print(f"Read {mol.label}")
        Z = torch.tensor(mol.species,dtype=torch.int64)
        R = torch.tensor(mol.coords,dtype=torch.float32).unsqueeze(0) # add batch dimension
        res = model(Z,R) # our model processes one unique molecule at a time
        shifts = res[2].tolist()
        print("Label\tShift (ppm)")
        for i in range(len(shifts)):
            shift = shifts[i]
            if not math.isnan(shift):
                label = mol.labels[i]
                print(f"{label}\t{shift:.5f}")
