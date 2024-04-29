
# Rodando o projeto


- git clone https://github.com/mouraribeiro/e-sus-segunda-versao.git


## Via Docker
docker-compose -f docker-compose.yml up --build

## Endpoints
Todos os dados:
- http://localhost:8001/api/v2/atendimentos
#### Exemplos de filtros:
- http://localhost:8001/api/v2/atendimentos?data_atendimento=2023-07-26
- http://localhost:8001/api/v2/atendimentos?condicao_saude=hipertensao&data_atendimento=2023-07-26
