import database

def test_complete_task(test_db):
    task_id = database.add_task("Belajar Python")
    result = database.complete_task(task_id)
    
    tasks = database.show_tasks()
    
    #memeriksa apakah data sudah diubah
    assert result is True
    
    #memeriksa apakah data sudah ditambahkan
    assert tasks[0][0] == task_id
    
    #memeriksa apakah task status sudah berubah
    assert tasks[0][2] == 1

def test_complete_nonexistent_task(test_db):
    result = database.complete_task(999)

    assert result is False
    