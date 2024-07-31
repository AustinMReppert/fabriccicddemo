# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "62fd2f9b-2c0a-497f-9ae1-f621af814120",
# META       "default_lakehouse_name": "tests",
# META       "default_lakehouse_workspace_id": "8312ec29-9c19-4212-9049-d50fcfd62ff4"
# META     },
# META     "environment": {
# META       "environmentId": "3d06b5e1-c565-40b8-8a66-cf3458a4e240",
# META       "workspaceId": "8312ec29-9c19-4212-9049-d50fcfd62ff4"
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

id = "latest"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

if len(id) == 0:
    raise ValueError("Invalid id parameter")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pytestmsfabric import plugin

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

await plugin.main([
    "--verbose",
    "--nunit-xml", f"/lakehouse/default/Files/tests/{id}.xml"
])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
