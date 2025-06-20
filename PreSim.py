from maya import cmds

"""
Script made by Oliver Silva aka @imoliversp

This script prepares a character for the simulation process by resetting transformation attributes 
and setting keyframes for a specific hierarchy, controllers or joints. It automates repetitive tasks such as:

1. Setting the start frame of the animation to a custom pre-roll time.
2. Setting the playback speed to "Play every Frame" to prepare the scene for simulation.
3. Resetting rotation and translation values to zero for the character's controllers or joints.
4. Setting keyframes for the reset attributes, ensuring that the character is in a neutral position for the simulation.

Depending on the case, it may happen one of the following cases:

Action A:
	If the user has selected the group with the contained joint hierarchy, the script will just affect the Controllers for that hierarchy.

Action B:
	If the user did not select anything, the script will use all the Controllers in scene.

Action C:
	If no controllers are found and the user did not select anything, it will proceed by resetting the joints instead.
"""

# With the "preRoll" variable, the user can set a custom pre roll needed.
preRoll = -50

# With the "clothDamp" variable, the user can set a custom time for the cloth pieces to stabilize before to start the sim.
clothDamp = -20

# Set the start time of the animation to the user's choice.
cmds.playbackOptions(minTime = preRoll)

# Set the Currentframe to the user's choice.
cmds.currentTime (preRoll)

#Set the Playback Speed to Play every Frame, Free = 0 which is necessary to start the Simulation process.
cmds.playbackOptions(playbackSpeed = 0)

# Get all the Curve Nurbs from the scene (Control Rig) for Action B.
controllers = cmds.ls(type="nurbsCurve")

# Function that sets a keyframe in -15 and in 0, to make the preroll work properly before to set to 0 the transformations.
# Store the steps inside a function "setkey_preroll" which is a repetitive action.
def setkey_preroll(target_node, key_preroll):

	"""
	Function that sets a keyframe for the transforms for Preroll.

	Args:
		target_node (string): The name of the nurb curve.
		key_preRoll (string): Is a token for rotate and translate in X, Y, Z.
	
	Commands:
		cmds.setKeyframe (objects):This command creates keyframes for the specified objects.
	"""

	cmds.setKeyframe(target_node, time=-0, attribute = key_preroll)
	cmds.setKeyframe(target_node, time= clothDamp, attribute = key_preroll)

# Store the steps inside a function "reset_ctrl_attr" which is a repetitive action.
def reset_ctrl_attr(target_node, ctrl_attr):

	"""
	Function that tests if the nurb is not locked and if its value is not 0.

	Args:
		target_node (string): The name of the nurb curve.
		ctrl_attr (string): The name of the attribute.

	Commands:
		cmds.setAttr (any): Sets the value of a node attribute.
		cmds.getAttr (attr, bool): Returns the value of the named object's attribute.
		lock=True (bool): Specifies the new lock state for the node. The default is true.
	"""

	# If the nurb is unlocked and differs from 0, it will be set back to zero.
	if not cmds.getAttr(f"{target_node}.{ctrl_attr}", lock=True) and cmds.getAttr(f"{target_node}.{ctrl_attr}") != 0:

		# "ctrl_attr" is the token which is going to receive the transform axis.
		# "target_node" is the token for each nurb.
		cmds.setAttr(f"{target_node}.{ctrl_attr}", 0)

# Function that sets a keyframe for the transform attributes.
# Store the steps inside a function "control_keyframe" which is a repetitive action.
def control_keyframe(target_node, ctrl_key):

	"""
	Function that sets a keyframe for the transforms.

	Args:
		target_node (string): The name of the nurb curve.
		ctrl_key (string): Is a token for rotate and translate in X, Y, Z.
	
	Commands:
		cmds.setKeyframe (objects):This command creates keyframes for the specified objects.
	"""

	cmds.setKeyframe(target_node, attribute = ctrl_key)

#Action A
# If the user execute this script selecting a hierarchy, reset the transformations and set keyframes it will only be afected over that hierarchy.
# The user may use this as a filter in case the user don't want the whole controllers to be affected by the script.
cmds.select(hierarchy=True)
selectedNurb = cmds.ls(sl=True, type="nurbsCurve")
transformNurb = cmds.listRelatives(selectedNurb, parent=True)

if transformNurb:
	for target_node in transformNurb:
		# Set keyframe with variable "clothDamp" and in frame 0 before resetting attributes in order to make a preroll.
		setkey_preroll(target_node, "rotateX")
		setkey_preroll(target_node, "rotateY")
		setkey_preroll(target_node, "rotateZ")

		setkey_preroll(target_node, "translateX")
		setkey_preroll(target_node, "translateY")
		setkey_preroll(target_node, "translateZ")

		# Reset rotation axis.
		reset_ctrl_attr(target_node, "rotateX")
		reset_ctrl_attr(target_node, "rotateY")
		reset_ctrl_attr(target_node, "rotateZ")

		# Reset translation axis.
		reset_ctrl_attr(target_node, "translateX")
		reset_ctrl_attr(target_node, "translateY")
		reset_ctrl_attr(target_node, "translateZ")

		# Set a keyframe for the rotate axis.
		control_keyframe(target_node, "rotateX")
		control_keyframe(target_node, "rotateY")
		control_keyframe(target_node, "rotateZ")

		# Set a keyframe for the translate axis in the current frame.
		control_keyframe(target_node, "translateX")
		control_keyframe(target_node, "translateY")
		control_keyframe(target_node, "translateZ")

