# MIT License

# Copyright (c) 2017 GiveMeAllYourCats

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Code author: Hotox
# Repo: https://github.com/michaeldegroot/cats-blender-plugin
# Edits by: GiveMeAllYourCats

import bpy
import webbrowser
import tools.common
import tools.eyetracking

mmd_tools_installed = False
try:
    import mmd_tools_local
    mmd_tools_installed = True
except:
    pass


class ImportModel(bpy.types.Operator):
    bl_idname = 'armature_manual.import_model'
    bl_label = 'Import Model'
    bl_description = 'Import a model of the selected type'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        tools.common.remove_unused_objects()
        if context.scene.import_mode == 'MMD':
            if not mmd_tools_installed:
                bpy.context.window_manager.popup_menu(popup_enable_mmd, title='mmd_tools is not installed!', icon='ERROR')
                return {'FINISHED'}

            try:
                bpy.ops.mmd_tools.import_model('INVOKE_DEFAULT', scale=0.08, types={'MESH', 'ARMATURE', 'MORPHS'})
            except AttributeError:
                bpy.context.window_manager.popup_menu(popup_enable_mmd, title='mmd_tools is not enabled!', icon='ERROR')
            except (TypeError, ValueError):
                bpy.ops.mmd_tools.import_model('INVOKE_DEFAULT')

        elif context.scene.import_mode == 'XPS':
            try:
                bpy.ops.xps_tools.import_model('INVOKE_DEFAULT')
            except AttributeError:
                bpy.context.window_manager.popup_menu(popup_install_xps, title='XPS Tools is not installed or enabled!', icon='ERROR')
            except (TypeError, ValueError):
                bpy.ops.xps_tools.import_model('INVOKE_DEFAULT')

        elif context.scene.import_mode == 'FBX':
            try:
                bpy.ops.import_scene.fbx('INVOKE_DEFAULT', automatic_bone_orientation=True)
            except (TypeError, ValueError):
                bpy.ops.import_scene.fbx('INVOKE_DEFAULT')

        return {'FINISHED'}


def popup_enable_mmd(self, context):
    layout = self.layout
    col = layout.column(align=True)

    row = col.row(align=True)
    row.label("The plugin 'mmd_tools' is required for this function.")
    col.separator()
    row = col.row(align=True)
    row.label("Please restart Blender.")


def popup_enable_xps(self, context):
    layout = self.layout
    col = layout.column(align=True)

    row = col.row(align=True)
    row.label("The plugin 'XPS Tools' is required for this function.")
    col.separator()
    row = col.row(align=True)
    row.label("Please enable it in your User Preferences.")


def popup_install_xps(self, context):
    layout = self.layout
    col = layout.column(align=True)

    row = col.row(align=True)
    row.label("The plugin 'XPS Tools' is required for this function.")
    col.separator()
    row = col.row(align=True)
    row.label("If it is not enabled please enable it in your User Preferences.")
    row = col.row(align=True)
    row.label("If it is not installed please click here to go to this link to download and install it")
    col.separator()
    row = col.row(align=True)
    row.operator('armature_manual.xps_tools', icon='LOAD_FACTORY')


class XpsToolsButton(bpy.types.Operator):
    bl_idname = 'armature_manual.xps_tools'
    bl_label = 'Install XPS Tools'

    def execute(self, context):
        webbrowser.open('https://github.com/johnzero7/XNALaraMesh')

        self.report({'INFO'}, 'XPS Tools link opened')
        return {'FINISHED'}


class ExportModel(bpy.types.Operator):
    bl_idname = 'armature_manual.export_model'
    bl_label = 'Export Model'
    bl_description = 'Export this model as .fbx for Unity.\n' \
                     '\n' \
                     'Automatically sets the optimal export settings'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        protected_export = False
        for mesh in tools.common.get_meshes_objects():
            if protected_export:
                break
            if mesh.data.shape_keys:
                for shapekey in mesh.data.shape_keys.key_blocks:
                    if shapekey.name == 'Basis Original':
                        protected_export = True
                        break

        try:
            if protected_export:
                bpy.ops.export_scene.fbx('INVOKE_DEFAULT',
                                         object_types={'EMPTY', 'ARMATURE', 'MESH', 'OTHER'},
                                         use_mesh_modifiers=False,
                                         add_leaf_bones=False,
                                         bake_anim=False,
                                         mesh_smooth_type='FACE')
            else:
                bpy.ops.export_scene.fbx('INVOKE_DEFAULT',
                                         object_types={'EMPTY', 'ARMATURE', 'MESH', 'OTHER'},
                                         use_mesh_modifiers=False,
                                         add_leaf_bones=False,
                                         bake_anim=False)
        except (TypeError, ValueError):
            bpy.ops.export_scene.fbx('INVOKE_DEFAULT')

        return {'FINISHED'}


