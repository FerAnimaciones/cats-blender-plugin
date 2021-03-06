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

# Code author: GiveMeAllYourCats
# Repo: https://github.com/michaeldegroot/cats-blender-plugin
# Edits by: GiveMeAllYourCats, Hotox

import os
import sys
import copy
import importlib
import bpy.utils.previews

from . import addon_updater_ops
from datetime import datetime

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import mmd_tools_local
# print("\n", mmd_tools_local.bl_info["version"])
# if mmd_tools_local.bl_info["version"] == (0, 5, 0):
#     print("mmd_tools deleting!")
#     bpy.ops.wm.addon_remove(module="mmd_tools")
#     print("mmd_tools deleted!")
#     import mmd_tools_local

import tools.viseme
import tools.atlas
import tools.eyetracking
import tools.bonemerge
import tools.rootbone
import tools.translate
import tools.armature
import tools.armature_bones
import tools.armature_manual
import tools.armature_custom
import tools.material
import tools.common
import tools.supporter
import tools.credits
import tools.decimation
import tools.shapekey
import tools.copy_protection


importlib.reload(mmd_tools_local)
importlib.reload(tools.viseme)
importlib.reload(tools.atlas)
importlib.reload(tools.eyetracking)
importlib.reload(tools.bonemerge)
importlib.reload(tools.rootbone)
importlib.reload(tools.translate)
importlib.reload(tools.armature)
importlib.reload(tools.armature_bones)
importlib.reload(tools.armature_manual)
importlib.reload(tools.armature_custom)
importlib.reload(tools.material)
importlib.reload(tools.common)
importlib.reload(tools.supporter)
importlib.reload(tools.credits)
importlib.reload(tools.decimation)
importlib.reload(tools.shapekey)
importlib.reload(tools.copy_protection)

# How to update mmd_tools:
# Paste mmd_tools folder into project
# Delete mmd_tools_local folder
# Refactor folder name "mmd_tools" to "mmd_tools_local"
# Search for "show_backface_culling" and set it to False in view.py
# Done

bl_info = {
    'name': 'Cats Blender Plugin',
    'category': '3D View',
    'author': 'GiveMeAllYourCats',
    'location': 'View 3D > Tool Shelf > CATS',
    'description': 'A tool designed to shorten steps needed to import and optimize MMD models into VRChat',
    'version': [0, 8, 0],  # Only change this version and the dev branch var right before publishing the new update!
    'blender': (2, 79, 0),
    'wiki_url': 'https://github.com/michaeldegroot/cats-blender-plugin',
    'tracker_url': 'https://github.com/michaeldegroot/cats-blender-plugin/issues',
    'warning': '',
}

dev_branch = False
version = copy.deepcopy(bl_info.get('version'))

# List all the supporters here
supporters = [
    # ['Display name', 'Icon name', 'Start Date', Support Tier]  yyyy-mm-dd  The start date should be the date when the update goes live to ensure 30 days
    ['Xeverian', 'xeverian', '2017-12-19', 0],  # 45
    ['Tupper', 'tupper', '2017-12-19', 1],  # 50
    # ['Jazneo', 'jazneo', '2017-12-19', 0],
    ['idea', 'idea', '2017-12-19', 0],  # -patr
    ['RadaruS', 'radaruS', '2017-12-19', 0],  # emtpy pic
    # ['Kry10', 'kry10', '2017-12-19', 0],
    # ['Smead', 'smead', '2017-12-25', 0],
    # ['kohai.istool', 'kohai.istool', '2017-12-25', 0],
    ['Str4fe', 'str4fe', '2017-12-25', 0],  # -niem
    ["Ainrehtea Dal'Nalirtu", "Ainrehtea Dal'Nalirtu", '2017-12-25', 0],
    # ['Wintermute', 'wintermute', '2017-12-19', 0],
    ['Raikin', 'raikin', '2017-12-25', 0],  # -soni
    ['BerserkerBoreas', 'berserkerboreas', '2017-12-25', 0],
    ['ihatemondays', 'ihatemondays', '2017-12-25', 0],
    ['Derpmare', 'derpmare', '2017-12-25', 0],
    # ['Bin Chicken', 'bin_chicken', '2017-12-25', 0],
    ['Chikan Celeryman', 'chikan_celeryman', '2017-12-25', 0],
    # ['migero', 'migero', '2018-01-05', 0],
    ['Ashe', 'ashe', '2018-01-05', 0],  # 50
    ['Quadriple', 'quadriple', '2018-01-05', 0],  # 30
    ['abrownbag', 'abrownbag', '2018-01-05', 1],  # cancelled april, remove soon
    ['Azuth', 'Azuth', '2018-01-05', 0],
    ['goblox', 'goblox', '2018-01-05', 1],
    # ['Rikku', 'Rikku', '2018-01-05', 0],
    ['azupwn', 'azupwn', '2018-01-05', 0],  # cancelled may, remove soon
    ['m o t h', 'm o t h', '2018-01-05', 0],
    # ['Yorx', 'Yorx', '2018-01-05', 0],
    # ['Buffy', 'Buffy', '2018-01-05', 0],
    ['Tomnautical', 'Tomnautical', '2018-01-05', 0],  # -psyo
    # ['akarinjelly', 'Jelly', '2018-01-05', 0],
    ['Atirion', 'Atirion', '2018-01-05', 0],
    ['Lydania', 'Lydania', '2018-01-05', 0],  # -tobi
    ['Shanie', 'Shanie-senpai', '2018-01-05', 0],  # -shan
    # ['Kal [Thramis]', 'Kal', '2018-01-12', 0],
    ['Sifu', 'Sifu', '2018-01-12', 0],  # -ylon
    ['Lil Clone', 'Lil Clone', '2018-01-12', 0],  # cancelled april, remove soon
    ['Naranar', 'Naranar', '2018-01-12', 1],
    # ['gwigz', 'gwigz', '2018-01-12', 0],
    # ['Lux', 'Lux', '2018-01-12', 0],
    ['liquid (retso)', 'liquid', '2018-01-12', 0],  # -oste
    # ['GreenTeaGamer', 'GreenTeaGamer', '2018-01-12', 0],
    # ['Desruko', 'Desruko', '2018-01-12', 0],
    ['Mute_', 'Mute_', '2018-01-12', 0],
    # icewind (don't add)
    ['qy_li', 'qy_li', '2018-01-22', 1],  # emtpy pic  - lqy
    # ['Sixnalia', 'Sixnalia', '2018-01-22', 0],
    ['ReOL', 'ReOL', '2018-01-22', 0],  # emtpy pic
    ['Rezinion', 'Rezinion', '2018-01-22', 0],
    ['Karma', 'Karma', '2018-01-22', 0],
    # ['\1B', 'BOXMOB', '2018-01-22', 0],
    # ['\2O', 'BOXMOB', '2018-01-22', 0],
    # ['\3X', 'BOXMOB', '2018-01-22', 0],
    # ['\1M', 'BOXMOB', '2018-01-22', 0],
    # ['\2O', 'BOXMOB', '2018-01-22', 0],
    # ['\3B', 'BOXMOB', '2018-01-22', 0],
    ['SolarSnowball', 'SolarSnowball', '2018-01-22', 0],  # is later in form list
    # ['Hordaland', 'Hordaland', '2018-01-22', 0],
    ['Bones', 'Bones', '2018-01-22', 0],  # PP 50
    # Joshua (onodaTV)    # cancelled april, don't add
    # charlie (discord) 24th missing
    ['Axo_', 'Axo_', '2018-04-10', 0],
    # Jerry (jt1990)
    ['Dogniss', 'Dogniss', '2018-03-10', 0],  # -Forc
    ['Syntion', 'Syntion', '2018-05-13', 0],  # -fabi
    ['Sheet_no_mana', 'Sheet_no_mana', '2018-04-10', 0],  # emtpy pic  -fina
    # Marcus (m.johannson) (ignore)
    ['Awrini', 'Awrini', '2018-03-10', 0],
    # ['Smooth', 'Smooth', '2018-03-10', 0],
    # FlammaRilva (fls81245) (ignore)
    ['NekoNatsuki', 'NekoNatsuki', '2018-03-10', 0],  # 42
    # Checked until here

    ['AlphaSatanOmega', 'AlphaSatanOmega', '2018-03-10', 0],
    # Murakuumoo (murakuumoo)
    ['Curio', 'Curio', '2018-03-10', 1],
    ['Deathofirish', 'Deathofirish', '2018-04-17', 0],  # emtpy pic  -jaco
    # eduardo (botello.eduardo19)
    ['Runda', 'Runda', '2018-04-17', 0],
    ['Rurikaze', 'Rurikaze', '2018-05-09', 0],  # -mist
    ['Brindin_wF', 'Brindin_wF', '2018-04-17', 0],  # -Bran
    ['Serry Jane', 'Serry_Jane', '2018-04-17', 1],  # emtpy pic  -ianc
    ['GV-97', 'GV-97', '2018-05-09', 0],  # -niels
    ['COMMEN', 'COMMEN', '2018-05-09', 0],  # emtpy pic  -do20
    ['Antivirus-Chan', 'Antivirus-Chan', '2018-05-09', 0],  #  -frost
    ['Rayduxz', 'Rayduxz', '2018-05-09', 0],  #  -hats
    ['BemVR', 'BemVR', '2018-05-14', 0],  #  -bemv
    # PorcelainShrine (questzero)
]

current_supporters = None


class ToolPanel:
    bl_label = 'Cats Blender Plugin'
    bl_idname = '3D_VIEW_TS_vrc'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'CATS'

    # Armature
    bpy.types.Scene.import_mode = bpy.props.EnumProperty(
        name="Import Mode",
        description="Import Mode",
        items=[
            ("MMD", "MMD", 'Import .pmx/.pmd files'),
            ("XPS", "XNALara", 'Import .xps/.mesh/.ascii files'),
            ("FBX", "FBX", 'Import .fbx files'),
        ],
        default='MMD'
    )

    bpy.types.Scene.armature = bpy.props.EnumProperty(
        name='Armature',
        description='Select the armature which will be used by Cats',
        items=tools.common.get_armature_list
    )

    bpy.types.Scene.full_body = bpy.props.BoolProperty(
        name='Apply Full Body Tracking Fix',
        description="Applies a general fix for Full Body Tracking.\n"
                    'Can potentially reduce the knee bending of every avatar in VRChat.\n'
                    'You can safely ignore the "Spine length zero" warning in Unity.\n'
                    'If you have problems with the hips ingame, uncheck this option and tell us!\n',
        default=False
    )

    bpy.types.Scene.remove_zero_weight = bpy.props.BoolProperty(
        name='Remove Zero Weight Bones',
        description="Cleans up the bones hierarchy, deleting all bones that don't directly affect any vertices.\n"
                    'Uncheck this if bones you want to keep got deleted',
        default=True
    )

    bpy.types.Scene.merge_mode = bpy.props.EnumProperty(
        name="Merge Mode",
        description="Mode",
        items=[
            ("ARMATURE", "Merge Armatures", "Here you can merge two armatures together."),
            ("MESH", "Attach Mesh", "Here you can attach a mesh to an armature.")
        ]
    )

    bpy.types.Scene.merge_armature_into = bpy.props.EnumProperty(
        name='Base Armature',
        description='Select the armature into which the other armature will be merged\n',
        items=tools.common.get_armature_list
    )

    bpy.types.Scene.attach_to_bone = bpy.props.EnumProperty(
        name='Attach to Bone',
        description='Select the bone to which the armature will be attached to\n',
        items=tools.common.get_bones_merge
    )

    bpy.types.Scene.merge_armature = bpy.props.EnumProperty(
        name='Merge Armature',
        description='Select the armature which will be merged into the selected armature above\n',
        items=tools.common.get_armature_merge_list
    )

    bpy.types.Scene.attach_mesh = bpy.props.EnumProperty(
        name='Attach Mesh',
        description='Select the mesh which will be attached to the selected bone in the selected armature\n',
        items=tools.common.get_top_meshes
    )

    # Decimation
    bpy.types.Scene.decimation_mode = bpy.props.EnumProperty(
        name="Decimation Mode",
        description="Decimation Mode",
        items=[
            ("SAFE", "Safe", 'Decent results - no shape key loss\n'
                             '\n'
                             "This will only decimate meshes with no shape keys.\n"
                             "The results are decent and you won't lose any shape keys.\n"
                             'Eye Tracking and Lip Syncing will be fully preserved.'),

            ("HALF", "Half", 'Good results - minimal shape key loss\n'
                             "\n"
                             "This will only decimate meshes with less than 4 shape keys as those are often not used.\n"
                             'The results are better but you will lose the shape keys in some meshes.\n'
                             'Eye Tracking and Lip Syncing should still work.'),

            ("FULL", "Full", 'Best results - full shape key loss\n'
                             '\n'
                             "This will decimate your whole model deleting all shape keys in the process.\n"
                             'This will give the best results but you will lose the ability to add blinking and Lip Syncing.\n'
                             'Eye Tracking will still work if you disable Eye Blinking.'),

            ("CUSTOM", "Custom", 'Custom results - custom shape key loss\n'
                                 '\n'
                                 "This will let you choose which meshes and shape keys should not be decimated.\n")
        ],
        default='HALF'
    )

    bpy.types.Scene.selection_mode = bpy.props.EnumProperty(
        name="Selection Mode",
        description="Selection Mode",
        items=[
            ("SHAPES", "Shape Keys", 'Select all the shape keys you want to preserve here.'),
            ("MESHES", "Meshes", "Select all the meshes you don't want to decimate here.")
        ]
    )

    bpy.types.Scene.add_shape_key = bpy.props.EnumProperty(
        name='Shape',
        description='The shape key you want to keep',
        items=tools.common.get_shapekeys_decimation
    )

    bpy.types.Scene.add_mesh = bpy.props.EnumProperty(
        name='Mesh',
        description='The mesh you want to leave untouched by the decimation',
        items=tools.common.get_meshes_decimation
    )

    bpy.types.Scene.decimate_fingers = bpy.props.BoolProperty(
        name="Save Fingers",
        description="Check this if you don't want to decimate your fingers!\n"
                    "Results will be worse but there will be no issues with finger movement.\n"
                    "This is probably only useful if you have a VR headset.\n"
                    "\n"
                    "This operation requires the finger bones to be named specifically:\n"
                    "Thumb(0-2)_(L/R)\n"
                    "IndexFinger(1-3)_(L/R)\n"
                    "MiddleFinger(1-3)_(L/R)\n"
                    "RingFinger(1-3)_(L/R)\n"
                    "LittleFinger(1-3)_(L/R)"
    )

    bpy.types.Scene.decimate_hands = bpy.props.BoolProperty(
        name="Save Hands",
        description="Check this if you don't want to decimate your full hands!\n"
                    "Results will be worse but there will be no issues with hand movement.\n"
                    "This is probably only useful if you have a VR headset.\n"
                    "\n"
                    "This operation requires the finger and hand bones to be named specifically:\n"
                    "Left/Right wrist\n"
                    "Thumb(0-2)_(L/R)\n"
                    "IndexFinger(1-3)_(L/R)\n"
                    "MiddleFinger(1-3)_(L/R)\n"
                    "RingFinger(1-3)_(L/R)\n"
                    "LittleFinger(1-3)_(L/R)"
    )

    bpy.types.Scene.max_tris = bpy.props.IntProperty(
        name='Tris',
        description="The target amount of tris after decimation",
        default=19999,
        min=1,
        max=100000
    )

    # Eye Tracking
    bpy.types.Scene.eye_mode = bpy.props.EnumProperty(
        name="Eye Mode",
        description="Mode",
        items=[
            ("CREATION", "Creation", "Here you can create eye tracking."),
            ("TESTING", "Testing", "Here you can test how eye tracking will look ingame.")
        ],
        update=tools.eyetracking.stop_testing
    )

    bpy.types.Scene.mesh_name_eye = bpy.props.EnumProperty(
        name='Mesh',
        description='The mesh with the eyes vertex groups',
        items=tools.common.get_meshes
    )

    bpy.types.Scene.head = bpy.props.EnumProperty(
        name='Head',
        description='The head bone containing the eye bones',
        items=tools.common.get_bones_head
    )

    bpy.types.Scene.eye_left = bpy.props.EnumProperty(
        name='Left Eye',
        description='The models left eye bone',
        items=tools.common.get_bones_eye_l
    )

    bpy.types.Scene.eye_right = bpy.props.EnumProperty(
        name='Right Eye',
        description='The models right eye bone',
        items=tools.common.get_bones_eye_r
    )

    bpy.types.Scene.wink_left = bpy.props.EnumProperty(
        name='Blink Left',
        description='The shape key containing a blink with the left eye',
        items=tools.common.get_shapekeys_eye_blink_l
    )

    bpy.types.Scene.wink_right = bpy.props.EnumProperty(
        name='Blink Right',
        description='The shape key containing a blink with the right eye',
        items=tools.common.get_shapekeys_eye_blink_r
    )

    bpy.types.Scene.lowerlid_left = bpy.props.EnumProperty(
        name='Lowerlid Left',
        description='The shape key containing a slightly raised left lower lid.\n'
                    'Can be set to "Basis" to disable lower lid movement',
        items=tools.common.get_shapekeys_eye_low_l
    )

    bpy.types.Scene.lowerlid_right = bpy.props.EnumProperty(
        name='Lowerlid Right',
        description='The shape key containing a slightly raised right lower lid.\n'
                    'Can be set to "Basis" to disable lower lid movement',
        items=tools.common.get_shapekeys_eye_low_r
    )

    bpy.types.Scene.disable_eye_movement = bpy.props.BoolProperty(
        name='Disable Eye Movement',
        description='IMPORTANT: Do your decimation first if you check this!\n'
                    '\n'
                    'Disables eye movement. Useful if you only want blinking.\n'
                    'This creates eye bones with no movement bound to them.\n'
                    'You still have to assign "LeftEye" and "RightEye" to the eyes in Unity',
        subtype='DISTANCE'
    )

    bpy.types.Scene.disable_eye_blinking = bpy.props.BoolProperty(
        name='Disable Eye Blinking',
        description='Disables eye blinking. Useful if you only want eye movement.\n'
                    'This will create the necessary shape keys but leaves them empty',
        subtype='NONE'
    )

    bpy.types.Scene.eye_distance = bpy.props.FloatProperty(
        name='Eye Movement Range',
        description='Higher = more eye movement\n'
                    'Lower = less eye movement\n'
                    'Warning: Too little or too much range can glitch the eyes.\n'
                    'Test your results in the "Eye Testing"-Tab!\n',
        default=0.8,
        min=0.0,
        max=2.0,
        step=1.0,
        precision=2,
        subtype='FACTOR'
    )

    bpy.types.Scene.eye_rotation_x = bpy.props.IntProperty(
        name='Up - Down',
        description='Rotate the eye bones on the vertical axis',
        default=0,
        min=-19,
        max=25,
        step=1,
        subtype='FACTOR',
        update=tools.eyetracking.set_rotation
    )

    bpy.types.Scene.eye_rotation_y = bpy.props.IntProperty(
        name='Left - Right',
        description='Rotate the eye bones on the horizontal axis.'
                    '\nThis is from your own point of view',
        default=0,
        min=-19,
        max=19,
        step=1,
        subtype='FACTOR',
        update=tools.eyetracking.set_rotation
    )

    bpy.types.Scene.iris_height = bpy.props.IntProperty(
        name='Iris Height',
        description='Moves the iris away from the eye ball',
        default=0,
        min=0,
        max=100,
        step=1,
        subtype='FACTOR'
    )

    bpy.types.Scene.eye_blink_shape = bpy.props.FloatProperty(
        name='Blink Strength',
        description='Test the blinking of the eye',
        default=1.0,
        min=0.0,
        max=1.0,
        step=1.0,
        precision=2,
        subtype='FACTOR'
    )

    bpy.types.Scene.eye_lowerlid_shape = bpy.props.FloatProperty(
        name='Lowerlid Strength',
        description='Test the lowerlid blinking of the eye',
        default=1.0,
        min=0.0,
        max=1.0,
        step=1.0,
        precision=2,
        subtype='FACTOR'
    )

    # Visemes
    bpy.types.Scene.mesh_name_viseme = bpy.props.EnumProperty(
        name='Mesh',
        description='The mesh with the mouth shape keys',
        items=tools.common.get_meshes
    )

    bpy.types.Scene.mouth_a = bpy.props.EnumProperty(
        name='Viseme AA',
        description='Shape key containing mouth movement that looks like someone is saying "aa".\nDo not put empty shape keys like "Basis" in here',
        items=tools.common.get_shapekeys_mouth_ah,
    )

    bpy.types.Scene.mouth_o = bpy.props.EnumProperty(
        name='Viseme OH',
        description='Shape key containing mouth movement that looks like someone is saying "oh".\nDo not put empty shape keys like "Basis" in here',
        items=tools.common.get_shapekeys_mouth_oh,
    )

    bpy.types.Scene.mouth_ch = bpy.props.EnumProperty(
        name='Viseme CH',
        description='Shape key containing mouth movement that looks like someone is saying "ch". Opened lips and clenched teeth.\nDo not put empty shape keys like "Basis" in here',
        items=tools.common.get_shapekeys_mouth_ch,
    )

    bpy.types.Scene.shape_intensity = bpy.props.FloatProperty(
        name='Shape Key Mix Intensity',
        description='Controls the strength in the creation of the shape keys. Lower for less mouth movement strength',
        default=1.0,
        min=0.0,
        max=1.0,
        step=0.1,
        precision=2,
        subtype='FACTOR'
    )

    # Bone Parenting
    bpy.types.Scene.root_bone = bpy.props.EnumProperty(
        name='To Parent',
        description='List of bones that look like they could be parented together to a root bone',
        items=tools.rootbone.get_parent_root_bones,
    )

    # Optimize
    bpy.types.Scene.optimize_mode = bpy.props.EnumProperty(
        name="Optimize Mode",
        description="Mode",
        items=[
            ("ATLAS", "Atlas", "Allows you to make a texture atlas."),
            ("MATERIAL", "Material", "Some various options on material manipulation."),
            ("BONEMERGING", "Bone Merging", "Allows child bones to be merged into their parents."),
        ]
    )

    bpy.types.Scene.island_margin = bpy.props.FloatProperty(
        name='Margin',
        description='Margin to reduce bleed of adjacent islands',
        default=0.01,
        min=0.0,
        max=1.0,
        step=0.1,
        precision=2,
        subtype='FACTOR'
    )

    bpy.types.Scene.area_weight = bpy.props.FloatProperty(
        name='Area Weight',
        description='Weight projections vector by faces with larger areas',
        default=0.0,
        min=0.0,
        max=1.0,
        step=0.1,
        precision=2,
        subtype='FACTOR'
    )

    bpy.types.Scene.angle_limit = bpy.props.FloatProperty(
        name='Angle',
        description='Lower for more projection groups, higher for less distortion',
        default=82.0,
        min=1.0,
        max=89.0,
        step=10.0,
        precision=1,
        subtype='FACTOR'
    )

    bpy.types.Scene.texture_size = bpy.props.EnumProperty(
        name='Texture Size',
        description='Lower for faster bake time, higher for more detail',
        items=tools.common.get_texture_sizes
    )

    bpy.types.Scene.one_texture = bpy.props.BoolProperty(
        name='One Texture Material',
        description='Texture baking and multiple textures per material can look weird in the end result. Check this box if you are experiencing this',
        default=True
    )

    bpy.types.Scene.pack_islands = bpy.props.BoolProperty(
        name='Pack Islands',
        description='Transform all islands so that they will fill up the UV space as much as possible',
        default=False
    )

    bpy.types.Scene.mesh_name_atlas = bpy.props.EnumProperty(
        name='Target Mesh',
        description='The mesh that you want to create a atlas from',
        items=tools.common.get_all_meshes
    )

    # Bone Merging
    bpy.types.Scene.merge_ratio = bpy.props.FloatProperty(
        name='Merge Ratio',
        description='Higher = more bones will be merged\n'
                    'Lower = less bones will be merged\n',
        default=50,
        min=1,
        max=100,
        step=1,
        precision=0,
        subtype='PERCENTAGE'
    )

    bpy.types.Scene.merge_mesh = bpy.props.EnumProperty(
        name='Mesh',
        description='The mesh with the bones vertex groups',
        items=tools.common.get_meshes
    )

    bpy.types.Scene.merge_bone = bpy.props.EnumProperty(
        name='To Merge',
        description='List of bones that look like they could be merged together to reduce overall bones',
        items=tools.rootbone.get_parent_root_bones,
    )

    # Copy Protection - obsolete
    # bpy.types.Scene.protection_mode = bpy.props.EnumProperty(
    #     name="Randomization Level",
    #     description="Randomization Level",
    #     items=[
    #         ("FULL", "Full", "This will randomize every vertex of your model and it will be completely unusable for thieves.\n"
    #                          'However this method might cause problems with the Outline option from Cubed shader.\n'
    #                          'If you have any issues ingame try again with option "Partial".'),
    #         ("PARTIAL", "Partial", 'Use this if you experience issues ingame with the Full option!\n'
    #                                '\n'
    #                                "This will only randomize a number of vertices and therefore will have a few unprotected areas,\n"
    #                                "but it's still unusable to thieves as a whole.\n"
    #                                'This method however reduces the glitches that can occur ingame by a lot.')
    #     ],
    #     default='FULL'
    # )


class ArmaturePanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_armature_v1'
    bl_label = 'Model'

    def draw(self, context):
        addon_updater_ops.check_for_update_background()

        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        if bpy.app.version < (2, 79, 0):
            col.separator()
            col.label('Old Blender version detected!', icon='ERROR')
            col.label('Some features might not work!', icon='ERROR')
            col.label('Please update to Blender 2.79!', icon='ERROR')
            col.separator()
            col.separator()

        # elif bpy.app.version == (2, 79, "a"):
        #     col.separator()
        #     col.separator()
        #     col.separator()
        #     col.label('Not supported Blender version detected!', icon='ERROR')
        #     col.label('Some features might not work!', icon='ERROR')
        #     col.label('Please use to Blender 2.79!', icon='ERROR')
        #     col.separator()
        #     col.separator()
        #     col.separator()
        #     col.separator()

        if addon_updater_ops.updater.update_ready:
            col.separator()
            col.label('New Cats version available!', icon='INFO')
            col.label('Check the Updater panel!', icon='INFO')
            col.separator()
            col.separator()

        # Show news from the plugin
        if tools.supporter.supporter_data and tools.supporter.supporter_data.get('news') and tools.supporter.supporter_data.get('news'):
            showed_info = False
            for i, news in enumerate(tools.supporter.supporter_data.get('news')):
                info = news.get('info')
                icon = news.get('icon')
                custom_icon = news.get('custom_icon')
                if info:
                    showed_info = True

                    row = col.row(align=True)
                    row.scale_y = 0.75
                    if custom_icon:
                        try:
                            row.label(info, icon_value=tools.supporter.preview_collections["supporter_icons"][custom_icon].icon_id)
                        except KeyError:
                            row.label(info)
                    elif icon:
                        try:
                            row.label(info, icon=icon)
                        except TypeError:
                            row.label(info)
                    else:
                        row.label(info)
            if showed_info:
                col.separator()
                col.separator()

        row = col.row(align=True)
        row.prop(context.scene, 'import_mode', expand=True)
        row = col.row(align=True)
        row.scale_y = 1.4
        row.operator('armature_manual.import_model', icon='ARMATURE_DATA')

        if tools.common.get_armature():
            row.operator('armature_manual.export_model', icon='ARMATURE_DATA')

        arm_count = len(tools.common.get_armature_objects())
        if arm_count == 0:
            return
        elif arm_count > 1:
            col.separator()
            col.separator()
            col.separator()
            row = col.row(align=True)
            row.scale_y = 1.1
            row.prop(context.scene, 'armature', icon='ARMATURE_DATA')

        col.separator()
        col.separator()
        row = col.row(align=True)
        row.prop(context.scene, 'full_body')
        row = col.row(align=True)
        row.prop(context.scene, 'remove_zero_weight')
        row = col.row(align=True)
        row.scale_y = 1.4
        row.operator('armature.fix', icon='BONE_DATA')

        if context.scene.full_body:
            row = col.row(align=True)
            row.scale_y = 0.9
            row.label('You can safely ignore the', icon='INFO')
            row = col.row(align=True)
            row.scale_y = 0.5
            row.label('"Spine length zero" warning in Unity.', icon_value=tools.supporter.preview_collections["custom_icons"]["empty"].icon_id)
            col.separator()

        col.separator()
        col.separator()
        ob = bpy.context.active_object
        if not ob or ob.mode != 'POSE':
            row = col.row(align=True)
            row.scale_y = 1.05
            row.operator('armature_manual.start_pose_mode', icon='POSE_HLT')
        else:
            row = col.row(align=True)
            row.scale_y = 1.05
            row.operator('armature_manual.stop_pose_mode', icon='POSE_DATA')
            if not tools.eyetracking.eye_left:
                row = col.row(align=True)
                row.scale_y = 1.05
                row.operator('armature_manual.pose_to_shape', icon='SHAPEKEY_DATA')

        # addon_updater_ops.update_notice_box_ui(self, context)


class ManualPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_manual_v1'
    bl_label = 'Model Options'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        # if not context.scene.show_manual_options:
        #     row = col.row(align=False)
        #     row.prop(context.scene, 'show_manual_options', emboss=True, expand=False, icon='TRIA_RIGHT')
        # else:
        #     row = col.row(align=True)
        #     row.prop(context.scene, 'show_manual_options', emboss=True, expand=False, icon='TRIA_DOWN')

        row = col.row(align=True)
        row.scale_y = 1.05
        row.label("Separate by:", icon='MESH_DATA')
        row.operator('armature_manual.separate_by_materials', text='Materials')
        row.operator('armature_manual.separate_by_loose_parts', text='Loose Parts')
        row = col.row(align=True)
        row.scale_y = 1.05
        row.operator('armature_manual.join_meshes', icon='MESH_DATA')

        col.separator()
        col.separator()
        row = col.split(percentage=0.23, align=True)
        row.scale_y = 1.05
        row.label("Delete:", icon='X')
        row.operator('armature_manual.remove_zero_weight', text='Zero Weight Bones')
        row.operator('armature_manual.remove_constraints', text='Constraints')
        row = col.row(align=True)
        row.scale_y = 1.05
        row.operator('armature_manual.merge_weights', icon='BONE_DATA')

        col.separator()
        col.separator()
        row = col.split(percentage=0.27, align=True)
        row.scale_y = 1.05
        row.label("Normals:", icon='SNAP_NORMAL')
        row.operator('armature_manual.recalculate_normals', text='Recalculate')
        row.operator('armature_manual.flip_normals', text='Flip')

        col.separator()
        row = col.row(align=True)
        # row.label("Translation:", icon_value=tools.supporter.preview_collections["custom_icons"]["TRANSLATE"].icon_id)
        row.label("Translation:", icon='FILE_REFRESH')
        row = col.row(align=True)
        row.scale_y = 1.05
        row.operator('translate.shapekeys', icon='SHAPEKEY_DATA')
        row.operator('translate.bones', icon='BONE_DATA')
        row = col.row(align=True)
        row.scale_y = 1.05
        row.operator('translate.meshes', icon='MESH_DATA')
        row.operator('translate.materials', icon='MATERIAL')


class CustomPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_custom_v1'
    bl_label = 'Custom Model Creation'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        row = col.row(align=True)
        row.operator('armature_custom.button', text='How to Use', icon='FORWARD')
        col.separator()

        row = col.row(align=True)
        row.prop(context.scene, 'merge_mode', expand=True)
        col.separator()

        # Merge Armatures
        if context.scene.merge_mode == 'ARMATURE':
            row = col.row(align=True)
            row.scale_y = 1.05
            row.label('Merge Armatures:')

            if len(tools.common.get_armature_objects()) <= 1:
                row = col.row(align=True)
                row.scale_y = 1.05
                col.label('Two armatures are required!', icon='INFO')
                return

            row = col.row(align=True)
            row.scale_y = 1.05
            row.prop(context.scene, 'merge_armature_into', text='Base', icon='OUTLINER_OB_ARMATURE')
            row = col.row(align=True)
            row.scale_y = 1.05
            row.prop(context.scene, 'merge_armature', text='To Merge', icon_value=tools.supporter.preview_collections["custom_icons"]["UP_ARROW"].icon_id)

            found = False
            base_armature = tools.common.get_armature(armature_name=context.scene.merge_armature_into)
            merge_armature = tools.common.get_armature(armature_name=context.scene.merge_armature)
            if merge_armature:
                for bone in tools.armature_bones.dont_delete_these_main_bones:
                    if 'Eye' not in bone and bone in merge_armature.pose.bones and bone in base_armature.pose.bones:
                        found = True
                        break

            if not found:
                row = col.row(align=True)
                row.scale_y = 1.05
                row.prop(context.scene, 'attach_to_bone', text='Attach to', icon='BONE_DATA')
            else:
                row = col.row(align=True)
                row.scale_y = 1.05
                row.label('Armatures can be automatically merged!')

            row = col.row(align=True)
            row.scale_y = 1.2
            row.operator('armature_custom.merge_armatures', icon='ARMATURE_DATA')

        # Attach Mesh
        else:
            row = col.row(align=True)
            row.scale_y = 1.05
            row.label('Attach Mesh to Armature:')

            if len(tools.common.get_armature_objects()) == 0 or len(tools.common.get_meshes_objects(mode=1)) == 0:
                row = col.row(align=True)
                row.scale_y = 1.05
                col.label('An armature and a mesh are required!', icon='INFO')
                return

            row = col.row(align=True)
            row.scale_y = 1.05
            row.prop(context.scene, 'merge_armature_into', text='Base', icon='OUTLINER_OB_ARMATURE')
            row = col.row(align=True)
            row.scale_y = 1.05
            row.prop(context.scene, 'attach_mesh', text='Mesh', icon_value=tools.supporter.preview_collections["custom_icons"]["UP_ARROW"].icon_id)

            row = col.row(align=True)
            row.scale_y = 1.05
            row.prop(context.scene, 'attach_to_bone', text='Attach to', icon='BONE_DATA')

            row = col.row(align=True)
            row.scale_y = 1.2
            row.operator('armature_custom.attach_mesh', icon='ARMATURE_DATA')


class DecimationPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_decimation_v1'
    bl_label = 'Decimation'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        row = col.row(align=True)
        row.label('Auto Decimation is currently experimental.')
        row = col.row(align=True)
        row.scale_y = 0.5
        row.label('It works but it might not look good. Test for yourself.')
        col.separator()
        row = col.row(align=True)
        row.label('Decimation Mode:')
        row = col.row(align=True)
        row.prop(context.scene, 'decimation_mode', expand=True)
        row = col.row(align=True)
        row.scale_y = 0.7
        if context.scene.decimation_mode == 'SAFE':
            row.label(' Decent results - No shape key loss')
        elif context.scene.decimation_mode == 'HALF':
            row.label(' Good results - Minimal shape key loss')
        elif context.scene.decimation_mode == 'FULL':
            row.label(' Best results - Full shape key loss')

        elif context.scene.decimation_mode == 'CUSTOM':
            col.separator()

            if len(tools.common.get_meshes_objects()) <= 1:
                row = col.row(align=True)
                row.label('Start by Separating by Materials:')
                row = col.row(align=True)
                row.scale_y = 1.2
                row.operator('armature_manual.separate_by_materials', text='Separate by Materials', icon='PLAY')
                return
            else:
                row = col.row(align=True)
                row.label('Stop by Joining Meshes:')
                row = col.row(align=True)
                row.scale_y = 1.2
                row.operator('armature_manual.join_meshes', icon='PAUSE')

            col.separator()
            col.separator()
            row = col.row(align=True)
            row.label('Whitelisted:')
            row = col.row(align=True)
            row.prop(context.scene, 'selection_mode', expand=True)
            col.separator()
            col.separator()

            if context.scene.selection_mode == 'SHAPES':
                row = col.split(0.7)
                row.prop(context.scene, 'add_shape_key', icon='SHAPEKEY_DATA')
                row.operator('add.shape', icon='ZOOMIN')
                col.separator()

                box2 = col.box()
                col = box2.column(align=True)

                if len(tools.decimation.ignore_shapes) == 0:
                    col.label('No shape key selected')

                for shape in tools.decimation.ignore_shapes:
                    row = col.split(0.8)
                    row.label(shape, icon='SHAPEKEY_DATA')
                    op = row.operator('remove.shape', icon='ZOOMOUT')
                    op.shape_name = shape
            elif context.scene.selection_mode == 'MESHES':
                row = col.split(0.7)
                row.prop(context.scene, 'add_mesh', icon='MESH_DATA')
                row.operator('add.mesh', icon='ZOOMIN')
                col.separator()

                if context.scene.add_mesh == '':
                    row = col.row(align=True)
                    col.label('Every mesh is selected. This equals no Decimation.', icon='ERROR')

                box2 = col.box()
                col = box2.column(align=True)

                if len(tools.decimation.ignore_meshes) == 0:
                    col.label('No mesh selected')

                for mesh in tools.decimation.ignore_meshes:
                    row = col.split(0.8)
                    row.label(mesh, icon='MESH_DATA')
                    op = row.operator('remove.mesh', icon='ZOOMOUT')
                    op.mesh_name = mesh

            col = box.column(align=True)

            if len(tools.decimation.ignore_shapes) == 0 and len(tools.decimation.ignore_meshes) == 0:
                col.label('Both lists are empty, this equals Full Decimation!', icon='ERROR')
                row = col.row(align=True)
            else:
                col.label('Both whitelists are considered during decimation', icon='INFO')
                row = col.row(align=True)

            # # row = col.row(align=True)
            # # rows = 2
            # # row = layout.row()
            # # row.template_list("auto.decimate_list", "", bpy.context.scene, "auto", bpy.context.scene, "custom_index", rows=rows)
            #
            # obj = context.object
            #
            # # template_list now takes two new args.
            # # The first one is the identifier of the registered UIList to use (if you want only the default list,
            # # with no custom draw code, use "UI_UL_list").
            # layout.template_list("ShapekeyList", "", ('heyho', 'heyho2'), "material_slots", ('heyho', 'heyho2'), "active_material_index")

        col.separator()
        col.separator()
        row = col.row(align=True)
        row.prop(context.scene, 'decimate_fingers')
        row = col.row(align=True)
        row.prop(context.scene, 'max_tris')
        col.separator()
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator('auto.decimate', icon='MOD_DECIM')


