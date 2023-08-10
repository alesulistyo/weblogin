@echo off
cmd /k "cd %~dp0\Env\Scripts & activate & cd /d %~dp0\myWeb & python manage.py runserver"