class StartPoseMode(bpy.types.Operator):
    bl_idname = 'armature_manual.start_pose_mode'
    bl_label = 'Start Pose Mode'
    bl_description = 'Starts the pose mode.\n' \
                     'This lets you test how your model will move'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if tools.common.get_armature() is None:
            return False
        return True

    def execute(self, context):
        current = ""
        if bpy.context.active_object is not None and bpy.context.active_object.mode == 'EDIT' and bpy.context.active_object.type == 'ARMATURE' and len(bpy.context.selected_editable_bones) > 0:
            current = bpy.context.selected_editable_bones[0].name

        armature = tools.common.set_default_stage()
        tools.common.switch('POSE')
        armature.data.pose_position = 'POSE'

        for mesh in tools.common.get_meshes_objects():
            if mesh.data.shape_keys is not None:
                for shape_key in mesh.data.shape_keys.key_blocks:
                    shape_key.value = 0

        for pb in armature.data.bones:
            pb.select = True
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.scale_clear()
        bpy.ops.pose.transforms_clear()

        bone = armature.data.bones.get(current)
        if bone is not None:
            for pb in armature.data.bones:
                if bone.name != pb.name:
                    pb.select = False
        else:
            for index, pb in enumerate(armature.data.bones):
                if index != 0:
                    pb.select = False

        bpy.context.space_data.transform_manipulators = {'ROTATE'}

        return {'FINISHED'}


class StopPoseMode(bpy.types.Operator):
    bl_idname = 'armature_manual.stop_pose_mode'
    bl_label = 'Stop Pose Mode'
    bl_description = 'Stops the pose mode and resets the pose to normal'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if tools.common.get_armature() is None:
            return False
        return True

    def execute(self, context):
        armature = tools.common.get_armature()
        for pb in armature.data.bones:
            pb.hide = False
            pb.select = True
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.scale_clear()
        bpy.ops.pose.transforms_clear()
        for pb in armature.data.bones:
            pb.select = False

        armature = tools.common.set_default_stage()
        armature.data.pose_position = 'REST'

        for mesh in tools.common.get_meshes_objects():
            if mesh.data.shape_keys is not None:
                for shape_key in mesh.data.shape_keys.key_blocks:
                    shape_key.value = 0

        bpy.context.space_data.transform_manipulators = {'TRANSLATE'}
        tools.eyetracking.eye_left = None

        return {'FINISHED'}


class PoseToShape(bpy.types.Operator):
    bl_idname = 'armature_manual.pose_to_shape'
    bl_label = 'Pose to Shape Key'
    bl_description = 'INFO: Join your meshes first!' \
                     '\n' \
                     '\nThis saves your current pose as a new shape key.' \
                     '\nThe new shape key will be at the bottom of your shape key list of the mesh'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        if not bpy.context.active_object or bpy.context.active_object.mode != 'POSE':
            return False

        meshes = tools.common.get_meshes_objects()
        return meshes and len(meshes) == 1

    def execute(self, context):
        mesh = tools.common.get_meshes_objects()[0]
        tools.common.unselect_all()
        tools.common.select(mesh)

        # Apply armature mod
        mod = mesh.modifiers.new("Pose", 'ARMATURE')
        mod.object = tools.common.get_armature()
        bpy.ops.object.modifier_apply(apply_as='SHAPE', modifier=mod.name)

        armature = tools.common.set_default_stage()
        tools.common.switch('POSE')
        armature.data.pose_position = 'POSE'

        self.report({'INFO'}, 'Pose successfully saved as shape key.')
        return {'FINISHED'}