# class ShapekeyList(bpy.types.UIList):
#     # The draw_item function is called for each item of the collection that is visible in the list.
#     #   data is the RNA object containing the collection,
#     #   item is the current drawn item of the collection,
#     #   icon is the "computed" icon for the item (as an integer, because some objects like materials or textures
#     #   have custom icons ID, which are not available as enum items).
#     #   active_data is the RNA object containing the active property for the collection (i.e. integer pointing to the
#     #   active item of the collection).
#     #   active_propname is the name of the active property (use 'getattr(active_data, active_propname)').
#     #   index is index of the current item in the collection.
#     #   flt_flag is the result of the filtering process for this item.
#     #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
#     #         need them.
#     def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
#         layout.label(text=item.name, translate=False, icon='SHAPEKEY_DATA')
#         # split.prop(item, "name", text="", emboss=False, translate=False, icon='BORDER_RECT')
#
#
# class Uilist_actions(bpy.types.Operator):
#     bl_idname = "custom.list_action"
#     bl_label = "List Action"


class EyeTrackingPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_eye_v1'
    bl_label = 'Eye Tracking'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        row = col.row(align=True)
        row.prop(context.scene, 'eye_mode', expand=True)

        if context.scene.eye_mode == 'CREATION':

            mesh_count = len(tools.common.get_meshes_objects())
            if mesh_count == 0:
                col.separator()
                row = col.row(align=True)
                row.scale_y = 1.1
                row.label('No meshes found!', icon='ERROR')
            elif mesh_count > 1:
                col.separator()
                row = col.row(align=True)
                row.scale_y = 1.1
                row.prop(context.scene, 'mesh_name_eye', icon='MESH_DATA')

            col.separator()
            row = col.row(align=True)
            row.scale_y = 1.1
            row.prop(context.scene, 'head', icon='BONE_DATA')
            row = col.row(align=True)
            row.scale_y = 1.1
            if context.scene.disable_eye_movement:
                row.active = False
            row.prop(context.scene, 'eye_left', icon='BONE_DATA')
            row = col.row(align=True)
            row.scale_y = 1.1
            if context.scene.disable_eye_movement:
                row.active = False
            row.prop(context.scene, 'eye_right', icon='BONE_DATA')

            col.separator()
            row = col.row(align=True)
            row.scale_y = 1.1
            if context.scene.disable_eye_blinking:
                row.active = False
            row.prop(context.scene, 'wink_left', icon='SHAPEKEY_DATA')
            row = col.row(align=True)
            row.scale_y = 1.1
            if context.scene.disable_eye_blinking:
                row.active = False
            row.prop(context.scene, 'wink_right', icon='SHAPEKEY_DATA')
            row = col.row(align=True)
            row.scale_y = 1.1
            if context.scene.disable_eye_blinking:
                row.active = False
            row.prop(context.scene, 'lowerlid_left', icon='SHAPEKEY_DATA')
            row = col.row(align=True)
            row.scale_y = 1.1
            if context.scene.disable_eye_blinking:
                row.active = False
            row.prop(context.scene, 'lowerlid_right', icon='SHAPEKEY_DATA')

            col.separator()
            row = col.row(align=True)
            row.prop(context.scene, 'disable_eye_blinking')

            row = col.row(align=True)
            row.prop(context.scene, 'disable_eye_movement')

            if not context.scene.disable_eye_movement:
                col.separator()
                row = col.row(align=True)
                row.prop(context.scene, 'eye_distance')

            col = box.column(align=True)
            row = col.row(align=True)
            row.operator('create.eyes', icon='TRIA_RIGHT')

            # armature = common.get_armature()
            # if "RightEye" in armature.pose.bones:
            #     row = col.row(align=True)
            #     row.label('Eye Bone Tweaking:')
        else:
            armature = tools.common.get_armature()
            if not armature:
                box.label('No model found!', icon='ERROR')
                return

            if bpy.context.active_object is not None and bpy.context.active_object.mode != 'POSE':
                col.separator()
                row = col.row(align=True)
                row.scale_y = 1.5
                row.operator('eyes.test', icon='TRIA_RIGHT')
            else:
                # col.separator()
                # row = col.row(align=True)
                # row.operator('eyes.test_stop', icon='PAUSE')

                col.separator()
                col.separator()
                row = col.row(align=True)
                row.prop(context.scene, 'eye_rotation_x', icon='FILE_PARENT')
                row = col.row(align=True)
                row.prop(context.scene, 'eye_rotation_y', icon='ARROW_LEFTRIGHT')
                row = col.row(align=True)
                row.operator('eyes.reset_rotation', icon='MAN_ROT')

                # global slider_z
                # if context.scene.eye_blink_shape != slider_z:
                #     slider_z = context.scene.eye_blink_shape
                #     eyetracking.update_bones(context, slider_z)

                col.separator()
                col.separator()
                row = col.row(align=True)
                row.prop(context.scene, 'eye_distance')
                row = col.row(align=True)
                row.operator('eyes.adjust_eyes', icon='CURVE_NCIRCLE')

                col.separator()
                col.separator()
                row = col.row(align=True)
                row.prop(context.scene, 'eye_blink_shape')
                row.operator('eyes.test_blink', icon='RESTRICT_VIEW_OFF')
                row = col.row(align=True)
                row.prop(context.scene, 'eye_lowerlid_shape')
                row.operator('eyes.test_lowerlid', icon='RESTRICT_VIEW_OFF')
                row = col.row(align=True)
                row.operator('eyes.reset_blink_test', icon='FILE_REFRESH')

                if armature.name != 'Armature':
                    col.separator()
                    col.separator()
                    col.separator()
                    row = col.row(align=True)
                    row.scale_y = 0.3
                    row.label("Your armature has to be named 'Armature'", icon='ERROR')
                    row = col.row(align=True)
                    row.label("      for Eye Tracking to work!")
                    row = col.row(align=True)
                    row.scale_y = 0.3
                    row.label("      (currently '" + armature.name + "')")

                if context.scene.mesh_name_eye != 'Body':
                    col.separator()
                    col.separator()
                    col.separator()
                    row = col.row(align=True)
                    row.scale_y = 0.3
                    row.label("The mesh containing the eyes has to be", icon='ERROR')
                    row = col.row(align=True)
                    row.label("      named 'Body' for Eye Tracking to work!")
                    row = col.row(align=True)
                    row.scale_y = 0.3
                    row.label("      (currently '" + context.scene.mesh_name_eye + "')")

                col.separator()
                col.separator()
                col.separator()
                row = col.row(align=True)
                row.scale_y = 0.3
                row.label("Don't forget to assign 'LeftEye' and 'RightEye'", icon='INFO')
                row = col.row(align=True)
                row.label("      to the eyes in Unity!")

                row = col.row(align=True)
                row.scale_y = 1.5
                row.operator('eyes.test_stop', icon='PAUSE')


class VisemePanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_viseme_v1'
    bl_label = 'Visemes'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        mesh_count = len(tools.common.get_meshes_objects())
        if mesh_count == 0:
            row = col.row(align=True)
            row.scale_y = 1.1
            row.label('No meshes found!', icon='ERROR')
            col.separator()
        elif mesh_count > 1:
            row = col.row(align=True)
            row.scale_y = 1.1
            row.prop(context.scene, 'mesh_name_viseme', icon='MESH_DATA')
            col.separator()

        row = col.row(align=True)
        row.scale_y = 1.1
        row.prop(context.scene, 'mouth_a', icon='SHAPEKEY_DATA')
        row = col.row(align=True)
        row.scale_y = 1.1
        row.prop(context.scene, 'mouth_o', icon='SHAPEKEY_DATA')
        row = col.row(align=True)
        row.scale_y = 1.1
        row.prop(context.scene, 'mouth_ch', icon='SHAPEKEY_DATA')
        col.separator()
        row = col.row(align=True)
        row.prop(context.scene, 'shape_intensity')
        col.separator()
        row = col.row(align=True)
        row.operator('auto.viseme', icon='TRIA_RIGHT')


class BoneRootPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_boneroot_v1'
    bl_label = 'Bone Parenting'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        row.prop(context.scene, 'root_bone', icon='BONE_DATA')
        row = box.row(align=True)
        row.operator('refresh.root', icon='FILE_REFRESH')
        row.operator('root.function', icon='TRIA_RIGHT')


class OptimizePanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_optimize_v1'
    bl_label = 'Optimization'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        row = col.row(align=True)
        row.prop(context.scene, 'optimize_mode', expand=True)

        if context.scene.optimize_mode == 'ATLAS':
            col.separator()

            mesh_count = len(tools.common.get_meshes_objects(mode=2))
            if mesh_count == 0:
                row = col.row(align=True)
                row.label('No meshes found!', icon='ERROR')
            elif mesh_count > 1:
                col.separator()
                row = col.row(align=True)
                row.prop(context.scene, 'mesh_name_atlas', icon='MESH_DATA')
            else:
                col.separator()

            row = col.row(align=True)
            row.prop(context.scene, 'texture_size', icon='TEXTURE')

            col.separator()
            row = col.row(align=True)
            row.prop(context.scene, 'island_margin')
            row = col.row(align=True)
            row.prop(context.scene, 'angle_limit')
            row = col.row(align=True)
            row.prop(context.scene, 'area_weight')

            row = box.row(align=True)
            row.scale_y = 1.1
            row.prop(context.scene, 'one_texture')
            row.prop(context.scene, 'pack_islands')
            row = box.row(align=True)
            row.operator('auto.atlas', icon='TRIA_RIGHT')

        if context.scene.optimize_mode == 'MATERIAL':
            col = box.column(align=True)
            row = col.row(align=True)
            row.scale_y = 1.1
            row.operator('combine.mats', icon='MATERIAL')
            row = col.row(align=True)
            row.scale_y = 1.1
            row.operator('one.tex', icon='TEXTURE')

        if context.scene.optimize_mode == 'BONEMERGING':
            if len(tools.common.get_meshes_objects()) > 1:
                row = box.row(align=True)
                row.prop(context.scene, 'merge_mesh')
            row = box.row(align=True)
            row.prop(context.scene, 'merge_bone')
            row = box.row(align=True)
            row.prop(context.scene, 'merge_ratio')
            row = box.row(align=True)
            col.separator()
            row.operator('refresh.root', icon='FILE_REFRESH')
            row.operator('bone.merge', icon='AUTOMERGE_ON')


class CopyProtectionPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_copyprotection_v1'
    bl_label = 'Copy Protection'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        row = col.row(align=True)
        row.scale_y = 0.8
        row.label('Protects your avatar from Unity cache ripping.')
        col.separator()
        row = col.row(align=True)
        row.label('Before use: Read the documentation!')
        row = col.row(align=True)
        row.operator('copyprotection.button', icon='FORWARD')
        col.separator()
        col.separator()
        # row = col.row(align=True)
        # row.label('Randomization Level:')
        # row = col.row(align=True)
        # row.prop(context.scene, 'protection_mode', expand=True)

        row = col.row(align=True)
        row.scale_y = 1.3
        meshes = tools.common.get_meshes_objects()
        if len(meshes) > 0 and meshes[0].data.shape_keys and meshes[0].data.shape_keys.key_blocks.get('Basis Original'):
            row.operator('copyprotection.disable', icon='KEY_DEHLT')
            row = col.row(align=True)
            col.separator()
            row.operator('armature_manual.export_model', icon='ARMATURE_DATA')
        else:
            row.operator('copyprotection.enable', icon='KEY_HLT')


class UpdaterPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_updater_v2'
    bl_label = 'Updater'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        # addon_updater_ops.check_for_update_background()
        addon_updater_ops.update_settings_ui(self, context)


class SupporterPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_supporter_v2'
    bl_label = 'Supporters'

    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)

        # supporter_data = tools.supporter.supporter_data

        row = col.row(align=True)
        row.label('Do you like this plugin and want to support us?')
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator('supporter.patreon', icon_value=tools.supporter.preview_collections["custom_icons"]["heart1"].icon_id)

        if not tools.supporter.supporter_data or not tools.supporter.supporter_data.get('supporters') or len(tools.supporter.supporter_data.get('supporters')) == 0:
            return

        col.separator()
        row = col.row(align=True)
        row.label('Thanks to our awesome supporters! <3')
        col.separator()

        supporter_count = self.draw_supporter_list(col, show_tier=1)

        if supporter_count > 0:
            col.separator()

        self.draw_supporter_list(col, show_tier=0)

        col.separator()
        row = col.row(align=True)
        row.scale_y = 1.2
        row.label('Is your name missing?', icon="INFO")
        row = col.row(align=True)
        row.scale_y = 0.3
        row.label('     Please contact us in our discord!')
        col.separator()
        row = col.row(align=True)
        row.scale_y = 0.8
        row.operator('supporter.reload', icon='FILE_REFRESH')

    def draw_supporter_list(self, col, show_tier=0):
        supporter_data = tools.supporter.supporter_data.get('supporters')
        preview_collections = tools.supporter.preview_collections.get("supporter_icons")

        i = 0
        j = 0
        cont = True

        while cont:
            try:
                supporter = supporter_data[j]
                name = supporter.get('displayname')
                tier = supporter.get('tier')
                idname = supporter.get('idname')

                if not name or not idname or supporter.get('disabled'):
                    j += 1
                    continue

                website = False
                if 'website' in supporter.keys():
                    website = True
                if not tier:
                    tier = 0

                if i % 3 == 0:
                    row = col.row(align=True)
                    if show_tier == 1:
                        row.scale_y = 1.1

                if tier == show_tier:
                    row.operator(idname,
                                 emboss=website,
                                 icon_value=preview_collections[name].icon_id)
                    i += 1
                j += 1
            except IndexError:
                if i % 3 == 0:
                    cont = False
                    continue
                row.label('')
                i += 1
        return i


class CreditsPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_credits_v1'
    bl_label = 'Credits'

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)

        version_str = 'Cats Blender Plugin ('
        if len(version) > 0:
            version_str += str(version[0])
            for index, i in enumerate(version):
                if index == 0:
                    continue
                version_str += '.' + str(version[index])
        if dev_branch:
            version_str += '-dev'
        version_str += ')'

        row.label(version_str, icon_value=tools.supporter.preview_collections["custom_icons"]["cats1"].icon_id)
        col.separator()
        row = col.row(align=True)
        row.label('Created by GiveMeAllYourCats and Hotox')
        row = col.row(align=True)
        row.label('For the awesome VRChat community <3')
        row.scale_y = 0.5
        col.separator()
        row = col.row(align=True)
        row.label('Special thanks to: Shotariya and Neitri')
        col.separator()
        row = col.row(align=True)
        row.label('Want to give feedback or found a bug?')

        row = col.row(align=True)
        row.operator('credits.discord', icon_value=tools.supporter.preview_collections["custom_icons"]["discord1"].icon_id)
        row = col.row(align=True)
        row.operator('credits.forum', icon_value=tools.supporter.preview_collections["custom_icons"]["cats1"].icon_id)


class UpdaterPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    auto_check_update = bpy.props.BoolProperty(
        name='Auto-check for Update',
        description='If enabled, auto-check for updates using an interval',
        default=True
    )
    updater_intrval_months = bpy.props.IntProperty(
        name='Months',
        description='Number of months between checking for updates',
        default=0,
        min=0
    )
    updater_intrval_days = bpy.props.IntProperty(
        name='Days',
        description='Number of days between checking for updates',
        default=1,
        min=1
    )
    updater_intrval_hours = bpy.props.IntProperty(
        name='Hours',
        description='Number of hours between checking for updates',
        default=0,
        min=0,
        max=0
    )
    updater_intrval_minutes = bpy.props.IntProperty(
        name='Minutes',
        description='Number of minutes between checking for updates',
        default=0,
        min=0,
        max=0
    )

    def draw(self, context):
        addon_updater_ops.update_settings_ui(self, context)


classesToRegister = [
    ArmaturePanel,
    tools.armature_manual.ImportModel,
    tools.armature_manual.ExportModel,
    tools.armature_manual.XpsToolsButton,
    tools.armature.FixArmature,
    tools.armature_manual.StartPoseMode,
    tools.armature_manual.StopPoseMode,
    tools.armature_manual.PoseToShape,

    ManualPanel,
    tools.armature_manual.SeparateByMaterials,
    tools.armature_manual.SeparateByLooseParts,
    tools.armature_manual.JoinMeshes,
    tools.armature_manual.MergeWeights,
    tools.armature_manual.RemoveZeroWeight,
    tools.armature_manual.RemoveConstraints,
    tools.armature_manual.RecalculateNormals,
    tools.armature_manual.FlipNormals,
    tools.translate.TranslateShapekeyButton,
    tools.translate.TranslateBonesButton,
    tools.translate.TranslateMeshesButton,
    tools.translate.TranslateMaterialsButton,

    CustomPanel,
    tools.armature_custom.MergeArmature,
    tools.armature_custom.AttachMesh,
    tools.armature_custom.CustomModelTutorialButton,

    DecimationPanel,
    tools.decimation.AutoDecimateButton,
    tools.decimation.AddShapeButton,
    tools.decimation.AddMeshButton,
    tools.decimation.RemoveShapeButton,
    tools.decimation.RemoveMeshButton,

    EyeTrackingPanel,
    tools.eyetracking.CreateEyesButton,
    tools.eyetracking.StartTestingButton,
    tools.eyetracking.StopTestingButton,
    tools.eyetracking.ResetRotationButton,
    tools.eyetracking.AdjustEyesButton,
    tools.eyetracking.TestBlinking,
    tools.eyetracking.TestLowerlid,
    tools.eyetracking.ResetBlinkTest,

    VisemePanel,
    tools.viseme.AutoVisemeButton,

    BoneRootPanel,
    tools.rootbone.RefreshRootButton,
    tools.rootbone.RootButton,

    OptimizePanel,
    tools.atlas.AutoAtlasButton,
    tools.material.CombineMaterialsButton,
    tools.material.OneTexPerMatButton,
    tools.bonemerge.BoneMergeButton,

    CopyProtectionPanel,
    tools.copy_protection.CopyProtectionEnable,
    tools.copy_protection.CopyProtectionDisable,
    tools.copy_protection.ProtectionTutorialButton,

    UpdaterPanel,
    UpdaterPreferences,

    SupporterPanel,
    tools.supporter.PatreonButton,
    tools.supporter.ReloadButton,

    CreditsPanel,
    tools.credits.DiscordButton,
    tools.credits.ForumButton,

    tools.shapekey.ShapeKeyApplier,
]


def register():
    print("\n### Loading CATS...")
    # bpy.utils.unregister_module("mmd_tools")
    try:
        mmd_tools_local.register()
    except AttributeError:
        pass

    if dev_branch and len(version) > 2:
        version[2] += 1

    # thread = Thread(target=tools.supporter.load_supporters, args=[])
    # thread.start()
    tools.supporter.load_settings()
    tools.supporter.load_other_icons()
    tools.supporter.load_supporters()
    tools.supporter.register_dynamic_buttons()

    try:
        addon_updater_ops.register(bl_info)
    except ValueError:
        print('Error while registering updater.')
        pass

    for value in classesToRegister:
        bpy.utils.register_class(value)

    bpy.context.user_preferences.system.use_international_fonts = True
    bpy.context.user_preferences.filepaths.use_file_compression = True

    bpy.types.MESH_MT_shape_key_specials.append(tools.shapekey.addToShapekeyMenu)
    print("### Loaded CATS successfully!")


def unregister():
    print("### Unloading CATS...")
    try:
        mmd_tools_local.unregister()
    except AttributeError:
        pass

    for value in classesToRegister:
        bpy.utils.unregister_class(value)
    tools.supporter.unregister_dynamic_buttons()
    addon_updater_ops.unregister()

    tools.supporter.unload_icons()

    bpy.types.MESH_MT_shape_key_specials.remove(tools.shapekey.addToShapekeyMenu)
    print("### Unloaded CATS successfully!")


if __name__ == '__main__':
    register()
