from .hkReferencedObject import hkReferencedObject
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree
from .hkaiStreamingCollectionInstanceInfo import hkaiStreamingCollectionInstanceInfo
from .hkaiNavMeshClearanceCacheManager import hkaiNavMeshClearanceCacheManager


class hkaiStreamingCollection(hkReferencedObject):
    isTemporary: bool
    tree: hkcdDynamicAabbTree
    instances: hkaiStreamingCollectionInstanceInfo
    clearanceCacheManager: hkaiNavMeshClearanceCacheManager
