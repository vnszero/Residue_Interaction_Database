"""
1ST part - Model
"""
# just to explain an concept
INTERACTION = True
MATRIX_DATA = True
AMINO_ACID_ID_POSITION = 34

# machine's states
CREATE_MATRIX = 0
GET_MATRIX_VALUES = 1
CREATE_AMINO_ACID = 2
CREATE_ATOM = 3
SAVE_CURRENT_GO_TO_NEXT = 4

# global variables
amino_acid_vector = []
pdb_file = open('proteina.pdb', 'r')
state = CREATE_MATRIX
amino_acid_id = 1
atom_id = 1

# classes
class Atom:
    pass

class AminoAcid:
    def __init__(self):
        self.id = 0
        self.atoms = []
    
    def insert_atom(self, atom:Atom):
        self.atoms.append(atom)
    
    def set_id(self, id):
        self.id = id
    
    def get_atoms(self) -> list:
        return self.atoms
    
class BaseMatrix:
    pass

"""
2ND Part - Recover info
"""
amino_acid = AminoAcid()
for line in pdb_file.readlines():
    # just happen in first lines of file
    if state == CREATE_MATRIX:
        # recover matrix info
        matrix = BaseMatrix()

        # go to next state
        state = GET_MATRIX_VALUES

    elif state == GET_MATRIX_VALUES:
        if line is MATRIX_DATA:
            matrix.set(line)
        else:
            state = CREATE_AMINO_ACID

    # just happen if there's a next id for amino acid
    if line[AMINO_ACID_ID_POSITION] != amino_acid_id and state != CREATE_MATRIX and state != GET_MATRIX_VALUES:
        #this is the next amino acid
        amino_acid_vector.append(amino_acid)
        state = CREATE_AMINO_ACID
        amino_acid_id += 1

    # starts with matrix
    if state == CREATE_AMINO_ACID:
        # define amino acid id
        amino_acid.set_id(amino_acid_id)
        
        # define first atom
        atom = Atom(atom_id)
        atom_id += 1

        # assemble amino acid
        amino_acid.insert_atom(atom)
    
    elif state == CREATE_ATOM:
        # define next atom
        atom = Atom(atom_id)
        atom_id += 1

"""
3ND part - interactions
"""
for amino_acid in amino_acid_vector:
    for atom_selected in amino_acid.get_atoms():
        for atom_to_compare in amino_acid.get_atoms():
            if atom_selected != atom_to_compare:
                # validar distancias
                if INTERACTION:
                    pass
                    # gerar um novo arquivo daquela interacao
                    # manter o modelo descrito no problema
                    # referenciar a proteina original

"""
4TH part - deliver solution
"""