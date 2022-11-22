import os
import sys
import anyio
import dagger

from shlex import split as sh


async def pipeline():
    config = dagger.Config(log_output=sys.stderr)
    async with dagger.Connection(config) as client:

        src_id = await client.host().workdir().id()

        node_container = (
            client.container()
            .from_("cgr.dev/chainguard/node:18.12.1")
            .with_mounted_directory("/workspace", src_id)
            .with_workdir("/workspace")
            .with_env_variable("PACKAGE_NAME", os.getenv("PACKAGE_NAME"))
            .exec(sh('npm ci'))
            .exec(sh('npm version prerelease --preid=rc'))
            .exec(sh('npm run build'))
            .exec(sh('npm run test'))
        )

        print(f"Starting pipeline ...")

        await node_container.exit_code()

        print(f"Done.")

if __name__ == "__main__":
    anyio.run(pipeline)