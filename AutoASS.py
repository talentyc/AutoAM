from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, IntegerProperty, StructuredRel, FloatProperty, DateProperty, DateTimeProperty
import neomodel
from datetime import datetime

class PLANNED_PpV(StructuredRel):
    # identifier = StringProperty()  # ID of production order
    quantity = IntegerProperty()

class PERFORMS_ApA(StructuredRel):
    pass
    
class HASROLE_RhR(StructuredRel):
    pass

class HASROLE_VhV(StructuredRel):
    pass

class HASROLE_FhF(StructuredRel):
    pass

class HASROLE_BhP(StructuredRel):
    pass

class SCHEDULEDAT_PsF(StructuredRel):
    pass

class BELONGSTO_ObA(StructuredRel):
    pass

class CONTAINS_FcA(StructuredRel):
    pass

class CONTAINS_AcW(StructuredRel):
    pass

class CONTAINS_OcW(StructuredRel):
    pass

class CONTAINS_WcW(StructuredRel):
    pass

class CONTAINS_PcO(StructuredRel):
    pass

class CONTAINS_VcV(StructuredRel):
    pass

class CONTAINS_AcT(StructuredRel):
    pass

class INCLUDES_ViV(StructuredRel):
    pass

class ASSEMBLEDIN_VaA(StructuredRel):
    pass

class ASSOCIATED_OaV(StructuredRel):
    pass

class UPDATES_RuP(StructuredRel):
    pass

class MODIFIES_RmW(StructuredRel):
    pass

class DESCRIBEDIN_VdP(StructuredRel):
    pass

class REFERENCES_WrP(StructuredRel):
    index = IntegerProperty()

class REFERENCES_OrO(StructuredRel):
    pass

class REFERENCE_TrO(StructuredRel):
    pass

class PERFORMEDAT_OpW(StructuredRel):
    pass

class PERFORMEDIN_OpW(StructuredRel):
    pass

class ASSIGNSTO_RaT(StructuredRel):
    pass

class ASSIGNSTO_PaT(StructuredRel):
    pass

class ASSIGNSTO_BaT(StructuredRel):
    pass

class ASSIGNSTO_FaT(StructuredRel):
    pass

class FOLLOWS_WfW(StructuredRel):
    pass

class COMPOSEDOF_VcP(StructuredRel):
    identifier = StringProperty() #VWS
    quantity = IntegerProperty()
    optionalcode = StringProperty()
    optionalpackage = StringProperty()

class REQUIRES_OrP(StructuredRel):
    quantity = IntegerProperty()
    optionalcode = StringProperty()

class REQUIRES_OrE(StructuredRel):
    pass

class REQUIRES_OrT(StructuredRel):
    pass

class REQUIRES_OrM(StructuredRel):
    pass

class REQUIRES_OrF(StructuredRel):
    pass

class REQUIRES_OrA(StructuredRel):
    pass

class HASDELIVERYPOINT_OhD(StructuredRel):
    partid = StringProperty()

class TRIGGERS_PtL(StructuredRel):
    pass

class GENERATES_PgA(StructuredRel):
    pass

class PRODUCES_ApV(StructuredRel):
    pass

class MANAGES_PmR(StructuredRel):
    pass

class ASSOCIATED_VaB(StructuredRel):
    pass

class SUPPLIEDBY_PsS(StructuredRel):
    pass

class SUPPLIEDTO_PsD(StructuredRel):
    pass
    # quantity = IntegerProperty()
    # optionalcode = StringProperty()

class LOCATEDAT_DlW(StructuredRel):
    pass

class DELIVEREDTO_LdD(StructuredRel):
    # identifier = StringProperty() # id of logistics process
    quantity = IntegerProperty()
    part = StringProperty()

class ASSOCIATES_LaP(StructuredRel):
    pass
    # identifier = StringProperty() # id of logistics process
    # quantity = IntegerProperty()

class DELIVERS_LdB(StructuredRel):
    quantity = IntegerProperty()
    batch = StringProperty()

class GENERATES_LgL(StructuredRel):
    pass

# class Thing(StructuredNode):
#     name = StringProperty()
#     identifier = StringProperty()

