# Mask
MASK, a project to control covid-19 and reduce deaths and diseases caused by it.

## 0. Introduction

Mask has 3 type of accounts: ***Admin*** - ***General user*** - ***Business owner***.

These three types of people try to help reduce the disease in the whole society by following a series of policies.

## 1. Installation

### Download requirements
```bash
git clone https://github.com/mhnasajpour/Mask.git
cd Mask

pip install virtualenv
python -m virtualenv venv
```

### Activate environment
#### Windows
```bash
venv\Scripts\activate
```
#### Linux
```bash
chmod +x ./venv/bin/activate
./venv/bin/activate
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Copy environment secrets
#### Windows
```
xcopy backend\config\sample.env backend\config\.env
```
#### Linux
```
cp backend/config/sample.env backend/config/.env
```

### Configuration
Go to `backend > config > .env` and edit the requested fields.

### Start the server
```
cd backend
python manage.py migrate
python manage.py runserver
```
You can now visit the website by going to the url you provided.

## 2. APIs
To see the list of APIs, you can refer to URL http://YOUR_PROVIDED_URL/swagger/

### Swagger images
![AUTH](https://github.com/mhnasajpour/Mask/blob/main/APIs/Auth_APIs.png)
![USER](https://github.com/mhnasajpour/Mask/blob/main/APIs/User_APIs.png)
![PLACE](https://github.com/mhnasajpour/Mask/blob/main/APIs/Place_APIs.png)
![HOSPITAL](https://github.com/mhnasajpour/Mask/blob/main/APIs/Hospital_APIs.png)
![MANAGER](https://github.com/mhnasajpour/Mask/blob/main/APIs/Manager_APIs.png)