@ECHO OFF

SET DJANGO_SETTINGS_MODULE=config.settings.windows_local
SET DATABASE_URL=sqlite:///%CD%\db.sqlite 
