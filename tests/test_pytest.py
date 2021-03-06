import myapp
import pytest

@pytest.fixture
def client():
    myapp.app.config['TESTING'] = True
    client = myapp.app.test_client()
    yield client
	
def test_mainmenu(client):
	response = client.get('/')
	assert response.status_code == 200
	assert b'Survey Results' in response.data

def test_agenda(client):
	response = client.get('/agenda', follow_redirects=True)
	assert b'DevOps demystified' in response.data
	assert b'Login' not in response.data	
	assert response.status_code == 200

def test_survey(client):
	response = client.get('/survey', follow_redirects=True)
	assert response.status_code == 200
	assert b'EVENT SURVEY' in response.data
	assert b'Division' in response.data
	assert b'State' in response.data
	assert b'SUBMIT' in response.data

def test_create_survey(client):
	response = client.post('/suthankyou.html', data=dict(
		division='Enterprise',
		state='NSW',
		feedback='Facemeltingly Awesome'
	), follow_redirects=True)
	assert response.status_code == 200
	assert b'THANKS FOR TAKING THE SURVEY' in response.data
	
def test_survey_dump(client):
	response = client.get('/dumpsurveys', follow_redirects=True)
	assert response.status_code == 200
	assert b'Division : Enterprise' in response.data
	assert b'State    : NSW' in response.data
	assert b'Feedback : Facemeltingly Awesome' in response.data
	
