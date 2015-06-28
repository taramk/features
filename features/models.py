from django.db import models
from django import forms
from django.forms import ModelForm, EmailField


class Customer(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Feature(models.Model):
    jira_id = models.IntegerField(null=True, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    customers = models.ManyToManyField(Customer, related_name="features")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    feature = models.ForeignKey(Feature)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    commenter = models.CharField(max_length=50)


class FeatureForm(ModelForm):
    customer_email = EmailField(required=False)

    class Meta:
        model = Feature
        fields = ["jira_id", "title", "description"]


class AddCustomerForm(forms.Form):
    customer_email = EmailField()


class DeleteFeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = []


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["commenter", "text"]