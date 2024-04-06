# Code generated from Pkl module `OpenModule`. DO NOT EDIT.
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional, Set, Union

import pkl


@dataclass
class OpenModule:
    foo: str

    bar: int

    _registered_identifier = "OpenModule"

    @classmethod
    def load_pkl(cls, source):
        # Load the Pkl module at the given source and evaluate it into `OpenModule.Module`.
        # - Parameter source: The source of the Pkl module.
        config = pkl.load(source, namespace=globals())
        return config
