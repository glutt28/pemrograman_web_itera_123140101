#!/bin/bash
# Script untuk membuat database PostgreSQL
# Edit password di bawah sesuai dengan password PostgreSQL Anda

echo "========================================"
echo "Script Pembuat Database PostgreSQL"
echo "========================================"
echo ""

# Edit password PostgreSQL Anda di bawah
PG_PASSWORD="postgres"

# Jalankan script Python
python create_database.py --password "$PG_PASSWORD"

