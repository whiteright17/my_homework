class Worker:
    def __init__(self, name, job_title, salary, employee_id):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        self.employee_id = employee_id

    def get_info(self):
        info = f"Name: {self.name}\n"
        info += f"Job Title: {self.job_title}\n"
        info += f"Salary: ${self.salary}\n"
        info += f"Employee ID: {self.employee_id}"
        return info
    def calculate_annual_salary(self):
        return self.salary * 12

worker1 = Worker(
    name="Vadym Andriienko",
    job_title="Quality Assurance",
    salary=123000,
    employee_id="EMP0604"
)
annual_salary = worker1.calculate_annual_salary()

print(worker1.get_info())
print(f"Annual Salary: ${annual_salary}")