class PoseToRest(bpy.types.Operator):
    bl_idname = 'armature_manual.pose_to_rest'
    bl_label = 'Apply as Rest Pose'
    bl_description = 'INFO: Join your meshes first!' \
                     '\n' \
                     '\nThis sets your current pose as the default pose.'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        if not bpy.context.active_object or bpy.context.active_object.mode != 'POSE':
            return False

        meshes = tools.common.get_meshes_objects()
        return meshes and len(meshes) == 1

    def execute(self, context):
        mesh = tools.common.get_meshes_objects()[0]
        tools.common.unselect_all()
        tools.common.select(mesh)

        # Apply armature mod
        mod = mesh.modifiers.new("Pose", 'ARMATURE')
        mod.object = tools.common.get_armature()
        bpy.ops.object.modifier_apply(apply_as='SHAPE', modifier=mod.name)

        armature = tools.common.set_default_stage()
        tools.common.switch('POSE')
        armature.data.pose_position = 'POSE'

        self.report({'INFO'}, 'Pose successfully saved as shape key.')
        return {'FINISHED'}


class JoinMeshes(bpy.types.Operator):
    bl_idname = 'armature_manual.join_meshes'
    bl_label = 'Join Meshes'
    bl_description = 'Joins the model meshes into a single one and applies all unapplied decimation modifiers'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        meshes = tools.common.get_meshes_objects()
        return meshes and len(meshes) > 0

    def execute(self, context):
        mesh = tools.common.join_meshes()
        if mesh:
            tools.common.repair_viseme_order(mesh.name)

        self.report({'INFO'}, 'Meshes joined.')
        return {'FINISHED'}


class SeparateByMaterials(bpy.types.Operator):
    bl_idname = 'armature_manual.separate_by_materials'
    bl_label = 'Separate by Materials'
    bl_description = 'Separates selected mesh by materials.\n' \
                     '\n' \
                     'Warning: Never decimate something where you might need the shape keys later (face, mouth, eyes..)'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj and obj.type == 'MESH':
            return True

        meshes = tools.common.get_meshes_objects()
        return meshes and len(meshes) >= 1

    def execute(self, context):
        obj = context.active_object

        if not obj or (obj and obj.type != 'MESH'):
            tools.common.unselect_all()
            meshes = tools.common.get_meshes_objects()
            if len(meshes) == 0:
                self.report({'ERROR'}, 'No meshes found!')
                return {'FINISHED'}
            if len(meshes) > 1:
                self.report({'ERROR'}, 'Multiple meshes found!'
                                       '\nPlease select the mesh you want to separate!')
                return {'FINISHED'}
            obj = meshes[0]

        tools.common.separate_by_materials(context, obj)

        self.report({'INFO'}, 'Successfully separated by materials.')
        return {'FINISHED'}


class SeparateByLooseParts(bpy.types.Operator):
    bl_idname = 'armature_manual.separate_by_loose_parts'
    bl_label = 'Separate by Loose Parts'
    bl_description = 'Can cause a lot of lag depending on the model!\n' \
                     '\n' \
                     'Separates selected mesh by loose parts sorted by materials.\n' \
                     'This acts like separating by materials but creates more meshes for more precision.\n'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj and obj.type == 'MESH':
            return True

        meshes = tools.common.get_meshes_objects()
        return meshes and len(meshes) >= 1

    def execute(self, context):
        obj = context.active_object

        if not obj or (obj and obj.type != 'MESH'):
            tools.common.unselect_all()
            meshes = tools.common.get_meshes_objects()
            if len(meshes) == 0:
                self.report({'ERROR'}, 'No meshes found!')
                return {'FINISHED'}
            if len(meshes) > 1:
                self.report({'ERROR'}, 'Multiple meshes found!'
                                       '\nPlease select the mesh you want to separate!')
                return {'FINISHED'}
            obj = meshes[0]

        tools.common.separate_by_loose_parts(context, obj)

        self.report({'INFO'}, 'Successfully separated by loose parts.')
        return {'FINISHED'}


