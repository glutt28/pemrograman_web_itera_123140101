@echo off
REM Script batch untuk membuat database PostgreSQL
REM Edit password di bawah sesuai dengan password PostgreSQL Anda

echo ========================================
echo Script Pembuat Database PostgreSQL
echo ========================================
echo.

REM Edit password PostgreSQL Anda di bawah
set PG_PASSWORD=postgres

REM Jalankan script Python
python create_database.py --password %PG_PASSWORD%

pause

