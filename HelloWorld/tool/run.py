import os

class pdb_deal:
    def __init__(self,):
        print "/*****PDB-DEAL******/"
        print "/*****Start this class to deal PDB file !*******/"
        self.key_dict()    
    def key_dict(self,): 
        self.centr_dict = {
        'CYS': ['CA', 'CB', 'SG'], 
        'ASP': ['OD1', 'CG', 'OD2'], 
        'SER': ['CA', 'CB', 'OG'], 
        'GLN': ['OE1', 'CD', 'NE2'], 
        'LYS': ['CD', 'CE', 'NZ'], 
        'ILE': ['CG1', 'CB', 'CG2'], 
        'PRO': ['N', 'CA', 'CB'], 
        'THR': ['OG1', 'CB', 'CG2'], 
        'PHE': ['CD1', 'CG', 'CD2'], 
        'ALA': ['N', 'CA', 'CB'], 
        'GLY': ['N', 'CA', 'C'], 
        'HIS': ['CD2', 'CG', 'ND1'], 
        'GLU': ['OE1', 'CD', 'OE2'], 
        'LEU': ['CD1', 'CG', 'CD2'], 
        'ARG': ['NH1', 'CZ', 'NH2'], 
        'TRP': ['CD1', 'CG', 'CD2'], 
        'VAL': ['CG1', 'CB', 'CG2'], 
        'ASN': ['OD1', 'CG', 'ND2'], 
        'TYR': ['CD1', 'CG', 'CD2'], 
        'MET': ['CG', 'SD', 'CE']
        }
        return 0

    def get_dimer(self,):
        ## path:Helloword/tool ##
        path = os.getcwd()
        print path
        flag = os.system("vmd -dispdev -eof <./tool/data.tcl")
        if flag == 0:
            print "Done get dimer!"
        return 0
       

