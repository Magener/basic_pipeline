CALL "%1\connection_data.bat"

set DATE=%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set BACKUP_FILE=%BACKUP_DIR%\%DB_NAME%_backup_%DATE%.sql

%POSTGRES_HOME%\bin\pg_dump.exe -U %DB_USER% -w %DB_NAME% > %BACKUP_FILE%

PAUSE