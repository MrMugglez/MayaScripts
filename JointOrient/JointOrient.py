import maya.cmds as mc

channels = ["X", "Y", "Z"]
all_channels = True
channel_x = True
channel_y = False
channel_z = False

window = mc.window(title="Joint Orientation Tool", iconName='Short Name', widthHeight=(200, 105))
mc.columnLayout(adjustableColumn=True)
mc.button(label="Reorient Single Joint", c="reorient_selected()")
mc.button(label="Reorient Joints", command="reorient_tree()")
ignore_children = mc.checkBox("Ignore Children")
mc.button(label="Reset Joint Orientation", command="reset_orientation()")
mc.button(label="Reset Joint Rotation", command="reset_rotation()")
mc.showWindow()


def is_parent(sel):
    mc.select(sel, add=False)
    mc.pickWalk(direction='down')
    child = mc.ls(selection=True)
    if sel == child[0]:
        return False
    return True


def reorient(selection, channel, additive=True):
    if additive:
        new_value = mc.getAttr(selection + ".jointOrient" + channel) + mc.getAttr(selection + ".rotate" + channel)
        print("value of the current orientation, and the rotation is", new_value)
        mc.setAttr(selection + ".jointOrient" + channel, new_value)
    else:
        mc.setAttr(selection + ".jointOrient" + channel, mc.getAttr(selection + ".jointOrient" + channel))
    mc.setAttr(selection + ".rotate" + channel, 0)


def reset_orientation_channel(selection, channel):
    mc.setAttr(selection + ".jointOrient" + channel, 0)


def reset_orientation():
    for sel in mc.ls(selection=True):
        for channel in channels:
            reset_orientation_channel(sel, channel)


def reset_rotation_channel(selection, channel):
    mc.setAttr(selection + ".rotate" + channel, 0)


def reset_rotation():
    for sel in mc.ls(selection=True):
        for channel in channels:
            reset_rotation_channel(sel, channel)


def point_joint_at_child(parent):
    parent = mc.ls(selection=True)
    mc.select(parent, add=False)
    if is_parent(parent):
        mc.pickWalk(direction='down')
        child = mc.ls(selection=True)[0]
        mc.parent(child, world=True)
        for channel in channels:
            reset_orientation_channel(parent, channel)
            reset_rotation_channel(parent, channel)
        aim_name = mc.aimConstraint([child, parent],
                                    offset=[0, 0, 0], weight=1, aimVector=[1, 0, 0], upVector=[0, 1, 0],
                                    worldUpType="vector", worldUpVector=[0, 1, 0], name="tempAimConst")
        mc.delete(parent + "_" + aim_name)
        mc.parent(child, parent)
    else:
        reset_orientation()


def reorient_specific_channel(sel):
    if channel_x:
        if not reset_orientation_channel:
            reorient(sel, "X")
        else:
            reset_orientation_channel(sel, "X")
    if channel_y:
        if not reset_orientation_channel:
            reorient(sel, "Y")
        else:
            reset_orientation_channel(sel, "Y")
    if channel_z:
        if not reset_orientation_channel:
            reorient(sel, "Z")
        else:
            reset_orientation_channel(sel, "Z")


def reorient_selected():
    for sel in mc.ls(selection=True):
        if all_channels:
            print("reorienting all channels")
            for channel in channels:
                reorient(sel, channel)
        else:
            reorient_specific_channel(sel)


def reorient_tree():
    print("Work in progress...")
    pass
