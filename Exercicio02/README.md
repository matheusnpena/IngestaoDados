# IngestaoDados

Inserção, tratamento e visualização de dados de arquivos CSV e chamada de API através do uso de Python, MySQL e Tableau


FONTE DE DADOS:
####
Nome da Base de Dados: Ranking de Instituições por Índice de Reclamações
Formato: CSV
Periodo: Anos: 2020 e 2021, consolidado por Trimestre
###
Nome da Base de Dados: Tarifas Bancárias - por Segmento e por Instituição
Formato: Leitura via API Rest (request)
Entrada: CNPJs encontrados na base "Ranking de Instituições por Índice de Reclamações"

Ingestão de Dados com Python. 

Ferramentas utilizadas:
1° Extração dos dados: Python
2° Load: MySQL (local)
3° Transform: SQL
3° Visualização: Tableau 

Cria-se uma rotina Job que realiza os seguintes passos:
#1) Criacao do database
#2) Criar tabelas stage
#3) Insercao tabelas stage
#4) Criacao fato1 e dim
#5) Criacao fato2 e dim
#6) Insercao dados fato1 e fato2

Posterior a inseção dos dados em cada uma das tabelas fato, é realizada a construção das visualização no Tablau. Obtou-se pelo uso do Tableau pela facilidade de relacionamento entres as dimensões e fatos do star schema. 

A seguir exibe-se através do comando describe cada uma das tabelas criadas: 

1° Tabela Stage para armazenar os dados da base "Ranking de Instituições por Índice de Reclamações":
![image](https://user-images.githubusercontent.com/60858939/180095486-463d8b54-2316-4d32-aea5-65d1b50cc6ae.png)

2° Tabela Stage para armazenar os dados lidos da base "Tarifas Bancárias - por Segmento e por Instituição"
![image](https://user-images.githubusercontent.com/60858939/180095609-a6272f3a-c55d-4a6e-8bed-cf4f25d767f8.png)

3° Tabela fato1: quantida de reclamações por instituição:
![image](https://user-images.githubusercontent.com/60858939/180095749-97c7a937-7db0-4a5f-826c-ac4e41290f64.png)

3.1° Tabela Dimensão Categoria:
![image](https://user-images.githubusercontent.com/60858939/180095822-269c7458-ed17-4be5-928a-96490385104c.png)

3.2° Tabela Dimensão Instituição:
![image](https://user-images.githubusercontent.com/60858939/180095982-138db878-de1a-4a88-9eca-5662e22fe0a0.png)

3.3° Tabela Dimensão Periodo:
![image](https://user-images.githubusercontent.com/60858939/180096037-1be9a0f6-c21e-4e78-a9d1-53741ca8ce02.png)

3.3° Tabela Dimensão Tipo:
![image](https://user-images.githubusercontent.com/60858939/180096351-170f1111-9dde-4a09-91aa-3bb3debc45e9.png)

4° Tabela Fato2: quantidade de serviços pro instituição
![image](https://user-images.githubusercontent.com/60858939/180096471-82e81f15-3008-46ae-afe7-7d7a68e30db4.png)

4.1° Tabela Dimensão Serviço
![image](https://user-images.githubusercontent.com/60858939/180096546-648fb805-e5f9-4958-a446-1086f807d16d.png)





