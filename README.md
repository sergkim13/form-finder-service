# Form-finder-servce


### Description:
Web service which allows to define form template according to request's data. If compatible form found service returns it's name. Otherwise tit returns a dictionary with request's field names and FIELD_TYPEs (date, phone, email or text).


Example of form:
```
{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}
```

Example of reqest data:
```
f_name1=value1&f_name2=value2
```

Example of response if form template found:
```
Form template name
```
Example of response if form template not found:
```
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
}
```

Made with:
- FastAPI,
- MongoDB (motor library),
- Docker.

### Requirements:
1. MacOS (prefer) / Linux / Windows10
2. `Docker`
3. `Make` utily for MacOS, Linux.

### Install:
1. Clone repository: https://github.com/sergkim13/form-finder-service
2. Type `make compose` (or `docker compose up -d`) for running application in docker container. App will be running at http://0.0.0.0:8000.   
For running test script type `python3 script.py` in project directory, but you need to install requirements and activate virtual environment before that.  
Also you can run script in running container by typing: `docker exec forms_app sh -c 'python3 -m script'`.
Type `make stop` (or `docker compose down`) to stop app container.  
3. Type `make compose-test` (or `docker compose -f docker-compose.test.yaml -p testing run --rm test_app`) for running tests in docker container. Type `make stop-test` (or `docker compose -f docker-compose.test.yaml -p testing down`) to stop app container.

### Demo test script:
[![asciicast](https://asciinema.org/a/O4HfljTjZUdY8UlUm5G0ny8dz.svg)](https://asciinema.org/a/O4HfljTjZUdY8UlUm5G0ny8dz)

### Demo tests:
[![asciicast](https://asciinema.org/a/D4DT2PAFSwIAP7ZMZ3hX90Mv4.svg)](https://asciinema.org/a/D4DT2PAFSwIAP7ZMZ3hX90Mv4)
