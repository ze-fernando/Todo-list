# Todo-list Django Rest Framework
## Environment Setup

### 1. Clone the repository:
```bash
git clone https://github.com/ze-fernando/SimplePayment-API

cd SimplePayment-API
```

### 2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Routes (Examples)

### 1. localhost:8000/user/register
```json
{
    "username": "zeca",
    "password": "abobrinha",
    "age": 27,
    "tel": 73981828384
}
``` 
the API return status 201 and:
```json
{
    "username": "zeca",
    "password": "abobrinha",
    "age": 27,
    "tel": 73981828384
}
```

### 2. localhost:8000/user/login
```json
{
    "username": "zeca",
    "password": "abobrinha"
}
```
the API returns:
```json
{
    "token": "JWT_TOKEN_HERE"
}
```

### 3. localhost:8000/task

In method GET api returns:

```json
[
    {
        "id": 1,
        "name": "estudar pydantic",
        "done": true,
        "created_at": "2024-03-15",
        "user_id": 1
    },
    {
        "id": 2,
        "name": "estudar dataclass",
        "done": false,
        "created_at": "2024-03-16",
        "user_id": 1
    }
]
```

In POST you send:
```json
{
    "name": "estudar kivymd",
    "done": false,
    "user_id": 1
}
```
 
### 4. localhost:8000/task/2

In method **GET** api return:

```json
{
    "id": 2,
    "name": "estudar dataclass",
    "done": false,
    "created_at": "2024-03-16",
    "user_id": 1
}
```
In method **PUT** you send:
```json
{
    "name": "estudar dataclass",
    "done": true,
    "user_id": 1
}
```
and API return:
```json
{
    "id": 2,
    "name": "estudar dataclass",
    "done": true,
    "created_at": "2024-03-16",
    "user_id": 1
}
```
In method **DELETE** API no retuns None

