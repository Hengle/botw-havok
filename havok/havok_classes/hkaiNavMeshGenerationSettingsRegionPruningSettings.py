from .common import any
from .hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection import hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection


class hkaiNavMeshGenerationSettingsRegionPruningSettings(object):
    minRegionArea: float
    minDistanceToSeedPoints: float
    borderPreservationTolerance: float
    preserveVerticalBorderRegions: bool
    pruneBeforeTriangulation: bool
    regionSeedPoints: any
    regionConnections: hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection
