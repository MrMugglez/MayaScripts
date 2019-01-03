import maya.cmds as mc

all_channels = True
channel_x = True
channel_y = False
channel_z = False

window = mc.window(title="Joint Orientation Tool", iconName='Short Name', widthHeight=(200, 105))
mc.columnLayout(adjustableColumn=True)
mc.button(label="Reorient Single Joint", command="reorient_selected()")
mc.button(label="Reorient Joints", command="reorient_selected()")
can_reset_orientation = mc.checkBox("Reset Orientation")
can_reset_rotation = mc.checkBox("Reset Rotation")
mc.showWindow()


def reorient(selection, channel, additive=True):
    if additive:
        new_value = mc.getAttr(selection + ".jointOrient" + channel) + mc.getAttr(selection + ".rotate" + channel)
        mc.setAttr(selection + ".jointOrient" + channel, new_value)
    else:
        mc.setAttr(selection + ".jointOrient" + channel, mc.getAttr(selection + ".jointOrient" + channel))
    mc.setAttr(selection + ".rotate" + channel, 0)


def reset_orientation(selection, channel):
    mc.setAttr(selection + ".jointOrient" + channel, 0)


def reset_rotation(selection, channel):
    mc.setAttr(selection + ".rotate" + channel, 0)


def reorient_specific_channel(sel):
    if channel_x:
        if not reset_orientation:
            reorient(sel, "X")
        else:
            reset_orientation(sel, "X")
    if channel_y:
        if not reset_orientation:
            reorient(sel, "Y")
        else:
            reset_orientation(sel, "Y")
    if channel_z:
        if not reset_orientation:
            reorient(sel, "Z")
        else:
            reset_orientation(sel, "Z")


def reorient_selected():
    for sel in mc.ls(selection=True):
        if all_channels:
            for channel in ["X", "Y", "Z"]:
                if reset_orientation:
                    reset_orientation(sel, channel)
                else:
                    reorient(sel, channel)
        else:
            reorient_specific_channel(sel)


def reorient_tree():
    pass
