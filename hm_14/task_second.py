class Worker:
    def custom_human(self, name, job_title, salary, employee_id):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        self.employee_id = employee_id
        self.spouse = None

    def set_wife(self, spouse_name):
        self.spouse = spouse_name

    def get_info(self):
        info = f"Name: {self.name}\n"
        info += f"Job Title: {self.job_title}\n"
        info += f"Salary: ${self.salary}\n"
        info += f"Employee ID: {self.employee_id}"
        return info

    def family(self):
        if self.spouse:
            return f"Spouse: {self.spouse}"
        else:
            return "Single"

    def calculate_annual_salary(self):
        return self.salary * 12

worker1 = Worker()
worker1.custom_human(
    name="Vadym Andriienko",
    job_title="Quality Assurance",
    salary=123000,
    employee_id="EMP0604"
)

worker1.set_wife("Test Andriienko")

print(worker1.get_info())
print(worker1.family())
