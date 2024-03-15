## criar um ambiente virtual

python -m venv venv

## ativar ambiente

venv/scripts/activate

## Etapa do dado

data raw -  todos os Dados, antes de qualquer polimentos, na sua forma mais crua.

data ready -  quando o dado passou pelo processo de refinamento.

## Scripts

caso o projeto possua mais de um arquivo de scripts, criar pasta scripts na "src"(source) para separalos ajuda na organização.

## pacotes utilizados

pip install pandas
pip install openpyxl
pip intall xlsxwriter

## Regras de tratamento

Prezar pela confiabilidadade e rastreabilidade dos dados.

## gitignore (proteger os dados cru)

criar arquivo .gitignore dentro da src e indicar o caminho da pasta a ser protegida. 

