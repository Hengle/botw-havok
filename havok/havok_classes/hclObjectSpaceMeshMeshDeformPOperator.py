from .hclObjectSpaceMeshMeshDeformOperator import hclObjectSpaceMeshMeshDeformOperator
from .hclObjectSpaceDeformerLocalBlockP import hclObjectSpaceDeformerLocalBlockP
from .hclObjectSpaceDeformerLocalBlockUnpackedP import hclObjectSpaceDeformerLocalBlockUnpackedP


class hclObjectSpaceMeshMeshDeformPOperator(hclObjectSpaceMeshMeshDeformOperator):
    localPs: hclObjectSpaceDeformerLocalBlockP
    localUnpackedPs: hclObjectSpaceDeformerLocalBlockUnpackedP
