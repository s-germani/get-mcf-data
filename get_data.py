
import sys,os
import shutil
import argparse


def parse_arguments():


    parser = argparse.ArgumentParser(description='Scarica i dati per le esercitazioni del corso di Metodi Computazionali per la Fisica (UniPG).')
    parser.add_argument('--year',          action="store",      required=True,  help='Anno di corso (2022,2023)')
    parser.add_argument('--exn',           action="store",      required=True,  help='Numero Esercitazione')
    parser.add_argument('--outdir',        action="store",      default='./',   help='Cartella di destinazione')
    
    return parser.parse_args()



def get_data():


    args = parse_arguments()
    

    outdir = args.outdir 
    doMove = False
    if outdir != './':
        doMove = True
        print(' I file verranno copiati nella cartella', outdir)

    
    ##################################### 2022 #####################################################à
    if args.year == 2022:
        
        if args.exn == 3:
        
            remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/integrazione_derivazione/vel_vs_time.csv'
            remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/integrazione_derivazione/oscilloscope.csv'
        
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
            
            return 

        if args.exn == 4:
        
            remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/integrazione_derivazione/vel_vs_time.csv'
            remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/equazioni_minimizzazione/fit_data.csv'
        
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
            
            return 


        if args.exn == 6:
        
            remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/trasformate_fourier/SN_m_tot_V2.0.csv'
            remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/trasformate_fourier/data_sample1.csv'
            remote_file3 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/trasformate_fourier/data_sample2.csv'
            remote_file4 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/trasformate_fourier/data_sample3.csv'
            remote_file5 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/trasformate_fourier/copernicus_PG_selected.csv'

        
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file3))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file4))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file5))

            
            return 

    
        if args.exn == 8:
        
            remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/mcmc/absorption_line.csv'
        
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))

            return 



        if args.exn == 9:
        
            remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/classi/hit_times_M0.csv'
            remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/classi/hit_times_M1.csv'
            remote_file3 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/classi/hit_times_M2.csv'
            remote_file4 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2022/main/dati/classi/hit_times_M3.csv'
        
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file3))
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file4))

            return



        ##################################### 2023 #####################################################à
        elif args.year == 2023:

            
            if args.exn == 5:
        
                remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2023/main/dati/classi/hit_times_M0.csv'
                remote_file2 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2023/main/dati/classi/hit_times_M1.csv'
                remote_file3 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2023/main/dati/classi/hit_times_M2.csv'
                remote_file4 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2023/main/dati/classi/hit_times_M3.csv'
        
                os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
                os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file2))
                os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file3))
                os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file4))

                return


            if args.exn == 6:
        
                remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2023/main/dati/integrazione_derivazione/vel_vs_time.csv'
                
                os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
            
            return 


        if args.exn == 7:
        
            remote_file1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2023/main/dati/equazioni_minimizzazione/fit_data.csv'
        
            os.system('wget --directory-prefix {:}  {:}'.format(outdir, remote_file1))
            
            return 





if __name__ == "__main__":
        
    get_data()
