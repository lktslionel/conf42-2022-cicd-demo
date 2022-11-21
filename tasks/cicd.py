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
            .from_("debian")
            .with_mounted_directory("/src", src_id)
            .with_workdir("/src")
            .with_env_variable("PACKAGE_NAME", os.environ.get("PACKAGE_NAME"))
            .exec(sh('echo "Package: $PACKAGE_NAME"'))
        )

        contents = await container.stdout().contents()

        print(f"Contents: {contents}")


if __name__ == "__main__":
    anyio.run(pipeline)