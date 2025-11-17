#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None, **kwargs):
        self._name = None
        self._job = None
        if name is not None:
            self.name = name
        elif 'name' in kwargs:
            self.name = kwargs['name']
        if job is not None:
            self.job = job
        elif 'job' in kwargs:
            self.job = kwargs['job']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
            self._name = new_name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, new_job):
        if new_job in APPROVED_JOBS:
            self._job = new_job
        else:
            print("Job must be in list of approved jobs.")
