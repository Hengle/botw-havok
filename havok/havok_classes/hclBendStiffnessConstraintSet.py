from .hclConstraintSet import hclConstraintSet
from .hclBendStiffnessConstraintSetLink import hclBendStiffnessConstraintSetLink


class hclBendStiffnessConstraintSet(hclConstraintSet):
    links: hclBendStiffnessConstraintSetLink
    useRestPoseConfig: bool
