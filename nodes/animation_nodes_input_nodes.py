'''
Copyright (C) 2014 Jacques Lucke
mail@jlucke.com

Created by Jacques Lucke

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import bpy
from bpy.types import NodeTree, Node, NodeSocket
from animation_nodes_node_helper import AnimationNode
from animation_nodes_utils import *


class IntegerInputNode(Node, AnimationNode):
	bl_idname = "IntegerInputNode"
	bl_label = "Integer"
	
	intProperty = bpy.props.IntProperty(default = 0)
	
	def init(self, context):
		self.outputs.new("IntegerSocket", "Number")
		
	def draw_buttons(self, context, layout):
		layout.prop(self, "intProperty", text = "")
		
	def execute(self, input):
		output = {}
		output["Number"] = self.intProperty
		return output


class StringInputNode(Node, AnimationNode):
	bl_idname = "StringInputNode"
	bl_label = "String"
	
	stringProperty = bpy.props.StringProperty(default = "text")
	
	def init(self, context):
		self.outputs.new("StringSocket", "Text")
		
	def draw_buttons(self, context, layout):
		layout.prop(self, "stringProperty", text = "")
		
	def execute(self, input):
		output = {}
		output["Text"] = self.stringProperty
		return output
		
		
class ObjectInputNode(Node, AnimationNode):
	bl_idname = "ObjectInputNode"
	bl_label = "Object"
	
	objectName = bpy.props.StringProperty()
	
	def init(self, context):
		self.outputs.new("ObjectSocket", "Object")
		
	def draw_buttons(self, context, layout):
		col = layout.column()
		row = col.row(align = True)
		row.prop(self, "objectName", text = "")
		selector = row.operator("animation_nodes.assign_active_object_to_node", text = "", icon = "EYEDROPPER")
		selector.nodeTreeName = self.id_data.name
		selector.nodeName = self.name
		selector.target = "objectName"
		col.separator()
		
	def execute(self, input):
		output = {}
		output["Object"] = self.objectName
		return output
		
class TimeInfoNode(Node, AnimationNode):
	bl_idname = "TimeInfoNode"
	bl_label = "Time Info"
	
	def init(self, context):
		self.outputs.new("IntegerSocket", "Frame")
		
	def execute(self, input):
		output = {}
		output["Frame"] = getCurrentFrame()
		return output
	
		
# register
################################
		
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)