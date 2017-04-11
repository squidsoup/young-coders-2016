from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block_id = 4
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, block_id)

y = y + 1
mc.setBlock(x, y, z, block_id)
