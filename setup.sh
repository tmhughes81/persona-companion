#!/bin/bash

if [ ! -f "db/db.sqlite3" ]; then
    cp examples/db.sqlite3.example db/db.sqlite3
    echo Creating database file from example...
else
    echo Database already exists...
fi
