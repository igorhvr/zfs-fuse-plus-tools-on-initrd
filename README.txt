Sat Jul 18 2009
Maximilian Mehnert <maximilian.mehnert@gmx.de>
These project is maintained at
http://github.com/mmehnert/zfs-fuse-on-initrd
If you get this file without the rest of the package, please fetch the
scripts from there.

This is about creating an initrd.gz to have your root partition on zfs-fuse.

ATTENTION!
Bear in mind, that all scripts are meant to be started in the directory that
they are in. If the working directory does not correspond to the location of
the script, results may not be what you expect and can even harm your
system.
The same is especially true for scripts that reside inside the initrd.gz.
They are meant to be run from the root of the booted ramdisk and from
nowhere else. Please make sure that you understand what the scripts are
doing before running them.
If you don't understand them, this whole thing is probably the wrong project
for you.
In no way am I responsible for what you do to your computer and setting up
/ on zfs-fuse needs some careful tinkering with your setup.

My advise is to first create either an usb stick or a bootable cdrom
(see apt-get bootcd) that includes the initrd.gz created here,
make sure that zfs-fuse can be started from there and that it
enables you to access both your system and your backup of
your complete system. After that, convert your current system :-)

Now to something completely different...

This is a bundle of scripts that I maintain to create 
an initrd.gz (cpio format) to boot with zfs-fuse as
a root filesystem.

The booting is stopped, offering a shell inside the ramdisk
which allows the user to start zfs-fuse (use start-zfs as a command)
and to mount the root filesystem to /initboot (zfs set mountpoint=...).

After exiting the shell, booting continues by remounting
a couple of things and chrooting into /initroot.
Please see the mount-stuff script for details.
The main purpose is to have the zfs-fuse socket and lockfile in both
environments and a /dev directory that can be accessed from inside
the chroot-jail your system will be running in.

Also, /mounts/zfs is used as a common mountpoint for zfs pools that are
attached to the system later.
Please look into the --make-shared option of mount and inside the scripts
for details.

Also, please have a look at the Makefile for ways of calling the scripts
that are included. They collect programs and libraries from your system into
the initrd.gz.
You will need to have the programs listed in lists.py installed.


Please use all this as you wish and send feedback and improvements if
you feel like it. :-)
No rights reserved.
