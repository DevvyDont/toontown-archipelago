from direct.directnotify import DirectNotifyGlobal

from otp.level import CutScene, EntityCreatorBase, AmbientSound, CollisionSolidEntity, EditMgr, EntrancePoint, LevelMgr, \
    LocatorEntity, LogicGate, ModelEntity, BasicEntities, PathEntity, PropSpinner, VisibilityExtender, ZoneEntity


def nothing(*args):
    return 'nothing'


def _nonlocal(*args):
    return '_nonlocal'


class EntityCreator(EntityCreatorBase.EntityCreatorBase):

    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        self.level = level
        self.privRegisterTypes({'attribModifier': nothing,
         'ambientSound': AmbientSound.AmbientSound,
         'collisionSolid': CollisionSolidEntity.CollisionSolidEntity,
         'cutScene': CutScene.CutScene,
         'editMgr': EditMgr.EditMgr,
         'entityGroup': nothing,
         'entrancePoint': EntrancePoint.EntrancePoint,
         'levelMgr': LevelMgr.LevelMgr,
         'locator': LocatorEntity.LocatorEntity,
         'logicGate': LogicGate.LogicGate,
         'model': ModelEntity.ModelEntity,
         'nodepath': BasicEntities.NodePathEntity,
         'path': PathEntity.PathEntity,
         'propSpinner': PropSpinner.PropSpinner,
         'visibilityExtender': VisibilityExtender.VisibilityExtender,
         'zone': ZoneEntity.ZoneEntity})

    def doCreateEntity(self, ctor, entId):
        return ctor(self.level, entId)
