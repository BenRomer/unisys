#
# Makefile for Unisys visorbus
#

obj-m	+= visorbus.o

visorbus-y := visorbus_main.o
visorbus-y += visorchannel.o
visorbus-y += visorchipset.o
visorbus-y += periodic_work.o

ccflags-y += -I$(src)/../include
