from .hkpCollisionFilter import hkpCollisionFilter
from .hkpPairCollisionFilterMapPairFilterKeyOverrideType import hkpPairCollisionFilterMapPairFilterKeyOverrideType


class hkpPairCollisionFilter(hkpCollisionFilter):
    disabledPairs: hkpPairCollisionFilterMapPairFilterKeyOverrideType
    childFilter: hkpCollisionFilter