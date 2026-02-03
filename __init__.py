# openassetio-comfyui
# Copyright (c) 2025 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0

"""
Top-level package for openassetio-comfyui.

This __init__.py will not be packaged, but is useful if the repository
is checked out under ComfyUI's custom_nodes directory, as it allows
ComfyUI to discover the nodes contained within.
"""

import sys
import pathlib

from comfy_api.latest import ComfyExtension, io

# __all__ = [
#     "NODE_CLASS_MAPPINGS",
#     "NODE_DISPLAY_NAME_MAPPINGS",
# ]

__author__ = """Contributors to the OpenAssetIO project"""
__email__ = "openassetio-discussion@lists.aswf.io"
__version__ = "1.0.0"

# Ensure src/ is on the path so we can import from there.
sys.path.append(str(pathlib.Path(__file__).parent / "src"))

# TODO(DF): Seems v3 schema and old schema cannot coexist.
# from openassetio_comfyui.nodes import NODE_CLASS_MAPPINGS
# from openassetio_comfyui.nodes import NODE_DISPLAY_NAME_MAPPINGS
from openassetio_comfyui.nodes import ResolveVideo, PublishVideo


class OpenAssetIOExtension(ComfyExtension):
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            ResolveVideo, PublishVideo
        ]


async def comfy_entrypoint() -> OpenAssetIOExtension:
    return OpenAssetIOExtension()
