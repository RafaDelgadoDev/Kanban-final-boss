import json
from src.app import app, tasks

def test_create_task(client):
    # start with empty tasks
    tasks.clear()
    response = client.post('/tasks', json={'title':'Test task','description':'desc'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test task'
    assert 'id' in data

def test_get_task(client):
    tasks.clear()
    resp = client.post('/tasks', json={'title':'Get me'})
    task = resp.get_json()
    resp2 = client.get(f"/tasks/{task['id']}")
    assert resp2.status_code == 200
    assert resp2.get_json()['title'] == 'Get me'

def test_update_task(client):
    tasks.clear()
    resp = client.post('/tasks', json={'title':'To update'})
    task = resp.get_json()
    resp2 = client.put(f"/tasks/{task['id']}", json={'title':'Updated','status':'done'})
    assert resp2.status_code == 200
    assert resp2.get_json()['title'] == 'Updated'
    assert resp2.get_json()['status'] == 'done'

def test_delete_task(client):
    tasks.clear()
    resp = client.post('/tasks', json={'title':'To delete'})
    task = resp.get_json()
    resp2 = client.delete(f"/tasks/{task['id']}")
    assert resp2.status_code == 204
    # now not found
    resp3 = client.get(f"/tasks/{task['id']}")
    assert resp3.status_code == 404

# test client fixture
import pytest
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c