class MergeWeights(bpy.types.Operator):
    bl_idname = 'armature_manual.merge_weights'
    bl_label = 'Merge Weights'
    bl_description = 'Deletes the selected bones and adds their weight to their respective parents.\n' \
                     '\n' \
                     'Only available in Edit or Pose Mode with bones selected'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    _armature = None
    _bone_names_to_work_on = None
    _objects_to_work_on = None

    @classmethod
    def poll(cls, context):
        if bpy.context.active_object is None:
            return False

        # if bpy.context.selected_editable_bones is None:
        #     return False

        # if bpy.context.active_object.mode == 'OBJECT' and len(bpy.context.selected_bones) > 0:
        #     return True

        if bpy.context.active_object.mode == 'EDIT' and bpy.context.selected_editable_bones and len(bpy.context.selected_editable_bones) > 0:
            return True

        if bpy.context.active_object.mode == 'POSE' and bpy.context.selected_pose_bones and len(bpy.context.selected_pose_bones) > 0:
            return True

        return False

    def execute(self, context):

        error = self.mustSelectBones()
        if error:
            return error

        armature_edit_mode = ArmatureEditMode(self._armature)

        # create lookup table
        bone_name_to_edit_bone = dict()
        for edit_bone in self._armature.data.edit_bones:
            bone_name_to_edit_bone[edit_bone.name] = edit_bone

        for bone_name_to_remove in self._bone_names_to_work_on:
            if bone_name_to_edit_bone[bone_name_to_remove].parent is None:
                continue
            bone_name_to_add_weights_to = bone_name_to_edit_bone[bone_name_to_remove].parent.name
            self._armature.data.edit_bones.remove(bone_name_to_edit_bone[bone_name_to_remove])  # delete bone

            for object in self._objects_to_work_on:

                vertex_group_to_remove = object.vertex_groups.get(bone_name_to_remove)
                vertex_group_to_add_weights_to = object.vertex_groups.get(bone_name_to_add_weights_to)

                if vertex_group_to_remove is not None:

                    if vertex_group_to_add_weights_to is None:
                        vertex_group_to_add_weights_to = object.vertex_groups.new(bone_name_to_add_weights_to)

                    for vertex in object.data.vertices:  # transfer weight for each vertex
                        weight_to_transfer = 0
                        for group in vertex.groups:
                            if group.group == vertex_group_to_remove.index:
                                weight_to_transfer = group.weight
                                break
                        if weight_to_transfer > 0:
                            vertex_group_to_add_weights_to.add([vertex.index], weight_to_transfer, 'ADD')

                    object.vertex_groups.remove(vertex_group_to_remove)  # delete vertex group

        armature_edit_mode.restore()

        self.report({'INFO'}, 'Deleted ' + str(len(self._bone_names_to_work_on)) + ' bones and added their weights to their parents')

        return {'FINISHED'}

    def optionallySelectBones(self):

        armature = bpy.context.object
        if armature is None:
            self.report({'ERROR'}, 'Select something')
            return {'CANCELLED'}

        # find armature, try to select parent
        if armature is not None and armature.type != 'ARMATURE' and armature.parent is not None:
            armature = armature.parent
            if armature is not None and armature.type != 'ARMATURE' and armature.parent is not None:
                armature = armature.parent

        # find armature, try to select first and only child
        if armature is not None and armature.type != 'ARMATURE' and len(armature.children) == 1:
            armature = armature.children[0]
            if armature is not None and armature.type != 'ARMATURE' and len(armature.children) == 1:
                armature = armature.children[0]

        if armature is None or armature.type != 'ARMATURE':
            self.report({'ERROR'}, 'Select armature, it\'s child or it\'s parent')
            return {'CANCELLED'}

        # find which bones to work on
        if bpy.context.selected_editable_bones and len(bpy.context.selected_editable_bones) > 0:
            bones_to_work_on = bpy.context.selected_editable_bones
        elif bpy.context.selected_pose_bones and len(bpy.context.selected_pose_bones) > 0:
            bones_to_work_on = bpy.context.selected_pose_bones
        else:
            bones_to_work_on = armature.data.bones
        bone_names_to_work_on = set([bone.name for bone in bones_to_work_on])  # grab names only

        self._armature = armature
        self._bone_names_to_work_on = bone_names_to_work_on
        self._objects_to_work_on = armature.children

    def mustSelectBones(self):

        armature = bpy.context.object

        if armature is None or armature.type != 'ARMATURE':
            self.report({'ERROR'}, 'Select bones in armature edit or pose mode')
            return {'CANCELLED'}

        # find which bones to work on
        if bpy.context.selected_editable_bones and len(bpy.context.selected_editable_bones) > 0:
            bones_to_work_on = bpy.context.selected_editable_bones
        else:
            bones_to_work_on = bpy.context.selected_pose_bones
        bone_names_to_work_on = set([bone.name for bone in bones_to_work_on])  # grab names only

        if len(bone_names_to_work_on) == 0:
            self.report({'ERROR'}, 'Select at least one bone')
            return {'CANCELLED'}

        self._armature = armature
        self._bone_names_to_work_on = bone_names_to_work_on
        self._objects_to_work_on = armature.children


