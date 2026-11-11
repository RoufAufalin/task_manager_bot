import database

def test_show_tasks(test_db):
    task_id = database.add_task("Belajar Python")
    result = database.show_tasks()
    
    assert len(result) == 1
    assert result[0][0] == task_id
    assert result[0][1] == "Belajar Python"
    assert result[0][2] == 0

def test_show_tasks_empty(test_db):
    result = database.show_tasks()
    
    assert result == []