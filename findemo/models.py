from django.db import models

# Create your models here.

class Employee_Data(models.Model):
    
    MALE = "M"
    FEMALE ="F"
    GENDER_TYPE = (
        (MALE, "male"),
        (FEMALE, "female"),
    )

    emp_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    birth_date = models.DateField()
    hire_date = models.DateField()
    gender = models.CharField(choices=GENDER_TYPE,max_length=5,default=MALE)

    class Meta:
        db_table = 'EMPLOYEES'
        
    def __str__(self):
        return self.first_name

class Departments(models.Model):
    dept_no = models.CharField(max_length=4,  primary_key=True)
    dept_name = models.CharField(max_length=40, unique=True)
    
    class Meta:
        db_table = 'DEPARTMENTS'
    
    def __str__(self):
        return self.dept_name

class Dept_Manager(models.Model):
    emp_no = models.ForeignKey(Employee_Data, on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Departments, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    
    class Meta:
        unique_together = (("emp_no", "dept_no"),)
        db_table = 'DEPT_MANAGER'

class Dept_emp(models.Model):
    emp_no = models.ForeignKey(Employee_Data, on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Departments, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    class Meta:
        unique_together = (("emp_no", "dept_no"),)
        db_table = 'DEPT_EMP'

class Titles(models.Model):
    emp_no = models.ForeignKey(Employee_Data, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    class Meta:
        unique_together = (("emp_no", "title","from_date"),)
        db_table = 'TITLES'
        

class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee_Data, on_delete=models.CASCADE)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    class Meta:
        unique_together = (("emp_no", "from_date"),)
        db_table = 'SALARIES'