class AssemblyShop(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    type = StringProperty()  # Assembly, Painting, Body, 
    contains_AcW = RelationshipTo('WorkStation', 'CONTAINS_AcW', model = CONTAINS_AcW)
    performs_ApA = RelationshipTo('AssemblyProcess', 'PERFORMS_ApA', model = PERFORMS_ApA)

class Factory(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    contains_FcA = RelationshipTo('AssemblyShop', 'CONTAINS_FcA', model = CONTAINS_FcA)
    location = StringProperty()
    capability = StringProperty()
    # value = StringProperty()
    # availableTime = StringProperty()

class ProductDescription(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    revisioncomment = StringProperty()
    revisiondatetime = DateProperty()
    revisionauthor = StringProperty()

class Supplier(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    # location= StringProperty()
    # contactinfo= StringProperty()

class WorkCell(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()


class DeliveryPoint(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    # minStorage = IntegerProperty() optional
    # maxStorage = IntegerProperty() optional
    locatedat_DlW = RelationshipTo('WorkCell', 'LOCATEDAT_DlW', model = LOCATEDAT_DlW)

class ResourceRole(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()


class PartRole(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    suppliedby_PsS = RelationshipTo('Supplier', 'SUPPLIEDBY_PsS', model = SUPPLIEDBY_PsS)
    suppliedto_PsD = RelationshipTo('DeliveryPoint', 'SUPPLIEDTO_PsD', model = SUPPLIEDTO_PsD)

class EquipmentRole(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()

class AuxiliaryMaterialRole(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    quota = FloatProperty()
    modelnumber = StringProperty()

class ToolRole(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    quota = FloatProperty()
    modelnumber = StringProperty()

class FasternToolRole(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    quota = FloatProperty()
    modelnumber = StringProperty()
    torque = StringProperty()
    quotaid = StringProperty()

class MachineRole(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()

class WorkStation(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    type = StringProperty()
    contains_WcW = RelationshipTo('WorkCell', 'CONTAINS_WcW', model = CONTAINS_WcW)

class Revision(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    revisioncontent = StringProperty()
    revisiondatetime = DateProperty()
    revisionauthor = StringProperty()
    updates_RuP = RelationshipTo('ProductDescription', 'UPDATES_RuP', model = UPDATES_RuP)
    modifies_RmW = RelationshipTo('WorkStep', 'MODIFIES_RmW', model = MODIFIES_RmW)

class WorkStep(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    revisioncomment = StringProperty()
    revisiondatetime = DateProperty()
    revisionauthor = StringProperty()
    instruction = StringProperty()
    # keyelement = StringProperty()
    references_WrP = RelationshipTo('ProductDescription', 'REFERENCES_WrP', model = REFERENCES_WrP)
    # requires_WrP = RelationshipTo('PartRole', 'REQUIRES_WrP', model = REQUIRES_WrP)
    # requires_WrE = RelationshipTo('EquipmentRole', 'REQUIRES_WrE', model = REQUIRES_WrE)
    # requires_WrA = RelationshipTo('AuxiliaryMaterialRole', 'REQUIRES_WrA', model = REQUIRES_WrA)
    follows_WfW = RelationshipTo('WorkStep', 'FOLLOWS_WfW', model = FOLLOWS_WfW)

class VehicleVariant(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    engine = StringProperty()
    power = StringProperty()
    transmission = StringProperty()
    trim = StringProperty()
    assembledin_VaA = RelationshipTo('AssemblyShop', 'ASSEMBLEDIN_VaA', model = ASSEMBLEDIN_VaA)
    # describedin_VdP = RelationshipTo('ProductDescription', 'DESCRIBEDIN_VdP', model = DESCRIBEDIN_VdP)
    # associated_VaO = RelationshipTo('Operation', 'ASSOCIATED_VaO', model = ASSOCIATED_VaO)    
    composedof_VcP = RelationshipTo('PartRole', 'COMPOSEDOF_VcP', model = COMPOSEDOF_VcP)

class VehicleFamily(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    # assembledin_VaA = RelationshipTo('AssemblyShop', 'ASSEMBLEDIN_VaA', model = ASSEMBLEDIN_VaA)
    describedin_VdP = RelationshipTo('ProductDescription', 'DESCRIBEDIN_VdP', model = DESCRIBEDIN_VdP)
    contains_VcV = RelationshipTo('VehicleVariant', 'CONTAINS_VcV', model = CONTAINS_VcV)
    # includes_ViV = RelationshipTo('VehicleSubsystem', 'INCLUDES_ViV', model = INCLUDES_ViV)

# class VehicleSubsystem(Thing):
#     describedin_VdP = RelationshipTo(ProductDescription, 'DESCRIBEDIN_VdP', model = DESCRIBEDIN_VdP)

class Operation(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    # revisioncomment = StringProperty()
    sequence = IntegerProperty()
    duration = FloatProperty()
    # follows_OfO = RelationshipTo('Operation', 'FOLLOWS_OfO', model = FOLLOWS_OfO)
    contains_OcW = RelationshipTo('WorkStep', 'CONTAINS_OcW', model = CONTAINS_OcW)
    performedin_OpW = RelationshipTo('WorkCell', 'PERFORMEDIN_OpW', model = PERFORMEDIN_OpW)
    # performedat_OpW = RelationshipTo('WorkStation', 'PERFORMEDAT_OpW', model = PERFORMEDAT_OpW)
    associated_OaV = RelationshipTo('VehicleFamily', 'ASSOCIATED_OaV', model = ASSOCIATED_OaV)
    belongsto_ObA = RelationshipTo('AssemblyShop', 'BELONGSTO_ObA', model = BELONGSTO_ObA)  
    requires_OrP = RelationshipTo('PartRole', 'REQUIRES_OrP', model = REQUIRES_OrP)
    requires_OrE = RelationshipTo('EquipmentRole', 'REQUIRES_OrE', model = REQUIRES_OrE)
    #### tool is subclass of equipment, do i need to define relationship bettween tool and operation? yes
    requires_OrT = RelationshipTo('ToolRole', 'REQUIRES_OrT', model = REQUIRES_OrT)
    requires_OrA = RelationshipTo('AuxiliaryMaterialRole', 'REQUIRES_OrA', model = REQUIRES_OrA)
    requires_OrF = RelationshipTo('FasternToolRole', 'REQUIRES_OrF', model = REQUIRES_OrF)
    requires_OrM = RelationshipTo('MachineRole', 'REQUIRES_OrM', model = REQUIRES_OrM)
    hasdeliverypoint_OhD = RelationshipTo('DeliveryPoint', 'HASDELIVERYPOINT_OhD', model = HASDELIVERYPOINT_OhD)
     
class Task(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    # workshift = StringProperty()
    datetime = DateProperty()
    reference_TrO = RelationshipTo('Operation', 'REFERENCE_TrO', model = REFERENCE_TrO)

class Resource(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    assignsto_RaT = RelationshipTo('Task', 'ASSIGNSTO_RaT', model = ASSIGNSTO_RaT)
    # hasRole_RhR = RelationshipTo(ResourceRole, 'HASROLE_RhR', model = HASROLE_RhR)

class BatchPart(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    partid = StringProperty()
    hasrole_BhP = RelationshipTo('PartRole', 'HASROLE_BhP', model = HASROLE_BhP)
    assignsto_BaT = RelationshipTo('Task', 'ASSIGNSTO_BaT', model = ASSIGNSTO_BaT)


class Vehicle(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    produceddate = DateProperty()
    hasrole_VhV = RelationshipTo('VehicleVariant', 'HASROLE_VhV', model = HASROLE_VhV)
    associated_VaB = RelationshipTo('BatchPart', 'ASSOCIATED_VaB', model = ASSOCIATED_VaB)

class AssemblyProcess(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    planned_quantity = IntegerProperty()
    starttime = DateProperty()
    endtime = DateProperty()
    status = StringProperty()
    workshift = StringProperty()
    produces_ApV = RelationshipTo('Vehicle', 'PRODUCES_ApV', model = PRODUCES_ApV)
    contains_AcT = RelationshipTo('Task', 'CONTAINS_AcT', model = CONTAINS_AcT)
    references_OrO = RelationshipTo('Operation', 'REFERENCES_OrO', model = REFERENCES_OrO)

class LogisticsProcess(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    starttime = DateProperty()
    type = StringProperty()
    status = StringProperty()
    # quantity = IntegerProperty()
    workshift = StringProperty()
    delivers_LdB = RelationshipTo('BatchPart', 'DELIVERS_LdB', model = DELIVERS_LdB)
    deliveredto_LdD = RelationshipTo('DeliveryPoint', 'DELIVEREDTO_LdD', model = DELIVEREDTO_LdD)
    associates_LaP = RelationshipTo('PartRole', 'ASSOCIATES_LaP', model = ASSOCIATES_LaP)

class LogisticsOrder(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    creationtime = DateProperty()
    duedate = DateProperty()
    status = StringProperty()
    generates_LgL = RelationshipTo('LogisticsProcess', 'GENERATES_LgL', model = GENERATES_LgL)

class ProductionOrder(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    creationtime = DateProperty()
    starttime = DateProperty()
    duetime = DateProperty()
    status = StringProperty()
    quantity = IntegerProperty()
    planned_PpV = RelationshipTo('VehicleVariant', 'PLANNED_PpV', model = PLANNED_PpV)
    scheduledat_PsF = RelationshipTo('Factory' ,'SCHEDULEDAT_PsF' , model = SCHEDULEDAT_PsF)
    generates_PgA = RelationshipTo('AssemblyProcess' ,'GENERATES_PgA' , model = GENERATES_PgA)
    triggers_PtL = RelationshipTo('LogisticsOrder' ,'TRIGGERS_PtL' , model = TRIGGERS_PtL)
    manages_PmR = RelationshipTo('Resource', 'MANAGES_PmR', model = MANAGES_PmR)

class Personnel(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    assignsto_PaT = RelationshipTo('Task', 'ASSIGNSTO_PaT', model = ASSIGNSTO_PaT)

class Equipment(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()

class AuxiliaryMaterial(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()

class Machine(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()

class Tool(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()

class FasternTool(StructuredNode):
    name = StringProperty()
    identifier = StringProperty()
    torque = StringProperty()
    validationdate = DateProperty()
    expirationdate = DateProperty()
    hasrole_FhF = RelationshipTo(FasternToolRole, 'HASROLE_FhF', model = HASROLE_FhF)
    assignsto_FaT = RelationshipTo('Task', 'ASSIGNSTO_FaT', model = ASSIGNSTO_FaT)