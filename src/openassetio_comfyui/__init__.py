# openassetio-comfyui
# Copyright (c) 2025 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0

"""Top-level package for openassetio-comfyui."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__author__ = """Contributors to the OpenAssetIO project"""
__email__ = "openassetio-discussion@lists.aswf.io"
__version__ = "1.0.0"

from comfy_api.latest import ComfyExtension, io

from .nodes import NODE_CLASS_MAPPINGS
from .nodes import NODE_DISPLAY_NAME_MAPPINGS
from .nodes import ResolveVideo, PublishVideo


class OpenAssetIOExtension(ComfyExtension):
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            ResolveVideo, PublishVideo
        ]


async def comfy_entrypoint() -> OpenAssetIOExtension:
    return OpenAssetIOExtension()
