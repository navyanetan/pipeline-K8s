from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from Python Flask App on Kubernetes!" in response.data 

def test_aboutme():
    tester = app.test_client()
    response = tester.get('/aboutme')
    assert response.status_code == 200
    assert b"My name is Navya. I am deploying these apps on K8s using github actions!" in response.data