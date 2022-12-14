
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
        print('  --e06: eserctiazione E06 - Trasformate di Fourier')
        print('  --e08: eserctiazione E08 - Monte Carlo Markov Chain')
        print('  --e09: eserctiazione E09 - Moduli e Classi')

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


    if args[0] == '--e06':
        
        remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/trasformate_fourier/SN_m_tot_V2.0.csv'
        remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/trasformate_fourier/data_sample1.csv'
        remote_file3 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/trasformate_fourier/data_sample2.csv'
        remote_file4 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/trasformate_fourier/data_sample3.csv'
        remote_file5 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/trasformate_fourier/copernicus_PG_selected.csv'

        
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file3))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file4))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file5))

            
        return 

    
    if args[0] == '--e08':
        
        remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/mcmc/absorption_line.csv'
        
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))

        return 



    if args[0] == '--e09':
        
        remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/classi/hit_times_M0.csv'
        remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/classi/hit_times_M1.csv'
        remote_file3 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/classi/hit_times_M2.csv'
        remote_file4 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica/main/dati/classi/hit_times_M3.csv'
        
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file3))
        os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file4))

        return 








if __name__ == "__main__":
        
    get_data(sys.argv[1:])
