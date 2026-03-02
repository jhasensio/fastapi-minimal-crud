import requests

BASE_URL = "http://localhost:8000/api/tasks"

def test_api_lifecycle():
    print("🚀 Starting API Integration Test...")

    # 1. POST: Create a new task
    new_task = {"title": "Test my new API", "completed": False}
    response = requests.post(BASE_URL, json=new_task)
    assert response.status_code == 201
    task = response.json()
    task_id = task["task_id"]
    print(f"✅ Created Task ID: {task_id}")

    # 2. GET: Verify task exists in the list
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert any(t["task_id"] == task_id for t in response.json())
    print(f"✅ Verified Task {task_id} exists in GET /tasks")

    # 3. PUT: Update the task
    updated_data = {"title": "Test my new API (Updated)", "completed": True}
    response = requests.put(f"{BASE_URL}/{task_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["completed"] is True
    print(f"✅ Updated Task {task_id} to 'completed'")

    # 4. DELETE: Remove the task
    response = requests.delete(f"{BASE_URL}/{task_id}")
    assert response.status_code == 200
    print(f"✅ Deleted Task {task_id}")

    # 5. Final Check: Ensure it's gone
    response = requests.get(BASE_URL)
    assert not any(t["task_id"] == task_id for t in response.json())
    print("✅ Verified Task removal. Test Passed! 🎉")

if __name__ == "__main__":
    try:
        test_api_lifecycle()
    except Exception as e:
        print(f"❌ Test Failed: {e}")
