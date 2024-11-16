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
- Dentro da pasta chamada calculadora-frontEnd clone o repositório: https://github.com/GustavoMatos13/angular-project.git
- Entre no diretorio e crie um user name e password: docker exec -it calculadora python manage.py createsuperuser
- Ainda na pasta do front crie uma imagem: docker build -t angular-docker .
- Em seguida, rode a imagem e crie um host: docker run -p 4200:4200 angular-docker 
- Na raiz do projeto principal rode o comando pra criar uma imagem e host do back-end: docker-compose up -d
- Acesse http://localhost:4200/app/login e entre com o username e password criados no back end do python pelo terminal