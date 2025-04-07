from django.db import models

class Customer(models.Model):
    customerID = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    SeniorCitizen = models.IntegerField()
    Partner = models.CharField(max_length=10)
    Dependents = models.CharField(max_length=10)
    tenure = models.IntegerField()
    PhoneService = models.CharField(max_length=10)
    MultipleLines = models.CharField(max_length=30)
    InternetService = models.CharField(max_length=30)
    OnlineSecurity = models.CharField(max_length=30)
    OnlineBackup = models.CharField(max_length=30)
    DeviceProtection = models.CharField(max_length=30)
    TechSupport = models.CharField(max_length=30)
    StreamingTV = models.CharField(max_length=30)
    StreamingMovies = models.CharField(max_length=30)
    Contract = models.CharField(max_length=30)
    PaperlessBilling = models.CharField(max_length=10)
    PaymentMethod = models.CharField(max_length=50)
    MonthlyCharges = models.FloatField()
    TotalCharges = models.CharField(max_length=20)
    Churn = models.CharField(max_length=10)

    def __str__(self):
        return self.customerID
