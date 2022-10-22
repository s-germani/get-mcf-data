
import sys,os
import shutil


def get_data(args):


    if len(args) == 0 :
        
        print('\nE\' necessario fornire almeno una opzione!\n')
        print('uso: python(3)  get_data.py opt [outdir]')
        print('  per informazioni sulle opzioni disponibili: python(3) get_data.py --help')

        return

    outdir = './'
    doMove = False
    if len(args) == 2:
        outdir = args[1]
        doMove = True
        print(' I file verranno copiati nella cartella', outdir)

    
        
    #print(f"Arguments count: {len(args)}")
    #for i, arg in enumerate(args):
    #    print(f"Argument {i:>6}: {arg}")

    if args[0] == '--help':
        print('get_data.py - scarica automaticamente i dati per le esrcitazioni del corso\n di Metodi Computazionali per la Fisica\n')
        print('uso: python(3)  get_data.py opt [outdir]')
        print('opzioni disponibili:')
        print('  --help: mostra questo help')
        print('  --e03: eserctiazione E03 - Integrazione e Derivazione')
        print('  --e04: eserctiazione E04 - Integrazione  + Minimizzazione')

        return

    
    if args[0] == '--e03':
        
        remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/integrazione_derivazione/vel_vs_time.csv'
        remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/integrazione_derivazione/oscilloscope.csv'
        
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
            
        return 

    if args[0] == '--e04':
        
        remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/integrazione_derivazione/vel_vs_time.csv'
        remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/equazioni_minimizzazione/fit_data.csv'
        
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
            
        return 

    








if __name__ == "__main__":
        
    get_data(sys.argv[1:])