class ArmatureEditMode:
    def __init__(self, armature):
        # save user state, select armature, go to armature edit mode
        self._armature = armature
        self._active_object = bpy.context.scene.objects.active
        bpy.context.scene.objects.active = self._armature
        self._armature_hide = self._armature.hide
        self._armature.hide = False
        self._armature_mode = self._armature.mode
        tools.common.switch('EDIT')

    def restore(self):
        # restore user state
        tools.common.switch(self._armature_mode)
        self._armature.hide = self._armature_hide
        bpy.context.scene.objects.active = self._active_object


class RemoveZeroWeight(bpy.types.Operator):
    bl_idname = 'armature_manual.remove_zero_weight'
    bl_label = 'Remove Zero Weight Bones'
    bl_description = "Cleans up the bones hierarchy, deleting all bones that don't directly affect any vertices\n" \
                     "Don't use this if you plan to use 'Fix Model'"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        if tools.common.get_armature():
            return True
        return False

    def execute(self, context):
        tools.common.set_default_stage()
        count = tools.common.delete_zero_weight()
        tools.common.set_default_stage()

        self.report({'INFO'}, 'Deleted ' + str(count) + ' zero weight bones.')
        return {'FINISHED'}


class RemoveConstraints(bpy.types.Operator):
    bl_idname = 'armature_manual.remove_constraints'
    bl_label = 'Remove Bone Constraints'
    bl_description = "Removes constrains between bones causing specific bone movement as these are not used by VRChat"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        if tools.common.get_armature():
            return True
        return False

    def execute(self, context):
        tools.common.set_default_stage()
        tools.common.delete_bone_constraints()
        tools.common.set_default_stage()

        self.report({'INFO'}, 'Removed all bone constraints.')
        return {'FINISHED'}


class RecalculateNormals(bpy.types.Operator):
    bl_idname = 'armature_manual.recalculate_normals'
    bl_label = 'Recalculate Normals'
    bl_description = "Don't use this on good looking meshes as this can screw them up.\n" \
                     "Makes normals point inside of the selected mesh.\n" \
                     "Use this if there are random inverted or darker faces on the mesh"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if obj and obj.type == 'MESH':
            return True

        meshes = tools.common.get_meshes_objects()
        return meshes and len(meshes) == 1

    def execute(self, context):
        obj = context.active_object
        if not obj or (obj and obj.type != 'MESH'):
            tools.common.unselect_all()
            meshes = tools.common.get_meshes_objects()
            if len(meshes) == 0:
                return {'FINISHED'}
            obj = meshes[0]
        mesh = obj

        tools.common.select(mesh)
        tools.common.switch('EDIT')

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)

        tools.common.set_default_stage()

        self.report({'INFO'}, 'Recalculated all normals.')
        return {'FINISHED'}


class FlipNormals(bpy.types.Operator):
    bl_idname = 'armature_manual.flip_normals'
    bl_label = 'Flip Normals'
    bl_description = "Flips the direction of the faces' normals of the selected mesh.\n" \
                     "Use this if all normals are inverted"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if obj and obj.type == 'MESH':
            return True

        meshes = tools.common.get_meshes_objects()
        return meshes and len(meshes) == 1

    def execute(self, context):
        obj = context.active_object
        if not obj or (obj and obj.type != 'MESH'):
            tools.common.unselect_all()
            meshes = tools.common.get_meshes_objects()
            if len(meshes) == 0:
                return {'FINISHED'}
            obj = meshes[0]
        mesh = obj

        tools.common.select(mesh)
        tools.common.switch('EDIT')

        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.mesh.flip_normals()

        tools.common.set_default_stage()

        self.report({'INFO'}, 'Recalculated all normals.')
        return {'FINISHED'}
