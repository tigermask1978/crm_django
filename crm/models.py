# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    '''客户信息表'''
    pass


class CustomerFollowUp(models.Model):
    '''客户跟进表'''
    pass


class Course(models.Model):
    '''课程表'''
    pass


class ClassList(models.Model):
    '''班级表'''
    pass


class CourseRecord(models.Model):
    '''上课记录'''
    pass


class StudyRecord(models.Model):
    '''学习记录'''
    pass

class Enrollment(models.Model):
    '''报名表'''
    pass


class UerProfile(models.Model):
    '''账号表'''
    pass


class Role(models.Model):
    '''角色表'''
    pass


