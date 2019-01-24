from .hclConstraintSet import hclConstraintSet
from .hclVolumeConstraintFrameData import hclVolumeConstraintFrameData
from .hclVolumeConstraintApplyData import hclVolumeConstraintApplyData


class hclVolumeConstraint(hclConstraintSet):
    frameDatas: hclVolumeConstraintFrameData
    applyDatas: hclVolumeConstraintApplyData
