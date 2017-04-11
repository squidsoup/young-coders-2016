from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x = -9.8
y = 14.0
z = -21.0 

mc.player.setTilePos(x, y, z)
