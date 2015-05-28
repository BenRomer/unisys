#
# Makefile for Unisys channel
#

obj-$(CONFIG_UNISYS_VISORHBA)	+= visorhba.o

visorhba-y := visorhba_main.o

ccflags-y += -Idrivers/staging/unisys/include
ccflags-y += -Idrivers/staging/unisys/visorbus
ccflags-y += -DCONFIG_SPAR_GUEST -DGUESTDRIVERBUILD -DNOAUTOVERSION

