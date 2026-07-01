import sqlite3
import os

db_path = "/app/mlflow.db"
if not os.path.exists(db_path):
    print(f"Database {db_path} not found.")
    exit(0)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Update experiments table
cursor.execute("SELECT experiment_id, artifact_location FROM experiments;")
for row in cursor.fetchall():
    exp_id, location = row
    if location and "mlartifacts" in location:
        idx = location.find("mlartifacts")
        new_location = "file:///app/" + location[idx:]
        cursor.execute(
            "UPDATE experiments SET artifact_location = ? WHERE experiment_id = ?;",
            (new_location, exp_id)
        )
        print(f"Updated experiment {exp_id}: {location} -> {new_location}")

# 2. Update runs table
cursor.execute("SELECT run_uuid, artifact_uri FROM runs;")
for row in cursor.fetchall():
    run_uuid, uri = row
    if uri and "mlartifacts" in uri:
        idx = uri.find("mlartifacts")
        new_uri = "file:///app/" + uri[idx:]
        cursor.execute(
            "UPDATE runs SET artifact_uri = ? WHERE run_uuid = ?;",
            (new_uri, run_uuid)
        )
        print(f"Updated run {run_uuid}: {uri} -> {new_uri}")

# 3. Update model_versions table
cursor.execute("SELECT name, version, source, storage_location FROM model_versions;")
for row in cursor.fetchall():
    name, version, source, storage_location = row
    if source and "mlartifacts" in source:
        idx = source.find("mlartifacts")
        new_source = "file:///app/" + source[idx:]
        cursor.execute(
            "UPDATE model_versions SET source = ? WHERE name = ? AND version = ?;",
            (new_source, name, version)
        )
        print(f"Updated model version {name} v{version} source: {source} -> {new_source}")
    if storage_location and "mlartifacts" in storage_location:
        idx = storage_location.find("mlartifacts")
        new_storage = "file:///app/" + storage_location[idx:]
        cursor.execute(
            "UPDATE model_versions SET storage_location = ? WHERE name = ? AND version = ?;",
            (new_storage, name, version)
        )
        print(f"Updated model version {name} v{version} storage_location: {storage_location} -> {new_storage}")

conn.commit()
conn.close()
print("MLflow database paths patched successfully.")
