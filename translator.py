from init import *

class DNATranslator:
        def __init__(self, info):
                '''
                Constructor for the DNATranslator class. It will originally take DNA string data.
                To parse file contents, use the class method constructor
                
                :param info: By default, a DNA text string we are using to provide the other info
                
                '''
                self.info = info
                
        @classmethod
        def dna_from_file(self, file_name):
                '''
                Alternative constructor to take an experimental string as DNA data
                
                :param file_name: Filename where the dna information resides
                '''
                with open(os.path.join(file_name), 'r') as f:
                        contents = f.read()
                        info = contents.strip()
                        
                return cls(info)
        
        def torna(self):
                ''' All the dna needs to be translated to RNA first '''
                return self.info.replace('T', 'U')

        def reverse(self, sequence):
                return sequence[::-1]

        def complement(self, sequence):
                '''
                Takes a dictionary map of base pair complements and assigns the complement to each
                character in the sequence

                :param sequence: Sequence string
                '''

                bases = {'A' : 'T', 'G': 'C' , 'T' : 'A', 'C' : 'G'}
                complement_sequence = ''.join([bases[s] for s in sequence])
                                              
                return complement_sequence
                
        def reverse_complement(self, sequence):
                '''
                Takes a dictionary map of base pair complements and assigns the complement to each
                character in the sequence, then reverses.

                :param sequence: Sequence string
                '''

                bases = {'A' : 'T', 'G': 'C' , 'T' : 'A', 'C' : 'G'}
                complement_sequence = ''.join([bases[s] for s in sequence])
                                              
                return complement_sequence[::-1]


