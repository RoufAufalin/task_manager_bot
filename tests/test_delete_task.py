import database

def test_delete(test_db):
    task_id = database.add_task("Belajar Python")
    result = database.delete_task(task_id)
    
    assert result is True
    assert database.show_tasks() == []
    
def test_delete_nonexistent_task(test_db):
    result = database.delete_task(999)

    assert result is False