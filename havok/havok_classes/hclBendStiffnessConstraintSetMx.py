from .hclConstraintSet import hclConstraintSet
from .hclBendStiffnessConstraintSetMxBatch import hclBendStiffnessConstraintSetMxBatch
from .hclBendStiffnessConstraintSetMxSingle import hclBendStiffnessConstraintSetMxSingle


class hclBendStiffnessConstraintSetMx(hclConstraintSet):
    batches: hclBendStiffnessConstraintSetMxBatch
    singles: hclBendStiffnessConstraintSetMxSingle
    useRestPoseConfig: bool
