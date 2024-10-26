from django.db import models

class Rule(models.Model):
    rule_id = models.CharField(max_length=50, unique=True)
    rule_string = models.TextField()

    def __str__(self):
        return self.rule_id
