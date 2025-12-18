#!/bin/bash
# Script untuk testing semua API endpoints
# Pastikan server sudah berjalan di http://localhost:6543

BASE_URL="http://localhost:6543/api/matakuliah"

echo "=== Testing API Matakuliah ==="
echo ""

echo "1. GET All Matakuliah"
curl -X GET $BASE_URL
echo -e "\n"

echo "2. POST - Create Matakuliah 1"
curl -X POST $BASE_URL \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF101", "nama_mk": "Algoritma dan Pemrograman", "sks": 3, "semester": 1}'
echo -e "\n"

echo "3. POST - Create Matakuliah 2"
curl -X POST $BASE_URL \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF102", "nama_mk": "Struktur Data", "sks": 3, "semester": 2}'
echo -e "\n"

echo "4. POST - Create Matakuliah 3"
curl -X POST $BASE_URL \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF103", "nama_mk": "Basis Data", "sks": 3, "semester": 3}'
echo -e "\n"

echo "5. GET All Matakuliah (setelah create)"
curl -X GET $BASE_URL
echo -e "\n"

echo "6. GET Matakuliah by ID (ID=1)"
curl -X GET $BASE_URL/1
echo -e "\n"

echo "7. PUT - Update Matakuliah (ID=1)"
curl -X PUT $BASE_URL/1 \
  -H "Content-Type: application/json" \
  -d '{"sks": 4, "nama_mk": "Algoritma dan Pemrograman Dasar"}'
echo -e "\n"

echo "8. GET Matakuliah by ID (ID=1) setelah update"
curl -X GET $BASE_URL/1
echo -e "\n"

echo "9. DELETE - Delete Matakuliah (ID=3)"
curl -X DELETE $BASE_URL/3
echo -e "\n"

echo "10. GET All Matakuliah (setelah delete)"
curl -X GET $BASE_URL
echo -e "\n"

echo "=== Testing Error Cases ==="
echo ""

echo "11. GET Matakuliah dengan ID tidak ada (ID=999)"
curl -X GET $BASE_URL/999
echo -e "\n"

echo "12. POST dengan data tidak lengkap"
curl -X POST $BASE_URL \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF104"}'
echo -e "\n"

echo "13. POST dengan kode_mk duplikat"
curl -X POST $BASE_URL \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF101", "nama_mk": "Test", "sks": 3, "semester": 1}'
echo -e "\n"

echo "=== Testing Selesai ==="

