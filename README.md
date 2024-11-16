# PROJETO CALCULADORA
O projeto contém um front-end em Angular e um back-end em Python (Django). 
Ao acessar a tela de login e inserir as credenciais, o usuário será redirecionado para a calculadora, 
onde poderá realizar a operação de calcular a soma de dois números. No entanto, 
será possível calcular apenas uma operação por vez.


## FERRAMENTAS
- Python: 3.12.6-slim
- Angular(node): 22.11.0
- Banco de dados: SqLite
- Docker
- Windows

## TESTES
- Entre na pasta raiz do projeto onde esta localizado o docker-compose.yml
- Use o comando no terminal para criar os containers: docker-compose up -d
- Use o comando e crie um user name e password: docker exec -it calculadora python manage.py createsuperuser
- Crie uma pasta chamada calculadora-frontEnd e clone o projeto dentro: https://github.com/GustavoMatos13/angular-project.git
- Dentro do projeto rode os comandos not terminal: docker build -t angular-docker .
- Em seguida: docker run -p 4200:4200 angular-docker 
- Na raiz do projeto rode o comando na: docker-compose up -d
- Acesse http://localhost:4200/login e acesse com o username e password criados no back end do python pelo terminal