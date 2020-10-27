from init import *

def print_as_df(step = 7, fromfile = False):
        '''
        Breaks up the DNA sequence into 7 character chunks and
        adds to a dict to process into a dataframe
        
        :param step: String to set each sequence length
        :param fromfile: Boolean to check if our data is coming from a file
        '''
        dna = DNATranslator('ATTTCCCAGCGTTATTTCCCGGG') if not fromfile else DNATranslator.dna_from_file(os.path.join(fromfile))
        # dna string data
        data = {}
        dna_data, reverse_data, complement_data, reverse_complement_data = [], [], [], []
        
        # go through the loop and add to each indivudal list 
        # then append to a dictionary
        for i in range(0, len(dna.info) + 1, step):
                seq = dna.info[i : i + step]
                dna_data.append(seq)
                reverse_data.append(dna.reverse(seq))
                complement_data.append(dna.complement(seq))
                reverse_complement_data.append(dna.reverse_complement(seq))
                
        data = {
                'Sequence' : dna_data, 
                'Reverse' : reverse_data, 
                'Complement' : complement_data, 
                'Reverse-Complement' : reverse_complement_data
        }
                
        df = pd.DataFrame(data)
        df.set_index('Sequence', inplace = True)
        print(df)
                
def main():
        print('''
        ---------------------
        1. Show Data
        2. Exit
        ---------------------
        
        ''')
        choice = input('>')
        try:
                programs = {'1' : print_as_df, '2' : sys.exit}
                # run a class method based off the number the user inputs
                programs[choice]()
        # 
        except KeyError as e:
                print(f'{e}: Not a valid choice')
                

if __name__ == '__main__':
    main()
