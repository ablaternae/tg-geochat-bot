# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import datetime
from typing import (Any, Dict, ForwardRef, List, Literal, Optional, Sequence,
                    Type, Union)


@dataclass
class tUser:
    name: str = None
    loginpass: str = None
    profiles: Optional[List[ForwardRef('tProfile')]] = field(default_factory=list)
    # accounts: Optional[List[tAccount]] = field(default_factory=list)
    # roles: Optional[List[tRole]] = Field(default_factory=list)
    pass


@dataclass
class tAccount:
    name: str = None
    pass


@dataclass
class tProfile:
    description: Optional[str] = None
    joined: Optional[datetime] = field(default_factory=datetime.utcnow)
    user: Optional[tUser] = field(default=None)
    pass


"""
@dataclass
class tRole:
    description: Optional[str] = None
    joined: Optional[datetime]
    owner
    admin
    operator
    manager
    user
    anonym
    pass
"""
