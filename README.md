# biblioteka_api 
This is V1 from biblioteka_api that was made with the collaboration of Lucas Magalhes and Daniel Delos Silva, we created using Python/Django an API that could help library staff to register new books and their copies in the system, and to manage loans and develutions with ease. 
From the user side we have the authenticated where the users can follow their prefered books and to maintain a control of which books they have loaned or they are following.
From the non authenticated users they can only consult specific books and or the full book archive from the library.

There's a function that periodicaly verify the database to see if there's any user that are late or bound to be late with a book devolution, and send an email till they regularize their situation.

It's a very scalable api that can be used as base for more complex aplication.


To Make use:
<br>
1. Set a virtual environment
```bash
python -m venv venv
```

2. Activate it:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Install the Dependencies
```
pip install -r requirements.txt
```

4. Run your server.

Extra: After Running the server u can make use of the documentation made by the drf-spetacular extension.
REDOC: localhost:8000/api/schema/redoc/
SWAGGER UI: localhost:8000/api/schema/swagger-ui/

Hope u have a wonderful day!
