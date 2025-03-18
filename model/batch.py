# Class Batch
from datetime import date
from typing import List
from model.trainee import Trainee # Custom import

class Batch:
    def __init__(
        self,
        batch_id: str,
        start_date: date,
        end_date: date,
        training_program: str,
    ):
        self._batch_id = batch_id
        self._start_date = start_date
        self._end_date = end_date
        self._training_program = training_program
        self._trainees: List[Trainee] = []

        if start_date >= end_date:
            raise ValueError("Start date must be before the end date.")
        
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        if not value.strip():
            raise ValueError("Batch ID cannot be empty.")
        self._batch_id = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if value >= self._end_date:
            raise ValueError("Start date must be before the end date.")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if value <= self._start_date:
            raise ValueError("End date must be after the start date.")
        self._end_date = value

    @property
    def training_program(self):
        return self._training_program

    @training_program.setter
    def training_program(self, value):
        self._training_program = value

    @property
    def trainees(self):
        return self._trainees

    def add_trainee(self, trainee: Trainee):
        self._trainees.append(trainee)
