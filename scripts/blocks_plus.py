from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block_id = int(input('What block id do you want?'))

pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, block_id)



