import argparse
import json
from azure.core.credentials import AccessToken
from azure.identity import DefaultAzureCredential
import fabricclientaio.models.responses
from fabricclientaio.auth.fabrictokenprovider import FabricTokenProvider
from fabricclientaio.fabricclient import FabricClient
from fabricclientaio.fabricworkspaceclient import FabricWorkspaceClient


class DefaultAzureCredentialProvider(FabricTokenProvider):

    def __init__(self) -> None:
        pass

    async def get_token(self) -> AccessToken:
        default_credentials = DefaultAzureCredential()
        return default_credentials.get_token("https://api.fabric.microsoft.com/.default")

async def main() -> None:
    parser = argparse.ArgumentParser(description="Fabric CI/CD.")
    parser.add_argument('--workspace-id', required=True, help='The ID of the workspace.')
    args = parser.parse_args()
    workspace_id = args.workspace_id

    fabric_client = FabricClient(DefaultAzureCredentialProvider())
    workspace_client = FabricWorkspaceClient(fabric_client, workspace_id)

    # Find the item id of the notebook called testrunner
    item_id = None
    async for item in workspace_client.get_items():
        if item.display_name == "unittestrunner" and item.type == fabricclientaio.models.responses.ItemType.notebook:
            item_id = item.id
            break

    if item_id is None:
        raise ValueError("unittestrunner not found.")
        return
    
    # Run the testrunner notebook.

    # Create a new run

    job_args = """
    {
        "executionData": {
            "parameters": {
                "parameterName": {
                    "id": "latest",
                    "type": "string"
                }
            }
        }
    }
    """

    job_args2: dict = json.loads(job_args)

    run = await workspace_client.run_on_demand_item_job(item_id, "RunNotebook", job_args2)

    # Wait for the run to complete
    while run.status == fabricclientaio.models.responses.Status.in_progress \
        or run.status == fabricclientaio.models.responses.Status.not_started:
        run = await workspace_client.get_item_job_instance(run.item_id, run.id)
        await asyncio.sleep(5)

    if run.status == fabricclientaio.models.responses.Status.failed:
        raise ValueError("Run failed.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())