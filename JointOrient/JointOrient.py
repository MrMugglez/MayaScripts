import maya.cmds as mc

all_channels = True
channel_x = True
channel_y = False
channel_z = False

window = mc.window()
mc.columnLayout()
mc.button(label="Reorient Single Joint", command="reorient_selected()")
mc.button(label="Reorient Joints", command="reorient_selected()")
mc.showWindow()


def reorient(selection, channel, additive=True):
    if additive:
        new_value = mc.getAttr(selection + ".jointOrient" + channel) + mc.getAttr(selection + ".rotate" + channel)
        mc.setAttr(selection + ".jointOrient" + channel, new_value)
    else:
        mc.setAttr(selection + ".jointOrient" + channel, mc.getAttr(selection + ".jointOrient" + channel))
    mc.setAttr(selection + ".rotate" + channel, 0)


def reorient_selected():
    for sel in mc.ls(selection=True):
        if all_channels:
            for channel in ["X", "Y", "Z"]:
                reorient(sel, channel)
        else:
            if channel_x:
                reorient(sel, "X")
            if channel_y:
                reorient(sel, "Y")
            if channel_z:
                reorient(sel, "Z")


def revert_orientation():
    pass


def reorient_tree():
    pass
