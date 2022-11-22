import os
import sys
import anyio
import dagger

from shlex import split as sh


async def pipeline():
    config = dagger.Config(log_output=sys.stderr)
    async with dagger.Connection(config) as client:

        src_id = await client.host().workdir().id()

        container = (
            client.container()
            .from_("node:18.12.1")
            .with_mounted_directory("/workspace", src_id)
            .with_workdir("/workspace")
            # .with_env_variable("PACKAGE_NAME", os.getenv("PACKAGE_NAME"))
            .with_entrypoint("bash")
            .exec(sh('-c "npm ci"'))
            .exec(sh('-c "npm version prerelease --preid=rc"'))
            .exec(sh('-c "npm run build"'))
            .exec(sh('-c "npm test"'))
        )

        contents = await container.stdout().contents()

        print(contents)

        print(f"Done.")


if __name__ == "__main__":
    anyio.run(pipeline)
