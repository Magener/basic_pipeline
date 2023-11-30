@echoff

CALL "./backup_environment.bat"

set ARG_PARSED_COMMAND="%BACKUP_SCRIPT_LOCATION%\backup\backup_db.bat %BACKUP_SCRIPT_LOCATION%\backup\"

schtasks /create /tn "AutomaticallyBackUp" /tr %ARG_PARSED_COMMAND% /sc DAILY /st 11:33 /ru SYSTEM

set ARG_PARSED_COMMAND=

PAUSE