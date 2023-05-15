O Case contém dois desafios:

O Primeiro é referente ao processo de transformação digital da empresa, onde é proposto a criação de uma apresentação com a definição de uma estrutura robusta, em cloud.

A apresentação deve conter o seguintes requisitos:

• Permear as camadas de ingestão, processamento, armazenamento, consumo, análise, segurança e governança;
• Substituição gradativa do cenário on-premises atual;
• Incorporação de componentes e tecnologias que permitam a analisarmos dados em tempo real;
• Que a arquitetura considere componentes que a habilitem a empresa organizar e fornecer dados para diferentes fins, tais como: Analytics, DataScience, API’s e serviços para integrações com aplicações. 
• Ressaltando quenecessariamente precisaremos manter a comunicação on-premises x cloud para diversas finalidades. 

Muvem escolhida: GCP


O Segundo desafio consiste em carregar 3 arquivos xls com dados de vendas conforme os requisitos abaixo:

1. Realizar a importação dos dados dos 3 arquivos em uma tabela criada por você no banco de dados de sua escolha;
2. Com os dados importados, modelar 4 novas tabelas e implementar processos que façam as transformações necessárias e insiram as seguintes visões nas tabelas:
a. Tabela 1: Consolidado de vendas por ano e mês;
b. Tabela 2: Consolidado de vendas por marca e linha;
c. Tabela 3: Consolidado de vendas por marca, ano e mês;
d. Tabela 4: Consolidado de vendas por linha, ano e mês;  

O Segundo desafio parte dois é fazer um request de dados da API do spotify conforme os requisitos abaixo:

a. Tabela 5: name = Nome do poscast. 
description = Descrição sobre o programa de poscast.
id = Identificador único do programa. total_episodes = Total de episódios lançados até
o momento.
4. Realizar a extração de dados de todos os episódios lançados pelos Data Hackers
via requests e ingerir esse resultado em duas tabelas seguindo os critérios abaixo:
a. Tabela 6: Resultado de todos os episódios.
b. Tabela 7: Apenas com os resultados dos episódios com participação do Grupo
Boticário. 
Levar apenas os campos abaixo para as tabelas 6 e 7:
id - Identificação do episódio.
name - Nome do episódio.
description - Descrição do episódio.
release_date - Data de lançamento do episódio.
duration_ms - Duração em milissegundos do episódio.
language - Idioma do episódio.
explicit - Flag booleano se o episódio possui conteúdo explícito.
type - O tipo de faixa de áudio (Ex: música / programa)


