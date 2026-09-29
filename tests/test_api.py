from tests.conftest import register_and_login


def test_register_duplicate_email(client):
    body = {"email": "dup@example.com", "password": "password123"}
    assert client.post("/api/v1/auth/register", json=body).status_code == 201
    assert client.post("/api/v1/auth/register", json=body).status_code == 400


def test_register_rejects_short_password(client):
    r = client.post("/api/v1/auth/register", json={"email": "a@example.com", "password": "short"})
    assert r.status_code == 422


def test_login_wrong_password(client):
    register_and_login(client, "b@example.com")
    r = client.post("/api/v1/auth/login", json={"email": "b@example.com", "password": "wrongpass"})
    assert r.status_code == 401


def test_me_requires_auth(client):
    assert client.get("/api/v1/users/me").status_code == 401


def test_me_and_update(client):
    headers = register_and_login(client, "me@example.com")
    assert client.get("/api/v1/users/me", headers=headers).json()["email"] == "me@example.com"
    r = client.patch("/api/v1/users/me", json={"full_name": "Me Myself"}, headers=headers)
    assert r.status_code == 200
    assert r.json()["full_name"] == "Me Myself"


def test_task_crud(client):
    headers = register_and_login(client)
    r = client.post("/api/v1/tasks/", json={"title": "Write tests"}, headers=headers)
    assert r.status_code == 201
    task_id = r.json()["id"]
    assert r.json()["completed"] is False

    r = client.get("/api/v1/tasks/", headers=headers)
    assert [t["id"] for t in r.json()] == [task_id]

    r = client.patch(f"/api/v1/tasks/{task_id}", json={"completed": True}, headers=headers)
    assert r.status_code == 200
    assert r.json()["completed"] is True
    assert r.json()["title"] == "Write tests"

    assert client.get("/api/v1/tasks/?completed=false", headers=headers).json() == []

    assert client.delete(f"/api/v1/tasks/{task_id}", headers=headers).status_code == 204
    assert client.get(f"/api/v1/tasks/{task_id}", headers=headers).status_code == 404


def test_tasks_are_private_to_owner(client):
    alice = register_and_login(client, "alice@example.com")
    bob = register_and_login(client, "bob@example.com")
    task_id = client.post("/api/v1/tasks/", json={"title": "Alice only"}, headers=alice).json()["id"]

    assert client.get(f"/api/v1/tasks/{task_id}", headers=bob).status_code == 404
    assert client.patch(f"/api/v1/tasks/{task_id}", json={"title": "x"}, headers=bob).status_code == 404
    assert client.delete(f"/api/v1/tasks/{task_id}", headers=bob).status_code == 404
    assert client.get("/api/v1/tasks/", headers=bob).json() == []


def test_invalid_token_rejected(client):
    r = client.get("/api/v1/tasks/", headers={"Authorization": "Bearer not-a-token"})
    assert r.status_code == 401
