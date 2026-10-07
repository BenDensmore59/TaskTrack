from tasktrack import remove_task_by_number

def test_remove_first_task():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Study"

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Exercise", "Read"]

def test_remove_middle_task():
    """Removing task 2 should remove the middle task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Exercise"

    # Act
    removed_task = remove_task_by_number(tasks, 2)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Read"]

def test_remove_last_task():
    """Removing task 3 should remove the last task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Read"

    # Act
    removed_task = remove_task_by_number(tasks, 3)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Exercise"]

def test_reject_zero_task():
    """Removing task 0 should be rejected."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = None

    # Act
    removed_task = remove_task_by_number(tasks, 0)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Exercise", "Read"]
    
def test_reject_greater_than_length_task():
    """Removing a task number greater than the length of the list should be rejected."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = None

    # Act
    removed_task = remove_task_by_number(tasks, 4)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Exercise", "Read"]

def test_reject_negative_task():
    """Removing a negative task number should be rejected."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = None

    # Act
    removed_task = remove_task_by_number(tasks, -1)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Exercise", "Read"]

