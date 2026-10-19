class Task:
    def __init__(self, title, assigned_to):
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

    def complete_task(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} - {self.status}"