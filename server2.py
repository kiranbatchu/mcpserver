from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
from sqlalchemy import create_engine, text
import json






POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres123"
POSTGRES_HOST = "postgres-db-v1.cbkaui220ofp.us-east-2.rds.amazonaws.com"
POSTGRES_PORT = "5432"
POSTGRES_DB = "call_transcripts"

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
id:str = 0


with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT *
            FROM raw_transcripts
            WHERE id = :id
        """),{"id": id})
        columns = result.keys()
        rows = [dict(zip(columns, row)) for row in result.fetchall()]
        print(rows)
        call_details = []
        for column in columns:  # Only show next 5 periods
            call_details_str = f"{column} : {rows[0][column]}"
            call_details.append(call_details_str)
        print("\n---\n".join(call_details))