# Show a message in console to tell the user which action is being taken.
	print("Action A: You have selected a hierarchy of Controllers, they have been set to 0.")
else:

	# Action B
	# If the user execute this script without selecting any hierarchy, it will use the whole Controllers of a scene.
	if controllers:
		for ctrl in controllers:

			# cmds.listRelatives (objects): This command lists parents and children, in thi case check from the child "shape" node and get the parent "transform" node.
			# It returns a list[].
			###print(transform_ctrl)
			target_node = cmds.listRelatives(ctrl, parent=True)

			# Get the items inside the list [], but ".getAttr" doesn't receive lists of strings, so we use the item, which is just one per joint.
			###print(transform_ctrl)
			target_node = target_node[0]

			# Set keyframe with variable "clothDamp" and in frame 0 before resetting attributes in order to make a preroll.
			setkey_preroll(target_node, "rotateX")
			setkey_preroll(target_node, "rotateY")
			setkey_preroll(target_node, "rotateZ")

			setkey_preroll(target_node, "translateX")
			setkey_preroll(target_node, "translateY")
			setkey_preroll(target_node, "translateZ")

			# Reset rotation axis.
			reset_ctrl_attr(target_node, "rotateX")
			reset_ctrl_attr(target_node, "rotateY")
			reset_ctrl_attr(target_node, "rotateZ")

			# Reset translation axis.
			reset_ctrl_attr(target_node, "translateX")
			reset_ctrl_attr(target_node, "translateY")
			reset_ctrl_attr(target_node, "translateZ")

			# Set a keyframe for the rotate axis.
			control_keyframe(target_node, "rotateX")
			control_keyframe(target_node, "rotateY")
			control_keyframe(target_node, "rotateZ")

			# Set a keyframe for the translate axis in the current frame.
			control_keyframe(target_node, "translateX")
			control_keyframe(target_node, "translateY")
			control_keyframe(target_node, "translateZ")

	# Show a message in console to tell the user which action is being taken.
		print("Action B: You have Controllers, they have been set to 0.")

	# Action C
	# If the user execute this script with a character that does not contain Controllers it will use the Joints.
	else:
		# Get all the joints in the scene with "" type = "joint" "".
		joints = cmds.ls(type = "joint")

		# Function that resets the rotation axis back to 0.
		# Store the steps inside a function "reset_jnt_attr" which is a repetitive action.
		def reset_jnt_attr(target_node, jnt_attr):

			"""
			Function that sets the rotation value to 0.

			It receives "target_node" which is the variable which stores the joints in each iteration.
			It receives "jnt_attr" which is a token for rotations in X,Y,Z.

			Commands:
			cmds.setAttr (any): Sets the value of a node attribute.
			"""

			cmds.setAttr(f"{target_node}.{jnt_attr}", 0)

		# Function that sets a keyframe for each joint.
		# Store the steps inside a funcion "joint_keyframe" which is a repetitive action.
		def joint_keyframe(target_node, jnt_key):

			"""
			Function that sets a keyframe for the transforms.

			It receives "target_node" which is the variable which stores the joints in each iteration.
			It receives "jnt_key" which is a token for rotate in X, Y, Z.

			Commands:
				cmds.setKeyframe (objects):This command creates keyframes for the specified objects.
			"""

			cmds.setKeyframe(target_node, attribute = jnt_key)

		# Loop that iterates for each joint you have in scene.
		for target_node in joints:

			# Set keyframe with variable "clothDamp" and in frame 0 before resetting attributes in order to make a preroll.
			setkey_preroll(target_node, "rotateX")
			setkey_preroll(target_node, "rotateY")
			setkey_preroll(target_node, "rotateZ")

			# Call the function "reset_jnt_attr" to set rotation values to 0 in all axis.
			reset_jnt_attr(target_node, "rotateX")
			reset_jnt_attr(target_node, "rotateY")
			reset_jnt_attr(target_node, "rotateZ")

			# Call the function "joint_keyframe" to set a KeyFrame in the current frame.
			joint_keyframe(target_node, "rotateX")
			joint_keyframe(target_node, "rotateY")
			joint_keyframe(target_node, "rotateZ")

		# Show a message in console to tell the user which action is being taken.
		print("Action C: You don't have Controllers, your joints have been set to 0.")