## importar bibliotecas e pacotes

import pandas as pd
import os
import glob

# caminho para ler os arquivos
folder_path = 'src\\data\\raw'

# listar todos os arquivos excel utilizando o glob e os path.join
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files: 
    print("Nenhum arquivo excel encontado")
else:

#dataframe = tabela na memoria para guardar os conteudos dos arquivos
    dfs = []

for excel_file in excel_files:

    try:
        #leio arquivo de excel 
        df_temp = pd.read_excel(excel_file)

        #pegar o nome do arquivo
        file_name = os.path.basename(excel_file)

        df_temp['filename'] = file_name
        
        #criamos uma nova coluna chamada country
        if 'brasil' in file_name.lower():
            df_temp ['Country'] = 'BR'

        elif 'france' in file_name.lower():
            df_temp ['Country'] = 'FR'
            
        elif 'italian' in file_name.lower():
            df_temp ['Country'] = 'IT'     

        
        #criamos uma nova coluna chamada campaign utilizando a função str.extract regex
            
        df_temp ['Campign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

        #guarda dados dentro de um dataframe comum, no caso o primeiro que criamos no incio do código
        dfs.append(df_temp)

        if dfs: 
            #concatena todas as tabelas salvas no dfs em uma unica tabela.
            result = pd.concat(dfs, ignore_index=True)
            # caminho de saída
            output_file = os.path.join('src', 'data', 'ready', 'clean_data.xlsx')

            #configuração do motor de escrita
            writer = pd.ExcelWriter(output_file, engine='xlsxwriter') 

            # leva o resultado dos dados a serem escritos no motor de excel configurado
            result.to_excel(writer, index=False)

            # salva o arquivo de excel
            writer._save()

        else: 
            print('Nenhum dado para ser salvo')
                    
    except Exception as e:
        print(f"Erro ao ler o arquivo {excel_file} : {e}")







