/* Copyright (c) 2012 - 2015 UNISYS CORPORATION
 * All rights reserved.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or (at
 * your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, GOOD TITLE or
 * NON INFRINGEMENT.  See the GNU General Public License for more
 * details.
 */

#include <linux/debugfs.h>
#include <linux/skbuff.h>
#include <linux/kthread.h>

#include "visorbus.h"
#include "iochannel.h"

static int visorhba_init(void)
{
	struct dentry *ret;
	printk(KERN_ALERT "Hello World\n");
}

/**
 *	visorhba_cleanup	- driver exit routine
 *
 *	Unregister driver from the bus and free up memory.
 */
static void visorhba_exit(void)
{
	printk(KERN_ALERT "Bye World\n");
}

module_init(visorhba_init);
module_exit(visorhba_exit);

MODULE_AUTHOR("Unisys");
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("sPAR hba driver for sparlinux: ver 1.0.0.0");
MODULE_VERSION("1.0.0.0");
