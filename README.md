All the Five services Postgres, Web, Celery Worker, Celery Beat and Redis are containerized.

1. Run "docker-compose build".
2. Run "docker-compose up".
3. After your services are up you will have to run migrations, so run the command "docker exec -it app_web_1 python manage.py migrate".

<b> Register API's </b>
  1. Writer Register API,
      Endpoint: <b>api/v1/register/writer/</b>
      payload: {
      
      "email": "test@test.com",
      "password": "testing", 
      "first_name": "test",#Optional
      "last_name": "test"#Optional
      
      }
      
  2. Editor Register API,<br>
      Endpoint: <b>api/v1/register/editor/</b>
      method: POST<br>
      payload: {<br>
      <br>
      "email": "test@test.com",<br>
      "password": "testing", <br>
      "first_name": "test",#Optional<br>
      "last_name": "test"#Optional<br>
      <br><br>
      }<br>
5. Get Token API, (I have used JWT token authentication)<br>
      method: POST<br>
      Endpoint : <b>api/v1/auth/token/obtain/</b><br>
      payload : {<br>
      "email": "test@test.com",<br>
      "password": "testing"<br>
      }<br>

6. Article API,<br>
    method: POST<br>
    endpoint: api/v1/publication/article/<br>
    Headers: {"Authorization": "JWT {JWT_TOKEN}"}<br>
    payload: {"name": "Coronavirus Pandemic", "status": "in_progress", "google_doc_link": "www.test.com"} # status and google doc link are optional
    <br><br>
    
    method: Patch <br>
    payload: <i> Any Field on Article Model</i><br>
<br><br>

The cronjob will run every five seconds and chec fo open articles with google doc link and mark them in review.
