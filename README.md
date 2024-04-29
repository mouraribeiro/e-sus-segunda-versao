
# Rodando o projeto


- git clone https://github.com/mouraribeiro/e-sus-segunda-versao.git


## Via Docker
docker-compose up


## Endpoints
Todos os dados:
- http://127.0.0.1:5000/api/v2/atendimentos
#### Exemplos de filtros:
- http://127.0.0.1:5000/api/v2/atendimentos?data_atendimento=2023-07-26
- http://127.0.0.1:5000/api/v2/atendimentos?condicao_saude=hipertensao&data_atendimento=2023-07-26
