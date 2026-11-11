import database

def test_add_task(test_db):
    task_id = database.add_task("Belajar Python")
    
    assert isinstance(task_id, int)
    
    tasks = database.show_tasks()
    
    assert len(tasks) == 1
    assert tasks[0][1] == "Belajar Python"
    assert tasks[0][2] == 0