# Employee Manager Application

Esse repositório baseia-se em https://github.com/rodrigoclira/employee-manager-app-v1 . Na versão v2 do repositório foi adicionado uma aplicação de frontend para acessar a API disponibilizada com DRF. Sendo assim, duas aplicações são inicializadas em _containers_ docker.

Ambas aplicações são levantadas usando o comando abaixo
```
sudo docker-compose up --build
```


![image](https://user-images.githubusercontent.com/276077/174942615-b4e7e945-2d89-4c23-836e-9ab8931b5ed3.png)

A aplicação de frontend fica disponível na porta 8000

![image](https://user-images.githubusercontent.com/276077/174942679-b3aa5eaa-ab51-4c51-aa21-36f55fb13a49.png)

Ela se comunica com a aplicação de backend que está disponível na porta 8001

![image](https://user-images.githubusercontent.com/276077/174942952-37e7e1f6-75b8-4db0-ba93-87933617a63e.png)


No frontend apenas o endpoint GET /employee e o GET /employee/ID estão sendo utilizados. Como é exibido na views.py da aplicação de frontend
![image](https://user-images.githubusercontent.com/276077/174943242-8d6cd8ff-691f-45bb-846e-0e029004bc00.png)


# Atividade

1. Como exibido na imagem do arquivo views.py, não há nenhuma estratégia de cache na view do frontend. 
Use o memcached (como exibido no exemplo de aula) para adicionar uma estratégia de cache nas funções 'views.usuarios' e 'views.detalhes'. 
Utilize o 'json' obtido da API para ser a informação salva no cache. 




## Referência
https://medium.com/@nutanbhogendrasharma/consume-rest-api-in-django-web-application-130c0daa6f70

